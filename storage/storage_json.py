from typing import TextIO
from storage.istorage import IStorage
import json
import os

"""
This module loads/creates a Json file and performs
SCRUM operations on it.
"""


class StorageJson(IStorage):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path


    def read_movies(self):
        """
        Loads a json file containing data about movies.

        Checks if the file exists. If it doesn't, creates
        and populates a new json file with example data.

        Handles errors by returning an empty dictionary.
        Handles errors for missing or corrupted JSON file.

        Returns a dictionary where keys = movie titles,
        values = dictionaries with movie attributes like
        rating and release year.
        """
        movie_dict_example = {
            "Titanic": {
                "rating": 9.0,
                "year": 1999
            }
        }

        try:
            if not os.path.exists(self.file_path):
                with open(file=self.file_path, mode='w',
                          encoding="utf-8") as handle:
                    json.dump(movie_dict_example, handle, indent=4)

            with open(file=self.file_path, mode="r",
                      encoding="utf-8") as handle:
                return json.load(handle)

        except FileNotFoundError:
            print(f"{self.file_path} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"{self.file_path} is corrupted")
            return {}


    def _update_json(self, updated_movie_dict):
        with open(file=self.file_path, mode='w',
                  encoding="utf-8") as handle:
            json.dump(updated_movie_dict, handle, indent=4)


    def _check_title(self):
        return super()._check_title()


    def _check_year(self):
        return super()._check_year()


    def _check_rating(self):
        return super()._check_rating()


    def add_movie(self): # menu command 2
        """
        Adds a movie to the movie database.
        """
        movies = self.read_movies()
        title = self._check_title()
        year = self._check_year()
        rating = self._check_rating()
        # poster = ...

        if title in movies:
            print(f"{title} already exists in database")
        else:
            movies[title] = {
                "rating": rating,
                "year": year
            }
        self._update_json(movies)

        ## inform the user with the result
        if title in self.read_movies():
            print(f"{title} successfully added")
        else:
            print("Something went wrong, movie not added")


    def delete_movie(self): # menu command 3
        """
        Deletes a movie from the movie database.

        Checks if there is data to delete, if so
        Checks movie exists in the database, if so
        Deletes the movie from the preloaded
        dict of dicts, and updates the json file with it.
        Raises a KeyError if the movie cannot be found
        in the database and thus, the operation cannot be
        performed (still same result).

        Prints a message to inform the user of the operation
        result.
        """
        movies = self.read_movies()
        title = self._check_title()

        ## Check if there is something to delete
        if len(movies) == 0:
            print("Currently there are no movies in the database")
            return

        ## Check if the title exists
        if not title in movies:
            raise KeyError(f"Movie {title} doesn't exist!")

        del movies[title]
        self._update_json(movies)

        ## inform the user with the result
        if title not in self.read_movies():
            print(f"Movie {title} successfully deleted")


    def update_movie(self): # menu command 4
        """
        Updates a movie rating from the movie database.
        """
        movies = self.read_movies()
        title = self._check_title()
        new_rating = self._check_rating()

        ## Check if there is something to update
        if len(movies) == 0:
            print("Currently there are no movies in the database")
            return

        ## Check if the title exists
        if not title in movies:
            print(f"Movie {title} doesn't exist!")
            return

        movies[title]["rating"] = new_rating
        self._update_json(movies)

        ## inform the user with the result
        if self.read_movies()[title]["rating"] == new_rating:
            print(f"Movie {title} successfully updated")

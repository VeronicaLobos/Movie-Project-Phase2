"""
This module loads/creates a Json file and performs
CRUD operations on it (persistent storage).
"""

import os
import csv
from storage.istorage import IStorage
import data_fetcher


class StorageCsv(IStorage):
    """
    A subclass of IStorage dedicated to CSV files.
    """
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path


    def _parse_csv_to_dict(self):
        """
        A utility command for read_movies() method.
        Parses through a csv file containing rows with
        movies, where each column contains the title,
        rating and year of the movie.

        Returns nested dictionaries where the first column
        fills the outer key (title), and the following
        columns are
        the keys for the movie attributes (rating, year).
        """
        movies_dictionary = {}
        with open(self.file_path, mode='r',
                  encoding='utf-8', newline='') as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                title = row["title"]
                movies_dictionary[title] = {
                    "rating": float(row["rating"]),
                    "year": int(row["year"]),
                    "poster": str(row["poster"])
                }
        return movies_dictionary


    def read_movies(self):
        """
        Loads/creates a csv file containing data about movies.

        Handles cases in which there is no csv file from
        an example *dictionary of dictionaries*, there
        is an empty csv file or empty with a header.

        Returns a *dictionary of nested dictionaries* that
        contains the movies information in the database.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
            "poster": "https://m.media-amazon.com/
                       images/...X300.jpg"
            }
        }
        """
        movie_list_example = [
            {"title": "Titanic", "rating": 9.0, "year": 1999,
             "poster": "https://m.media-amazon.com/images/M/"
                       "MV5BYzYyN2FiZmUtYWYzMy00MzViLWJkZTMtO"
                       "GY1ZjgzNWMwN2YxXkEyXkFqcGc@._V1_SX300.jpg"},
            {"title": "Up", "rating": 8.3, "year": 2009,
             "poster": "https://m.media-amazon.com/images/M/"
                       "MV5BNmI1ZTc5MWMtMDYyOS00ZDc2LTkzOTAtN"
                       "jQ4NWIxNjYyNDgzXkEyXkFqcGc@._V1_SX300.jpg"},
            {"title": "The Godfather", "rating": 9.0, "year": 1972,
             "poster": "https://m.media-amazon.com/images/M/"
                       "MV5BNGEwYjgwOGQtYjg5ZS00Njc1LTk2ZGEtM"
                       "2QwZWQ2NjdhZTE5XkEyXkFqcGc@._V1_SX300.jpg"}
                            ]

        try:
            if not os.path.exists(self.file_path):
                with open(file=self.file_path, mode='w',
                    encoding='utf-8', newline='') as handle:
                    writer = csv.writer(handle)
                    header = ["title", "rating", "year", "poster"]
                    writer.writerow(header)
                    for movie in movie_list_example:
                        writer.writerow([movie["title"], movie["rating"],
                                         movie["year"], movie["poster"]])

            return self._parse_csv_to_dict()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return {}
        except ValueError: #NoneType
            print(f"Error parsing data in {self.file_path}")
            self._reset_database()
            print("Database has been reset")
            return self._parse_csv_to_dict()


    def _update_csv(self, movies_dict):
        """
        Utility command for write, delete, update methods.
        Writes the provided movie dictionary to the csv file.
        """
        try:
            with open(self.file_path, mode='w',
                      encoding='utf-8', newline='') as handle:
                writer = csv.writer(handle)
                writer.writerow(["title", "rating", "year", "poster"])
                for movie_title, movie_data in movies_dict.items():
                    writer.writerow([movie_title, movie_data.get("rating"),
                                     movie_data.get("year"),
                                     movie_data.get("poster")])
        except Exception as e:
            print(f"Database wasn't updated: {e}")


    def add_movie(self): # menu command 2
        """
        Adds a movie to the movie database.

        Calls read_movies() in case there isn't a csv
        file stored, generates and populates one with
        example movies.
        Prompts the user for a movie title, fetches movie
        data (OMBd API), and adds it to the database if
        the title is unique.
        If the title already exists or data fetching fails,
        an appropriate error message is displayed.

        If the movie is successfully added, a confirmation
        message is printed.
        """
        self.read_movies()
        movies = self.read_movies()

        title = self.check_title()
        if title in movies:
            print(f"{title} already exists in database")
            return

        new_movie_data = data_fetcher.get_new_movie_data(title)
        if new_movie_data is None:
            print(f"Error fetching data, {title} not found in OMDb")
            return

        complete_title, movie_attributes = new_movie_data
        movies[complete_title] = movie_attributes
        self._update_csv(movies)

        if complete_title in self.read_movies().keys():
            print(f"{title} successfully added")


    def delete_movie(self): # menu command 3
        """
        Deletes a movie from the movie database.

        Checks if there is data to delete, if so
        Checks movie exists in the database, if so
        Deletes the movie from the preloaded
        dict of dicts, and updates the csv file with it.
        Raises a KeyError if the movie cannot be found
        in the database and thus, the operation cannot be
        performed (still same result).

        Prints a message to inform the user of the operation
        result.
        """
        movies = self.read_movies()

        if len(movies) == 0:
            print("Currently there are no movies in the database")
            return

        title = self.check_title()
        if not title in movies.keys():
            print(f"Movie {title} doesn't exist!")
            return

        del movies[title]
        self._update_csv(movies)

        if title not in self.read_movies():
            print(f"Movie {title} successfully deleted")
        else:
            print("Something went wrong...")


    def update_movie(self): # menu command 4
        """
        Updates a movie rating from the movie database.

        Checks if there is data to update, if so
        Checks movie exists in the database, if so
        modifies the value for 'rating' in the
        corresponding movie.
        Updates the csv file with the updated dict.

        Prints a message to inform the user with the operation
        result.
        """
        movies = self.read_movies()

        if len(movies) == 0:
            print("Currently there are no movies in the database")
            return

        title = self.check_title()
        if not title in movies:
            print(f"Movie {title} doesn't exist!")
            return

        new_rating = self.check_rating()
        movies[title]["rating"] = new_rating
        self._update_csv(movies)

        if self.read_movies()[title]["rating"] == new_rating:
            print(f"Movie {title} successfully updated")
        else:
            print("Something went wrong...")

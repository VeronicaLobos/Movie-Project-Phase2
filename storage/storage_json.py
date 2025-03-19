from storage.istorage import IStorage
import json
import os
import data_fetcher


"""
This module loads/creates a Json file and performs
CRUD operations on it (persistent storage).
"""

class StorageJson(IStorage):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path


    def _reset_database(self):
        """
        A utility command for read_movies() method.

        Deletes the contents of the CSV and populates
        it with the example data.
        Called as a result of corrupt files.
        """
        super()._reset_database()


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

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
            }
        }
        """
        movie_dict_example = {
            "Titanic": {"rating": 9.0, "year": 1999},
            "Up": {"rating": 8.3, "year": 2009},
            "The Godfather": {"rating": 9.0, "year": 1972}
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
            reset = input("Do you want to reset the CSV database? Y/N: ")
            if reset == "Y":
                self._reset_database()
            else:
                print("No action taken")
                return {}


    def _update_json(self, updated_movie_dict):
        """
        Utility command for write, delete, update methods.
        Writes the provided movie dictionary to the json file.
        """
        with open(file=self.file_path, mode='w',
                  encoding="utf-8") as handle:
            json.dump(updated_movie_dict, handle, indent=4)


    def check_title(self):
        """
        Utility command for checking str input in write,
        delete, update commands.
        """
        return super().check_title()


    def check_year(self):
        """
        Utility command for checking int input in write,
        delete, update commands.
        """
        return super().check_year()


    def check_rating(self):
        """
        Utility command for checking float input in write,
        delete, update commands.
        """
        return super().check_rating()


    def add_movie(self): # menu command 2
        """
        Adds a movie to the movie database.

        Checks if there is data in the database, if so
        Gets and checks title input.
        Checks title exists in the database, if not
        parses the data for the new movie into a dict
        and appends it into the dictionary loaded from
        the database. Updates the json file with it.

        Prints a message to inform the user of the operation
        result.
        """
        movies = self.read_movies()

        if len(movies) == 0:
            print("Currently there are no movies in the database")

        title = self.check_title()
        if title in movies.keys():
            print(f"{title} already exists in database")
            return
        else:
            #######------------------------------------------
            json_data = data_fetcher.get_new_movie_data(title)
            if json_data is None:
                print(f"Error fetching data for {title}")
            else:
                #movies[title] = json_data
                print("hi")
            #######------------------------------------------
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

        if len(movies) == 0:
            print("Currently there are no movies in the database")
            return

        title = self.check_title()
        if not title in movies:
            raise KeyError(f"Movie {title} doesn't exist!")
        else:
            del movies[title]
            self._update_json(movies)

        if title not in self.read_movies():
            print(f"Movie {title} successfully deleted")
        else:
            print("Something went wrong...")


    def update_movie(self): # menu command 4
        """
        Updates a movie rating from the movie database.

        Checks if there is data to update, if so
        Checks movie exists in the database, if so
        parses the data for the new movie into a dict
        and appends it into the dictionary loaded from
        the database. Updates the json file with it.

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
        else:
            new_rating = self.check_rating()
            movies[title]["rating"] = new_rating
            self._update_json(movies)

        if self.read_movies()[title]["rating"] == new_rating:
            print(f"Movie {title} successfully updated")
        else:
            print("Something went wrong...")

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
            "poster": "https://m.media-amazon.com/
                       images/...X300.jpg"
            }
        }
        """
        movie_dict_example = {
            "Titanic": {"rating": 9.0, "year": 1999,
                        "poster": "https://m.media-amazon.com/"
                            "images/M/MV5BYzYyN2FiZmUtYWYzMy00M"
                            "zViLWJkZTMtOGY1ZjgzNWMwN2YxXkEyXkF"
                            "qcGc@._V1_SX300.jpg"},
            "Up": {"rating": 8.3, "year": 2009,
                   "poster": "https://m.media-amazon.com/images/"
                             "M/MV5BNmI1ZTc5MWMtMDYyOS00ZDc2LTkz"
                             "OTAtNjQ4NWIxNjYyNDgzXkEyXkFqcGc@._"
                             "V1_SX300.jpg"},
            "The Godfather": {"rating": 9.0, "year": 1972,
                              "poster": "https://m.media-amazon."
                                "com/images/M/MV5BNGEwYjgwOGQtYj"
                                "g5ZS00Njc1LTk2ZGEtM2QwZWQ2NjdhZ"
                                "TE5XkEyXkFqcGc@._V1_SX300.jpg"}
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
        try:
            with open(file=self.file_path, mode='w',
                  encoding="utf-8") as handle:
                json.dump(updated_movie_dict, handle, indent=4)
        except Exception as e:
            print(f"Database wasn't updated: {e}")


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

        Calls read_movies() in case there isn't a json
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
        if title in movies.keys():
            print(f"{title} already exists in database")
            return

        new_movie_data = data_fetcher.get_new_movie_data(title)
        if new_movie_data is None:
            print(f"Error fetching data for {title}")
            return

        complete_title, movie_attributes = new_movie_data
        movies[complete_title] = movie_attributes
        self._update_json(movies)

        if title in self.read_movies().keys():
            print(f"{title} successfully added")


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

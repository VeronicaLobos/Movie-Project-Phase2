from storage.istorage import IStorage
import os
import csv

"""
This module loads/creates a Json file and performs
CRUD operations on it (persistent storage).
"""

class StorageCsv(IStorage):
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
                    "year": int(row["year"])
                }
        return movies_dictionary


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
                        "poster": "https://m.media-amazon.com/"
                            "images/M/MV5BYzYyN2FiZmUtYWYzMy00M"
                            "zViLWJkZTMtOGY1ZjgzNWMwN2YxXkEyXkF"
                            "qcGc@._V1_SX300.jpg"},
            {"title": "Up", "rating": 8.3, "year": 2009,
                   "poster": "https://m.media-amazon.com/images/"
                             "M/MV5BNmI1ZTc5MWMtMDYyOS00ZDc2LTkz"
                             "OTAtNjQ4NWIxNjYyNDgzXkEyXkFqcGc@._"
                             "V1_SX300.jpg"},
            {"title": "The Godfather", "rating": 9.0, "year": 1972,
                              "poster": "https://m.media-amazon."
                                "com/images/M/MV5BNGEwYjgwOGQtYj"
                                "g5ZS00Njc1LTk2ZGEtM2QwZWQ2NjdhZ"
                                "TE5XkEyXkFqcGc@._V1_SX300.jpg"}
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
            print(f"Database has been reset")
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
                writer.writerow(["title", "rating", "year"])
                for title, movie_data in movies_dict.items():
                    writer.writerow([title, movie_data["rating"],
                                     movie_data["year"]])
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

        Checks if there is data in the database, if so
        Gets and checks title input.
        Checks title exists in the database, if not
        parses the data for the new movie into a dict
        and appends it into the dictionary loaded from
        the database. Updates the csv file with it.

        Prints a message to inform the user of the operation
        result.
        """
        movies = self.read_movies()
        # poster = ...

        if len(movies) == 0:
            print("Currently there are no movies in the database")

        title = self.check_title()
        if title in movies:
            print(f"{title} already exists in database")
            return
        else:
            year = self.check_year()
            rating = self.check_rating()
            movies[title] = {
                "rating": rating,
                "year": year
            }
        self._update_csv(movies)

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
        if not title in movies:
            raise KeyError(f"Movie {title} doesn't exist!")

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
        else:
            new_rating = self.check_rating()
            movies[title]["rating"] = new_rating
            self._update_csv(movies)

        if self.read_movies()[title]["rating"] == new_rating:
            print(f"Movie {title} successfully updated")
        else:
            print("Something went wrong...")

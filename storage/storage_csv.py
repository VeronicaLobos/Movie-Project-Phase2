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
        fills the outer key, and the following columns are
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


    def read_movies(self):
        """
        Loads a csv file containing data about movies.

        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
            }
        }
        """
        movie_list_example = [
            {"title": "Titanic", "rating": 9.0, "year": 1999},
            {"title": "Up", "rating": 8.3, "year": 2009},
            {"title": "The Godfather", "rating": 9.0, "year": 1972}
        ]

        try:
            if not os.path.exists(self.file_path):
                with open(file=self.file_path, mode='w',
                    encoding='utf-8', newline='') as handle:
                    writer = csv.writer(handle)
                    header = ["title", "rating", "year"]
                    writer.writerow(header)
                    for movie in movie_list_example:
                        writer.writerow([movie["title"],
                            movie["rating"], movie["year"]])

                return self._parse_csv_to_dict()

            else:
                return self._parse_csv_to_dict()

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return {}
        except ValueError:
            print(f"Error parsing data in {self.file_path}")


    def _update_csv(self, updated_movie_dict):
        """
        Updates the database after performing RUD operation
        """
        with open(file=self.file_path, mode='w',
                  encoding="utf-8") as handle:
            pass


    def check_title(self):
        return super().check_title()


    def check_year(self):
        return super().check_year()


    def check_rating(self):
        return super().check_rating()


    def add_movie(self): # menu command 2
        """
        Adds a movie to the movie database.
        """
        pass


    def delete_movie(self): # menu command 3
        """
        Deletes a movie from the movie database.
        """
        pass


    def update_movie(self): # menu command 4
        """
        Updates a movie rating from the movie database.
        """
        pass

from storage.istorage import IStorage
import csv
import os


"""
This module loads/creates a csv file and performs
CRUD operations on it (persistent storage).
"""


class StorageCsv(IStorage): ## ???????????
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path


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
    movie_list_example = [{"title": "Titanic", "rating": 9.0, "year": 1999}]

    try:
        if not os.path.exists(self.file_path):
            with open(file=self.file_path, mode='w',
                      encoding="utf-8") as handle:
                writer = csv.writer(handle)
                header = ["title", "rating", "year"]
                writer.writerow(header)
                writer.writerows(movie_list_example)

        else:
            pass
    except Exception as e:
        print(e)
    pass


def _update_csv(self, updated_movie_dict):
     """
     Updates the database after performing RUD operation
     """
     with open(file=self.file_path, mode='w',
                  encoding="utf-8") as handle:
     pass


def check_title(self):
    return super()._check_title()


def check_year(self):
    return super()._check_year(self)


def check_rating(self):
    return super()._check_rating()


def add_movie(self):
    """
    Adds a movie to the movie database.
    """
    pass


def delete_movie(self):
    """
    Deletes a movie from the movie database.
    """
    pass


def update_movie(self):
    """
    Updates a movie rating from the movie database.
    """
    pass

    #### Methods to check input

"""
This program prints a user CLI, which instantiates
a Storage manager subclass for a json or csv file
database, with CRUD methods.

With that object instantiates and runs a MovieApp,
which contains methods for processing, formating
and printing the extracted data, and calling the
methods from Storage.
"""

from movie_app import MovieApp
from storage.storage_csv import StorageCsv
from storage.storage_json import StorageJson


if __name__ == "__main__":
    storage_json = StorageJson('data/movies.json')
    storage_csv = StorageCsv('data/movies.csv')
    movies_app = MovieApp(storage_json)
    movies_app.run()

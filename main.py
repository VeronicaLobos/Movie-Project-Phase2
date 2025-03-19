from movie_app import MovieApp
from storage.storage_csv import StorageCsv
from storage.storage_json import StorageJson


if __name__ == "__main__":
    """
    Imports and parses a Json file into a dictionary
    Creates an instance of the movie app with it
    """
    #storage = StorageJson('data/movies.json')
    storage = StorageCsv('data/movies.csv')
    movies_app = MovieApp(storage)
    movies_app.run()
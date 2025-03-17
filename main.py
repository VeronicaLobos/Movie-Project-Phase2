from movie_app import MovieApp
from storage.storage_csv import StorageCsv
#from storage.storage_json import StorageJson


##### Testing from here

def _print_movies(movies):
    # wip
    movies_dict = movies.list_movies()
    print(f"{len(movies_dict)} movie(s) in total")

    for title, attributes in movies_dict.items():
        print(f"{title} ({attributes['year']}): {attributes['rating']}")


if __name__ == "__main__":
    """
    Imports and parses a Json file into a dictionary
    Creates an instance of the movie app with it
    """
    #storage = StorageJson('data/movies.json')
    storage = StorageCsv('data/movies.csv')
    movies_app = MovieApp(storage)
    movies_app.run()
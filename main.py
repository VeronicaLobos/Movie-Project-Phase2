from movie_app import MovieApp
from storage.storage_json import StorageJson
import movie_app


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
    storage = StorageJson('data/movies.json')
    movies_app = MovieApp(storage)
    ## storage.add_movie('Up', 2009, 8.3, None)
    ## storage.delete_movie('Up')
    ## storage.update_movie('Up', 8.5)
    ## _print_movies(storage)
    movies_app.run()
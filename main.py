from movie_app import MovieApp
from storage.storage_json import StorageJson
import movie_app


##### The following commands will be moved later

def _check_title():
    """
    A utility command for checking correct input
    for a movie's title. Keeps prompting for input.
    Returns a string.
    """
    while True:
        movie_title = input("Enter movie name: ")
        if not movie_title:
            print("Title cannot be empty.")
            continue
        break
    return movie_title

def _check_year():
    """
    A utility command for checking correct input
    for a movie's release year. Keeps prompting for input.
    Returns an integer.
    """
    while True:
        try:
            movie_year = int(input("Enter new movie year: "))
            if (len(str(movie_year))) != 4 or not (
                    1894 <= movie_year <= 2030
            ):
                print("Please enter a valid year with four digits.")
                continue
        except (ValueError, TypeError):
            print("Please enter a valid year with four digits.")
        break
    return movie_year

def _check_rating():
    """
    A utility command for checking correct input
    for a movie's rating. Keeps prompting for input.
    Returns a float, rounds to a single decimal
    """
    while True:
        try:
            # movie_phase1 bonus3, round floats
            movie_rating = round(float(input(
                "Enter new Movie rating: ")), 1)
            if not 0.0 <= movie_rating <= 10.0:
                print("Rating must be a valid number"
                      "between 0.0 and 10.0")
                continue
        except (ValueError, TypeError):
            print("Rating must be a valid number"
                  "between 0.0 and 10.0")
            continue
        break
    return movie_rating


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
    app = MovieApp(storage)
    ## storage.add_movie('Up', 2009, 8.3, None)
    ## storage.delete_movie('Up')
    ## storage.update_movie('Up', 8.5)
    ## _print_movies(storage)
    app.run()
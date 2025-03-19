import requests as req
from dotenv import load_dotenv
import os


def get_movie_info(movie_title):
    """
    ????

    :param movie_title: The title of the movie to look for.
    :return: A json response as a string containing a dict
    of attributes from a movie.
    """
    load_dotenv()
    API_KEY = os.getenv("my_api_key")
    url = f"https://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

    try:
        response = req.get(url)
        response.raise_for_status() # handle bad responses
        print(f"Requesting '{movie_title}' to {url}")
        json_string = response.text
        if "Error" in json_string:
            print(json_string)
            return {}
    except ValueError as e:
        print(f"Error: {e}")
        return {}
    except NameError as e:
        print(f"Error: {e}")
        print("Check URL and API key and try again.")
        return {}


def get_new_movie_data(movie_title):
    """

    :return:
    """
    test = get_movie_info(movie_title)
    print(test)
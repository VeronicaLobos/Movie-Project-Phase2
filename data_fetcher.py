import requests as req
from dotenv import load_dotenv
import os
import json
import urllib3.exceptions

"""
A module for extracting movie data from OMDb API,
The Open Movie Database https://www.omdbapi.com/
a RESTful web service to obtain movie information.
"""


def _get_movie_rating(movie_info):
    """
    Fetches a movie rating.

    From the movie_info dictionary, extracts "Ratings",
    which value is a list of dictionaries.
    Iterates through all the dictionaries looking for
    one which attribute 'Source' contains the string
    "Internet Movie Database", then extracts it's
    corresponding attribute 'Value', and converts it
    to a float.

    Handles cases in which 'Value' is incorrect or
    there is no rating from Internet Movie Database.

    Returns a float.
    """
    all_ratings = movie_info.get('Ratings')
    for rating in all_ratings:
        if rating.get('Source') == "Internet Movie Database":
            rating_str = rating.get('Value')
            try:
                rating_float = float(rating_str.split("/")[0])
                return rating_float
            except (ValueError, IndexError):
                print("IMDb rating not found.")
                return 0


def _get_movie_info(movie_title):
    """
    Fetches movie information from the OMDb API based
    on the provided movie title.

    This function makes a request to the OMDb API using
    the given movie title and your API key.
    It parses the JSON response into a Python dictionary
    containing movie attributes.

    :param movie_title: The title of the movie to look for.
    Returns a dictionary containing movie attributes if
    found, or an empty dictionary if not found or an
    error occurs.
    """
    load_dotenv()
    API_KEY = os.getenv("my_api_key")
    url = f"https://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

    try:
        response = req.get(url)
        response.raise_for_status() # handle bad responses
        print(f"Requesting '{movie_title}' to {url}")
        json_string = response.text
        movie_info_dict = json.loads(json_string)
        if "Movie not found!" in json_string:
            print(json_string)
            return {}
        else:
            return movie_info_dict

    except NameError as e:
        print(f"Error: {e}")
        print("Check URL and API key and try again.")
        return {}
    except KeyError as e:
        print(f"Key Error: {e}")
        print("Check if the API key 'my_api_key' is set "
              "in your environment variables.")
        return {}
    except req.exceptions.ConnectionError as e:
        if isinstance(e.args[0], urllib3.exceptions.NameResolutionError):
            print(f"Name Resolution Error: {e}")
        else:
            print(f"Connection Error: {e}")
        print(e)
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return {}
    except (req.exceptions.HTTPError,
            req.exceptions.RequestException) as e:
        print(f"HTTP Error: {e}")
        return {}


def get_new_movie_data(movie_title):
    """
    Fetches and formats movie data from the OMDb API.

    This function takes a movie title, fetches movie
    information using _get_movie_info(), extracts the
    IMDb rating, year, and poster URL.
    If the title contains spaces, replaces them with
    "+".
    Returns a dictionary containing the extracted
    info as a dict of attributes.
    Returns an empty dictionary if any error occurs
    or if movie data is not found.
    """
    title = movie_title.replace(" ", "+")
    movie_info = _get_movie_info(title)
    if movie_info != {}:
        try:
            title = str(movie_info.get("Title"))
            rating = _get_movie_rating(movie_info)
            year = int(movie_info.get("Year"))
            poster_url = movie_info.get("Poster")

            new_movie_dict = {'rating': rating,
                              'year': year,
                              'poster': poster_url}
            return title, new_movie_dict
        except TypeError as e:
            print(e)
        except UnboundLocalError as e:
            print(e)
            return {}


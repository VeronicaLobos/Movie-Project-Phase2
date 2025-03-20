"""
A simple program to request the HTML and CSS from
the demo website from this school assignment.

It's meant to run independently of main.
"""
import os
import requests as req

URL = ("https://elementsamba-comradebinary.codio.io/"
       ".guides/demo/_static/expected_index.html")
URL_STYLE = ("https://elementsamba-comradebinary.codio.io/"
             ".guides/demo/_static/style.css")

html_file_path = os.path.join("_static", "index_template.html")
css_file_path = os.path.join("_static", "style.css")


def web_fetcher(file_path, url):
    """
    Fetches the content from a given URL and saves
    it to a specified file.

    Overwrites any existing files, asks for
    confirmation input.

    Handles errors for bad responses, or any other
    generic errors.
    """
    try:
        response = req.get(url)
        response.raise_for_status()
        website_content = response.text

        if os.path.exists(file_path):
            option = input(f"{file_path} already exists,"
                           f" overwrite? Y/N: ")
            if option.lower() != "y":
                print("File not overwritten.")
                return

        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(website_content)
            print(f"{file_path} successfully saved.")

    except req.exceptions.Timeout as e:
        print("Request timed out after 10 seconds: ", e)
    except req.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print("A generic error occurred: ", e)


web_fetcher(html_file_path, URL)
web_fetcher(css_file_path, URL_STYLE)

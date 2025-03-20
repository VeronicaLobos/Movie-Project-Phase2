"""
A simple program to request the html and css from
the demo website from this school assignment.

Generates an example
"""

import requests

URL = "https://elementsamba-comradebinary.codio.io/.guides/demo/_static/expected_index.html"
URL_STYLE = "https://elementsamba-comradebinary.codio.io/.guides/demo/_static/style.css"
html_file_path = "_static/index_template.html"
css_file_path = "_static/style.css"

def web_fetcher(file_path, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        website_content = response.text


        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(website_content)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print("A generic error occurred: ", e)


web_fetcher(html_file_path, URL)
web_fetcher(css_file_path, URL_STYLE)

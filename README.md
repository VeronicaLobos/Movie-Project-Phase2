# Movie App Project - Phase 2

This project is a Python-based application that manages a movie database. It allows users to interact with the database through a command-line interface (CLI), performing CRUD (Create, Read, Update, Delete) operations on movie data. The project fetches movie data from the OMDb API and stores it in either a **JSON** file (`movies.json`) or a **CSV** file (`data/movies.csv`) for persistent storage. It also includes a basic web page template to display movie information.

<img width="500" alt="Generated website preview" style="display: block; margin: 0 auto" src="https://github.com/user-attachments/assets/23b372e5-00ac-48f0-935d-1cf5e7ea59e0" />

## Key Features

*   **Movie Database Management:**
    *   **Add Movies:** Add new movies to the database by title, fetching details from the OMDb API.
    *   **Delete Movies:** Remove movies from the database.
    *   **Update Movies:** Modify the rating of existing movies.
    *   **Persistent Storage:** Movie data can be stored in either a **JSON** file (`movies.json`) or a **CSV** file (`data/movies.csv`), ensuring data persistence between sessions.
*   **User Interface:**
    *   **List Movies:** Display all movies in the database.
    *   **Rating Stats:** Calculate and display statistics about the movies in the database.
    *   **Filter by Title:** Search for movies by title.
    *   **Sort by Rating:** Sort movies by rating.
    *   **Random Movie:** Display a random movie from the database.
*   **Data Fetching:**
    *   Utilizes the OMDb API to retrieve movie details (title, year, IMDB rating, poster URL).
    *   The `data_fetcher.py` module handles the API requests.
*   **Web Page Template:**
    *   Includes a basic HTML template (`index_template.html`) and CSS stylesheet (`style.css`) to display movie information.
    *   `index.html` is a copy of the index_template.html file with placeholders for movie data cards with the info of each movie.
    *   The `web_extractor.py` script can be used to fetch the HTML and CSS from a demo website, providing a starting point for the web interface.
*   **Error Handling:**
    *   The program handles potential errors like API request failures, file not found, corrupted JSON or CSV files, and user input errors.
*   **User Interaction:**
    *   The program interacts with the user through the command line, prompting for input and providing feedback.
    *   The program presents a menu with the following options:
        *   `0. Exit`: Exits the application.
        *   `1. List movies`: Displays all movies in the database.
        *   `2. Add movie`: Adds a new movie to the database.
        *   `3. Delete movie`: Deletes a movie from the database.
        *   `4. Update movie`: Updates the rating of a movie in the database.
        *   `5. Stats`: Displays statistics about the movies in the database.
        *   `6. Random movie`: Displays a random movie from the database.
        *   `7. Search movie`: Searches for movies by title.
        *   `8. Movies sorted by rating`: Sorts movies by rating.
        *   `9. Generate website`: Generates a basic HTML website to display the movie data.

## Installation

1.  **Clone the Repository:**
    ```
    bash git clone <your-repository-url> cd Movie-Project-Phase2
    ```
2. **Create a `.env` File:**
    *   Create a file named `.env` in the project's root directory.
    *   Add your OMDb API key to the `.env` file in the following format:
    ```
    my_api_key="YOUR_OMDB_API_KEY" 
    ```
    *   You can get a free API key from http://www.omdbapi.com/.

3.  **No external dependencies are needed.** The project uses only built-in Python libraries.

## Usage

1.  **Run the Application:**
    *   The main entry point for the program is `main.py`.
    *   Run it using:
    ```
    bash python main.py
    ```
    *   The program will then present a menu of options for interacting with the movie database.
2.  **Run the Web Extractor:**
    *   You can run the `web_extractor.py` file to download the HTML and CSS files from the demo website.
    ```
    bash python web_extractor.py
    ```
    *   This will create the `_static` folder and download the `index_template.html` and `style.css` files.
3.  **Database files**
    *   The database files are:
        *   `movies.json`: JSON database file. It is created in the root folder of the project.
        *   `data/movies.csv`: CSV database file. It is a sample database.

## Project Structure

*   `.idea/`: Contains PyCharm project settings (including `.gitignore`).
*   `.env`: Stores the OMDb API key (not included in this repository).
*   `_static/`: Contains the HTML template (`index_template.html`), the HTML page with placeholders for movie data cards and main heading (`index.html`), and CSS stylesheet (`style.css`).
*   `storage/`: Contains the `storage_json.py` and `storage_csv.py` files, which handle JSON and CSV file operations, respectively.
*   `istorage.py`: Defines the abstract class interface `IStorage` for storage operations.
*   `data/`: Contains the`movies.json` and `movies.csv` files, which is a sample database.
*   `web_extractor.py`: An independent script. Fetches HTML and CSS from a demo website of your choosing. Mine was provided by my school.
*   `data_fetcher.py`: Handles the API requests to OMDb.
*   `main.py`: The main entry point of the application.

## Contributing

This project was developed as part of a bootcamp curriculum. Feel free to use it as a learning resource or modify it for your own purposes. Contributions are welcome!

## Notes

*   The `movies.json` and `movies.csv` files are created automatically when you run the application for the first time. No need to use the samples provided in `data\`.
*   The `storage_json.py` and `storage_csv.py` files implement the `IStorage` interface.
*   The program uses the `.env` file to get the API key. You'll need to include it for the command Add Movies to properly function.

from abc import ABC, abstractmethod

"""
This module contains an abstract class IStorage
which performs CRUD operations on persistent storage.
"""


class IStorage(ABC):
    @abstractmethod
    def read_movies(self):
        """Loads a file containing data about movies"""
        pass

    def check_title(self):
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


    def check_year(self):
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


    def check_rating(self):
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


    @abstractmethod
    def add_movie(self):
        """Adds a movie to a movie database
        Asks input for title, year, rating, poster"""
        pass

    @abstractmethod
    def delete_movie(self):
        """Deletes a movie from a movie database
        Asks input for title"""
        pass

    @abstractmethod
    def update_movie(self):
        """Updates a movie rating from a movie database
        Asks input for title, rating"""
        pass

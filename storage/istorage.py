from abc import ABC, abstractmethod
import json
import csv

"""
This module contains an abstract class IStorage
which performs CRUD operations on persistent storage.
"""


class IStorage(ABC):
    @abstractmethod
    def read_movies(self):
        """Loads a file containing data about movies"""
        pass


    def _reset_database(self):
        """
        A utility command for read_movies() method.

        Deletes the contents of the CSV and populates
        it with the example data.
        Called as a result of corrupt files.
        """
        try:
            #self.file_path = "data/movies.csv"
            print(f"Reseting {self.file_path}...")
            if ".json" in self.file_path:
                with open(file=self.file_path, mode='w',
                      encoding="utf-8") as handle:
                    json.dump({}, handle, indent=4)
            elif ".csv" in self.file_path:
                with open(file=self.file_path, mode='w',
                    encoding='utf-8', newline='') as handle:
                    writer = csv.writer(handle)
                    header = ["title", "rating", "year"]
                    writer.writerow(header)
        except FileNotFoundError:
            print("or here")
            return self.read_movies()


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


    #@abstractmethod
    def add_movie(self):
        """Adds a movie to a movie database
        Asks input for title, year, rating, poster"""
        pass

    #@abstractmethod
    def delete_movie(self):
        """Deletes a movie from a movie database
        Asks input for title"""
        pass

    #@abstractmethod
    def update_movie(self):
        """Updates a movie rating from a movie database
        Asks input for title, rating"""
        pass

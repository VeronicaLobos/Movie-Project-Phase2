from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Loads a file containing data about movies"""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Adds a movie to a movie database"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Deletes a movie from a movie database"""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """Updates a movie rating from a movie database"""
        pass

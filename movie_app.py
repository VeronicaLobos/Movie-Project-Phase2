import sys
import statistics
import random


class MovieApp:
    def __init__(self, storage):
        """
        A MovieApp class that contains all the logic of the movie app (menu, commands etc.).
        The MovieApp class will have a member (field) from the type IStorage.
        """
        self._storage = storage


    def _command_list_movies(self): # menu command 1
        """
        Fetches the data from the database as a dictionary
        Prints the number of movies listed in it
        Prints the info stored as formated strings, example:
            3 movie(s) in total
            Titanic (1999): 9
        """
        movies_dict = self._storage.read_movies()

        print(f"{len(movies_dict)} movie(s) in total")

        for title, attributes in movies_dict.items():
            print(f"{title} ({attributes['year']}): {attributes['rating']}")


    def _command_movie_stats(self):
        """
        Calculates and print statistics about the movies in
        the database: average rating, median rating, titles
        with the highest and lowest rating.

        Informs the user when there are no stats to show
        Makes a list with all the ratings in the database
        Prints the average and median averages in the database
        Makes a list of tuples with movie ratings and titles
        Sorts the list of tuples from lowest to highest rating
        Prints the movie(s) with the highest rating
        Prints the movie(s) with the lowest rating
        """
        movies_dict = self._storage.read_movies()
        if len(movies_dict) < 1:
            print("Currently there are no movies in the database.")
            return

        ratings = [movie['rating'] for movie in movies_dict.values()]
        average_rating = round(statistics.mean(sorted(ratings)), 2)
        print(f"\nAverage rating: {average_rating}")
        median_rating = round(statistics.median(sorted(ratings)), 2)
        print(f"Median rating: {median_rating}")

        rated_movies = [(movie_attributes['rating'], movie_title)
            for movie_title, movie_attributes in movies_dict.items()]
        sorted_ratings_title = sorted(rated_movies,
                                      key=lambda rating: rating[0])

        best_rating = max(sorted_ratings_title, key=lambda x: x[0])[0]
        best_movies = [movie for movie in rated_movies if movie[0] == best_rating]
        worst_rating = min(sorted_ratings_title, key=lambda x: x[0])[0]
        worst_movies = [movie for movie in rated_movies if movie[0] == worst_rating]

        best_worst = [("Best", best_movies), ("Worst", worst_movies)]
        for extremes, movies in best_worst:
            if len(movies) == 1:
                print(f"{extremes} movie: {movies[0][1]}, {movies[0][0]}")
            else:
                output_string = f"{extremes} movies: "
                for rating, title in movies:
                    output_string += f"{title}, {rating}, "
                print(output_string[:-2])



    def _generate_website(self):
        pass


    ####### run() utility commands

    def __command_dispatcher(self, user_input):
        """
        Pairs the menu options (key) with the functions
        available to the user in the CLI program (value).
        Returns a function call.
        """
        print("")

        commands = {
            0: self._exit_my_movies,  #tested
            1: self._command_list_movies,  #tested
            2: self._storage.add_movie,  #tested
            3: self._storage.delete_movie,  #tested
            4: self._storage.update_movie,  #tested
            5: self._command_movie_stats,  # movie_phase1
            #    6: movie_stats.random_movie,  # movie_phase1
            #    7: movie_stats.search_movie,  # movie_phase1
            #    8: movie_stats.sort_by_rating,  # movie_phase1
            #    9: movie_stats.sort_by_year, # movie_phase1_bonus_1
            #    10: movie_stats.filter_movies, # movie_phase1_bonus_2
        }

        try:
            return commands[user_input]()
        except KeyError:
            print(f"Choice currently not available")


    def _exit_my_movies(self): # menu command 0
        """
        Prints a message and exits the CLI.
        """
        print("Bye!")
        sys.exit()


    def __get_valid_user_input(self):
        """
        Prints menu with available commands
        Asks user for input, a number between 0 and 10
        Else, will continue asking for a valid input
        Returns an integer
        """
        while True:
            try:
                user_input = int(input("Enter choice (0-10): "))
                return user_input
            except ValueError:
                print("Please enter a valid number")
                continue


    def __print_menu(self):
        """
        Prints a menu with the number corresponding to
        the available commands.
        """
        menu = ("\nMenu:\n"
                "0. Exit\n"
                "1. List movies\n"
                "2. Add movie\n"
                "3. Delete movie\n"
                "4. Update movie\n"
                "5. Stats\n"
                "6. Random movie\n"
                "7. Search movie\n"
                "8. Movies sorted by rating\n"
                "9. Movies sorted by year\n"
                "10. Filter movies\n")
        print(menu)


    def run(self):
        """
        A command line interface with a command_dispatcher
        that performs SCRUM operations with a dictionary.

        1. Displays a program title
        2. Displays a menu with the operations available
        3. Requests and checks input from user
        4. Executes a command based on input
        5. Menu is displayed again, asks for input again
        """
        print("********** My Movies Database **********")
        while True:
            try:
                self.__print_menu()
                user_input = self.__get_valid_user_input()
                self.__command_dispatcher(user_input)
                input("\nPress enter to continue ")
            except ValueError:
                print("Please enter a valid number")
                continue

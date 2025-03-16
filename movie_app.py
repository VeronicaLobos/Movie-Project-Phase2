import sys

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
        movies_dict = self._storage.list_movies() #from a module that loads a json file

        print(f"{len(movies_dict)} movie(s) in total")

        for title, attributes in movies_dict.items():
            print(f"{title} ({attributes['year']}): {attributes['rating']}")


    def _command_movie_stats(self):
        pass


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
            #    2: add_movie,  # movie_phase2
            #    3: delete_movie,  # movie_phase2
            #    4: update_movie,  # movie_phase2
            #    5: movie_stats.show_stats,  # movie_phase1
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

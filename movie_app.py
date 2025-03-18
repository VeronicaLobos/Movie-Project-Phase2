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
        Handles cases in which the csv file could be corrupt
        or wrongly formated.

        Prints the number of movies listed in it
        Prints the info stored as formated strings, example:
            3 movie(s) in total
            Titanic (1999): 9
        """
        try:
            movies_dict = self._storage.read_movies()

            print(f"{len(movies_dict)} movie(s) in total")

            for title, attributes in movies_dict.items():
                print(f"{title} ({attributes['year']}):"
                      f" {attributes['rating']}")

        except (TypeError, FileNotFoundError) as e:
            """Deletes the contents of the CSV and populates 
            it with the example data."""
            print("Data base might be corrupt", e)
            corrupt_movies_dict = self._storage.read_movies()
            print(corrupt_movies_dict)
            self._storage._reset_csv_file()


    def __get_rated_movies(self):
        """
        A utility command for extracting all the titles and ratings
        from the movie database.
        Returns a list with tuples (rating, title).
        """
        movies_dict = self._storage.read_movies()

        rated_movies = [(movie_attributes['rating'], movie_title)
                        for movie_title, movie_attributes in movies_dict.items()]

        return rated_movies


    def _command_movie_stats(self): # menu command 5
        """
        Calculates and print statistics about the movies in
        the database: average rating, median rating, titles
        with the highest and lowest rating.

        - Fetches the data from the database as a dictionary

        - Calculates and prints average and median ratings
        1. Informs the user when there are no stats to show
        2. Makes a list with all the ratings in the database
        3. Prints the average and median averages in the database

        - Calculates highest and lowest ratings,
        prints movie(s) with highest and lower rating
        4. Calls __get_rated_movies() to get a list of
        tuples containing movie titles and their ratings
        Sorts the list of tuples from lowest to highest rating
        5. Finds the highest and lowest rating from the sorted
        list
        Makes a list with movie(s) matching the highest rating,
        and a list with movie(s) matching the lowest rating
        6. Prints the movie(s) in those lists formated as strings
        (all the movies that share that rating if there is more
        than one)
        """
        movies_dict = self._storage.read_movies()

        ## Step 1
        if len(movies_dict) < 1:
            print("Currently there are no movies in the database.")
            return

        ## Step 2
        ratings = [movie['rating'] for movie in movies_dict.values()]

        ## Step 3
        average_rating = round(statistics.mean(sorted(ratings)), 2)
        print(f"\nAverage rating: {average_rating}")
        median_rating = round(statistics.median(sorted(ratings)), 2)
        print(f"Median rating: {median_rating}")

        ## Step 4
        rated_movies = self.__get_rated_movies()
        sorted_rated_movies = sorted(rated_movies,
                                      key=lambda rating: rating[0])

        ## Step 5
        best_rating = max(sorted_rated_movies, key=lambda x: x[0])[0]
        best_movies = [movie for movie in rated_movies if movie[0] == best_rating]
        worst_rating = min(sorted_rated_movies, key=lambda x: x[0])[0]
        worst_movies = [movie for movie in rated_movies if movie[0] == worst_rating]

        ## Step 6
        best_worst = [("Best", best_movies), ("Worst", worst_movies)]
        for extremes, movies in best_worst:
            if len(movies) == 1:
                print(f"{extremes} movie: {movies[0][1]}, {movies[0][0]}")
            else: ##  When more than one movie has that rating
                output_string = f"{extremes} movies: "
                for rating, title in movies:
                    output_string += f"{title}, {rating}, "
                print(output_string[:-2])


    def _command_random_movie(self): # menu command 6
        """
        Prints the title and rating of a random movie
        from the database.

        - Calls __get_rated_movies() to get a list of
        tuples containing movie titles and their ratings
        - Randomly chooses a tuple from the list
        - Prints the tuple formated as a string
        """
        rated_movies = self.__get_rated_movies()
        random_movie = random.choice(rated_movies)

        print(f"Your movie for tonight:. {random_movie[1]}, "
              f"it's rated {random_movie[0]}")


    def _command_search_movie(self): # menu command 7
        """
        Asks the user to enter a part of a movie name,
        and then searches all the movies in the database.
        Prints all the movies that matched the user’s query,
        along with the rating. If there is no match it will
        print a message informing the user.
        """
        rated_movies = self.__get_rated_movies()
        search_term = input("Enter part of movie name: ").lower()
        match_found = False

        matches = [(rating, title) for (rating, title) in rated_movies if
                 search_term in title.lower()]

        if matches:
            for rating, title in matches:
                print(f"{title}, {rating}")
                match_found = True

        if not match_found:
            print("Movie matching search term not found")


    def _command_sort_by_rating(self): # menu command 8
        """
        Fetches and sorts movies sorted by descending rating.
        Prints all the movies and their ratings, in descending
        order by the rating.
        """
        rated_movies = self.__get_rated_movies()

        movies_sorted_desc_rating = sorted(rated_movies,
                                           key=lambda movies: movies[0],
                                           reverse=True)

        for rating, title in movies_sorted_desc_rating:
            print(f"{title}: {rating}")


    def _generate_website(self): # menu command 9
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
            5: self._command_movie_stats,  #tested
            6: self._command_random_movie,  #tested
            7: self._command_search_movie,  #tested
            8: self._command_sort_by_rating,  #tested
            9: self._generate_website, #wip
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
                user_input = int(input("Enter choice (0-9): "))
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
                "9. Generate website\n")
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

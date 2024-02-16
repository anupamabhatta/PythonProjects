import csv
from pathlib import Path
import pprint as pp


# Setup Code (DO NOT MODIFY)

ratings_count_check = {"PG": 3, "PG-13": 9, "R": 45, "Not Rated": 6, "Passed": 1, "Unrated": 1}

action_movies_check = {
    "Title": "The Mummy",
    "Year": 1999,
    "Rated": "PG-13",
    "Released": "07 May 1999",
    "Runtime": 124,
    "Genre": "Action, Adventure, Fantasy",
    "Director": "Stephen Sommers",
    "Writer": "Stephen Sommers, Lloyd Fonvielle, Kevin Jarre",
    "Actors": "Brendan Fraser, Rachel Weisz, John Hannah",
    "Plot": (
        "At an archaeological dig in the ancient city of Hamunaptra, an "
        "American serving in the French Foreign Legion accidentally awakens "
        "a mummy who begins to wreak havoc as he searches for the "
        "reincarnation of his long-lost love."
    ),
    "Language": "English, Egyptian (Ancient), Arabic, Chinese, Hebrew, Hungarian",
    "Country": "United States",
    "Awards": "Nominated for 1 Oscar. 5 wins & 24 nominations total",
    "imdbRating": "7.1",
}

horror_movies_filt_check = {
    "Actors": "Marilyn Burns, Edwin Neal, Allen Danziger",
    "Awards": "1 win & 2 nominations",
    "Country": "United States",
    "Director": "Tobe Hooper",
    "Genre": "Horror",
    "Language": "English",
    "Plot": (
        "Five friends head out to rural Texas to visit the grave of a "
        "grandfather. On the way they stumble across what appears to be a "
        "deserted house, only to discover something sinister within. "
        "Something armed with a chainsaw."
    ),
    "Rated": "R",
    "Released": "11 Oct 1974",
    "Runtime": 83,
    "Title": "The Texas Chain Saw Massacre",
    "Writer": "Kim Henkel, Tobe Hooper",
    "Year": 1974,
    "imdbRating": "7.4",
}

writers_in_movies_check = {
    "Actors": "Jack Nicholson, Shelley Duvall, Danny Lloyd",
    "Awards": "4 wins & 8 nominations",
    "Country": "United Kingdom, United States",
    "Director": "Stanley Kubrick",
    "Genre": "Drama, Horror",
    "Jumpscare_count": 3,
    "Jumpscare_rating": "0.5",
    "Language": "English",
    "Plot": (
        "A family heads to an isolated hotel for the winter where a sinister "
        "presence influences the father into violence, while his psychic son "
        "sees horrific forebodings from both past and future."
    ),
    "Rated": "R",
    "Released": "13 Jun 1980",
    "Runtime": 146,
    "Title": "The Shining",
    "Writer": "Stephen King, Stanley Kubrick, Diane Johnson",
    "Year": 1980,
    "imdbRating": "8.4",
}

long_writers_movies_check = {
    "Actors": "Chad Michael Murray, Paris Hilton, Elisha Cuthbert",
    "Awards": "5 wins & 11 nominations",
    "Country": "Australia, United States",
    "Director": "Jaume Collet-Serra",
    "Genre": "Horror, Thriller",
    "Jumpscare_count": 16,
    "Jumpscare_rating": 4,
    "Language": "English",
    "Plot": (
        "A group of teens are unwittingly stranded near a strange wax museum "
        "and soon must fight to survive and keep from becoming the next "
        "exhibit."
    ),
    "Rated": "R",
    "Released": "06 May 2005",
    "Runtime": 113,
    "Title": "House of Wax",
    "Writer": "Charles Belden, Chad Hayes, Carey W. Hayes",
    "Year": 2005,
    "imdbRating": "5.4",
}

recent_movies_check = {
    "Actors": "Emily Blunt, John Krasinski, Millicent Simmonds",
    "Awards": "Nominated for 1 Oscar. 34 wins & 124 nominations total",
    "Country": "United States",
    "Director": "John Krasinski",
    "Genre": "Drama, Horror, Sci-Fi",
    "Jumpscare_count": 14,
    "Jumpscare_rating": 4,
    "Language": "American Sign , English",
    "Plot": (
        "In a post-apocalyptic world, a family is forced to live in silence "
        "while hiding from monsters with ultra-sensitive hearing."
    ),
    "Rated": "PG-13",
    "Released": "06 Apr 2018",
    "Runtime": 90,
    "Title": "A Quiet Place",
    "Writer": "Bryan Woods, Scott Beck, John Krasinski",
    "Year": 2018,
    "imdbRating": "7.5",
}

horror_w_js_movies_check = {
    "Actors": "Naomi Watts, Martin Henderson, Brian Cox",
    "Awards": "14 wins & 12 nominations",
    "Country": "United States, Japan",
    "Director": "Gore Verbinski",
    "Genre": "Horror, Mystery",
    "Jumpscare_count": 9,
    "Jumpscare_rating": "2.5",
    "Language": "English",
    "Plot": (
        "A journalist must investigate a mysterious videotape which seems to "
        "cause the death of anyone one week to the day after they view it."
    ),
    "Rated": "PG-13",
    "Released": "18 Oct 2002",
    "Runtime": 115,
    "Title": "The Ring",
    "Writer": "Ehren Kruger, Kôji Suzuki, Hiroshi Takahashi",
    "Year": 2002,
    "imdbRating": "7.1",
}
# End of Setup Code


def calculate_avg(movies, score_type):
    """
    This function calculates the average score based off of the parameter passed and returns a
    float value rounded off to one decimal point


    Parameters:
    movies (list): A list of dictionaries containing all the movie data
    score_type (string): The type of score (e.g., "imdbRating", "Jump Scare Rating") to calculate
                         the average for.


    Returns:
    float: A float value indicating the average value, rounded to one decimal point
    """
    total_score = 0.0
    num_movies = 0

    for movie in movies:
        score = get_value(movie, score_type)
        if score is not None:
            total_score += float(score)
            num_movies += 1

    if num_movies == 0:
        return 0.0
    else:
        return round(total_score / num_movies, 1)


def check_movie_runtime(movies, runtime):
    """
    Checks if the 'Runtime' value of a movie is greater than the supplied runtime value.


    Parameters:
    movies (dict): A list of dictionaries containing information about all the movies.
    runtime (int): An integer value that represents the threshold runtime


    Returns:
    list: returns a list of movie dictionaries that satisfy the set condition
    """
    accumulator = []
    for movie in movies:
        movie_runtime = int(movie.get("Runtime", 0))
        if movie_runtime >= runtime:
            accumulator.append(movie)
    return accumulator


def clean_row(movie):
    """
    Uses error handling to try to apply both helper functions < clean_runtime() >
    and < convert_to_int() > to the movie dictionary, if there is an error, only apply
    the < convert_to_int() > function.


    Parameter:
    movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
    dict: dictionary containing key-value pairs representing data for one movie
    """
    try:
        movie = clean_runtime(movie)
        movie = convert_to_int(movie)
    except KeyError:
        movie = convert_to_int(movie)
    return movie


def clean_runtime(movie):
    """
    Accesses the value of the key 'Runtime' (str) and separates the number value and the unit
    by splitting the string. Assigns only the number value back to the key 'Runtime'.


    Parameters:
    movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
    dict: dictionary containing key-value pairs representing data for one movie
    """
    if 'Runtime' in movie:
        movie['Runtime'] = movie['Runtime'].split()[0]
    return movie


def convert_to_int(movie):
    """
    Loops through movie's key-value pairs and implement an error handling to
    check if each value can be converted to an integer.
    If possible, the value is converted and assigned back to its key.


    Parameters:
    movie (dict): dictionary containing key-value pairs representing data for one movie
    Returns:
    dict: dictionary containing key-value pairs representing data for one movie
    """
    for key, value in movie.items():
        try:
            movie[key] = int(value)
        except ValueError:
            continue
    return movie


def count_movie_by_rating(movies, rating):
    """
    Loops through movies (list) and check if rating (str) is included in the dictionary key: 'Rated'.
    Increment the count by 1 if the given rating matches the movie's rating.


    Parameters:
    movies (list): List of dictionaries representing all movies
    rating (str): Audience Rating of the movie to check for
    Returns:
    int: Number of movies that have the supplied Rating
    """
    count = 0
    for movie in movies:
        if rating.lower() == movie.get("Rated", "").lower():
            count += 1
    return count


def filter_movie_by_genre(movies, genre):
    """
    Loops through movies (list) and check if genre (str) is included in the dictionary key: 'Genre'.
    Append the dictionary and all of its data to an empty list and return the final list.


    Parameters:
    movies (list): List of dictionaries representing all movies
    genre (str): Movie genre to check for
    Returns:
    list: List with movie dictionaries that include the supplied genre
    """
    accumulator = []
    for movie in movies:
        if genre.lower() in movie.get("Genre", "").lower():
            accumulator.append(movie)
    return accumulator


def filter_movies_by_year_and_imdb(movies, year_lower_limit, year_upper_limit, imdb_score):
    """
    Checks if a movie was released between the upper and lower limits of the release
    year and if the imdb score of the movie is greater than 7.0


    Parameters:
    movies (dict): A dictionary of key-value pairs from multiple movies
    lower_limit (int): Integer value of the lower limit year value
    upper_limit (int): Integer value of the upper limit year value
    imdb_score (float): Float value of the threshold imdb score


    Returns:
    list: a list of dictionaries of horror movies that satisfy the above conditions
    """
    filtered_movies = []

    for movie in movies:
        year = int(movie.get("Year", 0))
        imdb_rating = float(movie.get("imdbRating", 0.0))  # Convert IMDb rating to float
        if year_lower_limit <= year <= year_upper_limit and imdb_rating >= imdb_score:
            filtered_movies.append(movie)
    return filtered_movies


def get_awards(movie, award_key):
    """
    Returns a string based on whether or not the movie has been nominated for or has
    won an Oscar. If the keyword exists, it returns the parameter of the movie, if it does not
    it returns False.


    Parameters:
    movie (dictionary): Contains all the data about one movie
    parameter (string): The key we are looking for in the dictionary


    Returns:
    string: list of awards if the value exists
    bool: returns False if the movie has not been nominated or won an Oscar
    """
    awards_info = movie.get(award_key, "")
    if "oscar" in awards_info.lower():
        return awards_info
    return None


def get_jumpscare_data(jumpscare_data, movie_title):
    """
    Loops through jumpscare data (list) and check to see if the value of the key 'Movie Name'
    matches the supplied movie_title (str) and returns the values of the keys 'Jump Count'
    and 'Jump Scare Rating' as a tuple


    Parameters:
    jumpscare_data (list): information about the movie's jump scares
    movie_title (str): value of the key 'Title' from a movie dictionary


    Returns:
    tuple: A tuple with the first value representing a jump count and the second value
    representing a jump scare rating. Both of these tuples should be None if the
    movie name does not exist in the jumpscare_data list.
    """
    for movie in jumpscare_data:
        if movie_title.lower() == movie.get("Movie Name", "").lower():
            return movie.get("Jump Count", ""), movie.get("Jump Scare Rating", "")
    return None, None


def get_value(movie, key_to_check):
    """
    This function checks if a parameter value exists or not in the dictionary, if it does it
    returns the value, else it returns False


    Parameters:
    movie (dict): a dictionary containing all the data about one movie
    key_to_check (string): a parameter of the dictionary


    Returns:
    value : if the value exists, return the value of the parameter. can be a string, float
    or int based on which parameter is being passed.
    None: if the value does not exist, return None
    """
    if key_to_check in movie:
        return movie[key_to_check]
    return None


def read_csv_to_dicts(filepath, encoding="utf-8", newline="", delimiter=","):
    """
    Accepts a file path for a .csv file to be read, creates a file object,
    and uses csv.DictReader() to return a list of dictionaries
    that represent the row values from the file.


    Parameters:
    filepath (str): path to csv file
    encoding (str): name of encoding used to decode the file
    newline (str): specifies replacement value for newline '\n'
    or '\r\n' (Windows) character sequences
    delimiter (str): delimiter that separates the row values


    Returns:
    list: nested dictionaries representing the file contents
    """

    with open(filepath, "r", newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line)
    return data


def search_movie_writer(movie, search_terms):
    """
    Loops through the search terms and use a conditional statement to check whether each
    search term appears in the movie's writers. If the search term is in the movie writers this
    function returns True, if the search term is not in the movie's writers, this function will
    return False


    Parameters:
    movie (dict): A dictionary containing information about one movie.


    search_terms (list): A list of search terms as strings


    Returns:
    bool: True if term appears in the writers, otherwise False
    """
    for term in search_terms:
        if term.lower() in movie.get("Writer", "").lower():
            return True
    return False


def write_dicts_to_csv(filepath, data, fieldnames, encoding="utf-8", newline=""):
    """
    Uses csv.DictWriter() to write a list of dictionaries to a target CSV file as row data.
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.


    Parameters:
    filepath (str): path to target file (if file does not exist it will be created)
    data (list): dictionary content to be written to the target file
    fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
    encoding (str): name of encoding used to encode the file
    newline (str): specifies replacement value for newline '\n'
    or '\r\n' (Windows) character sequences


    Returns:
    None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    """
    This function serves as the point of entry and controls the flow of this Python script


    Parameters:
    None

    Returns:
    None
    """

    # PROBLEM 1
    print("Problem 01")
    # 1.1

    filepath_movies = Path("data-horror_movies.csv")
    filepath_jumpscare = Path("data-movie_jumpscares.csv")
    horror_movies = read_csv_to_dicts(filepath_movies)
    jumpscare_data = read_csv_to_dicts(filepath_jumpscare)

    # 1.5
    horror_movies = [clean_row(movie) for movie in horror_movies]
    jumpscare_data = [clean_row(movie) for movie in jumpscare_data]

    pp.pprint(f"First element in horror_movies: {horror_movies[0]}")
    pp.pprint(f"First element in jumpscare_data: {jumpscare_data[0]}")

    # PROBLEM 2
    print("\nProblem 02")

    # 2.2
    action_movies = filter_movie_by_genre(horror_movies, "action")
    print(f"Action movies:\n")
    pp.pprint(action_movies)
    assert action_movies_check in action_movies
    assert len(action_movies) == 6

    # 2.3
    horror_movies = filter_movie_by_genre(horror_movies, "horror")
    print(f"First 5 elements of Horror movies:\n")
    pp.pprint(horror_movies[:5])
    assert horror_movies_filt_check in horror_movies
    assert len(horror_movies) == 65

    # PROBLEM 3
    print("\nProblem 03")
    unique_ratings = ["PG", "PG-13", "R", "Not Rated", "Passed", "Unrated"]

    # 3.2 & 3.3
    movie_ratings_count = {}
    for rating in unique_ratings:
        count = count_movie_by_rating(horror_movies, rating)
        movie_ratings_count[rating] = count
    print(f"Count of horror movies in each viewer ratings:\n{movie_ratings_count}")
    assert ratings_count_check == movie_ratings_count

    # PROBLEM 4
    print("\nProblem 04")

    # 4.2
    for movie in horror_movies:
        movie_title = movie.get("Title", "")
        jumpscare_count, jumpscare_rating = get_jumpscare_data(jumpscare_data, movie_title)
        movie["Jumpscare_count"] = jumpscare_count
        movie["Jumpscare_rating"] = jumpscare_rating
    print(f"First element of horror movies with jump scare data:\n")
    pp.pprint(horror_movies[0])
    print(f"\nLength of horror movies with jump scare data:\n{len(horror_movies)}")
    assert horror_w_js_movies_check in horror_movies
    assert "Jumpscare_count" in horror_movies[0]
    assert "Jumpscare_rating" in horror_movies[0]
    assert len(horror_movies) == 65

    # PROBLEM 5
    print("\nProblem 05")

    # 5.2
    all_recent_movies = filter_movies_by_year_and_imdb(horror_movies, 2018, 2023, 7.0)
    print(f"\nRecent Horror movies:\n")
    pp.pprint(all_recent_movies)

    assert recent_movies_check in all_recent_movies
    assert len(all_recent_movies) == 4

    # PROBLEM 6
    print("\nProblem 06")

    # 6.2
    writer_names = ["stephEN", "Chad", "dAVId", "jordan peeLe"]
    writer_movies = []
    for movie in horror_movies:
        if search_movie_writer(movie, writer_names):
            writer_movies.append(movie)
    pp.pprint(writer_movies)
    print(f"\nLength of writers in movies:\n{len(writer_movies)}")

    assert writers_in_movies_check in writer_movies
    assert len(writer_movies) == 12

    # 6.4
    long_writer_movies = check_movie_runtime(writer_movies, 100)
    print(f"\nLong movies by prolific writers:\n")
    pp.pprint(long_writer_movies)

    assert long_writers_movies_check in long_writer_movies

    # PROBLEM 7
    print("\nProblem 07")

    # 7.2
    movie_title = get_value(horror_movies[3], "Title")
    movie_viewer_rating = get_value(horror_movies[3], "Rated")
    assert movie_title == "The Skeleton Key"
    assert movie_viewer_rating == "PG-13"

    # 7.4 & 7.5
    high_rated_movies = []
    avg_imdb_rating = calculate_avg(horror_movies, "imdbRating")
    avg_jumpscare_rating = calculate_avg(jumpscare_data, "Jump Scare Rating")

    print(f"The average imdb Score is: {avg_imdb_rating}")
    print(f"The average jumpscare Score is: {avg_jumpscare_rating}")

    print("High-rated movies:")
    for movie in high_rated_movies:
        pp.pprint(movie)

    # PROBLEM 8
    print("\nProblem 08")

    # 8.2-3
    oscar_movies = []
    for movie in horror_movies:
        no_of_awards = get_awards(movie, "Awards")
        if no_of_awards:
            movie_info = {
                "Title": movie["Title"],
                "Director": movie["Director"],
                "Oscars Record": no_of_awards,
            }
            oscar_movies.append(movie_info)

    print(f"All movies that have been nominated for or have won an Oscar are {oscar_movies}")

    # 8.4
    write_dicts_to_csv("stu-oscar_movies.csv", oscar_movies, oscar_movies[0].keys())


if __name__ == "__main__":
    main()

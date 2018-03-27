"""
Class Movie Definition
======================
Contains the details of a movie.

"""

# import the webbrowser module to open URLs
import webbrowser


# define class Movie()
class Movie():
    """
    This class provides a way to store movie related information.

    Arguments:
        title: a string that stores movie title.
        storyline: a string that stores the blot of the movie.
        poster_image_url: a string that stores the URL to the movie poster.
        trailer_youtube_url: a string that stores the URL to the movie trailer.
        release_year: a string that stores the year of release of the movie.
        rating: a string that stores the movie's rating.
        duration: a string that stores the movie's duration in minutes

        *self: constructor keyword referring to the instance/object created*
    """

    # define constructor function __init__(arguments)
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_year,
                 movie_rating, movie_duration):
        """ The constructor initializes the class instance variables. """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = movie_release_year
        self.rating = movie_rating
        self.duration = movie_duration

    # define show_trailer() instance method
    def show_trailer(self):
        """ This instance method plays the youtube
            movie trailer in the web browser. """
        webbrowser.open(self.trailer_youtube_url)

"""
Class Movie Implementation
==========================
Stores details of movies (objects of class Movie) and
displays them on a website.

"""

# import fresh_tomatoes.py file to generate HTML file (from same directory)
import fresh_tomatoes
# import media.py file that contains the
# Movie class definition (from same directory)
import media

"""
The program:
  --creates 12 Movie objects
  --initializes each object with title, storyline, poster_image link,
    trailer link, release year, rating and duration
  --stores the objects in a list
  --opens the movie website featuring the objects on the user's browser
"""
# create and initialize 12 Movie objects
sound_of_music = media.Movie("The Sound of Music",
                             "A story of a woman who becomes the governess" +
                             " to the children of an officer.",
                             "https://vignette.wikia.nocookie.net/filmguide/images/b/b8/Soundofmusic40th.jpg/revision/latest?cb=20060508044847",  # noqa
                             "https://www.youtube.com/watch?v=lEcKXr3mJ_o",
                             "(1965)",
                             "Rated G",
                             "174min")

erin_brockovich = media.Movie("Erin Brockovich",
                              "A single mother becomes a legal assistant" +
                              " and uncovers a water pollution case.",
                              "https://vignette.wikia.nocookie.net/universalstudios/images/a/a9/Erin_Brockovich_%28film_poster%29.jpg/revision/latest?cb=20150720031554",  # noqa
                              "https://www.youtube.com/watch?v=AcwpbDvQaK8",
                              "(2000)",
                              "Rated R",
                              "131min")

saving_mr_banks = media.Movie("Saving Mr. Banks",
                              "Author P.L. Travers meets with Walt Disney," +
                              " who seeks to take her Mary Poppins books" +
                              " to the big screen.",
                              "https://vignette.wikia.nocookie.net/filmguide/images/1/16/Movies_saving-mr-banks-poster.jpg/revision/latest?cb=20130729180245",  # noqa
                              "https://www.youtube.com/watch?v=FvKcwNyOnWo",
                              "(2013)",
                              "Rated PG-13",
                              "125min")

breakfast_tiffanys = media.Movie("Breakfast At Tiffany's",
                                 "A young lady grows an interest for her" +
                                 " neighbor, but her past threatens to" +
                                 " get in the way.",
                                 "https://vignette.wikia.nocookie.net/breakfast-at-tiffanys/images/a/a9/Breakfast_at_Tiffanys.jpg/revision/latest?cb=20171005023920",  # noqa
                                 "https://www.youtube.com/watch?v=-XcLVQCDtbM",
                                 "(1961)",
                                 "Not Rated",
                                 "115min")

breakfast_club = media.Movie("The Breakfast Club",
                             "Five high school students from different walks" +
                             " of life endure a Saturday detention.",
                             "https://vignette.wikia.nocookie.net/thebreakfastclub/images/7/7e/Tbc.jpeg/revision/latest?cb=20110815170052",  # noqa
                             "https://www.youtube.com/watch?v=BSXBvor47Zs",
                             "(1985)",
                             "Rated R",
                             "97min")

the_intern = media.Movie("The Intern",
                         "A retired widower becomes a senior intern at" +
                         " an online fashion site.",
                         "https://vignette.wikia.nocookie.net/the-intern/images/c/c9/The_Intern_Poster.jpg/revision/latest?cb=20160613011610",  # noqa
                         "https://www.youtube.com/watch?v=ZU3Xban0Y6A",
                         "(2015)",
                         "Rated PG-13",
                         "121min")

the_princess_bride = media.Movie("The Princess Bride",
                                 "A grandfather reads a story about" +
                                 "  true love and heroism to his" +
                                 " sick grandson.",
                                 "https://vignette.wikia.nocookie.net/filmguide/images/0/00/Princess_bride_xlg.jpg/revision/latest?cb=20130418232951",  # noqa
                                 "https://www.youtube.com/watch?v=VYgcrny2hRs",
                                 "(1987)",
                                 "Rated PG",
                                 "98min")

harry_potter = media.Movie("Harry Potter and the Philosopher's Stone",
                           "Harry Potter gets entangled in the mystery" +
                           " of the Philosopher's Stone.",
                           "https://vignette.wikia.nocookie.net/transcripts/images/5/5c/Harry_Potter_and_the_Philosopher%27s_Stone_-_Theatrical_Poster.jpg/revision/latest?cb=20170130065413",  # noqa
                           "https://www.youtube.com/watch?v=eKSB0gXl9dw",
                           "(2001)",
                           "Rated PG",
                           "162min")

lord_of_rings = media.Movie("Lord of the Rings: The Fellowship of the Ring",
                            "A hobbit and his fellowship begin a journey" +
                            "  accross Middle-Earth to destroy the One" +
                            " Ring of Power.",
                            "https://vignette.wikia.nocookie.net/lotr/images/7/7d/Fellowship_of_the_Ring_Poster_02.jpg/revision/latest?cb=20150203041117",  # noqa
                            "https://www.youtube.com/watch?v=aStYWD25fAQ",
                            "(2001)",
                            "Rated PG-13",
                            "178min")

star_wars = media.Movie("Star Wars: A New Hope",
                        "Luke Skywalker teams up with a Jedi Knight to" +
                        " save the galaxy from the Empire.",
                        "https://vignette.wikia.nocookie.net/swfans/images/7/79/StarWarsIVPoster.jpg/revision/latest?cb=20130604205211",  # noqa
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "(1977)",
                        "Rated PG",
                        "121min")

back_to_future = media.Movie("Back to the Future",
                             "A high school student accidentally uses a" +
                             " time-travelling DeLorean and is sent into" +
                             " the past.",
                             "https://vignette.wikia.nocookie.net/bttf/images/5/52/Back_to_the_future.jpg/revision/latest?cb=20150928161335",  # noqa
                             "https://www.youtube.com/watch?v=qb7Fd0l_BRo",
                             "(1985)",
                             "Rated PG",
                             "116min")

interstellar = media.Movie("Interstellar",
                           "A team of scientists travel in space to find" +
                           " a new world and save humanity.",
                           "https://vignette.wikia.nocookie.net/filmguide/images/b/be/Interstellar-poster.jpg/revision/latest?cb=20150226092240",  # noqa
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ",
                           "(2014)",
                           "Rated PG-13",
                           "169min")

# store Movie objects in a list
movies = [sound_of_music, erin_brockovich, saving_mr_banks,
          breakfast_tiffanys, breakfast_club, the_intern,
          the_princess_bride, harry_potter, lord_of_rings,
          star_wars, back_to_future, interstellar]

# call open_movies_page() method to open the website in the web browser
fresh_tomatoes.open_movies_page(movies)

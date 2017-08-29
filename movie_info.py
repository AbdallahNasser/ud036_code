# this is the main file that contains all the movies you would like to list within the web page
# this file uses the Movie class and fresh_tomatoes as following
# Firstly, It creates an instance of "Movie" class to each movie which is located in "Movie.py"
# Secondly, It creates a list of all movies created
# Finally, It Calls a method located inside "fresh_tomatoes.py" called "open_movies_page", giving
# it the created list of movies "movies" to create an HTML file to view these movies in a web page

import movie
import fresh_tomatoes

# using Movie.Movie to make instance of Class Movie to each movie
the_shawshank_redemption = movie.Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg", "https://www.youtube.com/watch?v=NmzuHjWmXOc")
the_godfather = movie.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg", "https://www.youtube.com/watch?v=sY1S34973zA")
the_godfather_ii = movie.Movie("The Godfather: Part II", "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg", "https://www.youtube.com/watch?v=9O1Iy9od7-A")
the_dark_knight = movie.Movie("The Dark Knight", "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
twelve_angry_men = movie.Movie("12 Angry Men","A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.", "https://images-na.ssl-images-amazon.com/images/M/MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg", "https://www.youtube.com/watch?v=Dosg0p7LAB4")
schindler_list = movie.Movie("Schindler's List", "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.", "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg", "https://www.youtube.com/watch?v=gG22XNhtnoY")
pulp_fiction = movie.Movie("Pulp Fiction", "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg", "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
the_lord_of_the_rings = movie.Movie("The Lord of the Rings: The Return of the King", "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.", "https://images-na.ssl-images-amazon.com/images/M/MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3Njg@._V1_SY1000_SX668_AL_.jpg", "https://www.youtube.com/watch?v=r5X-hFf6Bwo")
good_bad_ugly = movie.Movie("The Good, the Bad and the Ugly", "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.", "https://images-na.ssl-images-amazon.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SY1000_CR0,0,656,1000_AL_.jpg", "https://www.youtube.com/watch?v=WCN5JJY_wiA")


# Making a list of all created movies
movies = [the_shawshank_redemption, the_godfather, the_godfather_ii, the_dark_knight, twelve_angry_men, schindler_list, pulp_fiction, the_lord_of_the_rings, good_bad_ugly]


# Call open_movies_page method to create the web page using the movie list
# fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)

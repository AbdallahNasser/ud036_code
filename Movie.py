# This class will be used as the core of the project
# as every Movie will be an instance of this class
# You will be able to give five(5) variables to each movie
# Title: Movie name
# storyline: the storyline of the movie
# Poster: a link to the movie's poster
# traileer: a link to the movie trailer on Youtube.com

class Movie():

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer


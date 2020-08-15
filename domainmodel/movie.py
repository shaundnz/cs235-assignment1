from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, movie_name: str, release_year: int):
        if (movie_name == "" or type(movie_name) is not str):
            self.__movie_name = None
        else:
            self.__movie_name = movie_name
        if release_year < 1900
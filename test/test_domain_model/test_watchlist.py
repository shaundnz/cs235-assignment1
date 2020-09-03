import pytest
from domainmodel.filter import Filter

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director
from domainmodel.watchlist import WatchList

@pytest.fixture
def new_watchlist():
    return WatchList()

@pytest.fixture
def new_movies_list():
    return [Movie("Casino Royale", 2006), Movie("Star Wars: A New Hope", 1977), Movie("The Matrix", 1999)]

def test_size(new_watchlist, new_movies_list):
    assert new_watchlist.size() == 0
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    assert new_watchlist.size() == 2


def test_add_new_movie(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    assert new_watchlist.size() == 1
    new_watchlist.add_movie(new_movies_list[1])
    assert new_watchlist.size() == 2
    new_watchlist.add_movie(new_movies_list[2])
    assert new_watchlist.size() == 3

def test_add_duplicate_movie(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    assert new_watchlist.size() == 2
    new_watchlist.add_movie(new_movies_list[0])
    assert new_watchlist.size() == 2


def test_remove_movie(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    new_watchlist.remove_movie(new_movies_list[0])
    assert new_watchlist.size() == 1
    new_watchlist.remove_movie(new_movies_list[1])
    assert new_watchlist.size() == 0
    new_watchlist.remove_movie(new_movies_list[0])
    assert new_watchlist.size() == 0


def test_remove_movie_not_in_watchlist(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    new_watchlist.remove_movie(new_movies_list[2])
    assert new_watchlist.size() == 2

def test_movie_to_watch(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    assert new_watchlist.select_movie_to_watch(1) == new_movies_list[1]
    assert new_watchlist.select_movie_to_watch(2) is None


def test_first_movie_in_watchlist(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    assert new_watchlist.first_movie_in_watchlist() == new_movies_list[0]
    new_watchlist.remove_movie(new_movies_list[0])
    assert new_watchlist.first_movie_in_watchlist() == new_movies_list[1]

def test_iterator(new_watchlist, new_movies_list):
    new_watchlist.add_movie(new_movies_list[0])
    new_watchlist.add_movie(new_movies_list[1])
    new_watchlist.add_movie(new_movies_list[2])
    movies = []
    for movie in new_watchlist:
        movies.append(movie)
    assert movies == new_movies_list



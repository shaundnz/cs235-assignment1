from collections import OrderedDict

import pytest
from domainmodel.filter import Filter

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

@pytest.fixture
def new_row():
    return OrderedDict([('Rank', '1'), ('Title', 'Test Movie'), ('Genre', 'Action,Adventure,Sci-Fi'),
                        ('Description', 'A movie used for unit tests'),
                        ('Director', 'John Doe'), ('Actors', 'Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana'),
                        ('Year', '2020'), ('Runtime (Minutes)', '121'), ('Rating', '8.1'), ('Votes', '757074'),
                        ('Revenue (Millions)', '333.13'), ('Metascore', '76')])


@pytest.fixture
def new_filter():
    return Filter(
        "C:\\Users\\Shaun\\Documents\\GDriveUoA\\2020\\Sem 2\\CompSci 235\\assignment-1\\datafiles\\Data1000Movies.csv")


def test_contains_title(new_row, new_filter):
    assert new_filter.contains_title("*", new_row) is True
    assert new_filter.contains_title("Test", new_row) is True
    assert new_filter.contains_title("Test Movie", new_row) is True
    assert new_filter.contains_title("Not in the title", new_row) is False


def test_contains_actor(new_row, new_filter):
    assert new_filter.contains_actor("*", new_row) is True
    assert new_filter.contains_actor("Chris Pratt", new_row) is True
    assert new_filter.contains_actor("Zoe", new_row) is True
    assert new_filter.contains_actor("Leo", new_row) is False


def test_contains_genre(new_row, new_filter):
    assert new_filter.contains_genre("*", new_row) is True
    assert new_filter.contains_genre("Adventure", new_row) is True
    assert new_filter.contains_genre("Acti", new_row) is True
    assert new_filter.contains_genre("Mystery", new_row) is False

def test_contains_director(new_row, new_filter):
    assert new_filter.contains_director("*", new_row) is True
    assert new_filter.contains_director("John Doe", new_row) is True
    assert new_filter.contains_director("John", new_row) is True
    assert new_filter.contains_director("Jane Doe", new_row) is False

def test_create_movie_instance(new_row, new_filter):
    movie = new_filter.create_movie_instance(new_row)
    assert movie.title == "Test Movie"
    assert movie.runtime_minutes == 121
    assert movie.release_year == 2020
    assert movie.description == "A movie used for unit tests"
    assert movie.actors == [Actor("Chris Pratt"), Actor("Vin Diesel"), Actor("Bradley Cooper"), Actor("Zoe Saldana")]
    assert movie.genres == [Genre("Action"), Genre("Adventure"), Genre("Sci-Fi")]
    assert movie.director == Director("John Doe")











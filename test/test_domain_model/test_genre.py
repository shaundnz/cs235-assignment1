import pytest
from domainmodel.genre import Genre

genre1 = Genre("Horror")
genre2 = Genre("Comedy")
genre3 = Genre("")
genre4 = Genre(12345)
genre5 = Genre("Horror")


def test_print():

    assert repr(genre1) == "<Genre Horror>"
    assert repr(genre2) == "<Genre Comedy>"
    assert repr(genre3) == "<Genre None>"
    assert repr(genre4) == "<Genre None>"

def test_equality():
    assert genre1 == genre1
    assert genre1 != genre2
    assert genre1 != genre3
    assert genre1 != genre4
    assert genre3 == genre3
    assert genre3 == genre4
    assert genre1 == genre5

def test_less_than():
    assert (genre1 < genre2) == ("Horror" < "Comedy")
    assert (genre1 < genre3) == ("Horror" < "")
    assert (genre1 < genre1) == ("Horror" < "Horror")
    assert (genre3 < genre4) is False
    assert (genre1 < genre5) is False

def test_hash():
    assert hash(genre1) == hash(genre5)
    assert hash(genre3) == hash(genre4)
    assert hash(genre1) != hash(genre2)
    assert hash(genre1) == hash(genre1)
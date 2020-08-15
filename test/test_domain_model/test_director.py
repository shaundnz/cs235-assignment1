import pytest
from domainmodel.director import Director;

@pytest.fixture
def new_director():
    return Director("")

def test_init():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None


def test_director_equality():
    director1 = Director("Jane Doe")
    director2 = Director("John Doe")
    director3 = Director("John Doe")
    director4 = Director("")

    assert director1 != "Jane Doe"
    assert director1 != 12345
    assert  director1 != director2
    assert director2 == director3
    assert director1 != director4
    assert director1 == director1
    assert director4 == director4

def test_less_than():
    director1 = Director("Jane Doe")
    director2 = Director("John Doe")
    director3 = Director("John Doe")
    director4 = Director("")

    assert (director1 < director2) == ("Jane Doe" < "John Doe")
    assert (director2 < director3) is False
    assert (director1 < director4) == ("Jane Doe" < "")


def test_hash():
    d1 = Director("John Doe")
    d2 = Director("John Doe")
    d3 = Director("Jane Doe")
    d4 = Director(420)

    assert hash(d1) == hash(d2)
    assert hash(d1) != hash(d3)
    assert hash(d1) != hash(d4)






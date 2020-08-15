import pytest
from domainmodel.actor import Actor

a1 = Actor("John Doe")
a2 = Actor("Jane Doe")
a3 = Actor("John Doe")
a4 = Actor("")
a5 = Actor(12345)

def test_repr():
    assert repr(a1) == "<Actor John Doe>"
    assert repr(a2) == "<Actor Jane Doe>"
    assert repr(a3) == "<Actor John Doe>"
    assert repr(a4) == "<Actor None>"
    assert repr(a5) == "<Actor None>"

def test_equality():
    assert a1 == a1
    assert a1 != a2
    assert a1 == a3
    assert a1 != a4
    assert a4 == a5

def test_less_than():
    assert (a1 < a2) == ("John Doe" < "Jane Doe")
    assert (a1 < a3) is False
    assert (a1 < a4) == ("John Doe" < "")
    assert (a4 < a5) is False

def test_colleague():
    assert a1.check_if_this_actor_worked_with(a3) is False
    assert a1.check_if_this_actor_worked_with(a4) is False
    a1.add_actor_colleague(a2)
    a1.add_actor_colleague(a4)
    assert a1.check_if_this_actor_worked_with(a2) is True
    assert a1.check_if_this_actor_worked_with(a4) is True
    assert a3.check_if_this_actor_worked_with(a2) is False

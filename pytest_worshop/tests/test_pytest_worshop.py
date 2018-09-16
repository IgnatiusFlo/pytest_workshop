
import pytest_worshop.pytest_worshop as pt

def test_init():
   c = pt.Calc()

def test_add_two_numbers():
    c = pt.Calc()

    result = c.add(5, 4)

    assert result == 9


def test_add_three_numbers():
    c = pt.Calc()

    result = c.add(10, 20, 30)

    assert result == 60


def test_add_many():
    c = pt.Calc()
    r = range(100)
    result =  c.add(*r)

    assert result == 4950

def test_sub():
    c = pt.Calc()

    result = c.sub(4, 5)

    assert result == -1




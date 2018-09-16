import pytest
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

def test_mul():
    c = pt.Calc()

    result = c.mul(4, 5)

    assert result == 20

def test_div():
    c = pt.Calc()

    result = c.div(4, 2)

    assert result == 2

def test_div_two_num_float():
    c = pt.Calc()
    result = c.div(15, 2)
    assert result == 7.5

def test_zero():
    c = pt.Calc()
    result = c.zero(4, 0)

    assert result == "inf"

def test_mu_by_zero_raises_exception():
    with pytest.raises(ValueError):
        pt.Calc().mul(3, 0)

    #assert Calc().div
    #assert Calc().div(13, 2)  6.5

def test_list_empty():
    result = "is empty"
    assert pt.Calc().is_empty

def test_average():
    assert pt.Calc().avg([2, 5,12, 98]) == 20.25

def remove_upper():
    assert pt.Calc().avg([2, 5,12, 98])

"""
average of an iterable
account for empty
upper and lower threshhold work seperatly

"""

import pytest

import time

import source.my_func as my_func

def test_add():
    result = my_func.add(number_one=2, number_two=3)
    assert result == 5

def test_add_strings():
    result = my_func.add(number_one="abc", number_two="def")
    assert result == "abcdef"

def test_divide():
    result = my_func.divide(number_one=10, number_two= 5)
    assert result == 2

# error zerodeivision was expected
def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_func.divide(number_one=10, number_two= 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_func.divide(number_one=10, number_two= 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_func.add(1,2)== 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_func.divide(4,0)
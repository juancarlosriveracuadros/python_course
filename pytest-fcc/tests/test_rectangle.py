import pytest
import source.shapes as shapes

## fixture

#@pytest.fixture
#def my_rectangle():
#    return shapes.Rectangle(10, 5)

#@pytest.fixture
#def weird_rectangle():
#    return shapes.Rectangle(5, 6)


def test_area(my_rectangle):
    assert my_rectangle.area() == 50

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 30


def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle

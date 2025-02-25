import pytest
import source.shapes as shapes


## Global fixture

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 5)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)
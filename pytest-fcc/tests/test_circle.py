import pytest
import source.shapes as shapes
import math

## Clase base Test

class TestCicle:

    # setup_method is called before each test method » initializ
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    # teardown_method is called after each test method » clean up
    def teardown_method(self, method):
        print(f"Teardown {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius

        assert result == expected

    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
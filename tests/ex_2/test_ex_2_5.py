from exercises.Ex_2 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(4, 5)
p2 = Point(7, 3)
p3 = Point(1, 2)
p4 = Point(3, 3)
p5 = Point(5, 0)
p6 = Point(4, 2)
p7 = Point(5, 3)
arrayOfPoints = [p1, p2, p3, p4, p5, p6, p7]


# Spiral polyline computation with Graham’s scan
def test_spiral_1():
    result = spiral(arrayOfPoints)
    assert result == [p3, p5, p2, p1, p4, p6, p7], f"Spiral polyline was calculated wrongly"

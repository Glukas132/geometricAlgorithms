from exercises.Ex_2 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])


# Test if True is returend for a square
def test_is_polygon_convex_1():
    assert is_polygon_convex(polygon1), f"Polygon is a square and is convex but your test failed."

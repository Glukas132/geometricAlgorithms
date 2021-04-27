from exercises.Ex_2 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])


# Centroid Test.
def test_polygon_centroid_1():
    assert polygon_centroid(polygon1) == Point(2.5, 2.5), f"Centroid function calculates the centroid not correctly."

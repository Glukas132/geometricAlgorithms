from exercises.Ex_3 import *
from exercises.helper_classes import Point, Line

p1 = Point(0, 0)
p2 = Point(0, 1)


# Test if bisector was calculated correctly
def test_bisector_1():
    bis_calculated = bisector(p1, p2)
    assert bis_calculated == Line(Point(-0.5, 0.5), Point(0.5, 0.5)), f"Bisector was calculated wrongly."

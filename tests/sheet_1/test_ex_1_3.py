from exercises.Ex_1 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])

p5 = Point(4.5, 4.5)
p6 = Point(5.5, 4.5)
p7 = Point(5.5, 5.5)
p8 = Point(4.5, 5.5)
polygon2 = Polygon(arrayOfPoints=[p5, p6, p7, p8, p5])


def test_non_overlapping_area_1_25_75():
    result = non_overlapping_area(polygon1, polygon2)
    assert result == [1, 25.75], f"Overlap is not recognized correctly or area is not 25.75 but {area}"

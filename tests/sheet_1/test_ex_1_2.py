from exercises.Sheet_1 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])

p5 = Point(1, 1)
p6 = Point(4, 1)
p7 = Point(4, 4)
p8 = Point(1, 4)
polygon2 = Polygon(arrayOfPoints=[p5, p6, p7, p8, p5])

h1 = Point(2, 2)
h2 = Point(3, 2)
h3 = Point(3, 3)
h4 = Point(2, 3)
hole_p2 = Hole([h1, h2, h3, h4, h1])

p9 = Point(10, 10)
p10 = Point(10, 15)
p11 = Point(15, 15)
p12 = Point(15, 10)
polygon3 = Polygon([p9, p10, p11, p12, p9])


# one polygon contains the other
def test_polygon_with_border_contains_polygon_T():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [1, p5, p6, p7, p8, p5], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_with_hole_contains_polygon_T():
    polygon1.holes.append(hole_p2)
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [0], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_contains_identical_polygon_T():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon1)
    assert polygon2_in_polygon1 == [1, p1, p2, p3, p4, p1, p1, p2, p3, p4, p1], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_contains_distinct_polygon_T():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon2, polygon3)
    assert polygon2_in_polygon1 == [0], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


test_polygon_with_border_contains_polygon_T()
test_polygon_contains_identical_polygon_T()
test_polygon_with_hole_contains_polygon_T()
test_polygon_contains_distinct_polygon_T()
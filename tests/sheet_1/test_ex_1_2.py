from exercises.Sheet_1 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])

p5 = Point(1, 2)
p6 = Point(3, 2)
p7 = Point(3, 5)
p8 = Point(1, 5)
polygon2 = Polygon(arrayOfPoints=[p5, p6, p7, p8, p5])

h1 = Point(2, 1)
h2 = Point(4, 1)
h3 = Point(4, 3)
h4 = Point(2, 3)
hole_p2 = Hole([h1, h2, h3, h4, h1])


# one polygon contains the other
def test_polygon_contains_polygon_T1():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [1, p5, p6, p7, p8, p5], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test 1 passed')


def test_polygon_with_hole_contains_polygon_T3():
    polygon2.holes.append(hole_p2)
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [0], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test 3 passed')


def test_polygon_contains_polygon_T2():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon1)
    assert polygon2_in_polygon1 == [1, p1, p2, p3, p4, p1, p1, p2, p3, p4, p1], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test 2 passed')



test_polygon_contains_polygon_T1()
test_polygon_contains_polygon_T2()
test_polygon_contains_polygon_T3()

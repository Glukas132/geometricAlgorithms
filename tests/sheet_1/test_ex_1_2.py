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
polygonh2 = Polygon([h1, h2, h3, h4, h1])

p9 = Point(10, 10)
p10 = Point(10, 15)
p11 = Point(15, 15)
p12 = Point(15, 10)
polygon3 = Polygon([p9, p10, p11, p12, p9])

p13 = Point(3, 1)
p14 = Point(13, 3)
p15 = Point(12, 7)
p16 = Point(6, 9)
p17 = Point(1, 4)
polygon4 = Polygon([p13, p14, p15, p16, p17, p13])

p18 = Point(5, 5)
p19 = Point(5, 6)
p20 = Point(6, 6)
polygon5 = Polygon([p18, p19, p20, p18])

p21 = Point(0, 0)
p22 = Point(100, 0)
p23 = Point(100, 100)
p24 = Point(0, 100)
polygon6 = Polygon([p21, p22, p23, p24, p21])
polygon6.holes.append(Hole([p5, p6, p7, p8, p5]))
polygon6.holes.append(Hole([p13, p14, p15, p16, p17, p13]))
polygon6.holes.append(Hole([p9, p10, p11, p12, p9]))

# one polygon contains the other
def test_polygon_with_border_contains_polygon_T():
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [1, p5, p6, p7, p8, p5], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_with_hole_contains_polygon_T():
    polygon1.holes.append(hole_p2)
    polygon2_in_polygon1 = polygon_contains_polygon(polygon1, polygon2)
    assert polygon2_in_polygon1 == [1, p5, p6, p7, p8, p5], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_contains_identical_polygon_T():
    polygon1_in_polygon1 = polygon_contains_polygon(polygon1, polygon1)
    assert polygon1_in_polygon1 == [1, p1, p2, p3, p4, p1, p1, p2, p3, p4, p1], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')


def test_polygon_contains_distinct_polygon_T():
    polygon2_in_polygon3 = polygon_contains_polygon(polygon2, polygon3)
    assert polygon2_in_polygon3 == [0], f"Wrong polygon is recognized to be inside other polygon or polygons do not contian each other"
    print('test passed')

def test_polygon_with_many_points_T():
    polygon5_in_polygon4 = polygon_contains_polygon(polygon4, polygon5)
    assert polygon5_in_polygon4 == [1, p18, p19, p20, p18]
    print('test passed')

def test_polygon_with_multiple_holes():
    polygonh2_in_polygon6 = polygon_contains_polygon(polygon6, polygonh2)
    assert polygonh2_in_polygon6 == [0]
    print('test passed')


polygon1.draw()

test_polygon_with_border_contains_polygon_T()
test_polygon_contains_identical_polygon_T()
test_polygon_contains_distinct_polygon_T()
test_polygon_with_many_points_T()
test_polygon_with_hole_contains_polygon_T()
test_polygon_with_multiple_holes()

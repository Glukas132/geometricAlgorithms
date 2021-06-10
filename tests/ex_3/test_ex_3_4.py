from exercises.Ex_3 import *
from exercises.helper_classes import Point

p1 = Point(0,0)
p2 = Point(6,0)
p3 = Point(3,5)
p4 = Point(3,1)
p5 = Point(4,2.5)
p6 = Point(2,2.5)
p7 = Point(3,2)
arrayOfPoints = [p4, p5, p6]
boundary = Polygon(arrayOfPoints=[p1, p2, p3, p1])


# test voronoi diagram
def test_voronoi_1():
    assert voronoi(arrayOfPoints, boundary) == {Polygon(arrayOfPoints=[p1, p7, p3, p1]),
                                                Polygon(arrayOfPoints=[p1, p2, p7, p1]),
                                                Polygon(arrayOfPoints=[p7, p2, p3, p7])}, f"VD was calculated wrongly"

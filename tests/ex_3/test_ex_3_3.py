from exercises.Ex_3 import *
from exercises.helper_classes import Point

p1 = Point(0,0)
p2 = Point(6,0)
p3 = Point(3,5)
p4 = Point(3,1)
p5 = Point(4,2.5)
p6 = Point(2,2.5)
arrayOfPoints = [p4, p5, p6]
bbTriangle = Polygon(arrayOfPoints=[p1, p2, p3, p1])


# test delaunay triangulation
def test_delaunay_triangulation_1():
    assert delaunay_triangulation(arrayOfPoints, bbTriangle) == {Polygon(arrayOfPoints=[p1, p6, p3, p1]),
                                                                 Polygon(arrayOfPoints=[p6, p5, p3, p6]),
                                                                 Polygon(arrayOfPoints=[p5, p2, p3, p5]),
                                                                 Polygon(arrayOfPoints=[p4, p2, p5, p4]),
                                                                 Polygon(arrayOfPoints=[p1, p2, p4, p1]),
                                                                 Polygon(arrayOfPoints=[p1, p4, p6, p1]),
                                                                 Polygon(arrayOfPoints=[p6, p4, p5, p6])}, f"DT was calculated wrongly"

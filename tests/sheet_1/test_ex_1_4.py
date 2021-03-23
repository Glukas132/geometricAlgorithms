from exercises.Sheet_1 import *
from exercises.helper_classes import Point, Polygon, Line, Polyline

p1 = Point(1, 3)
p2 = Point(5, 3)
p3 = Point(5, 6)
p4 = Point(1, 6)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])

p5 = Point(3, 2)
p6 = Point(7, 2)
p7 = Point(7, 4)
p8 = Point(3, 4)
polygon2 = Polygon(arrayOfPoints=[p5, p6, p7, p8, p5])

l1 = Line(Point(4, 5), Point(6, 5))
l2 = Line(Point(6, 5), Point(9, 5))
polyline1 = Polyline([l1, l2])

l3 = Line(Point(3.5, 5), Point(3.5, 3))
l4 = Line(Point(3.5, 3), Point(3.5, 0))
polyline2 = Polyline([l3, l4])

# polyline lies completely inside the polygon
def test_percentage_polylines_in_polygons_50():
    result = percentage_polylines_in_polygons([polyline1, polyline2], [polygon1, polygon2])
    assert result == [polyline2], f"Polyline(s) with less than 50% of their length are selected as to be inside."
    print('test passed!')

test_percentage_polylines_in_polygons_50()
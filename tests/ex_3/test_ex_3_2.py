from exercises.Ex_3 import *
from exercises.helper_classes import Point, Line

l1 = Line(Point(2, 0), Point(4, 4))
l2 = Line(Point(0, 4), Point(6, 0))
l3 = Line(Point(7, 0), Point(7, 5))
list_of_lines = [l1,l2,l3]

# Test if plane sweep finds all intersections
def test_point_intersection_plane_sweep_1():
    intersections_detected = point_intersection_plane_sweep(list_of_lines)
    intersections_detected == [Point(3.00,2.00)]
    assert is_polygon_convex(polygon1), f"Line intersections were detected wrongly."

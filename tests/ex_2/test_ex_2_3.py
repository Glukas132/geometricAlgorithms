from exercises.Ex_2 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])


# Random points should lie inside the polygon and be pairwise distinct.
def test_random_points_in_polygon_1():
    random_generated_points = random_points_in_polygon(polygon1, n=4, seed=5)
    if len(random_generated_points) != 0:
        all_points_inside = True
        for point in random_generated_points:
            # the functionality of the function point_in_polygon should have been implmented during the first exercise sheet.
            if not point_in_polygon(point, polygon1):
                all_points_inside = False
                break

    assert all_points_inside, f"All random generated points should be inside the polygon and different pairwise"

from exercises.Ex_1 import *
from exercises.helper_classes import Point

p1 = Point(0, 0)
p2 = Point(2, 0.8)
p3 = Point(1, 0.6)
p4 = Point(4, 0.5)

point_list = [p1, p2, p3, p4]


# sort list according to West-East direction in reverse order
def test_sort_points_ew():
    sorted_list = sort_points(point_list, mode="WE", reverse=True)
    assert sorted_list == [p4, p2, p3, p1], f"Points are not sorted correctly according to East-West direction"

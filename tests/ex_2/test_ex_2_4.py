from exercises.Ex_2 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(1.05, 0.5)
p3 = Point(1, 1)
p4 = Point(2, 0)
arrayOfPoints = [p1, p2, p3, p4]


# MergeHull test
def test_jarvis_march_1():
    assert jarvis_march(arrayOfPoints) == [p1, p4, p3], f"Convex Hull was calculated wrongly"

if __name__ == "__main__":
    test_jarvis_march_1()
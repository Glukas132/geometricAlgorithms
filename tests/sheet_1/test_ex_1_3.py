from exercises.Sheet_1 import *
from exercises.helper_classes import Point, Polygon

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)
polygon1 = Polygon(arrayOfPoints=[p1, p2, p3, p4, p1])

p5 = Point(4.5, 4.5)
p6 = Point(5.5, 4.5)
p7 = Point(5.5, 5.5)
p8 = Point(4.5, 5.5)
polygon2 = Polygon(arrayOfPoints=[p5, p6, p7, p8, p5])

p9 = Point(-1, 0)
p10 = Point(0.5, 2.6)
p11 = Point(-1, 5.2)
p12 = Point(-4, 5.2)
p13 = Point(-5.5, 2.6)
p14 = Point(-4, 0)
polygon3 = Polygon([p9, p10, p11, p12, p13, p14, p9])

p15 = Point(0, 0)
p16 = Point(-4, 2)
p17 = Point(-7.73, -0.46)
p18 = Point(-7.46, -4.93)
p19 = Point(-3.46, -6.93)
p20 = Point(0.27, -4.46)
polygon4 = Polygon([p15, p16, p17, p18, p19, p20, p15])

p21 = Point(4, 4)
p22 = Point(6, 4)
p23 = Point(6, 6)
p24 = Point(4, 6)
polygon5 = Polygon([p21, p22, p23, p24, p21])

p25 = Point(0, 0)
p26 = Point(5, 3)
p27 = Point(7, 7)
p28 = Point(3, 5)
polygon6 = Polygon([p25, p26, p27, p28, p25])

def test_non_overlapping_area_1_25_75():
    result = non_overlapping_area(polygon1, polygon2)
    assert result == [1, 25.75], f"Overlap is not recognized correctly or area is not 25.75 but {result[1]}"
    print(polygon1.calculate_area())
    print(polygon2.calculate_area())
    print(polygon1.calculate_area() + polygon2.calculate_area() - result[1])
    print(result[1])
    print('test passed')


def test_non_overlapping_area_2():
    result = non_overlapping_area(polygon3, polygon4)
    assert result == [1, 70.72], f"Overlap is not recognized correctly or area is not 25.75 but {result[1]}"
    print(polygon3.calculate_area())
    print(polygon4.calculate_area())
    print(polygon3.calculate_area()+polygon4.calculate_area()-result[1])
    print(result[1])
    print('test passed')

def test_non_overlapping_area_3():
    result = non_overlapping_area(polygon5, polygon6)
    assert result == [1, 14.5], f"Overlap is not recognized correctly or area is not 25.75 but {result[1]}"
    print(polygon5.calculate_area())
    print(polygon6.calculate_area())
    print(polygon5.calculate_area() + polygon6.calculate_area() - result[1])
    print(result[1])
    print('test passed')

test_non_overlapping_area_2()
test_non_overlapping_area_1_25_75()
test_non_overlapping_area_3()

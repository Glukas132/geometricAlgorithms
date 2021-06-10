# Excercise sheet 2 (100 points in total)
# You are allowed to write own helper functions but the signatures for the solution functions (name and parameter)
# must be as they are provided. You cannot change the name because automatic tests will fail and you will get 0 points
# for this exercise.

from exercises.helper_classes import *
import random as rnd


# Exercise 1
def is_polygon_convex(polygon):
    """
    Checks if a polygon is convex or not.
    :param polygon: Polygon to be checked.
    :return: If the given polygon is convex True is returned, otherwise False.
    """
    return polygon.is_convex()


# Exercise 2
# Please answer the question: Is the centroid always inside the given polygon?
# No, the centroid of a polygon may be for example in a hole or in a "cave" of a concave polygon

def polygon_centroid(polygon):
    """
    Calculates the centroid of a polygon.
    :param polygon: The polygon whose centroid will be calculated.
    :return: The centroid of the given Polygon. It is a Point object.
    """
    return polygon.calculate_centroid()


# Exercise 3
def random_points_in_polygon(polygon, n, seed):
    """
    Generates n random points in a polygon. Points are pairwise different.
    :param polygon: The polygon where random points will be generated in.
    :param n: Number of random points to be generated.
    :param seed: Seed used for random number generation. Useful to reproduce same results.
    :return: Returns a list of Point objects which lie inside the given polygon.
    """
    rnd.seed(seed)
    x_min, x_max, y_min, y_max = polygon.calculate_bounds()
    random_points = []
    while len(random_points) < n:
        x = x_min + rnd.random() * (x_max - x_min)
        y = y_min + rnd.random() * (y_max - y_min)
        new_point = Point(x, y)
        if point_in_polygon(new_point, polygon):
            skip = False
            for point in random_points:
                if point == new_point:
                    skip = True
            if not skip:
                random_points.append(new_point)
    return random_points


def point_in_polygon(point: Point, polygon: Polygon):
    segments = polygon.get_line_segments()
    for segment in segments:
        if point.point_position(segment.startNode, segment.endNode) == -1:
            return False

    for hole in polygon.holes:
        if point_in_polygon(point, hole):
            return False
    return True


# Exercise 4
def jarvis_march(point_list):
    """
    Calculates the convex hull of a given point list with the MergeHull algorithm.
    :param point_list: Point list whose convex hull will be calculated
    :return: A list with Point objects being part of the convex hull of the the given point list.
    This list starts with the point with the lowest x coordinate and then  points are sorted in counterclockwise
    order from that point.
    """
    convex_hull = []
    # find the point with the lowest Y-Coordinate; if two points have same Y-Coordinate, take the one with lower X-Coord
    p0 = point_list[0]
    for point in point_list:
        if point.yCoord < p0.yCoord or (point.yCoord == p0.yCoord and point.xCoord < p0.xCoord):
            p0 = point

    convex_hull.append(p0)
    convex_hull.append(lowest_angle(point_list, p0, p0 + Point(1, 0)))

    while convex_hull[0] != convex_hull[-1]:
        convex_hull.append(lowest_angle(point_list, convex_hull[-2], convex_hull[-1]))

    return convex_hull[:-1]


def lowest_angle(point_list, point1, point2):
    """
    finds the point from point_list with the lowest angle to the line between point1 and point2
    :param point_list: a list of points to be searched
    :param point1: the startpoint of the line
    :param point2: the endpoint of the line
    :return: the point with the lowest angle
    """
    min_angle = math.inf
    min_point = None
    for point in point_list:
        if point != point1 and point != point2:
            point_along_line = Point(2 * point2.xCoord - point1.xCoord, 2 * point2.yCoord - point1.yCoord)
            angle = point2.angle_between(point_along_line, point)
            if angle < min_angle:
                min_angle = angle
                min_point = point
    return min_point


# Exercise 5
def spiral(point_list):
    """
    Calculates the spiral-like Polyline of a given point list with Graham’s scan.
    :param point_list: Point list from which the spiral-like Polyline will be calculated
    :return: The list of sorted Point objects starting from the left-most point and proceeding counter-clockwise.
    """
    p0 = find_leftmost_point(point_list)
    point_list.remove(p0)
    sorted_list = polar_sort(point_list, p0)
    convex_hull = [p0]
    for k in sorted_list:
        j = convex_hull[-1]
        try:
            i = convex_hull[-2]
        except:
            i = None
        while i is not None and i.point_position(j, k) == -1:
            convex_hull.pop()
            j = i
            try:
                i = convex_hull[-2]
            except:
                i = None
        convex_hull.append(k)
    for point in convex_hull:
        if point in point_list:
            point_list.remove(point)
    if len(point_list) > 1:
        convex_hull.extend(spiral(point_list))
    else:
        convex_hull.extend(point_list)
    return convex_hull


def find_leftmost_point(point_list):
    result = Point(math.inf, math.inf)
    for point in point_list:
        if point.xCoord < result.xCoord or (point.xCoord == result.xCoord and point.yCoord < result.yCoord):
            result = point
    return result


def polar_sort(point_list, p0):
    if len(point_list) <= 1:
        return point_list

    ref_point = point_list[len(point_list) // 2]
    ref_angle = p0.angle_between(p0 + Point(0, -1), ref_point)

    result_list = []
    lower_list = []
    middle_list = []
    upper_list = []

    for point in point_list:
        point_angle = p0.angle_between(p0 + Point(0, -1), point)
        if ref_angle == point_angle:
            middle_list.append(point)
        elif ref_angle > point_angle:
            lower_list.append(point)
        else:
            upper_list.append(point)

    if len(middle_list) > 1:
        sort_points_by_length(middle_list, p0)

    result_list.extend(polar_sort(lower_list, p0))
    result_list.extend(middle_list)
    result_list.extend(polar_sort(upper_list, p0))

    return result_list


def sort_points_by_length(point_list, p0):
    ref_point = point_list[len(point_list) // 2]
    lower_list = []
    middle_list = []
    upper_list = []
    for point in point_list:
        if p0.length_to(ref_point) == p0.length_to(point):
            middle_list.append(point)
        elif p0.length_to(ref_point) > p0.length_to(point):
            lower_list.append(point)
        else:
            upper_list.append(point)

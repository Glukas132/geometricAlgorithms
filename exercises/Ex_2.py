# Excercise sheet 2 (100 points in total)
# You are allowed to write own helper functions but the signatures for the solution functions (name and parameter)
# must be as they are provided. You cannot change the name because automatic tests will fail and you will get 0 points
# for this exercise.

from exercises.helper_classes import Point


# Exercise 1
def is_polygon_convex(polygon):
    """
    Checks if a polygon is convex or not.
    :param polygon: Polygon to be checked.
    :return: If the given polygon is convex True is returned, otherwise False.
    """
    return True


# Exercise 2
# Please answer the question: Is the centroid always inside the given polygon?
def polygon_centroid(polygon):
    """
    Calculates the centroid of a polygon.
    :param polygon: The polygon whose centroid will be calculated.
    :return: The centroid of the given Polygon. It is a Point object.
    """
    return Point


# Exercise 3
def random_points_in_polygon(polygon, n, seed):
    """
    Generates n random points in a polygon. Points are pairwise different.
    :param polygon: The polygon where random points will be generated in.
    :param n: Number of random points to be generated.
    :param seed: Seed used for random number generation. Useful to reproduce same results.
    :return: Returns a list of Point objects which lie inside the given polygon.
    """
    return [Point]


# Exercise 4
def jarvis_march(point_list):
    """
    Calculates the convex hull of a given point list with the MergeHull algorithm.
    :param point_list: Point list whose convex hull will be calculated
    :return: A list with Point objects being part of the convex hull of the the given point list.
    This list starts with the point with the lowest x coordinate and then  points are sorted in counterclockwiseorder from that point.
    """
    return [Point]


# Exercise 5
def spiral(point_list):
    """
    Calculates the spiral-like Polyline of a given point list with Graham’s scan.
    :param point_list: Point list from which the spiral-like Polyline will be calculated
    :return: The list of sorted Point objects starting from the left-most point and proceeding counter-clockwise.
    """
    return [Point]

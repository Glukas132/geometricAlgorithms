# Excercise sheet 3 (100 points in total)
# You are allowed to write own helper functions but the signatures for the solution functions (name and parameter)
# must be as they are provided. You cannot change the name because automatic tests will fail and you will get 0 points
# for this exercise.

from exercises.helper_classes import *


# Exercise 1
def bisector(point1, point2, length=1):
    """
    Calculates the bisector for two given points
    :param point1: First point for the bisector.
    :param point2: Second point for the bisector.
    :param length: Length of the calculated bisector. Default is 1.
    :return: The bisector for point1 and point2 of the given length as Line object.
    """
    return Line


# Exercise 2
def point_intersection_plane_sweep(lines):
    """
    Calculates all intersections for a given set of lines.
    :param lines: The list of lines whose mutual intersections will be calculated.
    :return: A list of intersection points for the given list of lines.
    """
    return [Point]


# Exercise 3
def delaunay_triangulation(point_list, bb_triangle):
    """
    Calculates the delaunay triangulation of a given point list.
    :param point_list: Point list whose delaunay triangulation will be calculated
    :param bb_triangle: the traingle containing all points in it and represent the boundary of triangulation.
    :return: A set of Polygon objects representing the formed triangles.
    """
    return {Polygon}

# Exercise 4
def voronoi(point_list, boundary):
    """
    Calculates the voronoi diagram of a given point list.
    :param point_list: Point list whose delaunay triangulation will be calculated
    :param boundary: the traingle containing all points in it and represent the boundary of voronoi diagram.
    :return: A set of Polygon objects representing the formed voronoi cells.
    """
    return {Polygon}


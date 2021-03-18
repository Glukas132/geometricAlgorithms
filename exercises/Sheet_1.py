# Exercise sheet 1 (100 points in total)
# You are allowed to write own helper functions but the signatures for the solution functions (name and parameter)
# must be as they are provided. You cannot change the name because automatic tests will fail and you will get 0 points
# for this exercise.

from exercises.helper_classes import *

# Exercise 1
# Write your answer please as comment.
# Write your code that provides you with the above answer.
def smallest_n():
    n = 1
    while 100*n**2 > 2**n:
        n += 1
    print(n)

# smallest n for which O(100*n**2) faster than O(2**n) = 15
# smallest_n()

# Exercise 2
def polygon_contains_polygon(polygon1, polygon2):
    """
    :param polygon1: Polygon 1 of type Polygon
    :param polygon2: Polygon 2 of type Polygon
    :return: A list containing 0(False: no polygon contains the other) or 1(True: one polygon contains the other)
    as the first element and the vertices (Point objects) of the polygon which is inside the other.
    """

    result = [0]
    vertices_of_inside_polygon1 = []
    vertices_of_inside_polygon2 = []

    poly1_in_poly2 = True
    for vertex in polygon1.points:
        if is_vertex_inside_polygon(vertex, polygon2):
            vertices_of_inside_polygon1.append(vertex)
        else:
            poly1_in_poly2 = False

    poly2_in_poly1 = True
    for vertex in polygon2.points:
        if is_vertex_inside_polygon(vertex, polygon1):
            vertices_of_inside_polygon2.append(vertex)
        else:
            poly2_in_poly1 = False

    if poly1_in_poly2:
        result[0] = 1
        result.extend(vertices_of_inside_polygon1)
    if poly2_in_poly1:
        result[0] = 1
        result.extend(vertices_of_inside_polygon2)
    # in case poly1 == poly2 then poly1 is inside poly2 and poly2 is inside poly1 -> all vertices are in return list

    return result


def is_vertex_inside_polygon(vertex: Point, polygon: Polygon):
    segments = polygon.get_line_segments()
    for segment in segments:
        if vertex.point_position(segment.startNode, segment.endNode) == -1:
            return False

    for i, hole in enumerate(polygon.holes):
        segments = polygon.get_hole_line_segments(i)
        for segment in segments:
            if vertex.point_position(segment.startNode, segment.endNode) != -1:
                return False

    return True


# Exercise 3
def non_overlapping_area(polygon1, polygon2):
    """
    :param polygon1: Polygon 1 of type Polygon
    :param polygon2: Polygon 2 of type Polygon
    :return: A list containing 0(False: in case of no overlap) or 1(True: in case of overlap) as the first element
    and the area of the non_overlapping area of both polygons summed and rounded to two decimal digits (example 23.43).
    """
    overlapping_result = 0
    non_overlapping_area = 0
    return [overlapping_result, non_overlapping_area]


# Exercise 4
def percentage_polylines_in_polygons(polyline_list, polygon_list):
    """

    :param polyline_list: A list of objects of type Polyline
    :param polygon_list: A list of objects of type Polygon
    :return: the list of polylines that satisfies the condition of lying more than 50% (>= 50%)
    inside the provided polygons.
    """
    lines_50_percent = []
    return lines_50_percent


# Exercise 5
def sort_points(point_list, mode="SN", reverse=False):
    """

    :param point_list: List of points to be sorted
    :param mode: According to which feature the list should be sorted, possible values are: SN, WE, distance_to_centroid
    :param reverse: If the list should be reversed (default condition in case of mode="distance_to_centroid" is ascending)
    :return: The sorted list of points
    """
    return []

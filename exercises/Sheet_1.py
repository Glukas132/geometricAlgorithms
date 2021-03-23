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
    while 100 * n ** 2 > 2 ** n:
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

    for hole in polygon.holes:
        if is_vertex_inside_polygon(vertex, hole):
            return False
    return True


# Exercise 3
def create_in_out_lists(polygon1, polygon2):
    string1 = 'intersection'
    string2 = 'intersection'
    poly1_points = []
    poly1_in_out = []
    intersection_counter = 0
    for point in polygon1.points:
        if len(poly1_in_out) > 0:
            for line in polygon2.get_line_segments():
                if Line(poly1_points[-1], point).is_intersecting_line(line):
                    if intersection_counter % 2 == 0:
                        poly1_in_out.append(string1)
                    else:
                        poly1_in_out.append(string2)
                    intersection_counter += 1
                    poly1_points.append(Line(poly1_points[-1], point).intersect_line(line))
        if is_vertex_inside_polygon(point, polygon2):
            poly1_in_out.append('in')
            poly1_points.append(point)
        else:
            poly1_in_out.append('out')
            poly1_points.append(point)
        if intersection_counter == 0:
            if poly1_in_out[0] == 'in':
                string1 = 'leaving'
                string2 = 'entering'
            else:
                string1 = 'entering'
                string2 = 'leaving'
    poly1_in_out.pop()
    poly1_points.pop()

    for i in range(len(poly1_in_out)-1):
        if poly1_in_out[i] == 'entering' and poly1_in_out[i+1] != 'in':
            if Line(poly1_points[i-1], poly1_points[i]).get_length() - Line(poly1_points[i-1], poly1_points[i+1]).get_length() > 0:
                poly1_points[i], poly1_points[i+1] = poly1_points[i+1], poly1_points[i]

    return [poly1_in_out, poly1_points, intersection_counter]

def non_overlapping_area(polygon1, polygon2):
    """
    :param polygon1: Polygon 1 of type Polygon
    :param polygon2: Polygon 2 of type Polygon
    :return: A list containing 0(False: in case of no overlap) or 1(True: in case of overlap) as the first element
    and the area of the non_overlapping area of both polygons summed and rounded to two decimal digits (example 23.43).
    """
    contains_result = polygon_contains_polygon(polygon1, polygon2)
    if contains_result[0] == 1:
        if len(contains_result[1:]) == len(polygon1.points)+len(polygon2.points):
            return [1, 0]  # polygons are identical, they overlap completely and the non overlapping area is 0
        else:
            if polygon1.points[0].sameCoordinates(contains_result[1]) and \
                    polygon1.points[1].sameCoordinates(contains_result[2]):
                return [1, polygon2.calculate_area() - polygon1.calculate_area()]  # polygon2 contains polygon1
            else:
                return [1, polygon1.calculate_area() - polygon2.calculate_area()]  # polygon1 contains polygon2


    overlapping_result = 0
    overlapping_polygon_points = []
    poly1_in_out, poly1_points, intersection_counter = create_in_out_lists(polygon1, polygon2)
    poly2_in_out, poly2_points, intersection_counter = create_in_out_lists(polygon2, polygon1)
    i = 0
    j = 0
    if len(poly1_in_out) == 0:
        print('polys not overlapping')
        return
    for intersection in range(intersection_counter//2):
        while poly1_in_out[i % len(poly1_in_out)] != 'entering':
            i += 1
        while poly1_in_out[i % len(poly1_in_out)] != 'leaving':
            overlapping_polygon_points.append(poly1_points[i % len(poly1_in_out)])
            i += 1
        while poly2_in_out[j % len(poly2_in_out)] != 'entering' or not poly2_points[j % len(poly2_in_out)].sameCoordinates(poly1_points[i % len(poly1_in_out)]):
            j += 1
        while poly2_in_out[j % len(poly2_in_out)] != 'leaving':
            overlapping_polygon_points.append(poly2_points[j % len(poly2_in_out)])
            j += 1

    non_overlapping_area = polygon1.calculate_area() + polygon2.calculate_area()
    if len(overlapping_polygon_points) > 3:
        overlapping_result = 1
        overlapping_polygon_points.append(overlapping_polygon_points[0])
        overlapping_polygon = Polygon(overlapping_polygon_points)
        non_overlapping_area -= overlapping_polygon.calculate_area()
    non_overlapping_area = round(non_overlapping_area, 2)
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

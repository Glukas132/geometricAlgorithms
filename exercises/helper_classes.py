# point class
import math


class Point:
    # xCoord and yCoord are numeric values
    def __init__(self, xCoord=0, yCoord=0):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def __eq__(self, other):
        if abs(self.yCoord - other.yCoord) < 10 ** -9 and abs(self.xCoord - other.xCoord) < 10 ** -9:
            return True
        else:
            return False

    def __add__(self, other):
        x = self.xCoord + other.xCoord
        y = self.yCoord + other.yCoord
        return Point(x, y)

    def __sub__(self, other):
        x = self.xCoord - other.xCoord
        y = self.yCoord - other.yCoord
        return Point(x, y)

    def __mul__(self, scalar):
        x = self.xCoord * scalar
        y = self.yCoord * scalar
        return Point(x, y)

    def __div__(self, scalar):
        x = self.xCoord / scalar
        y = self.yCoord / scalar
        return Point(x, y)

    def sameCoordinates(self, point):
        if abs(self.yCoord - point.yCoord) < 0.00001 and abs(self.xCoord - point.xCoord) < 0.00001:
            return True
        else:
            return False

    def angle_between(self, point1, point2):
        """
        Calculates the angle between self-point1 and self-point2 in radians
        :param point1: first point
        :param point2: second point
        :return: the angle in radians
        """
        angle = math.atan2(point2.yCoord - self.yCoord, point2.xCoord - self.xCoord) - \
                math.atan2(point1.yCoord - self.yCoord, point1.xCoord - self.xCoord)
        return angle

    def length_to(self, point):
        return ((self.xCoord - point.xCoord) ** 2 + (self.yCoord - point.yCoord) ** 2) ** 0.5

    # taken from the slides
    def point_position(self, point1, point2):
        """
        Calculates whether this point is left, right or collinear to another two points
        :param point1: first point to define a line
        :param point2: second point to define a line
        :return: 0 - if the points are collinear;
                 1 if the point is to the left of the line;
                 -1 if the point is to the right of the line
        """
        z_mod = (point2.xCoord - point1.xCoord) * (self.yCoord - point1.yCoord) - (self.xCoord - point1.xCoord) * (
                point2.yCoord - point1.yCoord)
        if z_mod == 0:
            return 0
        elif z_mod > 0:
            return 1
        else:
            return -1


# line class
class Line:
    # Line constructor which requires two points
    def __init__(self, p1, p2):
        if type(p1) is not Point or type(p2) is not Point:
            raise Exception("P1 and P2 has to be of type Point")
        self.startNode = p1
        self.endNode = p2

    def __eq__(self, other):
        return self.endNode == other.endNode and self.startNode == other.startNode or \
               self.endNode == other.startNode and self.startNode == other.endNode

    # taken from the slides
    def is_intersecting_line(self, line):
        """
        Calculates whether this line intersects another line
        :param line: the line to intersection with
        :return: 1 if the lines intersect; 0 if the lines don't intersect
        """
        return \
            (line.startNode.point_position(self.startNode, self.endNode) *
             line.endNode.point_position(self.startNode, self.endNode)) < 0 and \
            (self.startNode.point_position(line.startNode, line.endNode) *
             self.endNode.point_position(line.startNode, line.endNode)) < 0

    def intersect_line(self, line):
        '''
        Calculates the coordinates of the intersection between two lines and returns it as a point
        :param line: the line to intersect with
        :return: the intersection as a point; False if there is no intersection
        '''
        intersection = Point(0, 0)
        if not self.is_intersecting_line(line):
            return False
        x1 = self.startNode.xCoord
        y1 = self.startNode.yCoord
        x2 = self.endNode.xCoord
        y2 = self.endNode.yCoord
        x3 = line.startNode.xCoord
        y3 = line.startNode.yCoord
        x4 = line.endNode.xCoord
        y4 = line.endNode.yCoord
        # Formula taken from
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line_segment
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection.xCoord = (x1 + t * (x2 - x1))
        intersection.yCoord = (y1 + t * (y2 - y1))
        return intersection

    def get_length(self):
        """
        Calculates the length of the line
        :return: the length
        """
        return ((self.endNode.xCoord - self.startNode.xCoord) ** 2 + (
                self.endNode.yCoord - self.startNode.yCoord) ** 2) ** 0.5


# polyline class
class Polyline:
    # pointList is a list [] of Point class objects
    def __init__(self, line_list):
        if len(line_list) <= 1:
            raise Exception('Polyline must have at least 2 lines')
        self.lines = line_list

    def get_length(self):
        length = 0
        for line in self.lines:
            length += line.get_length()
        return length

    def get_points(self):
        points = []
        for line in self.lines:
            if len(points) == 0:
                points.append(line.startNode)
            points.append(line.endNode)


# Polygon class (CCW - see picture in readme file)
class Polygon:
    def __init__(self, arrayOfPoints, arrayOfHoles=None):
        if arrayOfHoles is None:
            arrayOfHoles = []
        if len(arrayOfPoints) < 4:
            raise Exception("Polygon has to have at least 4 points (first and last point should be the same)")
        if not arrayOfPoints[0].sameCoordinates(arrayOfPoints[-1]):
            raise Exception("First and last point should be the same")
        if not all(type(point) is Point for point in arrayOfPoints):
            raise Exception("Only Points should be in the list")
        self.points = arrayOfPoints
        self.holes = arrayOfHoles

    def calculate_area(self):
        area = 0
        for i in range(len(self.points) - 1):
            area += (self.points[i].xCoord + self.points[i + 1].xCoord) * (
                    self.points[i + 1].yCoord - self.points[i].yCoord)

        for hole in self.holes:
            area -= hole.calculate_area()

        return abs(area / 2)

    def get_line_segments(self):
        segments = []
        for segment_number in range(len(self.points) - 1):
            segments.append(Line(self.points[segment_number], self.points[segment_number + 1]))
        return segments

    def is_convex(self):
        for i in range(2, len(self.points)):
            if self.points[i].point_position(self.points[i - 2], self.points[i - 1]) == -1:
                return False
        return True

    def calculate_centroid(self):
        area = self.calculate_area()
        centroid_x = 0
        centroid_y = 0
        for i in range(len(self.points) - 1):
            centroid_x += (self.points[i].xCoord + self.points[i + 1].xCoord) * \
                          (self.points[i].xCoord * self.points[i + 1].yCoord -
                           self.points[i + 1].xCoord * self.points[i].yCoord)
        centroid_x /= 6 * area

        for i in range(len(self.points) - 1):
            centroid_y += (self.points[i].yCoord + self.points[i + 1].yCoord) * \
                          (self.points[i].xCoord * self.points[i + 1].yCoord -
                           self.points[i + 1].xCoord * self.points[i].yCoord)
        centroid_y /= 6 * area

        for hole in self.holes:
            hole_centroid = hole.calculate_centroid()
            hole_area = hole.calculate_area()
            centroid_x = (centroid_x * area - hole_centroid.xCoord * hole_area) / (area - hole_area)
            centroid_y = (centroid_y * area - hole_centroid.yCoord * hole_area) / (area - hole_area)

        return Point(centroid_x, centroid_y)

    def calculate_bounds(self):
        x_min, y_min = math.inf, math.inf
        x_max, y_max = -math.inf, -math.inf
        for point in self.points:
            if point.xCoord > x_max:
                x_max = point.xCoord
            if point.yCoord > y_max:
                y_max = point.yCoord
            if point.xCoord < x_min:
                x_min = point.xCoord
            if point.yCoord < y_min:
                y_min = point.yCoord
        return x_min, x_max, y_min, y_max

    def draw(self):
        output = ''
        counter = 0
        for i in range(19, -1, -1):
            for j in range(20):
                found = False
                for point in self.points[:-1]:
                    if point.yCoord == i and point.xCoord == j:
                        output += '\u25CF'
                        counter += 1
                        found = True
                if not found:
                    output += ' '
            if counter == len(self.points) - 1:
                break
            output += '\n'
        print(output)
        print('____________________')


# A hole is a polygon but WITHOUT further holes inside it
class Hole:
    def __init__(self, arrayOfPoints):
        if len(arrayOfPoints) < 4:
            raise Exception("A Hole has to have at least 4 points (first and last point should be the same)")
        if not arrayOfPoints[0].sameCoordinates(arrayOfPoints[-1]):
            raise Exception("First and last point should be the same")
        if not all(type(point) is Point for point in arrayOfPoints):
            raise Exception("Only Points should be in the list")
        self.points = arrayOfPoints
        # no further holes inside holes
        self.holes = []

    def is_convex(self):
        for i in range(2, len(self.points)):
            if self.points[i - 2].point_position(self.points[i - 1], self.points[i]) == -1:
                return False
        return True

    def get_line_segments(self):
        segments = []
        for segment_number in range(len(self.points) - 1):
            segments.append(Line(self.points[segment_number], self.points[segment_number + 1]))
        return segments

    def calculate_area(self):
        area = 0
        for i in range(len(self.points) - 1):
            area += (self.points[i].xCoord + self.points[i + 1].xCoord) * (
                    self.points[i + 1].yCoord - self.points[i].yCoord)
        return abs(area / 2)

    def calculate_centroid(self):
        area = self.calculate_area()
        centroid_x = 0
        centroid_y = 0
        for i in range(len(self.points) - 1):
            centroid_x += (self.points[i].xCoord + self.points[i + 1].xCoord) * \
                          (self.points[i].xCoord * self.points[i + 1].yCoord -
                           self.points[i + 1].xCoord * self.points[i].yCoord)
        centroid_x /= 6 * area

        for i in range(len(self.points) - 1):
            centroid_y += (self.points[i].yCoord + self.points[i + 1].yCoord) * \
                          (self.points[i].xCoord * self.points[i + 1].yCoord -
                           self.points[i + 1].xCoord * self.points[i].yCoord)
        centroid_y /= 6 * area
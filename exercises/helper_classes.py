# point class
class Point:
    # xCoord and yCoord are numeric values
    def __init__(self, xCoord=0, yCoord=0):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def sameCoordinates(self, point):
        if self.yCoord == point.yCoord and self.xCoord == point.xCoord:
            return True
        else:
            return False

    # taken from the slides
    def point_position(self, point1, point2):
        """
        Calculates whether the point is left, right or collinear to another two points
        :param point1: first point to define a line
        :param point2: second point to define a line
        :return: 0 - if the points are collinear;
                 1 if the point is to the left of the line;
                 -1 if the point is to the right of the line
        """
        z_mod = (point2.xCoord - point1.xCoord) * (self.yCoord - point1.yCoord) - (self.xCoord - point1.xCoord) * (point2.yCoord - point1.yCoord)
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

    # taken from the slides
    def intersect_line(self, line):
        """
        Calculates whether this line intersects another line
        :param line: the line to intersection with
        :return: 1 if the lines intersect; 0 if the lines don't intersect
        """
        return  \
            (line.startNode.point_position(self.startNode, self.endNode) *
             line.endNode.point_position(self.startNode, self.endNode)) < 0 and \
            (self.startNode.point_position(line.startNode, line.endNode) *
             self.endNode.point_position(line.startNode, line.endNode)) < 0

    def get_length(self):
        """
        Calculates the length of the line
        :return: the length
        """
        return ((self.endNode.xCoord - self.startNode.xCoord)**2+(self.endNode.yCoord - self.startNode.yCoord)**2)**0.5


# polyline class
class Polyline:
    # pointList is a list [] of Point class objects
    def __init__(self, line_list):
        if len(line_list) <= 1:
            raise Exception('Polyline must have at least 2 lines')
        self.lines = line_list


# Polygon class (CCW - see picture in readme file)
class Polygon:
    def __init__(self, arrayOfPoints, arrayOfHoles=None):
        if arrayOfHoles is None:
            arrayOfHoles = [].copy()
        if len(arrayOfPoints) < 4:
            raise Exception("Polygon has to have at least 4 points (first and last point should be the same)")
        if not arrayOfPoints[0].sameCoordinates(arrayOfPoints[-1]):
            raise Exception("First and last point should be the same")
        if not all(type(point) is Point for point in arrayOfPoints):
            raise Exception("Only Points should be in the list")
        self.points = arrayOfPoints
        self.holes = arrayOfHoles

    def get_line_segments(self):
        segments = []
        for segment_number in range(len(self.points)-1):
            segments.append(Line(self.points[segment_number], self.points[segment_number+1]))
        return segments

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
            if counter == len(self.points)-1:
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

    def get_line_segments(self):
        segments = []
        for segment_number in range(len(self.points)-1):
            segments.append(Line(self.points[segment_number], self.points[segment_number+1]))
        return segments

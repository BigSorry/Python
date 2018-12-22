import math
class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
class Circle:
    def __init__(self, center, radius):
        self.center = Point(center.x, center.y)
        self.radius = radius
class Rectangle:
    def __init__(self, leftUpper, rightDown):
        self.leftUpper = Point(leftUpper.x, leftUpper.y)
        self.rightDown = Point(rightDown.x, rightDown.y)


def pointInCircle(circle, point):
    distanceCenter = math.sqrt( (point.x-circle.center.x)**2 + (point.y - circle.center.y)**2 )
    if distanceCenter > circle.radius:
        return False
    else:
        return True
def rectInCircle(circle, rectangle):
    distanceUpper = math.sqrt((rectangle.leftUpper.x - circle.center.x) ** 2 + (rectangle.leftUpper.y - circle.center.y) ** 2)
    distanceLow = math.sqrt((rectangle.rightDown.x - circle.center.x) ** 2 + (rectangle.rightDown.y - circle.center.y) ** 2)
    if distanceUpper > circle.radius or distanceLow > circle.radius:
        return False
    else:
        return True
def rectCircleOverlap(circle, rectangle):
    distanceUpperLeft = math.sqrt((rectangle.leftUpper.x - circle.center.x) ** 2 + (rectangle.leftUpper.y - circle.center.y) ** 2)
    distanceUpperRight = math.sqrt((rectangle.rightDown.x - circle.center.x) ** 2 + (rectangle.leftUpper.y - circle.center.y) ** 2)
    distanceLowLeft = math.sqrt((rectangle.leftUpper.x - circle.center.x) ** 2 + (rectangle.rightDown.y - circle.center.y) ** 2)
    distanceLowRight = math.sqrt((rectangle.rightDown.x - circle.center.x) ** 2 + (rectangle.rightDown.y - circle.center.y) ** 2)
    if distanceUpperLeft > circle.radius and distanceUpperRight > circle.radius and distanceLowLeft > circle.radius and distanceLowRight > circle.radius:
        return False
    else:
        return True

point = Point(1, 1)
radius = 10
circle = Circle(Point(0,0), radius)
rectangle = Rectangle(Point(1,1), Point(2,0))
print(pointInCircle(circle, point))
print(rectInCircle(circle, rectangle))
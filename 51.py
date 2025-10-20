# Collections Module

from collections import namedtuple

# Define a namedtuple to represent a Point
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)

print(p1)
print(p1.x, p1.y)
#  File: Geometry.py

#  Description:

#  Student Name: Simaak Siddiqi
 
#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) +')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot( (self.x - other.x) + (self.y - other.y) + (self.z - other.z) )

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    delta = 10e-6
    return abs(self.x - other.x) < delta and abs(self.y - other.y) \
        < delta and abs(self.z - other.z) < delta
class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.radius = radius
    self.center = Point(x,y,z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(self.center) + '), Radius: ' + self.radius 
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    area = 4 * math.pi*(self.radius ** 2)
    return area
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    volume = 4/3 * math.pi * (self.radius ** 3)
    return volume
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if abs(self.center.distance(p)) > self.radius:
        return False
    return True
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    if abs(self.center.distance(other.center)) + other.radius > self.radius:
        return False
    return True
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    return (self.is_inside_point(a_cube.corner1) and self.is_inside_point(a_cube.corner2) \
           and self.is_inside_point(a_cube.corner3) and self.is_inside_point(a_cube.corner4) \
           and self.is_inside_point(a_cube.corner5) and self.is_inside_point(a_cube.corner6) \
           and self.is_inside_point(a_cube.corner7) and self.is_inside_point(a_cube.corner8))
  # determine if a Cube is strictly outside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # outside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_outside_cube(self, a_cube):
    if self.center.distance(a_cube.center) < self.radius + (a_cube.side / math.sqrt(2)):
        return False
    return True
  # determine if another Sphere is strictly outisde this Sphere
  # other is a Sphere object
  # returns a Boolean  
  def is_outside_sphere(self, other):
    if abs(self.radius) + abs(other.radius) > self.center.distance(other.center):
        return False
    return True
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    return ((not self.is_inside_sphere(other) and not self.is_outside_sphere(other)))  
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    return ((not self.is_inside_cube(a_cube) and not self.is_outside_cube(a_cube))) 
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    other = Cube(self.center.x, self.center.y, self.center.z, self.radius*math.sqrt(2))
    return other


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = side
    # attribute that stores the corners of a cube
    # the order is the top corners first, going in clockwise
    # direction, then the bottom corners, going in clockwise
    # direction 
    corner1 = Point(self.center.x + ((self.side/2))  , (self.center.y + (self.side/2)), (self.center.z + (self.side/2)))
    corner2 = Point(self.center.x  + ((self.side/2)), (self.center.y - (self.side/2)), (self.center.z + (self.side/2)))
    corner3 = Point(self.center.x - ((self.side/2)), (self.center.y - (self.side/2)), (self.center.z + (self.side/2)))
    corner4 = Point(self.center.x - ((self.side/2)), (self.center.y + (self.side/2)), (self.center.z + (self.side/2)))
    corner5 = Point(self.center.x + ((self.side/2)), (self.center.y + (self.side/2)), (self.center.z - (self.side/2)))
    corner6 = Point(self.center.x + ((self.side/2)), (self.center.y - (self.side/2)), (self.center.z - (self.side/2)))
    corner7 = Point(self.center.x - ((self.side/2)), (self.center.y - (self.side/2)), (self.center.z - (self.side/2)))
    corner8 = Point(self.center.x - ((self.side/2)), (self.center.y + (self.side/2)), (self.center.z - (self.side/2)))

    self.corners = [corner1, corner2, corner3, corner4, corner5, corner6, corner7, corner8]


  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) +'),\
         Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return float(6 * self.side ** 2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return float(self.side ** 3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    xMin = min(self.center.x + (self.side / 2),  self.center.x - (self.side / 2))
    xMax = max(self.center.x + (self.side / 2),  self.center.x - (self.side / 2))
    yMin = min(self.center.y + (self.side / 2),  self.center.y - (self.side / 2))
    yMax = max(self.center.y + (self.side / 2),  self.center.y - (self.side / 2))
    zMin = min(self.center.z + (self.side / 2),  self.center.z - (self.side / 2))
    zMax = max(self.center.z + (self.side / 2),  self.center.z - (self.side / 2))
    return xMin < p.x < xMax and yMin < p.y < yMax and zMin < p.z < zMax

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return self.center.distance(self, a_sphere.center) < a_sphere.radius

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    for point in other.corners:
        if self.is_inside_point(point):
            continue
        else:
            return False
    return True


  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return not self.is_inside_cube(other) and \
        not other.is_inside_cube(self)

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    if self.does_intersect_cube(other):
        # finds the intersection on each plane
        xLength = min(self.corners[0].x, other.corners[0].x) \
            - max(self.corners[6].x, other.corners[6].x)
        yLength = min(self.corners[0].y, other.corners[0].y) \
            - max(self.corners[6].y, other.corners[6].y)
        zLength = min(self.corners[0].z, other.corners[0].z) \
        - max(self.corners[6].z, other.corners[6].z)
        return xLength * yLength * zLength
    else:
        return float(0)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    r = self.side / 2
    return Sphere(self.center.x, self.center.y, self.center.z, r)


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point(x,y,z)
    self.radius = radius
    self.height = height
    self.minz = self.center.z - self.height / 2
    self.maxz = self.center.z + self.height / 2

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' \
      + str(self.z) + ')'

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return (2 * math.pi * self.radius * self.radius) \
      + (2 * math.pi * math.radius ** 2)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return math.pi * (self.radius ** 2) * self.radius

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.minz < self.center.z < self.maxz and math.hypot((p.x - self.center.x) \
      + (p.y - self.center.y)) < self.radius

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    ...
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    for point in a_cube.corners:
        if a_cube.is_inside_point(point):
            continue
        else:
            return False
    return True


  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    return self.minz < other.minz < other.maxz < self.maxz and \
      math.hypot( (self.center.x - other.center.x) \
        + (self.center.y - other.center.y) ) + other.radius < self.radius

def main():
  # read data from standard input

  # read the coordinates of the first Point p

  # create a Point object 

  # read the coordinates of the second Point q

  # create a Point object 

  # read the coordinates of the center and radius of sphereA

  # create a Sphere object 

  # read the coordinates of the center and radius of sphereB

  # create a Sphere object

  # read the coordinates of the center and side of cubeA

  # create a Cube object 

  # read the coordinates of the center and side of cubeB

  # create a Cube object 

  # read the coordinates of the center, radius and height of cylA

  # create a Cylinder object 

  # read the coordinates of the center, radius and height of cylB

  # create a Cylinder object

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin

  # print if Point p is inside sphereA

  # print if sphereB is inside sphereA

  # print if cubeA is inside sphereA

  # print if sphereA intersects with sphereB

  # print if cubeB intersects with sphereB

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA

  # print if Point p is inside cubeA

  # print if sphereA is inside cubeA

  # print if cubeB is inside cubeA

  # print if cubeA intersects with cubeB

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA

  # print if Point p is inside cylA

  # print if sphereA is inside cylA

  # print if cubeA is inside cylA
  ...
if __name__ == "__main__":
  main()
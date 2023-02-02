#  File: Geometry.py

#  Description: This assignment is on object oriented programming. 
#         This assignment focuses on several classes that are fundamental 
#         in Solid Geometry - Point, Sphere, Cube, and Cylinder. 

#  Student Name: Simaak Siddiqi
 
#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 1/27/2023

#  Date Last Modified: 1/30/2023

import sys
import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) \
      + ', ' + str(self.z) +')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot( (self.x - other.x), \
      (self.y - other.y), (self.z - other.z) )

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    delta = 10e-6
    return abs(self.x - other.x) < delta \
      and abs(self.y - other.y) \
      < delta and abs(self.z - other.z) < delta
class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.radius = float(radius)
    self.center = Point(x,y,z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(self.center.x) + ', ' \
    + str(self.center.y) + ', ' \
    + str(self.center.z) +'), Radius: ' + str(self.radius)
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
    if self.center.distance(other.center) \
      + other.radius < self.radius:
        return True
    return False
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    for i in range(len(a_cube.corners)):
      if self.is_inside_point(a_cube.corners[i]):
        continue
      else:
        return False
    return True
  # determine if a Cube is strictly outside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # outside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_outside_cube(self, a_cube):
    if self.center.distance(a_cube.center) < self.radius \
      + (a_cube.side / math.sqrt(2)):
        return False
    return True
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    if self.radius >= other.radius:
      return ((not self.is_inside_sphere(other) \
        and (self.center.distance(other.center) \
        <= (self.radius + other.radius))))
    else:
      return ((not other.is_inside_sphere(self) \
        and (self.center.distance(other.center) \
        <= (self.radius + other.radius))))
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    return ((not self.is_inside_cube(a_cube) \
      and not self.is_outside_cube(a_cube))) 
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    other = Cube(self.center.x, self.center.y, self.center.z, \
      2*(self.radius/math.sqrt(3)))
    return other

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = float(side)
    # attribute that stores the corners of a cube
    # the order is the top corners first, going in clockwise
    # direction, then the bottom corners, going in clockwise
    # direction 
    corner1 = Point(self.center.x + ((self.side/2)), \
      (self.center.y + (self.side/2)), (self.center.z + (self.side/2)))
    corner2 = Point(self.center.x  + ((self.side/2)), \
      (self.center.y - (self.side/2)), (self.center.z + (self.side/2)))
    corner3 = Point(self.center.x - ((self.side/2)), \
      (self.center.y - (self.side/2)), (self.center.z + (self.side/2)))
    corner4 = Point(self.center.x - ((self.side/2)), \
      (self.center.y + (self.side/2)), (self.center.z + (self.side/2)))
    corner5 = Point(self.center.x + ((self.side/2)), \
      (self.center.y + (self.side/2)), (self.center.z - (self.side/2)))
    corner6 = Point(self.center.x + ((self.side/2)), \
      (self.center.y - (self.side/2)), (self.center.z - (self.side/2)))
    corner7 = Point(self.center.x - ((self.side/2)), \
      (self.center.y - (self.side/2)), (self.center.z - (self.side/2)))
    corner8 = Point(self.center.x - ((self.side/2)), \
      (self.center.y + (self.side/2)), (self.center.z - (self.side/2)))

    self.corners = [corner1, corner2, corner3, corner4, \
      corner5, corner6, corner7, corner8]

    self.minx = min(self.center.x + (self.side / 2),  \
      self.center.x - (self.side / 2))
    self.maxx = max(self.center.x + (self.side / 2),  \
      self.center.x - (self.side / 2))
    self.miny = min(self.center.y + (self.side / 2),  \
      self.center.y - (self.side / 2))
    self.maxy = max(self.center.y + (self.side / 2),  \
      self.center.y - (self.side / 2))
    self.minz = min(self.center.z + (self.side / 2),  \
      self.center.z - (self.side / 2))
    self.maxz = max(self.center.z + (self.side / 2),  \
      self.center.z - (self.side / 2))

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(self.center.x) + ', ' \
    + str(self.center.y) + ', ' \
    + str(self.center.z) +'), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return float(6 * self.side ** 2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return (float(self.side ** 3))

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.minx < p.x < self.maxx and self.miny < p.y < self.maxy \
      and self.minz < p.z < self.maxz

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return self.center.distance(a_sphere.center) \
      + a_sphere.radius < self.side / 2

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
  
  # determine if another Cube is strictly outside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_outside_cube(self, other):
    if other.minx <= self.minx and other.maxx <= self.minx:
      return True
    elif other.minx >= self.maxx and other.maxx >= self.maxx:
      return True
    elif other.miny <= self.miny and other.maxy <= self.miny:
      return True
    elif other.miny >= self.maxy and other.maxy >= self.maxy:
      return True
    elif other.minz <= self.minz and other.maxz <= self.minz:
      return True
    elif other.minz >= self.maxz and other.maxz >= self.maxz:
      return True
    else:
      return False

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    if self.side >= other.side:
      return (not self.is_inside_cube(other) and not self.is_outside_cube(other))
    elif self.side < other.side:
      return (not other.is_inside_cube(self) and not other.is_outside_cube(self))

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
    self.radius = float(radius)
    self.height = float(height)
    self.minz = self.center.z - self.height / 2
    self.maxz = self.center.z + self.height / 2

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(self.center.x) + ', ' \
    + str(self.center.y) + ', ' + str(self.center.z) + \
    '), Radius: ' + str(self.radius) + ', Height: ' + str(self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return (2 * math.pi * self.radius * self.height) \
      + (2 * math.pi * self.radius ** 2)

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return (math.pi * (self.radius ** 2) * self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.minz < p.z < self.maxz \
      and math.hypot((p.x - self.center.x), \
      (p.y - self.center.y)) < self.radius

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return ((self.center.distance(a_sphere.center) \
      + a_sphere.radius) < self.radius) \
      and ((self.center.distance(a_sphere.center) \
      + a_sphere.radius) < self.height / 2)
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    for point in a_cube.corners:
        if self.is_inside_point(point):
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
  line = sys.stdin.readline().strip()
  # read the coordinates of the first Point p
  coords = line.split()
  # create a Point object 
  p = Point(float(coords[0]), float(coords[1]), float(coords[2]))
  # read the coordinates of the second Point q
  line = sys.stdin.readline().strip()
  coords = line.split()
  # create a Point object 
  q = Point(float(coords[0]), float(coords[1]), float(coords[2]))
  # read the coordinates of the center and radius of sphereA
  line = sys.stdin.readline().strip()
  center_and_radius = line.split()
  # create a Sphere object 
  sphereA = Sphere(float(center_and_radius[0]), \
    float(center_and_radius[1]), float(center_and_radius[2]),\
    float(center_and_radius[3]))
  # read the coordinates of the center and radius of sphereB
  line = sys.stdin.readline().strip()
  center_and_radius = line.split()
  # create a Sphere object
  sphereB = Sphere(float(center_and_radius[0]), \
    float(center_and_radius[1]), float(center_and_radius[2]),\
    float(center_and_radius[3]))
  # read the coordinates of the center and side of cubeA
  line = sys.stdin.readline().strip()
  center_and_side = line.split()
  # create a Cube object 
  cubeA = Cube(float(center_and_side[0]), \
    float(center_and_side[1]), float(center_and_side[2]),\
    float(center_and_side[3]))
  # read the coordinates of the center and side of cubeB
  line = sys.stdin.readline().strip()
  center_and_side = line.split()
  # create a Cube object 
  cubeB = Cube(float(center_and_side[0]), float(center_and_side[1]),\
    float(center_and_side[2]), float(center_and_side[3]))
  # read the coordinates of the center, radius and height of cylA
  line = sys.stdin.readline().strip()
  center_rad_height = line.split()
  # create a Cylinder object 
  cylA = Cylinder(float(center_rad_height[0]), \
    float(center_rad_height[1]), float(center_rad_height[2]),\
    float(center_rad_height[3]), float(center_rad_height[4]))
  # read the coordinates of the center, radius and height of cylB
  line = sys.stdin.readline().strip()
  center_rad_height = line.split()
  # create a Cylinder object
  cylB = Cylinder(float(center_rad_height[0]), \
    float(center_rad_height[1]), float(center_rad_height[2]),\
    float(center_rad_height[3]), float(center_rad_height[4]))
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  origin = Point()
  if p.distance(origin) > q.distance(origin):
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
  # print if Point p is inside sphereA
  if sphereA.is_inside_point(p):
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')
  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA):
    print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')
  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere(sphereB):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB):
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  cube = sphereA.circumscribe_cube()
  if cube.volume() > cylA.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  # print if Point p is inside cubeA
  if cubeA.is_inside_point(p):
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
    print('cubeB is inside cubeA')
  else: 
    print('cubeB is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeB.intersection_volume(cubeA) > sphereA.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  sphere = cubeA.inscribe_sphere()
  if sphere.area() > cylA.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  # print if Point p is inside cylA
  if cylA.is_inside_point(p):
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')
  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA):
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA):
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')

if __name__ == "__main__":
  main()
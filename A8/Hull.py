
#  File: Hull.py

#  Description:

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/19/2023

#  Date Last Modified: 2/20/2023

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return ( ((q.x * r.y) - (r.x * q.y)) - ((p.x * r.y) - (r.x * p.y)) \
         + ((p.x * q.y) - (q.x * p.y)))

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  for i in range(2, len(sorted_points)):
    upper_hull.append(sorted_points[i])
    while (len(upper_hull) >= 3) and \
    det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) >= 0:
      upper_hull.pop(-2)
  
  # lower hull 
  lower_hull = []
  
  # Append the last two points p_n and p_n-1 in order into lower_hull
  #       with p_n as the first point.
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])

  # For i going from n - 2 downto 1
  for i in range((len(sorted_points) - 3), -1, -1):
    # Append p_i to lower_hull
    lower_hull.append(sorted_points[i])
    # While lower_hull contains three or more points and the last three
    #     points in the lower_hull do not make a right turn do
    while (len(lower_hull) >= 3) and \
          det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
      # Delete the middle of the last three points from lower_hull
      lower_hull.pop(-2)

  # Remove the first and last points for lower_hull to avoid duplication
  #       with points in the upper hull.
  lower_hull.pop(0) 
  lower_hull.pop(-1)

  # Append the points in the lower_hull to the points in the upper_hull 
  #       and call those points the convex_hull
  convex_hull = upper_hull + lower_hull

  # Return the convex_hull.
  return convex_hull
      
# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  x_coords = []
  y_coords = []
  for point in convex_poly:
    x_coords.append(point.x)
    y_coords.append(point.y)
  det = 0
  for i in range(len(convex_poly)):
    det += (x_coords[i] * y_coords[ (i+1) % (len(convex_poly))] \
           - y_coords[i] * x_coords[(i+1) % (len(convex_poly))] )
  area = (1/2) * abs(det)
  return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  convex_poly = convex_hull(sorted_points)
  print('Convex Hull')
  # print your results to standard output
  for point in convex_poly:
    # print the convex hull
    print(str(point))
  print()

  # run your test cases

  # get the area of the convex hull
  # print the area of the convex hull
  print('Area of Convex Hull =', area_poly(convex_poly))
  print()

if __name__ == "__main__":
  main()
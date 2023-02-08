#  File: OfficeSpace.py

#  Description:  This program sets up a system that lets employees make their office space requests.

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 1/28/2023

#  Date Last Modified: 2/5/2023

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  x = rect[2] - rect[0]
  y = rect[3] - rect[1]
  return abs(x * y)

# Input: a point which is two integers
# Output: an empty 2D matrix with row length x and column length y
def createBldg(x, y):
  building = []
  for i in range(y):
    building.append([])
    for j in range(x):
      building[i].append('')
  return building

# Input: an empty matrix, bldg, an employee ID, 
#           and a rectangle in the form of a tuple of 4 integers
# Output: a 2d matrix with the ID that describes the desired space
def assignSpace(bldg, nameID, rect):
  for i in range(rect[1], rect[3]):
    for j in range(rect[0],rect[2]):
      bldg[i][j] += str(nameID)
  return bldg

# Input: two rectangles in the form of tuples of 4 integers
# Output: a boolean describing if the two rectangles overlap
def doesOverlap(r1, r2):
  rect1min = (r1[0], r1[1])
  rect2min = (r2[0], r2[1])
  rect1max = (r1[2], r1[3])
  rect2max = (r2[2], r2[3])

  # If the squares are the same, then they do overlap
  if rect1max == rect2min or rect2min == rect1max:
    return True
  # Rectangles are to the left/right of eachother
  if rect1max[0] <= rect2min[0] or rect2max[0] <= rect1min[0]:
    return False 
  # Rectangles are above/below eachother
  if rect1max[1] <= rect2min[1] or rect2max[1] <= rect1min[1]:
    return False
  
  return True

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):

  if not doesOverlap(rect1, rect2):
    return (0, 0, 0, 0)
  larger_minimum_x = max(rect1[0], rect2[0])
  smaller_maximum_y = min(rect1[3], rect2[3])
  
  larger_minimum_y = max(rect1[1], rect2[1])
  smaller_maximum_x = min(rect1[2], rect2[2])
  

  return (larger_minimum_x, larger_minimum_y, smaller_maximum_x, smaller_maximum_y)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  freeSpace = 0
  for aisle in bldg:
    for space in aisle:
      if space:
        continue
      else:
        freeSpace += 1
  return freeSpace



# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  busySpace = 0
  for aisle in bldg:
    for space in aisle:
      if len(space) >= 2:
        busySpace += 1
  return busySpace

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  specialSpace = 0
  for i in range(rect[1], rect[3]):
    for j in range(rect[0], rect[2]):
      if len(bldg[i][j]) == 1:
        specialSpace += 1
  return specialSpace

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  # create the matrix representation of the office
  building = createBldg(office[2], office[3])
  nameID = 1
  # assign space to each person that requests a cubicle
  for cubicle in cubicles:
    building = assignSpace(
      building, nameID, (cubicle[0], 
      cubicle[1], cubicle[2], cubicle[3]))
    nameID += 1
  # by completion of loop, we should have a 2-D list 
  # with integers where each integer corresponds to a 
  # unique person that is requesting a cubicle

  # loop replaces each entry within the constructed 2-D 
  # list with the length of said entry
  for i in range(len(building)):
    for j in range(len(building[i])):
      building[i][j] = len(building[i][j])
  
  return building
  
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  # area test cases
  assert area ((0, 0, 1, 1)) == 1
  assert area ((5,6,7,10)) == 8
  # write your own test cases

  return "all test cases passed"


def main():
  # read the data
  # create the empty office
  empty_office = sys.stdin.readline().strip().split()
  total_space = tuple((0,0,int(empty_office[0]), int(empty_office[1])))
  office = createBldg(int(empty_office[0]), int(empty_office[1]))
  
  # x is the number of employees who are requesting office space
  x = int(sys.stdin.readline().strip())
  
  employee_IDs = {}
  employee_rects = []
  
  # create a loop for the amount of employees. We want to index at one 
  #         so we can have the first employee as '1' 
  #         which does not conflict with our other functions
  for i in range(1,x+1):
    employee = sys.stdin.readline().strip().split()
    employee_IDs[int(i)] = employee[0]
    employee_rects.append(((int(employee[1]), int(employee[2]), int(employee[3]), int(employee[4]))))
    office = assignSpace(office, i, employee_rects[-1])

  # run your test cases
  '''
  print (test_cases())
  '''
  # print the following results after computation

  # compute the total office space
  print('Total ' + str(area(total_space)))

  # compute the total unallocated space
  print('Unallocated ' + str(unallocated_space(office)))

  # compute the total contested space
  print('Contested ' + str(contested_space(office)))

  # compute the uncontested space that each employee gets
  for j in range(1, x + 1):
    print(str(employee_IDs[j]) + ' ' + str(uncontested_space(office, employee_rects[j-1])))

if __name__ == "__main__":
  main()

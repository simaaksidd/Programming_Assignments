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
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  xMax = max(rect1[2], rect2[2])
  yMax = max(rect1[3], rect2[3])
  building = createBldg(xMax, yMax)
  building = assignSpace(
    building, 1, (rect1[0], rect1[1], rect1[2], rect1[3]))
  building = assignSpace(
    building, 2, (rect2[0], rect2[1], rect2[2], rect2[3]))
  
  # traverse the building in search for overlap
  dummyBuilding = createBldg(xMax, yMax)
  for i in range(len(building)):
    for j in range(len(building[i])):
      if len(building[i][j]) > 1:
        dummyBuilding[i][j] = 1
  
  # create vector that will store useful information on indexing
  y = []
  y_value = 1

  # y will store which indexes of dummybuilding contain 
  # the y coordinates
  for row in dummyBuilding:
    if 1 in row:
      y.append(y_value)
      y_value += 1
    else:
      y.append(0)

  # check if y indicates an overlap
  if 1 in y:
    # if so, get coordinates
    overlapMinY = y.index(1)
    overlapMinX = dummyBuilding[overlapMinY].index(1)
    overlapMaxY = overlapMinY + y_value - 1
    rowOfInterest = dummyBuilding[overlapMinY][::-1]
    overlapMaxX = len(dummyBuilding[overlapMaxY]) \
      - rowOfInterest.index(1)

    return (overlapMinX, overlapMinY, overlapMaxX, overlapMaxY)
  
  # otherwise, no coordinates
  return (0,0,0,0)

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
  county = -1
  for aisle in bldg:
    county += 1
    countx = -1
    for space in aisle:
      countx += 1
    # if the point is in between the rect coords and the length is 1 then we want to add 1 to specialspace
      if rect[0] <= countx <= rect[2] and rect[1] <= county <= rect[3] and len(space) == 1:
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
  
office1 = (0,0,10,10)
cubicles1 = [(5,6,7,10), (5,5,7,7), (6,6,8,8)]

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
  print(str(employee_IDs[1]) + ' ' + str(uncontested_space(office, employee_rects[0])))
  print(str(employee_IDs[2]) + ' ' + str(uncontested_space(office, employee_rects[1])))
  print(str(employee_IDs[3]) + ' ' + str(uncontested_space(office, employee_rects[2])))

if __name__ == "__main__":
  main()

#  File: OfficeSpace.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  x = rect[2] - rect(0)
  y = rect[3] - rect[1]
  return abs(x * y)

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  x = rect1[3] - rect2[1]

def createBldg(x, y):
  building = []
  for i in range(y):
    building.append([])
    for j in range(x):
      building[i].append('')
  return building

def assignSpace(bldg, name, x1,y1,x2,y2):
  for i in range(y1, y2):
    for j in range(x1,x2):
      bldg[i][j] += str(name)
  return bldg

building = createBldg(10,10)
name1 = 1
name2 = 2


updateBuilding = assignSpace(assignSpace(building, name1, 5,5,7,7), name2, 6,6,8,8)

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

print(unallocated_space(updateBuilding))


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

print(contested_space(updateBuilding))

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  bldg = assignSpace(bldg, 0, rect[0], rect[1], rect[2], rect[3])
  print(bldg)
  specialSpace = 0
  for aisle in bldg:
    for space in aisle:
      if space == '0':
        specialSpace += 1
  print(specialSpace)
  return specialSpace
uncontested_space(updateBuilding, (5,6,7,10))

# testing to see if I can push
# test yo

# hello

'''
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data

  # run your test cases
  print (test_cases())

  # print the following results after computation

  # compute the total office space

  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()
'''
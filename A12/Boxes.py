
#  File: Boxes.py

#  Description:

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

# Input: nesting_list is a list of all nesting boxes. 
#        Max_now is the max number of boxes that fit in eachother
# Output: function returns the , the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def get_maxs(nesting_list, max_now):
  if len(nesting_list) == 0:
    return 0
  if nesting_list[0] == int(max_now):
    return 1 + get_maxs(nesting_list[1:], max_now)
  else:
    return 0 + get_maxs(nesting_list[1:], max_now)

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  # The maximum number of boxes that fit inside each other
  max_now = 0 
  # a list of nesting boxes. Each index is the number of
  #       boxes which nest in the respective box in box_list
  nesting_list = []
  for i in range(len(box_list)):
    # The first box always has the nesting value of one
    if i == 0:
      nesting_list.append(1)
      continue
    # Find all of the nesting values
    for j in range(i-1, -1, -1):
      if does_fit(box_list[j], box_list[i]):
        nesting_list.append(nesting_list[j]+1)
        break
    # If the loop completes and no value is assigned,
    #     then the nesting value is one
    if len(nesting_list) != (i+1):
      nesting_list.append(1)

  max_now = max(nesting_list)
  print(nesting_list)

  return max_now, get_maxs(nesting_list, max_now)

# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()


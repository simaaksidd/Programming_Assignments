#  File: Boxes.py

#  Description: Finds the largest number of boxes that can be nested 
#  and the number of such sets of boxes that do fit

#  Student Name: Julian Canales

#  Student UT EID: jac22779 

#  Partner Name: Simmak Siddiqi

#  Partner UT EID: srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/4/2023

#  Date Last Modified: 3/6/2023

import sys

# Initialize memo to store results of already computed subproblems
memo = {}

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes(box_list):
    max_nesting = 0  # maximum number of boxes that fit inside each other
    num_sets = 0  # number of sets of boxes that achieve the maximum nesting
    n = len(box_list)

    # Iterate through all boxes and compute the maximum nesting starting from each box
    for i in range(n):
        nesting, count = max_nesting_from_box(i, box_list)
        if nesting > max_nesting:
            max_nesting = nesting
            num_sets = count
        elif nesting == max_nesting:
            num_sets += count

    return max_nesting, num_sets

# returns the maximum number of boxes that fit inside the box at index i
# and the number of sets of such boxes
def max_nesting_from_box(i, box_list):
    # Check if we've already computed the result for this box
    if i in memo:
        return memo[i]

    max_nesting = 1  # every box fits inside itself
    count = 1  # at least one set of boxes fits inside each other
    n = len(box_list)
    for j in range(i+1, n):
        if does_fit(box_list[i], box_list[j]):
            nesting, set_count = max_nesting_from_box(j, box_list)
            nesting += 1
            if nesting > max_nesting:
                max_nesting = nesting
                count = set_count
            elif nesting == max_nesting:
                count += set_count

    # Store the result in memo before returning
    memo[i] = (max_nesting, count)
    return memo[i]

# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # print to make sure that the input was read in correctly
    #print(box_list)
    #print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    #print(box_list)
    #print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print(max_boxes)

    # print the number of sets of such boxes
    print(num_sets)

if __name__ == "__main__":
    main()

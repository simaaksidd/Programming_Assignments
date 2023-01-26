#  File: WordSearch.py

#  Description: This program  take a set of intervals and collapse all
#         the overlapping intervals and print the smallest set of
#         non-intersecting intervals in ascending order of the lower
#         end of the interval and then print the intervals in increasing
#         order of the size of the interval.

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/23/2023

#  Date Last Modified: 1/23/2023

'''
How to use this Template:
For this assignment, do not change the function names or parameters
You will need to read from standard input. In order to do this, when 
you run your program in the command line, you will do it as follows:

$ python3 Intervals.py < intervals.in

If you read intervals.in as a file, it will not work on HackerRank. 
You should be able to paste this whole file into HackerRank. Please 
run your code to ensure it passes, and write your own test cases to 
ensure your answer is correct.
'''
import sys
# Input: 2 tuples
# Output: a boolean describing if they can be merged from the left side
#def is_collapsableL(tuple1, tuple2):
#  return (tuple1[0] < tuple2[0] and tuple1[1] > tuple2[1])

def not_intersecting(tuple1, tuple2):
  return tuple1[1] < tuple2[0]
# Input: 2 tuples
# Output: a boolean describing if they can be merged from the right side
def is_collapsableR(tuple1, tuple2):
  (tuple1[0] <= tuple2[0] and tuple1[1] > tuple2[1])

# Input: 2 tuples
# Output: a boolean describing if they can be merged from both sides
def is_collapsableB(tuple1, tuple2):
  return (tuple1[0] < tuple2[0] and tuple1[1] > tuple2[1])


# Input: 2 tuples
# Output: one merged tuple
def merge_both(tuple1, tuple2):
  return tuple1

# Input: 2 tuples
# Output: one merged tuple
def merge_right(tuple1, tuple2):
  pass

# Input: 2 tuples
# Output: one merged tuple
def merge_left(tuple1, tuple2):
  pass

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
    # First we want to get rid of all duplicates
    cleaned = set(tuples_list)
    cleaned = list(cleaned)
    cleaned.sort()
    # Since this is a sorted list with no duplicates, 
    #         we know that we do not need left merge and
    #         we know that we need to add the first value to new_list
    new_list = [cleaned[0]]

    # Now we want to compare the smaller and larger 
    #         values of the tuples (besides the first 1!)
    for tuples in cleaned[1:]:
        # In the new list, we have 1 value at the start,
        #         we want to compare to it once, but then 
        #         after we want the more recent value because 
        #         we will have known that the previous value
        #         is completely separate from the others 
        #         to do this, set "boundaries" for the smaller and
        #         larger values of the most recent addition to new_list
        smaller_boundary = new_list[-1][0]
        larger_boundary = new_list[-1][1]
        # merge 
        if tuples[0] <= larger_boundary and larger_boundary < tuples[1]:
            new_list[-1] = smaller_boundary, tuples[1]

        # new distinct value
        elif larger_boundary < tuples[0]:
            new_list.append((tuples[0], tuples[1]))

    return new_list




# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    sorted = []
    differences = []
    for tup in tuples_list:
      differences.append(tup[1]-tup[0])
    differences.sort()
    while differences:
      for i in tuples_list:
        if differences != []:
          if (i[1]-i[0]) == differences[0]:
            sorted.append(i)
            if differences != []:
              differences = differences[1:]
    return sorted


def main():
  # read the input data and create a list of tuples
  n = int(sys.stdin.readline())
  tuples_list = []
  for x in range(n):
    line = sys.stdin.readline()
    temp = line.split()
    tup = tuple(int(val) for val in temp)
    tuples_list.append(tup)
  
  tuples_list.sort()
  # merge the list of tuples
  merged_list = merge_tuples(tuples_list)
  
  # print the merged list
  print(merged_list)
  # sort the list of tuples according to the size of the interval
  sorted_list = sort_by_interval_size(merged_list)
  # print the sorted list
  print(sorted_list)

if __name__ == "__main__":
  main()

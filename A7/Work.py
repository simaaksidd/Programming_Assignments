#  File: Work.py 

#  Description:  

#  Student Name:  Simaak Siddiqi

#  Student UT EID:  srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 2/15/2023

#  Date Last Modified: 2/17/2023

import sys, time

# Input: int v, # of lines of code to write before his first coffee
#        int k, the productivity factor
# Output: the number for which v // k ** p converges to 
def converge(v, k):
  # first, the lines of code will be equal to v, since he's had no coffee
  lines = v
  total_lines = 0
  # while lines is not 0, add lines // k ** (n+1) to total_lines
  while lines:
    total_lines += lines
    lines = lines // k
  print(total_lines)
  return total_lines

converge(300, 2)

# Input: int n, the number of lines of code to write 
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  

  return 0 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here

  return 0 # placeholder

# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
#if __name__ == "__main__":
#  main()



#  File: Triangle.py

#  Description: Finds the greatest path sum starting at the top
#  of the triangle and moving only to adjacent numbers on the row below

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: Simaak Siddiqi

#  Partner UT EID: 

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/2/2023

#  Date Last Modified:

import sys

from timeit import timeit

def brute_force_helper (grid,idx1,idx2, sum):
  sums = []
  if idx1 == len(grid):
    sums.append(sum)
  else:
    if idx1 == 0:
       sums.extend(brute_force_helper(grid, idx1+1, idx2+1, sum + grid[idx1][idx2]))
    else:
        sums.extend(brute_force_helper(grid, idx1+1, idx2, sum + grid[idx1][idx2-1]))
        sums.extend(brute_force_helper(grid, idx1+1, idx2+1, sum + grid[idx1][idx2]))
  return sums


# returns the greatest path sum using exhaustive search
def brute_force (grid):
  sol = max(brute_force_helper(grid,0,0,0))
  return sol

# returns the greatest path sum using greedy approach
def greedy (grid):
  x = len(grid)
  sum = 0
  nexMax = max(grid[0])
  sum += nexMax
  for i in range(x-1):
    inf = grid[i].index(nexMax) - 1
    sup = grid[i].index(nexMax) + 1
    if inf < 0:
      inf = 0
    if sup >= len(grid):
      sup = (len(grid)-1)
    space = []
    for j in range(inf, sup+1):
      val = grid[i+1][j]
      space.append(val)
    nexMax = max(space)
    sum += nexMax
  return sum


def divide_conquer_helper (grid, idx1, idx2):
  if idx1 == len(grid) - 1:
    return grid[idx1][idx2]
  left_sum = divide_conquer_helper(grid, idx1+1, idx2)
  right_sum = divide_conquer_helper(grid, idx1+1, idx2+1)
  return grid[idx1][idx2] + max(left_sum, right_sum)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid) :
  return divide_conquer_helper(grid, 0, 0)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  ''' 
  # check that the grid was read in properly
  print (grid)
  '''
  

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()


#  File: Triangle.py

#  Description: Finds the greatest path sum starting at the top
#  of the triangle and moving only to adjacent numbers on the row below

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: Simaak Siddiqi

#  Partner UT EID: srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/2/2023

#  Date Last Modified: 3/3/2023

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
  row = 0
  col = 0
  pathSum = grid[row][col]
  while row < len(grid) - 1:
    right = grid[row+1][col+1]
    left = grid[row+1][col]
    if right > left:
      col += 1
    row += 1
    pathSum += grid[row][col]
  return pathSum


def divide_conquer_helper (grid, idx1, idx2):
  if idx1 == len(grid) - 1:
    return grid[idx1][idx2]
  left_sum = divide_conquer_helper(grid, idx1+1, idx2)
  right_sum = divide_conquer_helper(grid, idx1+1, idx2+1)
  return grid[idx1][idx2] + max(left_sum, right_sum)

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid) :
  sol = divide_conquer_helper(grid, 0, 0)
  return sol



# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  n = len(grid)
  triangSum = [[0]*n for _ in range(n)]
  triangSum[-1] = grid[-1]
  for i in range(len(grid)-2, -1, -1):
    for j in range(i+1):
      triangSum[i][j] = grid[i][j] + max(triangSum[i+1][j], triangSum[i+1][j+1])
  return triangSum[0][0]

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
  print('The greatest path sum through exhaustive search is', brute_force(grid))
  print('The time taken for exhaustive search in seconds is', times)
  print()

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The greatest path sum through greedy search is', greedy(grid))
  print('The time taken for greedy approach in seconds is', times)
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is', divide_conquer(grid))
  print('The time taken for recursive search in seconds is', times)
  print()

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is', dynamic_prog(grid))
  print('The greatest path sum through dynamic programming is ', times)
  print()

if __name__ == "__main__":
  main()
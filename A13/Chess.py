
#  File: Chess.py

#  Description:

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/9/2023

#  Date Last Modified: 3/10/2023

import sys

class Queens (object):
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
  
 # given a board is fully filled out check if a board is a valid solution 
  def is_solution(self):
    for i in range(self.n):
      for j in range(self.n):
        if self.board[i,j] == 'Q' and not self.is_valid(i,j):
          return False
    return True


  # do the recursive backtracking
  def recursive_solve (self, col):
    if (col == self.n):
      return True
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          if (self.recursive_solve(col + 1)):
            return True
          self.board[i][col] = '*'
      return False
  
  def rotate(self):
    n = self.n
    # Transpose the matrix
    for i in range(n):
      for j in range(i, n):
        self.board[i][j], self.board[j][i] = self.board[j][i], self.board[i][j]
    # Reverse each row of the transposed matrix
    for i in range(n):
      self.board[i] = self.board[i][::-1]
    return self.board
  
  def flipx(self):
    n = self.n
    # Swap the rows of the matrix
    for i in range(n // 2):
      self.board[i], self.board[n-i-1] = self.board[n-i-1], self.board[i]
    return self.board

  def flipy(self):
    n = self.n
    # Swap the columns of the matrix
    for i in range(n):
      for j in range(n // 2):
        self.board[i][j], self.board[i][n-j-1] = self.board[i][n-j-1], self.board[i][j]
    return self.board
  
  def find_non_distinct_solutions(self):
    # count is 1 because there is 1 solution already
    count = 1
    original_board = self.board
    
    for i in range(1,4):  
      self.rotate()
      if self.is_solution():
        count += 1

    self.board = original_board
    self.flipx()
    
    if self.is_solution():
      count+=1
    
    self.board = original_board
    self.flipy()
    
    if self.is_solution():
      count+=1
    self.board = original_board
  
  def find_all_solutions(self, distinct_solutions):
    solutions = 0
    for x in distinct_solutions:
      self.board = x
      solutions += self.find_non_distinct_solutions
    return solutions

    


  # if the problem has a solution print the board
  def solve (self):
    for i in range (self.n):
      if (self.recursive_solve(i)):
        self.print_board()

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)

  # place the queens on the board and count the solutions
  game.solve()

  # print the number of solutions
 
if __name__ == "__main__":
  main()


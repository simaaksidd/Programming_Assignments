#  File: Chess.py

#  Description: This program will find all solutions to the n-Queens problem

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: Simaak Siddiqi

#  Partner UT EID: srs5826

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
    # added an attribute that keeps track of the number of solutions
    self.count = 0

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
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    if (col == self.n):
      # add 1 to the count for associated solution
      self.count += 1
      #self.print_board()
      # ends the search after adding 1 to count
      return
    else:
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          # find all other solutions for all cols
          self.recursive_solve(col + 1)
          self.board[i][col] = '*'

  # if the problem has a solution print the board
  def solve (self):
    # start at col 0 and find all solutions from there
    self.recursive_solve(0)

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
  print(game.count)
 
if __name__ == "__main__":
  main()
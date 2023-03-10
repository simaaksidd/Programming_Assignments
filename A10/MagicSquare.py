#  File: MagicSquare.py

#  Description: This program generates all 3x3 magic squares and 
#          checks if any nxn square is a magic square. It also turns 1D 
#          matricies in to nxn matrices and prints them neatly. 

#  Student's Name: Julian Canales

#  Student's UT EID: jac22779
 
#  Partner's Name: Simaak Siddiqi

#  Partner's UT EID: srs5826

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 2/25/2023

#  Date Last Modified: 2/27/2023

#  Input: 1-D list of integers a
#  Output: returns True if this list is a magic square
#          or False otherwise
def is_magic ( a ):
  n = int(len(a)**0.5)
  magic_sum = int(n*(((n**2)+1)/2))
  
  #check if matrix is 1
  if n == 1:
    return a[0] == 1

  # checks rows
  for i in range(n):
    rowSum = sum(a[(i*n):((i+1)*n)])
    if rowSum != magic_sum:
      return False

  # checks cols
  for i in range(n):
    colSum = 0
    for j in range(n): 
      colSum += a[n*j + i] 
    if colSum != magic_sum:
      return False

  # checks diags
  diagSum = 0
  for i in range(n):
    diagSum += a[i*(n+1)]
  if diagSum != magic_sum:
    return False
    
  # returns True if passes through all loops successfully 
  return True

#  Input: 1-D list of integers a and index idx
#  Output: whether a satisfies conditions
def validate(a, idx):
  if idx == 0:
    return True
  if idx % 3 == 0:
    if sum(a[idx-3:idx]) != 15:
      return False
  if idx > 6:
    if a[idx-7] + a[idx-4] + a[idx-1] != 15:
      return False
  if idx == 7:
    if a[2] + a[4] + a[6] != 15:
      return False
  if idx == 9:
    if a[0] + a[4] + a[8] != 15:
      return False
  return True

#  Input: 1-D list of integers a and an index idx
#  Output: prints only those permutations that are magic
def permute ( a, idx ):
  magicPerms = []
  if not validate(a, idx):
    return magicPerms
  hi = len(a)
  if (idx == hi):
    magicPerms.append(a.copy())
  else:
    for i in range(idx, hi):
      a[idx], a[i] = a[i], a[idx]
      magicPerms.extend(permute (a,idx+1))
      a[idx], a[i] = a[i], a[idx]
  return magicPerms


#  Input: 1-D list of integers a
#  Output: prints this as a 2-D list
def print_square ( a ):
  n = int(len(a)**0.5)
  sq = reshape(a)
  for i in range(n):
    for j in range(n):
      if j == (n-1):
        print(sq[i][j])
      else:
        print(sq[i][j], end=' ')


#  Input: 1-D list of integers a
#  Output: returns a 2-D list
def reshape ( a ):
  n = int(len(a)**0.5)
  if n == 1:
    return [a]
  square = []
  for i in range(n):
    row = []
    for j in range(n):
      row.append(a[n*i+j])
    square.append(row)
  return square

def main():
  # create a 1-D list of numbers from 1 to 9
  input = [i for i in range(1,10)]

  # call permute to get all 3x3 magic squares
  magicSquares = permute(input, 0)

  # formatting
  for square in magicSquares:
    square1 = reshape(square)
    for row in square1:
      print(*row)
    print()
    

if __name__ == "__main__":
  main()
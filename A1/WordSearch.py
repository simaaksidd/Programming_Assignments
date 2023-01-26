#  File: WordSearch.py

#  Description: This program finds k words in an nxn grid
#         and shows its location in a tuple (y,x)

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 1/20/2023

#  Date Last Modified: 1/20/2023

import sys

# Input: the current row, the current column, the, length of the word,
#         the length of the row and columns in the grid 
# Output: an integer describing what axes have enough space
#         1: y axis 2: x axis 3: both
def enough_space(y,x,len,boundary):
    if y + len <= boundary and x + len <= boundary:
        return 3
    elif x + len <= boundary:
        return 2
    elif y + len <= boundary:
        return 1
    return -1
# Input: 2 letters
# Output: a boolean value describing whether or not the two letters match
def is_match(a, b):
    return a == b

# Input: the grid, current word, current row, and current column
# Output: a boolean value describing whether or not
#         there was a full horizontal match
def horizontal_match(grid,word,i,j, boundary):
    if word == '':
        return True
    if is_match(word[0],grid[i][j]) and (enough_space(i,j,len(word),boundary) == 2 or enough_space(i,j,len(word),boundary) == 3): 
        j+=1
        return horizontal_match(grid,word[1:], i, j, boundary)
    return False

# Input: the grid, current word, current row, and current column
# Output: a boolean value describing whether or not
#         there was a full vertical match
def vertical_match(grid, word, i, j, boundary):
    if word == '':
        return True
    if is_match(word[0],grid[i][j]) and (enough_space(i,j,len(word),boundary) == 1 or enough_space(i,j,len(word),boundary) == 3): 
        i+=1
        return vertical_match(grid,word[1:], i, j, boundary)
    return False

# Input: the grid, current word, current row, and current column
# Output: a boolean value describing whether or not
#         there was a full diagonal match
def diagonal_match(grid, word, i, j, boundary):
    if word == '':
        return True
    if is_match(word[0],grid[i][j]) and enough_space(i,j,len(word), boundary) == 3: 
        i+=1
        j+=1
        return diagonal_match(grid,word[1:], i, j, boundary)
    return False

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    # store the number, n, which describes the length and width of the
    #       letter grid
    line = sys.stdin.readline()
    n = int(line)

    # skip a line
    line = sys.stdin.readline()

    # store the word grid inside a 2-D list 
    word_grid = []
    for i in range(n):    
        line = sys.stdin.readline()
        word_grid.append(line.strip().split(sep=" "))
    
    # skip a line
    line = sys.stdin.readline()

    # store the number, k, which describes the number of words in the
    #       word search
    line = sys.stdin.readline()
    k = int(line)

    # store the list of words to find in a 1-D list
    word_list = []
    for i in range(k):
        line = sys.stdin.readline()
        word_list.append(line.strip())

    # return the 2-D grid and the 1-D list of words as a tuple
    return (word_grid, word_list)

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):
    # find an instance of the first or last letter in in the grid
    first_letter = word[0]
    
    # There are 6 possible directions. Right, left, diagonal right up,
    #         diagonal left up, diagonal right down, and diagonal left down 
    # flip the grid on the x axis  
    grid_flippedx = grid[::-1]

    # flip the grid on the y axis
    grid_flippedy = []
    for list in grid:
        grid_flippedy.append(list[::-1])
    
    # flip the grid on both axes
    grid_flippedxy = []
    for list in grid:
        grid_flippedxy.append(list[::-1])
    grid_flippedxy = grid_flippedxy[::-1]
    
    # create a boundary variable to make sure we dont go out of range
    boundary = len(grid[0])
    # for each column and row, we want to find an instance of
    # the first or last letter in the word
    for i in range(len(grid)):
        for j in range(boundary):
            # if the first letter matches and we have space, we continue
            if is_match(first_letter, grid[i][j]):
                # if we find a match, return the tuple containing the i,j
                #       of the first letter plus one to account for indexing
                if horizontal_match(grid, word, i, j, boundary):
                    return (i+1,j+1)
                if vertical_match(grid, word, i, j, boundary):
                    return (i+1,j+1)
                if diagonal_match(grid, word, i, j, boundary):
                    return (i+1,j+1)
            if is_match(first_letter, grid_flippedx[i][j]):
                # flip the grid by the x axis
                if vertical_match(grid_flippedx, word, i, j, boundary):
                        return (boundary-i,j+1)
                if diagonal_match(grid_flippedx, word, i, j, boundary):
                        return (boundary-i,j+1)                
            if is_match(first_letter, grid_flippedy[i][j]):
                # flip the grid by the y axis
                if horizontal_match(grid_flippedy, word, i, j, boundary):
                        return (i+1,boundary-j)
                if diagonal_match(grid_flippedy, word, i, j, boundary):
                        return (i+1,boundary-j)  
            if is_match(first_letter, grid_flippedxy[i][j]):
                # flip the grid by the both axes
                if diagonal_match(grid_flippedxy, word, i, j, boundary):
                        return (boundary-i,boundary-j)               
    
    # if we dont find a match, return (0,0)
    return(0,0)

def main():
    # read the input file from stdin
    word_grid, word_list = read_input()

  # find each word and print its location
    for word in word_list:
      location = find_word (word_grid, word)
      print (word + ": " + str(location))

if __name__ == "__main__":
    #print("grid: " + str(read_input()[1]))
    #find_word()
    main()

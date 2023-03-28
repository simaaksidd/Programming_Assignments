
#  File: Radix.py

#  Description: This assignment implements a Radix Sort algorithm 
#        It sorts a mix of lower case letters and digits. 

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/26/2023

#  Date Last Modified: 3/27/2023

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

  def __str__(self):
    return str(self.queue)

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  # We need to define the lexicographic order
  lex_order = '.0123456789abcdefghijklmnopqrstuvwxyz'

  queue_list = [Queue() for i in range(37)]

  queue_dict = {tok: idx for idx, tok in enumerate(lex_order)}

  # first, we have to find the largest length 
  largest = len(max(a, key=len))
  
  # make all of the lengths in a the same
  b = []
  
  # add . as a filer character
  for string in a:
    while len(string) < largest:
      string += '.'
    b.append(string)

  # Radix Sort (probably easier to do recursively but yolo)
  for i in range(largest):
    
    for string in b:
      tok = string[(largest-1) - i]
      queue_list[queue_dict[tok]].enqueue(string) 

    b = []
    for queue in queue_list:
      strs = []
      while not queue.is_empty():
        strs.append(queue.dequeue())
      b.extend(strs)
  
  c= []
  for string in b:
    new_str = ''
    for char in string:
      if char != '.':
        new_str += char
    c.append(new_str)

  
  return c

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    

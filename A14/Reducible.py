#  File: Reducible.py

#  Description: This program outputs a list of the longest words that are reducible. 

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/16/2023

#  Date Last Modified: 

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  # calling hash_word with const as the size gives (key % const)
  key_mod_const = hash_word(s, const)
  return (const - key_mod_const)


# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing

###########################################################################

def insert_word (s, hash_table):
  size = len(hash_table)
  hash_idx = hash_word(s, size)
  if hash_table[hash_idx % size] == '':
    hash_table[hash_idx % size] = s
  else:
    ss = step_size(s, 11)
    while True:
      hash_idx += ss
      if hash_table[(hash_idx % size)] == '':
        hash_table[(hash_idx % size)] = s
        return

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  size = len(hash_table)
  hash_idx = hash_word(s, size)
  if hash_table[hash_idx % size] == s:
    return True
  else:
    count = 1
    ss = step_size(s, 11)
    while count < size:
      hash_idx += ss
      if hash_table[hash_idx % size] == s:
        return True
      count += 1
    return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  # If s is in hash memo, then we know that s is reductible
  if find_word(s, hash_memo):
    return True
  elif s == 'a' or s == 'i' or s == 'o':
    insert_word(s, hash_memo)
    return True
  else:
    for i in range(len(s)):
      reduct = (s[0:i] + s[(i+1):])
      if find_word(reduct, hash_table):
        return is_reducible(reduct, hash_table, hash_memo)
    return False
##################################################################### 

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  max_words = []
  length = max(string_list)
  for i in range(len(string_list)):
    if len(string_list[i]) == length:
      max_words.append(string_list[i])
  return max_words

def main():
  # create an empty word_list
  word_list = []
  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)

  # find length of word_list
  num_words = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  N = 2 * num_words
  while not is_prime(N):
    N += 1

  # create an empty hash_list
  # populate the hash_list with N blank strings
  hash_list = ['' for i in range(N)]
  
  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for word in word_list:
    insert_word(word, hash_list)

  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  M = int(0.2 * num_words)
  while not is_prime(M):
    M += 1
  # populate the hash_memo with M blank strings
  hash_memo = ['' for i in range(M)]

  # create an empty list reducible_words
  reductibles = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    if is_reducible(word, hash_list, hash_memo):
      reductibles.append(word)

  # find the largest reducible words in reducible_words  
  largest_reducts = get_longest_words(reductibles)
    
  # print the reducible words in alphabetical order
  
  #idk if I need this
  #largest_reducts.sort()
  
  # one word per line
  for word in largest_reducts:
    print(word)

if __name__ == "__main__":
  main()
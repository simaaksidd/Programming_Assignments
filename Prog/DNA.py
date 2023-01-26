
#  File: DNA.py

#  Description:

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 1/9/2023

#  Date Last Modified: 

import sys

def test_cases():
  # test all_substrings()
  assert all_substrings("a") == ["a"]
  assert all_substrings("abc") == ["abc", "ab", "bc", "a", "b", "c"]
  assert all_substrings("") == []
  # test longest_sequence()
  assert longest_subsequence("a", "a") == []
  assert longest_subsequence("abcd", "bc") == ["bc"]
  assert longest_subsequence("abc", "xyz") == []
# return the result
  return "all test cases passed"

# Input: s, a string
# Output: a list of all substrings of s
def all_substrings(s):
  # a list of all substrings of s
  result = []

  # define a window
  wnd = len(s)

  # get all substrings
  while (wnd > 0):
    idx = 0
    while (idx + wnd) <= len(s):
      sub_str = s[idx:idx+wnd]
      result.append(sub_str)
      idx = idx + 1
    wnd = wnd - 1

  # return the result
  return result

# Input: s1 and s2 are the two lists of substrings
# Output: returns a list of common substrings
def find_common_substrings(s1, s2):
  common_substrings = []
  for substring in s1:
    if substring in s2:
      common_substrings.append(substring)
  return common_substrings

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
def longest_subsequence (s1, s2):
  # get substrings for s1 and s2
    s1_substrings = all_substrings(s1)
    s2_substrings = all_substrings(s2)
    # find out which is longer
    s1_is_shorter = len(s1) < len(s2)
    
    # find a list of common substrings between s1 and s2
    if s1_is_shorter:
      common_substrings = find_common_substrings(s1_substrings, s2_substrings)
    else:
      common_substrings = find_common_substrings(s2_substrings, s1_substrings)
    print("common substrings: " + str(common_substrings))
    # if there are no common substrings, return an empty list
    if len(common_substrings) == 0:
      return []
    else:
      # desginate the longest substring as the first string in the list 
      longest_substring = []
      longest_substring.append(max(common_substrings, key=len))
      for i in range(1,len(common_substrings)):
        if len(common_substrings[i]) == len(longest_substring[0]):
          longest_substring.append(common_substrings[i])

      for x in longest_substring:
        if len(x) <= 1:
          longest_substring.remove(x)
      print("longest: " + str(longest_substring))
      return longest_substring

def main():
  # test all functions
  # print(test_cases())
  line = sys.stdin.readline()
  line = line.strip()
  num_pairs = int(line)
  # read the data

  # for each pair
    # call longest_subsequence
  for i in range(num_pairs):
    line = sys.stdin.readline()
    s1 = line.strip()
    
    line = sys.stdin.readline()
    s2 = line.strip()

    #convert to uppercase
    s1 = s1.upper()
    s2 = s2.upper()
    print("s1: " + str(s1))
    print("s2: " + str(s2))
    #get longest subsequences
    result = longest_subsequence(s1, s2)
    # write out result(s)
    if (len(result) == 0):
      print("No Common Sequence Found")
    else:
      for item in result:
        print("result: " + str(result))
        print(item)
	  # insert blank line
    print()

main()
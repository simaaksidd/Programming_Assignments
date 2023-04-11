#  File: TestBinaryTree.py

#  Description: Adds methods to Binary Tree data structure

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: Simmak Siddiqi

#  Partner UT EID: srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 4/10/23

#  Date Last Modified: 4/10/23

import sys


class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild
      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
  
  # Returns true if two binary trees are similar
  def is_similar(self, pNode):

    def is_similar_helper(node1, node2):
      if node1 is None and node2 is None:
        return True
      elif node1 is not None and node2 is not None:
        return (node1.data == node2.data
                and is_similar_helper(node1.lChild, node2.lChild)
                and is_similar_helper(node1.rChild, node2.rChild))
      else:
        return False

    return is_similar_helper(self.root, pNode.root)

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
    def get_level_helper(node, curr_level, res):
      if node is None:
        return
      if curr_level == level:
        res.append(node)
      else:
        get_level_helper(node.lChild, curr_level+1, res)
        get_level_helper(node.rChild, curr_level+1, res)

    res = []
    get_level_helper(self.root, 0, res)
    return res

  # Returns the height of the tree
  def get_height (self): 
    def get_height_helper(node):
      if node is None:
        return 0
      else:
        return 1 + max(get_height_helper(node.lChild), get_height_helper(node.rChild))

    return get_height_helper(self.root)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    def num_nodes_helper(node):
      if node is None:
        return 0
      else:
        return 1 + num_nodes_helper(node.lChild) + num_nodes_helper(node.rChild)

    return num_nodes_helper(self.root)

def main():
  # Create three trees - two are the same and the third is different
  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree1_input = list (map (int, line)) 	# converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree2_input = list (map (int, line)) 	# converts elements into ints

  line = sys.stdin.readline()
  line = line.strip()
  line = line.split()
  tree3_input = list (map (int, line)) 	# converts elements into ints 

  tree1 = Tree()
  for value in tree1_input:
    tree1.insert(value)

  tree2 = Tree()
  for value in tree2_input:
    tree2.insert(value)

  tree3 = Tree()
  for value in tree3_input:
    tree3.insert(value)


'''
  # Test your method is_similar()
  print(tree1.is_similar(tree2)) # True

  # Print the various levels of two of the trees that are different
  print(tree1.get_level(2)) # [10, 40, 60, 80]
  print(tree3.get_level(2)) # [7, 38, 65, 96]

  # Get the height of the two trees that are different
  print(tree1.get_height()) #4
  print(tree3.get_height()) #6

  # Get the total number of nodes a binary search tree
  print(tree3.num_nodes()) #15

'''

if __name__ == "__main__":
  main()
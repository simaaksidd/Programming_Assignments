#  File: Poly.py

#  Description: Create a polynomial field (with addition and multiplication closure) using linked lists

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: Simaak Siddiqi

#  Partner UT EID: srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/3/23

#  Date Last Modified: 3/3/23

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    link = Link(coeff, exp)
    current = self.first
    previous = None
    while current != None and current.exp < exp:
      previous = current
      current = current.next
    if previous == None:
      self.first = link
    else:
      previous.next = link
    link.next = current

  # add an item at the beginning of the list
  def insert_first (self, coeff, exp): 
    link = Link(coeff, exp)
    link.next = self.first
    self.first = link

  def reverse_list (self): 
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_first(current.coeff, current.exp)
      current = current.next
    return newList
  
  def insert_last (self, coeff, exp):
    link = Link(coeff, exp)
    if self.first == None:
      self.first = link 
      return
    position = self.first
    while position.next != None:
      position = position.next
    position.next = link
  
  def copy_list (self):
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_last(current.coeff, current.exp)
      current = current.next
    return newList

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    # add each term in p to self (without simplification)
    current_p = p.first
    while current_p != None:
      self.insert_in_order(current_p.coeff, current_p.exp)
      current_p = current_p.next
    
    # simplify our expression
    seen = {}
    current = self.first
    while current != None:
      if current.exp not in seen:
        seen[current.exp] = current.coeff
        current = current.next
      else:
        newCoeff = current.coeff + seen[current.exp]
        seen[current.exp] = newCoeff
        current = current.next
    
    # create new linked list to represent sum
    sum = LinkedList()
    for exp in seen:
      if seen[exp] != 0:
        link = Link(seen[exp], exp)
        sum.insert_in_order(link.coeff, link.exp)
    return sum

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    # multiply each term in self with each term in p
    product = LinkedList()
    current_self = self.first
    while current_self != None:
      current_p = p.first
      while current_p != None:
        coeff = current_self.coeff * current_p.coeff
        exp = current_self.exp + current_p.exp
        product.insert_in_order(coeff, exp)
        current_p = current_p.next
      current_self = current_self.next

    # simplify the product expression
    seen = {}
    current = product.first
    while current != None:
      if current.exp not in seen:
        seen[current.exp] = current.coeff
        current = current.next
      else:
        newCoeff = current.coeff + seen[current.exp]
        seen[current.exp] = newCoeff
        current = current.next

    # create new linked list to represent the simplified product
    simplified = LinkedList()
    for exp in seen:
      if seen[exp] != 0:
        link = Link(seen[exp], exp)
        simplified.insert_in_order(link.coeff, link.exp)

    return simplified

  # create a string representation of the polynomial
  def __str__ (self):
    reverse = self.reverse_list()
    s = ''
    current = reverse.first
    while current != None:
      s += str(current)
      if current.next != None:
        s += ' + ' 
      current = current.next
    return s

def main():
  # read data from file poly.in from stdin

  numTerms = int(sys.stdin.readline())


  # create polynomial p

  r = LinkedList()

  for i in range(numTerms):
    info = sys.stdin.readline().split()
    r.insert_in_order(int(info[0]), int(info[1]))

  line = sys.stdin.readline()

  # create polynomial q

  numTerms = int(sys.stdin.readline())

  w = LinkedList()
  for i in range(numTerms):
    info = sys.stdin.readline().split()
    w.insert_in_order(int(info[0]), int(info[1]))

  r_copy = r.copy_list()
  w_copy = w.copy_list()

  # get sum of p and q and print sum

  print(str(r_copy.add(w_copy)))

  # get product of p and q and print product

  print(str(r.mult(w)))

if __name__ == "__main__":
  main()
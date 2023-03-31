#  File: TestLinkedList.py

#  Description: Tests a series of methods for the LinkedList class

#  Student Name: Julian Canales

#  Student UT EID: jac22779

#  Partner Name: simaak Siddiqi 

#  Partner UT EID: srs5826

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 3/31/23

#  Date Last Modified: 3/31/23

class Link (object):
  # represents a link between a node self and node other
  def __init__ (self, data):
    self.data = data
    self.next = None


class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None
    self.last = None

  # get number of links 
  def get_num_links (self):
    count = 0 
    position = self.first
    while position != None:
      count += 1
      position = position.next
    return count

  # add an item at the beginning of the list
  def insert_first (self, data): 
    link = Link(data)
    link.next = self.first
    self.first = link

  # add an item at the end of a list
  def insert_last (self, data):
    link = Link(data)
    if self.first == None:
      self.first = link 
      return
    position = self.first
    while position.next != None:
      position = position.next
    position.next = link

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    link = Link(data)
    current = self.first
    previous = None
    while current != None and current.data < data:
      previous = current
      current = current.next
    if previous == None:
      self.first = link
    else:
      previous.next = link
    link.next = current

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first
    while current != None:
      if current.data == data:
        return current
      current = current.next
    return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first
    while current != None and current.data <= data:
      if current.data == data:
        return current
      current = current.next
    return None
    

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    current = self.first
    previous = None
    while current != None and current.data != data:
      previous = current
      current = current.next
    if current == None:
      return None
    if previous == None:
      self.first = current.next
    else:
      previous.next = current.next
    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    output = ''
    count = 0
    current = self.first
    numLinks = self.get_num_links() - 1
    
    while current is not None:
        if ((count + 1) % 10 == 0):
          output += str(current.data) + '\n'
          count += 1
        elif count == numLinks:
          output += str(current.data)
          count += 1
        else:
          output += str(current.data) + '  '
          count += 1
        current = current.next
    
    return output

  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_last(current.data)
      current = current.next
    return newList

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_first(current.data)
      current = current.next
    return newList

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_in_order(current.data)
      current = current.next
    return newList

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    while current != None and current.next != None:
      if current.data > current.next.data:
        return False
      current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return self.first == None

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    merged_list = LinkedList()

    current_self = self.first
    current_other = other.first

    while current_self is not None and current_other is not None:
      if current_self.data < current_other.data:
        # if the current link in self is smaller, add it to the merged list
        merged_list.insert_last(current_self.data)
        current_self = current_self.next
      else:
        # Otherwise, add the current link in other to the merged list
        merged_list.insert_last(current_other.data)
        current_other = current_other.next

    # add any remaining links from self to the merged list
    while current_self is not None:
      merged_list.insert_last(current_self.data)
      current_self = current_self.next

    # Add any remaining links from other to the merged list
    while current_other is not None:
      merged_list.insert_last(current_other.data)
      current_other = current_other.next

    return merged_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if self.get_num_links() != other.get_num_links():
      return False
    
    current_self = self.first
    current_other = other.first

    while current_self is not None and current_other is not None:
      if current_self.data != current_other.data:
        return False

      current_self = current_self.next
      current_other = current_other.next

    return True
    

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    uniqueList = LinkedList()
    seenValues = set()
    current = self.first

    while current is not None:
      if current.data not in seenValues:
        # if we haven't seen this value before, add it to the new list
        uniqueList.insert_last(current.data)
        seenValues.add(current.data)
      current = current.next

    return uniqueList


def main():
    ''' 
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    lst = LinkedList()
    for i in range(1, 12):
      lst.insert_first(i)
    print("Testing insert_first() and __str__():")
    print(lst)

    # Test method insert_last()
    lst.insert_last(0)
    print("Testing insert_last():")
    print(lst)

    # Test method insert_in_order()
    lst.insert_in_order(7)
    print("Testing insert_in_order():")
    print(lst)

    # Test method get_num_links()
    print("Testing get_num_links():")
    print(lst.get_num_links())

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    print("Testing find_unordered():")
    print(lst.find_unordered(5))  # should print True
    print(lst.find_unordered(20))  # should print False

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print("Testing find_ordered():")
    print(lst.find_ordered(7))  # should print True
    print(lst.find_ordered(20))  # should print False

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 
    print("Testing delete_link():")
    print(lst.delete_link(7))  # should print True
    print(lst.delete_link(20))  # should print False
    print(lst)  # print updated linked list

    # Test method copy_list()
    print("Testing copy_list():")
    new_lst = lst.copy_list()
    print(new_lst)

    # Test method reverse_list()
    print("Testing reverse_list():")
    reversed_lst = lst.reverse_list()
    print(reversed_lst)

    # Test method sort_list()
    print("Testing sort_list():")
    sorted_lst = lst.sort_list()
    print(sorted_lst)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Testing is_sorted():")
    print(lst.is_sorted())  # should print False
    print(sorted_lst.is_sorted())  # should print True

    # Test method is_empty()
    print("Testing is_empty():")
    empty_lst = LinkedList()
    print(empty_lst.is_empty())  # should print True
    print(lst.is_empty())  # should print False

    # Test method merge_list()
    print("Testing merge_list():")
    lst1 = LinkedList()
    lst2 = LinkedList()
    for i in range(1, 6):
      lst1.insert_first(i)
      lst2.insert_first(i + 5)
    merged_lst = lst1.merge_list(lst2)
    print(merged_lst)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print("Testing is_equal():")
    print(lst.is_equal(new_lst))  # should print True
    print(lst.is_equal(merged_lst))  # should print False

    # Test remove_duplicates()
    print("Testing remove_duplicates():")
    lst.insert_first(7)
    lst.insert_first(3)
    lst.insert_first(5)
    lst.insert_first(7)
    lst.insert_first(9)
    lst.insert_first(1)
    print(lst)
    unique_lst = lst.remove_duplicates()
    print(unique_lst)
    '''
  

if __name__ == "__main__":
  main()

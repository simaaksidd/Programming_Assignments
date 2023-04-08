#  File: ExpressionTree.py

#  Description:

#  Student Name: Simaak Siddiqi

#  Student UT EID: srs5826

#  Partner Name: Julian Canales

#  Partner UT EID: jac22779

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 4/7/2023

#  Date Last Modified: 4/7/2023

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild
    def isLeaf(self):
        if (self.lChild == None and self.rChild == None):
            return True
        return False

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        stack = Stack()
        toks = expr.split()
        self.root = Node()
        cur_node = self.root
        for tok in toks:
            # Add new node as the lChild of cur_node. 
            # Push cur_node onto stack. cur_node = lChild.
            if tok == '(':
                cur_node.lChild = Node()
                stack.push(cur_node)
                cur_node = cur_node.lChild 
            # cur_node's data = operator. Push cur_node on the stack. 
            # Add a new node as the rchild of cur_node. cur_node = rchild. 
            elif tok in operators:
                cur_node.data = tok
                stack.push(cur_node)
                cur_node.rChild = Node()
                cur_node = cur_node.rChild
            # make cur_node = parent node 
            # by popping the stack if it is not empty.
            elif tok == ')':
                if not stack.is_empty():
                    cur_node = stack.pop()
            # cur_node's data = operand. 
            # cur_node = parent by popping the stack. 
            else:
                cur_node.data = tok
                cur_node = stack.pop()
    def operate(self, op, right, left):
        if op == '//':
            return right // left
        if op == '**':
            return right ** left
        if op == '*':
            return right * left
        if op == '%':
            return right % left
        if op == '+':
            return right + left
        if op == '-':
            return right - left
        if op == '*':
            return right * left
        if op == '/':
            return right / left
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        if aNode == None:
            return 0
        if aNode.isLeaf():
            return float(aNode.data)
        left = self.evaluate(aNode.lChild)
        right = self.evaluate(aNode.rChild)
        return self.operate(aNode.data, left, right)
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        preorder = ''
        stack = Stack()
        stack.push(aNode)
        while not stack.is_empty():
            cur_node = stack.pop()
            if cur_node != None:
                preorder += cur_node.data + ' '
                stack.push(cur_node.rChild)
                stack.push(cur_node.lChild)
        return preorder


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        postorder = ''
        stack = Stack()
        stack.push(aNode)
        while not stack.is_empty():
            cur_node = stack.pop()
            if cur_node != None:
                postorder += cur_node.data + ' '
                stack.push(cur_node.lChild)
                stack.push(cur_node.rChild)
        postorder = postorder.split()
        for i in range(len(postorder)):
            if '.' in postorder[i]:
                pass
            else:
                postorder[i] = postorder[i][::-1]
        reverse = ' '.join(postorder[::-1])
        return reverse


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()

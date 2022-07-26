#!/usr/bin/python3
# This is a program CircularLinkedList.py

class Node:
    """This is the class node to create a node of the linked list."""  
    def __init__ (self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p
        
    def __str__ (self):
        return ('(' + str(self.data) + ')')
      
 
class CircularLinkedList:
   """This is the class CircularLinkedList to create the linked list."""
    def __init__ (self, r = None):
        self.root = r
        self.size = 0

    def add (self, d):
        if self.size == 0:
            self.root = Node(d)
            self.root.next_node = self.root
        else:
            new_node = Node (d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find (self, d):
        this_node = self.root
        while True:
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove (self, d):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == d:   # found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True     # data removed
            elif this_node.next_node == self.root:
                return False    # data not found
            prev_node = this_node
            this_node = this_node.next_node
        
    def print_list (self):
        if self.root is None:
            return
        this_node = self.root
        print (this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print (this_node, end='->')
        print()

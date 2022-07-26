#!/usr/bin/python3
# Stack Data Structure

"""Stack data structure is LIFO, last in last out."""

class Stack:
    def __init__(self):
        self.stack = list()
        
    def __str__(self):
        print(f"Stack: {str(self.stack)}.")
        
    def isStackEmpty(self):
        return len(self.stack) == 0 
        
    def addStack(self, data):
        return self.stack.append(data)
        
    def removeStack(self):
        if self.isStackEmpty():
            return "Stack is empty."
        else:
            return self.stack.pop()
    
    def peekStack(self):
        if self.isStackEmpty():
            return "Stack is empty."
        else:
            return self.stack[len(self.stack) - 1]
    
    def stackSize(self):
        self.stack = list()
        if self.isStackEmpty():
            return "Stack is empty."
        else:
            return f"Size of Stack is {len(self.stack)}."

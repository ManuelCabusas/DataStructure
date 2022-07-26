#!/usr/bin/python3
# Queue Data Structure
"""Queue Data Structure is FIFO, first in, first out."""

class Queue:
    def __init__(self):
        self.queue = list()
    
    def __str__(self):
        return str(self.queue)
    
    def __repr__(self):
        return str(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def addQueue(self, data):
        return self.queue.append(data)
    
    def peekQueue(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "Queue is empty."
    
    def removeQueue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."
        
    def queueSize(self):
        if not self.isEmpty():
            return len(self.queue)
        else:
            return "Queue is empty."
        
        

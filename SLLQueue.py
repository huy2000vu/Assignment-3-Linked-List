from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
    def new_node(self,x):
      return SLLQueue.Node(x)

    def __init__(self) :
        self.head = None #beginning
        self.tail = None #end 
        self.n = 0 #keeps track of how many elements are in the list
        
    def add(self, x :np.object) :
      u = self.new_node(x) #x is what we are trying to insert
      if self.n == 0: self.head = u #if theres only 1 element in the list, head is u
      else: self.tail.next = u
      self.tail = u 
      self.n += 1
      return True


    def remove(self) -> np.object:
      return self.pop()

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

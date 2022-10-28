
from Interfaces import Stack
import numpy as np
class SLLDequeue(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
      u = SLLDequeue.Node(x)
      u.next = self.head
      self.head = u  
      if self.n==0: self.tail = u 
      self.n+=1
      return x
       # pass
        
    def pop(self) -> np.object:
      if self.n == 0: return None
      x = self.head
      self.head = self.head.next
      self.n -= 1
      if self.n == 0: self.tail = None
      return x 
      pass

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

    def add_first(self,x:np.object): #add an element to the last node
      u = SLLDequeue.Node(x) #create a node containing value x 
      self.tail.next = u #set u to be tail
      self.tail = u 
      self.n += 1
      return x

    def remove_first(self):  #remove last node
      u = self.head
      while u.next.next != None:
        u=u.next
      u.next = None
      self.n -= 1
      
    def second_last(self): 
      u = self.head 
      while u.next.next != None:
        u=u.next
      return u.x
'''
Big O:
-The running time for second_last() method is
O(N), N represent how many nodes are in the linked list
-Unlike arrays, linked list has to iterate through the entire list to retrieve an element if the element happen to be in the end of the list
-The more nodes means that the function will have to iterate 
through all of the nodes to find the second to last. 
'''         
          


#add_first -> add tail
#remove_first -> remove tail
#add_last -> head
#remove_last -> head
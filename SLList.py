from Interfaces import Stack
import numpy as np
class SLList(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
      u = SLList.Node(x)
      u.next = self.head
      self.head = u  
      if self.n==0: self.tail = u 
      self.n+=1
      return x
        
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

    def get(self,i):
      u = self.head
      counter = 0
      while counter < i:
        u=u.next
        counter+=1
      return u

    def set(self,i,x): 
      u=self.get(i) 
      u.x = x
      
    def add(self,i,x):
      if i == 0: #if youre trying to adding at the beginning of the list
        self.push()
        return 
      u = self.get(i-1)
      t=SLList.Node(x)
      t.next = u.next
      u.next = t
      #self.n+=1
      pass

    def remove(self,i):
      if i == 0: self.pop()
      u = self.get(i-1)
      t = u.next.next
      u.next = t 
      #self.n-=1

    def reverse(self):
      i=0
      while i < self.n:
        self.add(self.n,self.get(0).x)
        self.pop()
        i=+1

    def check_size(self):
      #return self.n
      n = 1#number of nodes
      u = self.head 
      while u.next!=None:
        u=u.next
        n+=1
      if n == self.n: return None
      if n!=self.n: raise ('size does not match the value of n')

    def min(self):
      u = self.head
      smallest = u.x
      while u.next!=None:
        if smallest < u.x:
          smallest = u.x
        u=u.next
      return smallest
      
'''
Big O Analysis for revevse function:
I use add and pop method in my reverse function
I believe that the speed of my reverse function is O(N^2)
There are two loops running, one in my reverse function to iterate thru
the entire linked list
The second loop is from my add, which derived from my get method
'''
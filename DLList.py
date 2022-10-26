from Interfaces import List
import numpy as np
class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
          self.next = None
          self.prev = None
          self.x = x

    def __init__(self) :
      self.dummy = DLList.Node("")
      self.dummy.next = self.dummy #dummy node doesn't contain any data  
      self.dummy.prev = self.dummy
      self.n = 0 #number of element in the DLL
   
    def get_node(self, i : int):
      if i < self.n/2:
        p = self.dummy.next
        for i in range(0,i,1):
          p=p.next
      else:
        p=self.dummy
        for i in range(self.n,i,-1):
          p=p.prev
      return p
        
        
    def get(self, i) -> np.object:
      return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
      u=self.get_node(i)
      y = u.x
      u.x = x   
      return y 

    def add_before(self,w,x): #w is node 
      u = DLList.Node(x)
      u.prev = w.prev
      u.next = w
      u.next.prev = u
      u.prev.next = u
      self.n+=1
      return u
            
    def add(self,i,x): # i is the position, x is the number
      self.add_before(self.get_node(i),x)

    def _remove(self, w : Node) :
      w.prev.next = w.next
      w.next.prev = w.prev
      self.n-=1
    
    def remove(self, i :int) :
      self._remove(self.get_node(i))

    def size(self) -> int:
      return self.n

    def append(self, x : np.object)  :
      self.add(self.n, x)

    def isPalindrome(self) -> bool :
      pass

    def reverse(self) :
      pass
    
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise "Not implemented. Please use the references next and prev"
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
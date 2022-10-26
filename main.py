import SLLStack
import SLLDequeue
import SLList
import DLList
print('Question 1: ')
sample = SLLDequeue.SLLDequeue()
print('push 5 elements: ')
for i in range(1,6):
  sample.push(i)
  print(sample)
print('pop 4 elements: ')
for j in range(1,5):
  sample.pop()
  print(sample)

print('adding elements at the end of the list')
sample.add_first(90)
print(sample)
sample.add_first(100)
print(sample)
sample.add_first(80)
print(sample)
sample.add_first(70)
print(str(sample))
print('removing the last element')
sample.remove_first()
print(sample)
print('the second last element is: '+str(sample.second_last()))

print('\nQuestion 2: ')
newList = SLList.SLList()
for i in range(1,6):
  newList.push(i)
print("the list is: "+ str(newList))
print('get method: '+ str(newList.get(0).x))
print(str(newList))
newList.set(3,10)
print('Set function: '+str(newList))
newList.add(1,20)
print('add function: ' + str(newList))
newList.remove(3)
print('remove function: '+str(newList))

print('\nQuestion 3:')
newList.reverse()
print('Reverse function '+str(newList))
print('\nQuestion 4:')
#print(newList.check_size())
example = SLList.SLList()
for i in range(1,3):
  example.push(i)
print(example)
example.check_size()

print('\nQuestion 5:')
DLL = DLList.DLList()
#DLL.add_before(DLL.dummy.next,1)
print('adding 5 elements: ')
DLL.add(1,10)
DLL.add(2,20)
DLL.add(3,30)
DLL.add(4,20)
DLL.add(5,10)
DLL.add(6,'remove this')
print(DLL)

DLL.remove(5)
print(DLL)
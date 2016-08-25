class Node:
	def __init__(self,data):
		self.data = data 
		self.next = None
		self.prov = None
		self.front = None
class ListIterator:
	def __init__(slef,node):
		self.node = node 
		...
class List:
	def __init__(self):
		self.head = None 
		self.tail = None # to support fast append
	
def insert_after(A,k,v):
	N = A.head
	for i in range(k):
		N = N.next
	M = Node(v)
	M.next = N.next
	N.next = M	


A = 1-> 2-> 4-> 5-x	

insert_after(A,2,3)

A = 1-> 2-> 3-> 4-> 5-x

Queue - line - FIFO

enqueue - add to end

dequeue - removes from front


Stack - LIFO

push -add to end 

pop - remove from the end


Bag - push, pop

Set - add

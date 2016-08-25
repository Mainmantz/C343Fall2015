class BSTNode:
	def __init__(self, key, left=None, right=None):
		self.key = key
   	   	self.left = left
   	   	self.right = right
def less_than(x,y):
	return x < y
def search(self,k,less):
	if less(k,self.key):
		if self.left:
			return self.left.search(k,less)
		else:
			return None
	else: 
		if self.right:
			return self.right.search(k,less)
		else:
			return None
def search_func(key,node,less):
	current = self.root
	while current:
		if less(k,current.key):
			current = current.left
		elif less(current.key,k):
			current = current.right
		else:
			break
	return current
	
	
class BinarySearchTree:
	
	def __init__(self,root=None,less=less_than):
		self.root = root
		self.less = less_than
	def search(self,k):
		if self.root:
			return self.root.search(k,self.less)
		else: 
			return None
	def search_node(self,k): #This is how it will be done on the PROJECT3
		current = self.root
		while current:
			if self.less(k,current.key):
				current = current.left
			elif self.less(current.key,k):
				current = current.right
			else:
				break
		return current
	def insert(self, k):
			current = self.root
			while current:
				if self.less(k,current.key):
					if current.left is None:
						current.left = k 
						break
					else:
						current = current.left
				else:
					if current.right is None:
						current.right = k
						break
					else:
						current = current.right
			
if __name__ == "__main__":
	r = BSTNode(5,BSTNode(2),BSTNode(8))
	T = BinarySearchTree(r)
	#assert T.search(8).key == 8
	#print T.search_node(10) 
	T.insert(10)
	print T.search_node(10)

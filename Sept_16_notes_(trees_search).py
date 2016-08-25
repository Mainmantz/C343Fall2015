class BST Node:
	def __init__(self.key,left,right):
		self.key = key 
		self.left = left
		self.right = right



def tree_search(node,key):
	if node.key == key:
		return node
	elif node.key > key:
		if node.left == None:
			return node
		else:
			return tree.search(node.left,key)
	else:
		if node.right == None:
			return node
		else:
			return tree.search(node.right,key)
			
			
			
def tree_minimum(node):
	if node.left:
		return tree_minimum(node,left)
	else:
		return node
		
def greater_ancestor(n):
	p = n.parent
	if p and n == p.right:
		return greater_ancestor(p)
	else:
		return p
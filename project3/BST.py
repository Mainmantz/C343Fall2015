from stack import ArrayStack

class BSTNode:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        

def less_than(x,y):
    return x < y

class BinarySearchTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less

    # takes value, returns node with key value
    def insert(self, k):
        
        if self.root.key == k:
            return self.root
        
        if self.root is None:
            self.root = BSTNode(k)
            return self.root
            
        if self.less(self.root.key, k): # checks if it's less and empty
            if self.root.right is None:
                self.root.right = BSTNode(k, self.root)
                return self.root.right
            else:
                BinarySearchTree(self.root.right).insert(k)
                
        else: 
            # no need to recheck since it must be greater than
            if self.root.left is None:
                self.root.left = BSTNode(k, self.root)
                return self.root.left
            else:
                BinarySearchTree(self.root.left).insert(k)

        

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n): 
        if n.right:
            n = n.right
            while n.left:
                n = n.left  
            return n
            
        tmp = n.parent
        while tmp:
            if tmp.parent < n.parent:
                return n.parent
            tmp = tmp.parent
        
        return None                

    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        if n.left:
            n = n.left
            while n.right:
                n = n.right
            return n
        
        tmp = n.parent
        while tmp:
            if tmp.parent < n.parent:
                return n.parent
            tmp = tmp.parent
        
        return None                        
        
    # takes key returns node
    # can return None
    def search(self, k):
        
        ## check if the key is already the node
        if k == self.root.key:
            return self.root
        ## recursively call the key until you find it or it doesn't 
        ## exsist, in which case return none
        if self.root.left:
            if self.less(k, self.root.key):
                return BinarySearchTree(self.root.left).search(k)
        if self.root.right:    
                return BinarySearchTree(self.root.right).search(k)
        else:
            return None
        
            
    # takes node, returns node
    def delete_node(self, n):
        new = self.predecessor(n)
        if new:
            n.key = new.key
            new.key = None
            
            extra = new.left
            if new.left:
                self.delete_node(extra)
                self.insert(extra.key)
                
            return n
                
        elif self.successor(n).key:
            n.key = self.successor(n).key
            n.left = self.successor(n).left
            n.right = self.successor(n).right
            return n
        
        else: 
            n.key = None
            n.left = None
            n.right = None
            return n
            
 
 
        
r = BSTNode(5)

t = BinarySearchTree(r)
t.insert(1)



t.insert(10)
t.insert(8)
t.insert(9)
t.insert(90)
t.insert(1)
t.insert(9)
t.insert(3)

def unit_test(tree):
    # print(t.successor(r).key)
    # print(t.predecessor(r).key)

    print(t.search(5).key)
    print(t.search(10).key)
    print(t.search(3).key)
    print(t.search(90).key)
                
unit_test(t)

# t.delete_node(r)

print(t.successor(r).key)
print(t.predecessor(r).key)
print(t.search(3).key)


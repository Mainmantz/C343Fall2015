from stack import ArrayStack

class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 0
def less_than(x,y):
    return x < y

class BinarySearchTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less
    # takes value, returns node with key value
    def calheight(self):
        current = self.root
        while current:
            if not current.left:
                if not current.right:
                    return 1
                else:
                    1 + current.right.height
            else:
                if not current.right:
                    1 + current.left.height
                else:
                    return max(current.left.height,current.right.height)+1
    def insert(self, k):
        current = self.root
        while current:
            if self.less(k,current.key):
                if current.left is None:
                    current.left = BSTNode(k)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(k)
                    break
                else:
                    current = current.right


        

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
            if tmp.parent > n.parent:
                return n.parent
            tmp = tmp.parent
        
        return None
                    
        #print smallest
        
            
            
            
            
        
        

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
                    
        #print largest

    # takes key returns node
    # can return None
    def search(self, k):
        current = self.root
        while current:
            if self.less(k,current.key):
                current = current.left
            elif self.less(current.key,k):
                current = current.right
            else:
                break
        return current
    # takes node, returns node
    def delete_node(self, k):
        current = self.root
        while current:
            if current.key == k:
                current.key = None
                break
            elif self.less(k,current.key):
                current = current.left
            elif self.less(current.key,k):
                current = current.right
            else:
                print "System Error"
                break
        return current

if __name__ == "__main__":
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
    print(t.search(5).key)
    print(t.search(10).key)
    print(t.search(3).key)
    print(t.search(90).key)

    print(t.successor(r).key)
    print(t.predecessor(r).key)
    print(t.search(3).key)





    
##    r = BSTNode(5,BSTNode(2),BSTNode(8))
##    T = BinarySearchTree(r)
##    #assert T.search(8).key == 8
##    print T.search(10) 
##    T.insert(10)
##    print T.successor(7).key
##    #T.predecessor(11)
##    print T.search(10).key
##    #T.delete_node(10)
##    #print T.search(10)
##    #print T.calheight()

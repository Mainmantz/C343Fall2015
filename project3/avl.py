# AVL Trees, by Elizabeth Feicke

class AVLNode():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        
    
def less_than(x,y):
    return x < y

class AVLTree():
    def __init__(self, root = None, less=less_than, *args):
        self.root = root
        self.less = less
        
        self.balance = 0
        
    

    def height_right(self):
        current = self.root
        left = 0
        right = 0
        while current:
            if current.right is None:
                if current.left is None:
                    break
                else:
                    left = left + 1
                    current = current.left
            else:
                right = right + 1
                current = current.right
                
        return (right - left)+1
    def height_bal(self):
        current = self.root
        left = 0
        right = 0
        while current:
            if current.right is None:
                if current.left is None:
                    break
                else:
                    left = left + 1
                    current = current.left
            else:
                right = right + 1
                current = current.right
                
        return left - right
    def height_left(self):
        current = self.root
        left = 0
        right = 0
        while current:
            if current.right is None:
                if current.left is None:
                    break
                else:
                    left = left + 1
                    current = current.left
            else:
                right = right + 1
                current = current.right
                
        return (left - right)+1
    
    
    
    def rrotate(self):
        current = self.root
        A = current
        B = current.left
        T = B.current.right

        current = B
        B.current.right = A
        A.current.left = T 
    def lrotate(self):
        current = self.root
        A = current
        B = current.right
        T = B.current.left

        current = B
        B.current.left = A
        A.current.right = T
    def rebalance(self):
        while self.height_bal() < -1 or self.height_bal() > 1:
            if self.height_bal() > 1:
                if self.height_left < 0:
                    self.lrotate()
            self.rrotate()
            if self.height_bal() < -1:
                if self.height_right() > 0:
                    self.rrotate()

                self.lrotate()
        
        
        
    # takes value, returns node with key value
    def insert(self, k):
        
        current = self.root
        while current:
            if self.less(k,current.key):
                if current.left is None:
                    current.left = AVLNode(k)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = AVLNode(k)
                    break
                else:
                    current = current.right
        self.rebalance()




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
    def delete_node(self, n):
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
        self.rebalance()
        return current

if __name__ == "__main__":
    r = AVLNode(5,AVLNode(2),AVLNode(8))
    T = AVLTree(r)
    #T.update_heights()
    
    #print T.height_left()
    T.insert(10)
    T.insert(11)
    #print T.height_right()
    #print T.height_bal()
    
    
   

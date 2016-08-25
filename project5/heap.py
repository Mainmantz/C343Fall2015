from swap import swap

def less(x, y):
    return x < y

def less_key(x, y):
    return x.key < y.key

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * (i + 1)

def parent(i):
    return (i-1) / 2

# Student code -- fill in all the methods that have pass as the only statement
class Heap:
    def __init__(self, data, 
                 less = less):
        self.data = data
        self.less = less
        self.build_min_heap()
        
    def __repr__(self):
        return repr(self.data)
    
    def minimum(self):
        if len(self.data) == 0:
            print "No data"
        else:
            return self.data[0]
        
        

    def insert(self, obj):
        #Add a char-key pair to the heap"
        #self.data.append(self
        self.data.append(obj)
        #build_min_heap(self.data)

    def extract_min(self):
        #remove and return (char,key) tuple with minimum key.
        #Rasie empty exception if empty.
        A = self.data[0]
        del self.data[0]
        #build_min_heap(self.data)
        return A
        
        
    def min_heapify(self, i):
		#walk through each problem node swapping if need be to make the heap a min heap.
        if left(i) < len(self.data) and self.data[i] > self.data[left(i)]:
            smallest = left(i)
        else:
            smallest = i
        if right(i) < len(self.data) and self.data[smallest] > self.data[right(i)]:
            smallest = right(i)
        if smallest != i:
            swap(self.data,i,smallest)
            min_heapify(self.data,smallest)
    
    def build_min_heap(self):
		#Actually builds the heap going through each node
        last_parent = (len(self.data)/2) - 1
        for i in range(last_parent,-1,-1):
            min_heapify(self.data,i)
        
    
class PriorityQueue:
    def __init__(self, less=less_key):
        self.heap = Heap([], less)

    def __repr__(self):
        return repr(self.heap)

    def push(self, obj):
        self.heap.insert(obj)

    def pop(self):
        return self.heap.extract_min()

if __name__ == "__main__":
    pass
    
    # unit tests here
    

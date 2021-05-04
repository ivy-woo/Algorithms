#Define a max heap class and a min heap class


#Maxheap:
    #major object properties:
        #.size: number of elements in heap
        #.max: maximum key in heap
    #major object methods:
        #.insert(x): insert key x into heap in O(logn)-time
        #.popMax(): remove and return maximum key from heap in O(logn)-time
    
class MaxHeap:
  
    def __init__(self):  
        self.Heap = []
        self.size = 0
        self.max = 'No maximum, heap is empty.'

    #ceiling division
    def ceildiv(self, a, b):
        return -(-a//b)
    
    #return position of parent of pos
    def parent(self, pos):
        return self.ceildiv(pos,2)-1
    
    #return position of the left child of pos
    def leftChild(self, pos):
        return 2*pos+1
    
    #return position of right child of pos
    def rightChild(self, pos):
        return 2*(pos+1)
    
    #return True if pos is a leaf node
    def isLeaf(self, pos):
        if pos > self.parent(self.size-1) and pos <= self.size-1:
            return True
        return False
    
    #return True if pos has only one (left) child
    def oneChild(self, pos):
        if pos == self.parent(self.size-1) and self.size%2==0:
            return True
        return False
    
    #swap two nodes in the heap
    def swap(self, pos1, pos2):
        self.Heap[pos1], self.Heap[pos2] = (self.Heap[pos2], self.Heap[pos1])
    
    #bubble-down pos
    def bubbleDown(self, pos):
        #if pos is a non-leaf node
        if not self.isLeaf(pos):
            #if pos has two children
            if not self.oneChild(pos):
                #and if pos is smaller than either one
                if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):
                    #if left child > right child, swap with left child and recursively call bubble-down
                    if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                        self.swap(pos, self.leftChild(pos))
                        self.bubbleDown(self.leftChild(pos))
                    #else swap with right child and recursively call bubble-down
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.bubbleDown(self.rightChild(pos))
            #if pos has only one child, compare only with that child            
            elif self.Heap[pos] < self.Heap[self.leftChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.bubbleDown(self.leftChild(pos))
                        
    #insert a node into the heap
    def insert(self, element):
        self.size += 1
        self.Heap.append(element) 
        current = self.size -1  #-1 for indexing from 0
        while current != 0 and self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        self.max = self.Heap[0]
  
    #remove and return the minimum element from the heap
    def popMax(self):
        if self.size==0:
            return "Heap is empty."
        if self.size==1:
            self.size -= 1
            self.max = 'No maximum, heap is empty.'
            return self.Heap.pop()
        else:
            self.size -= 1
            pop = self.Heap[0]  #pop root element
            self.Heap[0] = self.Heap.pop()  #last element to root
            self.bubbleDown(0)  #bubble down root
            self.max = self.Heap[0]  #new max is new root
            return pop


#MinHeap:
    #major object properties:
        #.size: number of elements in heap
        #.min: minimum key in heap
    #major object methods:
        #.insert(x): insert key x into heap in O(logn)-time
        #.popMin(): remove and return minimum key from heap in O(logn)-time
    
class MinHeap:
  
    def __init__(self):  
        self.Heap = []
        self.size = 0
        self.min = 'No minimum, heap is empty.'

    #ceiling division
    def ceildiv(self, a, b):
        return -(-a//b)
    
    #return position of parent of pos
    def parent(self, pos):
        return self.ceildiv(pos,2)-1
    
    #return position of the left child of pos
    def leftChild(self, pos):
        return 2*pos+1
    
    #return position of right child of pos
    def rightChild(self, pos):
        return 2*(pos+1)
    
    #return True if pos is a leaf node
    def isLeaf(self, pos):
        if pos > self.parent(self.size-1) and pos <= self.size-1:
            return True
        return False
    
    #return True if pos has only one (left) child
    def oneChild(self, pos):
        if pos == self.parent(self.size-1) and self.size%2==0:
            return True
        return False
    
    #swap two nodes in the heap
    def swap(self, pos1, pos2):
        self.Heap[pos1], self.Heap[pos2] = (self.Heap[pos2], self.Heap[pos1])
    
    #bubble-down pos
    def bubbleDown(self, pos):
        #if pos is a non-leaf node
        if not self.isLeaf(pos):
            #if pos has two children
            if not self.oneChild(pos):
                #and if pos is greater than either one
                if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                    #if left child < right child, swap with left child and recursively call bubble-down
                    if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                        self.swap(pos, self.leftChild(pos))
                        self.bubbleDown(self.leftChild(pos))
                    #else swap with right child and recursively call bubble-down
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.bubbleDown(self.rightChild(pos))
            #if pos has only one child, compare only with that child            
            elif self.Heap[pos] > self.Heap[self.leftChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.bubbleDown(self.leftChild(pos))
                        
    #insert a node into the heap
    def insert(self, element):
        self.size += 1
        self.Heap.append(element) 
        current = self.size -1  #-1 for indexing from 0
        while current != 0 and self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        self.min = self.Heap[0]
  
    #remove and return the minimum element from the heap
    def popMin(self):
        if self.size==0:
            return "Heap is empty."
        if self.size==1:
            self.size -= 1
            self.min = 'No minimum, heap is empty.'
            return self.Heap.pop()
        else:
            self.size -= 1
            pop = self.Heap[0]  #pop root element
            self.Heap[0] = self.Heap.pop()  #last element to root
            self.bubbleDown(0)  #bubble down root
            self.min = self.Heap[0]  #new min is new root
            return pop


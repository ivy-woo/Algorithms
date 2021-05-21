# =============================================================================
# Define the binaryTrees class, 
# in which the n vertices are part of k binary trees for some k in [1,2...,n]. 
# =============================================================================
# Made for use in Huffman code.
#%%

#Intialization:
    #given array A containing weights of each node,
    #binaryTrees(A) initialize the structure with each node forming one individual tree
#Major functions:
    #.combine(x,y): combine the trees with roots x and y into one, with a new root with 
    #               left child being x and right child being y
    #.traverse(): return (1) the binary code of all leaf nodes in order of appearance in A 
                 #(assume left path = 0, right path = 1), (2) depth of all leaf nodes, and 
                 #(3) the weighted average depth of the tree(s)

class binaryTrees:
    
    def __init__(self, weights):
        self.nleaf = len(weights)   #number of leaves
        self.nnode = len(weights)   #number of nodes
        self.ntree = len(weights)   #number of trees
        self.parent = [i for i in range(self.nnode)]   #parent of node is node itself  
        self.leftchild = [None]*self.nnode
        self.rightchild = [None]*self.nnode
        self.weights = [i for i in weights]   #weight of each node (hard copy)
        
    #return True if x is a leaf, else False
    def isLeaf(self, x):
        if self.leftchild[x]==None and self.rightchild[x]==None:
            return True
        return False
    
    #return all indices of nodes which are roots as list
    def findRoot(self):
        root = []
        for i in range(self.nnode-1,-1,-1):
            if self.parent[i] == i:
                root.append(i)
                if len(root) == self.ntree:
                    break
        return root
                
    #depth-first-search, called by .traverse
    def DFS(self, x, code, depth, i, j):
        if self.isLeaf(x):   #if x is leaf
            code.append((x,i))   #apend binary code i for x
            depth.append((x,j))   #apend depth j for x
        else:
            j += 1
            if self.leftchild[x] != None:
                k = i + "0"
                self.DFS(self.leftchild[x], code, depth, k, j)
            if self.rightchild[x] != None:
                k = i + "1"
                self.DFS(self.rightchild[x], code, depth, k, j)
            
    #combine the trees with roots x and y into one, with a new root
    def combine(self, x, y):
        if self.parent[x]!=x or self.parent[y]!=y:
            print("Error, one or more of the input nodes are not originally root.")
            return
        self.nnode += 1   #add new node to structure
        self.ntree -= 1 
        self.parent[x] = self.nnode-1   #parent of x and y is new node  #-1 for indexing from 0
        self.parent[y] = self.nnode-1
        self.parent.append(self.nnode-1)   #parent of new node is itself
        self.leftchild.append(x)   #left child of new node is x
        self.rightchild.append(y)   #right child of new node is y
        self.weights.append(self.weights[x]+self.weights[y])   #new node's weight = sum of weights of x and y
    
    #return the represented binary code (assuming left path =0, else 1) and depth for all leaf nodes, 
    #as well as the weight average depth of the tree(s)
    def traverse(self):
        if self.ntree>1:
            print("Warning, there exist more than one tree in the structure.")
        code = []   #to contain binary codes
        depth = []   #to contain depths
        i = ""   #i and j running variables
        j = 0
        for r in self.findRoot():   #do DFS starting from root(s)
            self.DFS(r, code, depth, i, j)
        code =  [i for _,i in sorted(code)]   #sort according to nodes' ordering
        depth = [i for _,i in sorted(depth)]
        avgdepth = sum([i*j for i,j in zip(self.weights[:self.nleaf],depth)])/self.nleaf   #weighted average depth
        return code, depth, avgdepth

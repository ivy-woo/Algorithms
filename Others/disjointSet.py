# =============================================================================
# Define a disjoint-set class
# =============================================================================

#initialization in O(n)-time:
#    disjointSet(A): disjoint-set with the n elements in array A, 
#                    each constituting one group whose parent is the element itself
#functions:
#    .find(x): find the parent of the group where vertice x belongs to in O(logn)-time
#    .union(x,y): combine the two groups where x and y respectively belong to into one in O(logn)-time

#%%
class disjointSet:

    def __init__(self,vertices):
        self.parent = {}
#        self.parent = vertices
        self.size = {}
#        self.size = [1 for i in vertices]
        self.initDict(vertices)   #funciton to initialize the two dictionaries

    def initDict(self, vertices):
        for i in vertices:
            self.parent[i] = i
            self.size[i] = 1

    def find(self,x):
        if self.parent[x]==x:   #if x is parent
            return x   #return x
        return self.find(self.parent[x])   #else recursively look for parent

    def union(self,x,y):  
        i = self.find(x)  
        j = self.find(y)
        if i==j:
            return   #do nth if x and y have same parent
        if self.size[i]>=self.size[j]:   #if group of i larger
            self.parent[j] = i   #make i as parent of j 
            self.size[i] += self.size[j]   #update size of group
        else:  #do converse if group j larger
            self.parent[i] = j
            self.size[j] += self.size[i]

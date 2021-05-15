# =============================================================================
# 2-SAT problem
# Given a set of n boolean variables and m constraints which are disjunctions of 2 literals ('A or B'),
# determine whether there exists solution to the variables with which all constraints are satisfied.
# =============================================================================
#%%

#Input: list of 2-literal constraints, n=total number of variables
#Output: True if there exists solution to the variables, else False
#Time complexity: O(m+n) (assume healthy data and hash functions for dictionaries), 
                # where m=number of constraints, n=number of variables
def twoSAT(constraints):
    edges = translate(constraints)   #translate the constraints to edges of a directed graph
    #compute the strongly connected components in the graph
    scc = Kosaraju(edges)   #see script '../Others/Kosaraju.py'
    for i in scc.keys():
        if i>0 and scc[i]==scc[-i]:   #if there exists any i, where i implies not i and not i implies i
            return False   #then there is no solution satisfying the set of constraints
    return True


#translate the constraints to edges of a directed graph 
#Input: list of all constraints (negative number means negation), n=total number of variables
#Output: list of tuples (i,j), each representing an edge from node i to node j in a directed graph
def translate(constraints):
    edges = []
    for temp in constraints:   #for each constraints (A or B)
        edges.append((-temp[0],temp[1]))   #not A implies B
        edges.append((-temp[1],temp[0]))   #and not B implies A
    return edges   #set of edges is set of all implications from the constraints



# =============================================================================
#%% function to read example data (in examples/)

#each of the following lines "A B" is the constraint "A or B", negative number means negation
def loadData(path): 
    with open(path) as file:
        data = file.readlines()
        data = [[int(n) for n in data[i].split()] for i in range(len(data))]
    return data


#%% example

##see plot in examples/ for visualization of constrains as graph
constraints = loadData('examples/twoSAT.txt')   #file contains 100 constraints
twoSAT(constraints)   #exists no solution

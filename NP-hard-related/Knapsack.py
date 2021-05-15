# =============================================================================
# 0-1 Knapsack problem
# Given a set of n items, each with a postive value and a postive integral size, determine the maximum 
# total value attainable by some subset of the items (each item can appear either 0 or 1 time), with which 
# the total size does not exceed the Knapsack capacity which is some positive integral C.
# =============================================================================
#Two appraches are implemented

#Input: arrays `values` and `sizes` containing positive values and positive integral sizes of n items, 
#       and an integral knapsack capacity C
#Output: the maximum total value attainable by some subset of the items, with which the total size <= C.
#        if fullArray, return the complete 2-D array used for computation.
#Time complexity: O(nC)


#Approach 1
def Knapsack(values, sizes, C, fullArray=False):
    if len(values)!=len(sizes):
        print("Error, number of values does not mach number of sizes.")
        return
    n = len(values)
    A = [[0 for i in range(C+1)]] + [[None for i in range(C+1)] for j in range (n)]   # 0's are base case
    for i in range(1,n+1):
        for c in range(C+1):
            if sizes[i-1]>c:   #-1 for indexing from 0
                A[i][c] = A[i-1][c]
            else:
                #A[i][j] = optimal max total value when there are first i items and capacity is j
                A[i][c] = max(A[i-1][c], A[i-1][c-sizes[i-1]] + values[i-1])
    if fullArray:
        return A
    return A[n][C]   #return max total value for original problem, when there're n items and capacity=C


#Approach 2 - fill array A only when needed (use esp. when C is large and/or n is small)
def Knapsack2(values, sizes, C, fullArray=False):
    if len(values)!=len(sizes):
        print("Error, number of values does not mach number of sizes.")
        return
    n = len(values)
    A = [[None for i in range(C+1)] for j in range (n+1)]    
    fill(A,n,C,values,sizes)   #call fill to fill A[n][C] which is the element of interest
    if fullArray:
        return A
    return A[n][C]   

def fill(A, i, c, values, sizes):   #fill A[i][c] based on values, sizes and selected elements in A
    if i==0 or c<=0:
        A[i][c] = 0   #base case
        return
    if A[i-1][c] == None:   #if A[i-1][c] not yet calculated
        fill(A,i-1,c,values,sizes)   #call fill recursively
    if sizes[i-1]>c:
        A[i][c] = A[i-1][c]
    else:
        if A[i-1][c-sizes[i-1]] == None:   #if A[i-1][c-sizes[i-1]] not yet calculated
            fill(A,i-1,c-sizes[i-1],values,sizes)   #call fill recursively
        A[i][c] = max(A[i-1][c], A[i-1][c-sizes[i-1]] + values[i-1])



# =============================================================================
# example

from ramdom import sample
n=100   #set number of items
C=5000   #set capacity
V = sample(range(1,500),n)
S = sample(range(100,5000),n)
Knapsack(V,S,C)   #return the max total value
Knapsack2(V,S,C)   #both approaches return the same result
#Knapsack(V,S,C,True)   #return the complete 2-Darray

#timing
#if C is large and/or n is small
n=30   
C=100000
V = sample(range(1000,50000),n)
S = sample(range(10000,100000),n)
%time A = Knapsack(V,S,C)
%time B = Knapsack2(V,S,C)   #approach2 is much faster

# =============================================================================
# Randomized selection algorithm
# Compute the k-th smallest element in the input array A in linear time
# =============================================================================
# Note: array A is partially sorted in-place
#%%

#Input: list A containing n numbers, integer k
#Output: the k-th smallest element in A
#Time complexity: O(n)
def Selection(A,k):
    k-=1  #because first element has index 0
    return RSelect(A,k)


#randomized selection
def RSelect(A,k):
    n = len(A)
    if n==1:
        return A[0]
    i = choosePivot(n)  #i = chosen pivot's index
    swap(A,0,i)     #swap pivot to the front
    j = partition(A,n)  #j = pivot's updated index
    if j==k:
        return A[j]
    elif j>k:
        return RSelect(A[:j],k)
    else: 
        return RSelect(A[j+1:],k-j-1)


#adopt uniform randomness to pick pivot
from random import randint
def choosePivot(n):
    return randint(0,n-1)


#swap list elements A[i] and A[j]
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return


#postcondition: pivot locates at its correct position in A, i.e. all other 
#elements precede(succeed) pivot if being smaller(larger) than pivot 
def partition(A,n):
    i = 1
    for j in range(n):
        if A[j]<A[0]:
            swap(A,i,j)
            i+=1
    swap(A,0,i-1)
    return i-1  #return pivot's updated index



# =============================================================================
#%% checking/example
from random import sample
N=10001
A=sample(range(-50000,50000),N)
B = sorted(A)
i = randint(0,N-1)
Selection(A,i) == B[i-1]  #True


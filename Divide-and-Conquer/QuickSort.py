# =============================================================================
# Randomized quick sort
# Sorting list elements from smallest to largest in-place
# =============================================================================
#%%

#Input: list A, integers l and r
#Post-condition: elements A[l] to A[r] inclusive sorted from smallest to largest
#Time complexity: O(nlogn), n=r-l+1
def QuickSort(A,l,r):
    if l>=r:
        return
    i = choosePivot(l,r)  #i = chosen pivot's index
    swap(A,i,l)
    j = partition(A,l,r)  #j = pivot's updated index
    QuickSort(A,l,j-1)
    QuickSort(A,j+1,r)
    return


#adopt uniform randomness to pick pivot
from random import randint
def choosePivot(l,r):
    return randint(l,r)

#swap list elements A[i] and A[j]
def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return

#postcondition: across all A[j] where j in [l,r], pivot locates at its correct position, 
#i.e. all other A[j] precede(succeed) pivot if being smaller(larger) than pivot 
def partition(A,l,r):
    i = l+1
    for j in range(l+1,r+1,1):
        if A[j]<A[l]:
            swap(A,i,j)
            i+=1
    swap(A,l,i-1)
    return i-1  #return pivot's updated index

# =============================================================================
#%% checking/example
from random import sample
A=sample(range(-50000,50000),10001)
B = sorted(A)
QuickSort(A,0,len(A)-1)  #sorting in-place
A==B  #True


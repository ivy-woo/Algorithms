# =============================================================================
# Counting inversions
# Compute and return the number of inversions in an array of n elements in O(nlogn)-time
# Inversion defined as the event of A[i]>A[j] where i<j
# =============================================================================
#%%

#Input: list A of unsorted real numbers
#Output: tuple (A,n), A=list of sorted inputs, n=number of inversions
#Time complexity: O(nlogn)
def countInv(A):
    n=len(A)
    if n==0 or n==1:
        return A, 0
    m=n//2
    Lsort, Linv = countInv(A[:m])  #recurse on first half of A
    Rsort, Rinv = countInv(A[m:])  #recurse on second half of A 
    #merge first and second half, count inversions involving both halves
    sort, Sinv = countSplitInv(Lsort,Rsort,n,m)  
    return sort, Linv+Rinv+Sinv


def countSplitInv(Lsort,Rsort,n,m):
    i = 0
    j = 0
    count = 0
    sort = [0]*n
    for k in range(n):
        if i==m:
            sort[k:] = Rsort[j:]
            break
        if j==n-m:
            sort[k:] = Lsort[i:]
            break
        if Lsort[i]<Rsort[j]:
            sort[k] = Lsort[i]
            i += 1
        else:
            sort[k] = Rsort[j]
            j += 1
            count += m-i
    return sort, count


#%%
#Brute-force search (in O(n^2)-time) for checking
def BFcountInv(A):
    n=len(A)
    count=0
    for i in range(n-1):
        for j in range(i+1,n,1):
           if A[i]>A[j]:
               count+=1
    return count


# =============================================================================
#%% timing and cross-checking

from random import sample
A=sample(range(-50000,50000),10001)   #randomly pick integers from specified range
%time B=countInv(A)[1]   #divide-and-conquer
%time C=BFcountInv(A)   #brute-force search, much slower
B==C  #True, two algo return same result

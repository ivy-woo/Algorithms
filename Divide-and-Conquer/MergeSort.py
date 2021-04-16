#Merge sort
#Return list with elements sorted from smallest to largest

def MergeSort(A):
    n=len(A)
    if n==1:
        return A
    m=n//2
    B=MergeSort(A[:m])  #B has m elements
    C=MergeSort(A[m:])  #C has m elements if n is even, m+1 if n is odd
    return Merge(B,C,n,m)

def Merge(B,C,n,m):
    i=0
    j=0
    D=[0]*n
    for k in range(n):
        if i==m:
            D[k:]=C[j:]
            break
        if j==n-m:
            D[k:]=B[i:]
            break
        if B[i]<C[j]:
            D[k]=B[i]
            i+=1
        else:
            D[k]=C[j]
            j+=1
    return D


#checking
from random import sample
A=sample(range(-50000,50000),10001)
MergeSort(A) == sorted(A)  #True

#timing
#%time B=MergeSort(A)


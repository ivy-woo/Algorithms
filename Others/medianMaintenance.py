# =============================================================================
# Median maintenance problem
# Suppose numeric data arrives consecutively, update the median of the arrived data
# in O(logn)-time for each round by using two heaps
# =============================================================================

#return the sequence of n medians, with the i-th median, i in [1,2,...,n], being the 
#median of the first i data points 
def medians(data):
    #MaxHeap and MinHeap object classes defined in MaxMinHeap.py
    h1 = MaxHeap()  #max heap
    h2 = MinHeap()  #min heap
    n = len(data)
    med = [0]*n
    h2.insert(data[0])
    med[0] = data[0]
    for i in range(1,n):
        if data[i] < h2.min:
            h1.insert(data[i])
        else:
            h2.insert(data[i])    
        if h1.size-h2.size > 1:
            h2.insert(h1.popMax())
        elif h2.size-h1.size > 1:
            h1.insert(h2.popMin())
        #median defined as the (i+1)/2-th element in the i sorted elements if i is odd,
        #and as the i/2-th element if i is even.
        if h1.size >= h2.size:
            med[i] = h1.max
        else:
            med[i] = h2.min
    return med


#example
from random import sample
data=sample(range(-500,500),30)
print(data)
print(medians(data))


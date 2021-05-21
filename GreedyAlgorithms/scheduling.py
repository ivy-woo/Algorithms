# =============================================================================
# Greedy Algorithms for the scheduling problem
# Problem: given a set of n jobs with positive weights w_i's and positive lengths 
# l_i's for i in [1,2,...,n], compute the sequence of completing the jobs s.t.
# the weighted sum of completion time (WSCT) is minimized.
# =============================================================================
#%%
# GreedyRatio:
# schedule the n jobs in A using the ratio of weight and length of jobs, break ties arbitrarily. 
# Time complexity: O(nlogn)

#returns the sequence of jobs in A to be completed
#if completionTime=True, returns also WSCT
def GreedyRatio(A, completionTime=True):  
    n = len(A)
    ratio = [i[0]/i[1] for i in A]   #compute ratio
    #append job indices and schedule by ratio in descending order
    seq = [i[0] for i in sorted(enumerate(ratio), key=lambda x:x[1], reverse=True)]  
    if not completionTime:
        return seq
    t = [0]*n
    t[0] = A[seq[0]][1]  
    for i in range(1,n):        
        t[i] = t[i-1] + A[seq[i]][1]   #t contains completion time of each scheduled job
    wsct = sum([A[seq[i]][0]*t[i] for i in range(n)])
    return seq, wsct


#%%
# GreedyDiff:
# schedule the n jobs in A using the difference of weight and length of jobs,
# break ties by scheduling the job with the heavier weight first. 
# *****This algorithm does NOT always return the optimal solution*****
# Time complexity: O(nlogn)

#returns the sequence of jobs in A to be completed
#if completionTime=True, returns also WSCT
def GreedyDiff(A, completionTime=True):  
    n = len(A)
    diff = [i[0]-i[1] for i in A]   #compute difference
    seq = [(i, diff[i], A[i][0]) for i in range(n)]   #append job indices and weights
    #schedule first by the difference in descending order, then break ties according to weights
    seq = sorted(seq, key=lambda x:(x[1],x[2]), reverse=True)  
    seq = [i[0] for i in seq]
    if not completionTime:
        return seq
    t = [0]*n
    t[0] = A[seq[0]][1]  
    for i in range(1,n):        
        t[i] = t[i-1] + A[seq[i]][1]   #t contains completion time of each scheduled job
    wsct = sum([A[seq[i]][0]*t[i] for i in range(n)])
    return seq, wsct



# =============================================================================
#%% function to read example data (in examples/)

#for each line n, tuple (w,l) means job n's weight = w and its length = l.
def loadData(path): 
    with open(path) as file:
        A = file.readlines()
        A = [[int(n) for n in A[i].split()] for i in range(len(A))]
    return A


#%% example

A = loadData('example/scheduling.txt')  #file contains 10 jobs for easy checking
seqR, wsctR = GreedyRatio(A)  #seqR=[8,9,0,6,5...], wsctR=104255 (optimal)
seqD, wsctD = GreedyDiff(A)  #seqD=[9,8,0,6,5,...], wsctD=104913 (not optimal)


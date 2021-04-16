#Karatsuba multiplication algorithm
#Positive integers multiplication in O(nlogn)-time where n is number of digits

#Note: algo written to read numerical strings instead of integers, so that
#large numbers (over 64-bits) can also be handled. see example at the bottom


#inputs: x and y numerical strings of positive integers
#output: multiple of x and y as string
def Karatsuba(x,y):
    x,y,n = equalDigits(x,y)
    if n==1:
        return str(int(x)*int(y))
    a,b = split(x)
    c,d = split(y)
    p = str(int(a)+int(b))
    q = str(int(c)+int(d))
    ac = Karatsuba(a,c)
    bd = Karatsuba(b,d)
    pq = Karatsuba(p,q)
    adbc = str(int(pq)-int(ac)-int(bd))
    return add(trailZeros(ac,n), add(trailZeros(adbc,n/2), bd))


#make strings x and y to have equal number of digits which is power of 2,
#by adding leading zeros when necessary.
def equalDigits(x,y):
    x,nx = powerTwo(x)
    y,ny = powerTwo(y)
    if nx>ny:
        y = str(0)*(nx-ny) + y
        return x, y, nx
    elif ny>nx:
        x = str(0)*(ny-nx) + x
    return x, y, ny


#make no. digits of string x to be power of 2, by adding the least possible 
#leading zeros.
def powerTwo(x):
    nx = len(x)
    power = True
    i = 0
    while nx>1:
        if nx%2==1:
            power=False
        nx = (nx-nx%2)/2
        i += 1
    if not power:
        nx = 2**(i+1)
        nz = nx-len(x)
        return str(0)*nz + x , nx
    return x, len(x)


#split string x into two parts of equal length (x has even no. digits)
def split(x):
    i = int(len(x)/2)
    return x[:i], x[i:]


#add z trailing zeros to string x
def trailZeros(x,z):
    return x + str(0)*int(z)


#addition of two numerical strings of positive integers
def add(x,y):
    nx = len(x)
    ny = len(y)
    n = nx
    if nx>ny:
        y = str(0)*(nx-ny) + y
    else:
        x = str(0)*(ny-nx) + x
        n = ny
    sum = [0]*n
    carry = False
    for i in range(n-1,-1,-1):
        sum[i] = int(x[i])+int(y[i])+carry
        carry = False
        if sum[i]>9:
            carry = True
            sum[i] -= 10
    if carry:
        sum.insert(0,1)
    while len(sum)>1 and sum[0]==0:
        del sum[0]
    return ''.join(map(str,sum))



#checking
from random import sample
A=sample(range(1,1000000),2)
Karatsuba(str(A[0]),str(A[1])) == str(A[0]*A[1])  #True

#large numbers
A[0]='38420173497578724650122349587208642398463052394862034920438654873498748'
A[1]='230290234693356278014352468704238621058923190'
print(len(A[0]), len(A[1]))
Karatsuba(str(A[0]),str(A[1]))  #can be handled in form of strings

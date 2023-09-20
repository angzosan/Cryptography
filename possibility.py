import math

def divisors(m): #find the divisors of the integer m
    L=[]         #and returns them in an array
    for i in range(1,m):
        if (m%i==0):
            L.append(i)
    return L

m=56353
m1=str(m) #we turn the number to a string so we can find the number of bits easier
upper=math.floor(len(m1)/2)+1   #setting the upper limit
bottom=math.floor(len(m1)/2)-1   #setting the bottom limit
total=0   # counter for the percentage
L=divisors(m)
print(L)
for i in L:
    d1=str(i)
    if (len(d1)>=bottom and len(d1)<=upper):
        total=total+1
print(total/(len(L)))

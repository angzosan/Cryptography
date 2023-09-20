import math


def fast(a, g, N):
    g_bin = bin(g)
    
    x = int(a,base=10)        #where a=the current letter xi
    d = 1
    for i in range(len(g_bin) -1, 1, -1):
        if (g_bin[i] == '1'):
            d = (d*x) % N
        x = (x**2) % N

    return d

def continuous_fraction(N,e):   # euclidean algorithm - we need to find an approximation cause k/d ~ e/N
    a=[-1 for i in range(0,1000)]
    a[0]=0
    i=1
    while N/e>0:
        temp=N
        N=e
        e=temp
        x=e/N
        a[i]=math.floor(x)
        e=e-(N*a[i])
        i=i+1
        if (e==0):
            break
    a_=[a[i] for i in range(0,i)]
    return a_
        


def k_d(a):

    kd=[[0 for x in range(0,2)] for y in range(0,len(a))]
    kd[1][0]=1
    kd[1][1]=a[1]
    for i in range(2,len(a)):
        ar=1
        par=1
        temp1=a[i]
        for j in range(i,1,-1):
            par=a[j-1]*temp1+ar
            ar=temp1
            temp1=par
        kd[i][0]=ar
        kd[i][1]=par
    return kd
            
def f_(e,k,d):     # we check if the equation has integer solutions 
    return int((e*d - 1)/k)

def eq(N,f):
    temp=-N+f-1
    D=int(temp**2-4*N)
    if (D<0):
        return False
    if (D==0):
        if (temp==N):
            return True
    
    x1=int(temp-math.sqrt(D))
    x1=int(x1/2)
    x2=int(temp+math.sqrt(D))
    x2=int(x2/2)
   # print(x1,"   ",x2)
   # print(x1*x2)
    return x1*x2==N
        
def check_effectiveness(N,d):
    return N**(1/4)/3>d and d != 1


N=5697733
N = int(input ('Give the N number : '))  # public modulus 
e=3105251
e = int(input ('Give the e number : '))  # public exponent

a=continuous_fraction(N, e)

kd=k_d(a)
effect = False
d=0
for i in range(1,len(a)):
    f=f_(e,kd[i][0],kd[i][1])
    if(eq(N,f)):
        d=kd[i][1]
        print(d)
        if (check_effectiveness(N,d)):
            print("Number "+d +' is effective')
        else:
            print("Number "+ d +' is not effective')
        effect = True
        break
if not effect: 
     print('There is no d value for the numbers given')
        

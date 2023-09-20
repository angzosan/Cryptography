def pow1(base, exponent, modulus):
 
    result = 1;
    base = base % modulus;
    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base) % modulus;
        exponent = int(exponent) >> 1;
        base = (base * base) % modulus;
 
    return result;
 
# utility function to find gcd
def gcd(a, b):
    if (b == 0):
        return a;
    else:
        return gcd(b, a % b);
 
# Returns k such that b^k = 1 (mod p)
def order(p, b):
 
    if (gcd(p, b) != 1):
        print("p and b are not co-prime.\n");
        return -1;
 
    # Initializing k with first
    # odd prime number
    k = 3;
    while (True):
        if (pow1(b, k, p) == 1):
            return k;
        k += 1;
 
# function return p - 1 (= x argument) as
# x * 2^e, where x will be odd sending e
# as reference because updation is needed
# in actual e
def convertx2e(x):
    z = 0;
    while (x % 2 == 0):
        x = x / 2;
        z += 1;
         
    return [x, z];

def STonelli(n, p):
 
    # a and p should be coprime for
    # finding the modular square root
    if (gcd(n, p) != 1):
        print("a and p are not coprime\n");
        return -1;
 
    # If below expression return (p - 1) then
    # modular square root is not possible
    if (pow1(n, (p - 1) / 2, p) == (p - 1)):
        print("no sqrt possible\n");
        return -1;
 
    # expressing p - 1, in terms of s * 2^e,
    # where s is odd number
    ar = convertx2e(p - 1);
    s = ar[0];
    e = ar[1];
 
    # finding smallest q such that
    # q ^ ((p - 1) / 2) (mod p) = p - 1
    q = 2;
    while (True):
       # print(q)
        # q - 1 is in place of (-1 % p)
        if (pow1(q, (p - 1) / 2, p) == (p - 1)):
            break;
        q += 1;
 
    # Initializing variable x, b and g
    x = pow1(n, (s + 1) / 2, p);
    b = pow1(n, s, p);
    g = pow1(q, s, p);
 
    r = e;
 
    # keep looping until b become
    # 1 or m becomes 0
    while (True):
        m = 0;
        while (m < r):
            if (order(p, b) == -1):
                return -1;
 
            # finding m such that b^ (2^m) = 1
            if (order(p, b) == pow(2, m)):
                break;
            m += 1;
 
        if (m == 0):
            return x;
 
        # updating value of x, g and b
        # according to algorithm
        x = (x * pow1(g, pow(2, r - m - 1), p)) % p;
        g = pow1(g, pow(2, r - m), p);
        b = (b * g) % p;
 
        if (b == 1):
            return x;
        r = m;


n=17592194433025
p=309485009821345068724781063


x = STonelli(n, p);
 
if (x == -1):
    print("Modular square root is not exist\n");
else:
    print("Modular square root of", n,
          "and", p, "is", x);

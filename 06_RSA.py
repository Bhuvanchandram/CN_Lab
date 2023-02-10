import math
import random

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def generate_pq():
    nums = [i for i in range(2,101)]
    
    for n in range(2,101):
        for i in range(2,int(math.ceil(n/2)+1)):
            if n%i == 0:
                nums.remove(n)
                break
            else:
                continue
    
    p = random.choice(nums)
    nums.remove(p)
    q = random.choice(nums)
    return p,q

p,q = generate_pq()

print("The value of p is:{}".format(p))
print("The value of q is:{}".format(q))

n = p * q
phi = (p - 1) * (q - 1)

def generate_e(phi):
    poss_values = []
    
    for i in range (2,phi):
        if gcd(i,phi) == 1:
            e = i
            poss_values.append(e)
    
    e = random.choice(poss_values)
    return e

e = generate_e(phi)

print("The value of the public key 'e' is:{}".format(e))

def generate_d(phi):
    #poss_values = []
    for i in range (2,phi):
        if (i*e)%phi == 1:
            d = i
            break
            #poss_values.append(e)
    
    return d

d = generate_d(phi)

print("The value of the private key 'd' is:{}".format(d))

msg = random.randint(1,n)

print("The message to be encrypted is:{}".format(msg))

def encrypt(msg,e,n):
    c = pow(msg,e,n)
    return c

c = encrypt(msg,e,n)

print("The encrypted message(ciphertext) is:{}".format(c))

def decrypt(msg,d,n):
    dec = pow(msg,d,n)
    return dec

dec = decrypt(c,d,n)

print("The decrypted message(original message/plaintext) is:{}".format(dec))
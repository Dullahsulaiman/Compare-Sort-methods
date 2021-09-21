
"""
Abdallah Sulauman
Austin Welter
Srisaipranay Bande

Project 1

"""
import math
import random


# Input Prime Numbers
print("PLEASE ENTER THE 'p' AND 'q' :")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))




# Check if P and Q are Prime
def prime_check(a):
    if( a==2):
        return True
    elif(( a <2) or (( a %2 )==0)):
        return False
    elif( a >2):
        for i in range(2 ,a):
            if not( a %i):
                return False
    return True

Pcheck = prime_check(p)
Qcheck = prime_check(q)
while (((Pcheck == False) or (Qcheck == False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    Pcheck = prime_check(p)
    Qcheck = prime_check(q)

# RSA Modulus
n = p * q
print("RSA Modulus(n) is:" ,n)

# Eulers Toitent
r=(p - 1) * (q - 1)
print("Eulers Toitent(r) is:", r)


# GCD
def egcd(e, r):
    while(r != 0):
        e, r = r, e % r
    return e


# Euclid's Algorithm
def eugcd(e, r):
    for i in range(1, r):
        while (e != 0):
            a, b = r // e, r % e
            if (b != 0):
                print("%d = %d*(%d) + %d" % (r, a, e, b))
            r = e
            e = b


# Extended Euclidean Algorithm
def eea(a, b):
    if (a % b == 0):
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return (gcd, t, s)


# Multiplicative Inverse
def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if (gcd != 1):
        return None
    else:
        if (s < 0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d." % (s, s, s % r))
        elif (s > 0):
            print("s=%d." % (s))
        return s % r

# e Value Calculation



ran = random.randint(1,r)
for i in range(1,(r-ran)):
    if (egcd(i, r) == 1) and (i < r):
        e = i
    ran = random.randint(1,r)




# d, Private and Public Keys
print("EUCLID'S ALGORITHM:")
eugcd(e, r)

print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e, r)
while(d == e):
    for i in range(1, (r - ran)):
        if (egcd(i, r) == 1) and (i < r):
            e = i
        ran = random.randint(1, r)
    d = mult_inv(e, r)

print("The value of d is:", d)
print("The value of e is:", e)
public = (e, n)
private = (d, n)
print("Private Key is:", private)
print("Public Key is:", public)
print("*****************************************************")

# Encryption
def encrypt(pub_key, n_text):
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        if (i.isupper()):
            m = ord(i) - 65
            c = (m ** e) % n
            x.append(c)
        elif (i.islower()):
            m = ord(i) - 97
            c = (m ** e) % n
            x.append(c)
        elif (i.isspace()):
            spc = 400
            x.append(400)
    return x


# Decryption
def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ' '
    m = 0
    for i in txt:
        if (i == '400'):
            x += ' '
        else:
            m = (int(i) ** d) % n
            m += 65
            c = chr(m)
            x += c
    return x
message = 0
counter =0

# Message
while message != 'end':
    text = input("are you a general user or owner of the keys?( input user or owner) : ")
    if text == 'owner':
        if counter != 0:
            public = (e, n)
            private = (d, n)
        print("Private Key is:", private)
        print("Public Key is:", public)



        # Choose Encrypt or Decrypt and Print
        choose = input("Type '1' to generate a digital signature and '2' for decrytion.")
        if (choose == '1'):
            message = input("what message would you like to use for your digital signature  :")
            ds = encrypt(private, message)
            print('Your digital signature is: ', ds)
        elif (choose == '2'):
            message = input("Input the message would you like to decrypt(Separate numbers with ',' for decryption):")
            print("Your message is:", message)
            dec_msg = decrypt(private, message)
            print("Your decrypted message is:", dec_msg)
        else:
            print("You entered the wrong option.")

    else:
        print("input public key:")
        ee = int(input('input e: '))
        nn = int(input('input n: '))
        public = (ee, nn)

        choose = input("Type '1' for encryption and '2' for verify digital signature")
        if (choose == '1'):
            message = input("What would you like encrypted :")
            print("Your message is:", message)
            enc_msg = encrypt(public, message)
            print("Your encrypted message is: ", enc_msg)
        elif choose == '2':
            ds = input('input digital signature ')
            message = decrypt(public, ds)
            print("if message is clear the sender is verified, if not discard message : ", message)
    counter += 1
    print("*****************************************************")
    message = input("do you have another task? (type end to end)")

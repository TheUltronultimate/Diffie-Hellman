import random


def isPrime(n):
    
    '''Checks if a number n is Prime
    Input: int;
    Output: Boolean;
    '''
    flag = True
    for i in range(1, (n**0.5)+1, 2 ):
        print(i)
        if (n % i) == 0 and i != 1:
            return False
        
    return flag

#Values for generating random Primes
p = 1
q = random.SystemRandom().randint(0, 200)

#Value n to be used as modulo for the key exchange
n = random.SystemRandom().randint(0, 200*10**12)
primes = [i for i in range(p,q) if isPrime(i)]
g = random.choice(primes)


chloe_number = random.SystemRandom().randint(1, 10000) #private number for Alice
louis_number = random.SystemRandom().randint(1, 10000) #private number for Bob

def DiffieHellman(a, b):
    n = random.SystemRandom().randint(0, 200*10**12)
    primes = [i for i in range(p,q) if isPrime(i)]
    g = random.choice(primes)
    B_T1 = ((g)**b) % n
    A_T1 = ((g)**a) % n
    A_T2 = ((B_T1)**a) % n
    B_T2 = ((A_T1)**b) % n
    if A_T2 == B_T2:
        key = A_T2
        return key

#DiffieHellman(alice_number, bob_number)
#print(DiffieHellman(chloe_number, louis_number))

        
    
    
import random
import math



def is_prime(num, k=5):  # Using the Miller-Rabin primality test for better efficiency
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    
    # Write num as (2^r) * d + 1
    r, d = 0, num - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Perform the Miller-Rabin test k times
    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

def generate_prime(min_value, max_value):
    while True:
        prime = random.randrange(min_value | 1, max_value, 2)  # Generate only odd numbers
        if is_prime(prime):
            return prime

def mod_inverse(e, phi):    # Using the Extended Euclidean Algorithm to find the modular inverse
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
        
def phi_n(p, q):    # Calculate the Euler's totient function
    return (p - 1) * (q - 1)



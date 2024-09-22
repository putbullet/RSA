from main import *

head_txt ="""
888b. 8888 8b  8 88888    db       888b. .d88b.    db    
8  .8 8www 8Ybm8   8     dPYb      8  .8 YPwww.   dPYb   
8wwP' 8    8  "8   8    dPwwYb     8wwK'     d8  dPwwYb  
8     8888 8   8   8   dP    Yb    8  Yb `Y88P' dP    Yb """
print(head_txt)
print("\n" * 2)
print("Welcome to RSA encryption!\n")
message = input("Enter the message to encrypt: \n")

# Generate prime numbers (adjust range if needed)
print("Generating primes...")
q, p = generate_prime(5**5, 5**6), generate_prime(5**5, 5**6)
while q == p:
    q = generate_prime(5**5, 5**6)

# RSA calculations
n = p * q
phi = phi_n(p, q)
e = random.randint(3, phi - 1)

while math.gcd(e, phi) != 1:
    e = random.randint(3, phi - 1)

d = mod_inverse(e, phi)

# Output results
print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)
print("q: ", q)
print("p: ", p)
print("Please save the public key and private key somewhere safe for decryption\n")

message_encod = [ord(c) for c in message]
cipher_text = [pow(c, e, n) for c in message_encod]
cipher_text_join = "".join(map(str, cipher_text))
print("Cipher text: ", cipher_text_join)

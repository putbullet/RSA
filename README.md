# Penta RSA Encryption

Welcome to **Penta RSA Encryption**, a simple implementation of RSA encryption in Python. This project demonstrates the fundamental concepts of RSA encryption, including key generation, encryption, and decryption.

## Project Overview

RSA (Rivest-Shamir-Adleman) is a widely used asymmetric encryption algorithm that relies on the mathematical properties of large prime numbers. The Penta RSA Encryption project allows you to:

- Generate RSA keys (public and private)
- Encrypt messages using the public key
- Decrypt messages using the private key

## Features

- **Prime Number Generation**: Efficiently generates large prime numbers for RSA key generation.
- **Key Generation**: Creates public and private keys based on generated prime numbers.
- **Encryption & Decryption**: Encrypts and decrypts messages using the RSA algorithm.

## Installation

To use this project, you need Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

First, clone the repository to your local machine:

```
git clone https://github.com/putbullet/RSA.git
cd penta-rsa-encryption
```

### Run the Code

Run the RSA encryption script using Python:

```
python RSA.py
```

## How It Works

1. **Generate Prime Numbers**: The `generate_prime` function creates two large prime numbers needed for RSA key generation.
2. **Key Generation**: The public key (e) and private key (d) are computed. The public key is used for encryption, while the private key is used for decryption.
3. **Encryption**: Messages are converted to numeric format and encrypted using the public key.
4. **Decryption** (under developpement): Encrypted messages can be decrypted using the private key.

### Example Usage

```python
# Run the script
python RSA.py

# Enter the message to encrypt when prompted
Enter the message to encrypt: hello

# Output
Public key:  65537
Private key:  1234567890
n:  3233
q:  61
p:  53
Please save the public key and private key somewhere safe for decryption

Cipher text:  22012657202626572790
```

## Code Structure

- **`RSA.py`**: Main script to run the RSA encryption and decryption process.
- **`main.py`**: Contains helper functions for prime number generation, modular inverse calculation, and RSA key calculations.

## Contributing

Contributions to this project are welcome! If you have suggestions, improvements, or bug fixes, please create a pull request or open an issue.

## Contact

If you have any questions or feedback, feel free to reach out:

- **Email**: soulaimanettabaas@gmail.com
- **GitHub**: [putbullet](https://github.com/putbullet)

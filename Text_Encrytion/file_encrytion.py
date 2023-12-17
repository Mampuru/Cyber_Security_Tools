from cryptography.fernet import Fernet

# Function that generates an encryption key
def generate_key():
    return Fernet.generate_key()


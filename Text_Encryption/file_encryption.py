from cryptography.fernet import Fernet

# Function that generates an encryption key
def generate_key():
    return Fernet.generate_key()

# Function that will take a file and encrypt the contents of the file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(data)

    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

# Function that will decrypt the file content once correct key is supplied
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path[:-len('.encrypted')]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_pat

# Function to test the encrypt and decrpyt functions
if __name__ == "__main__":
    key = generate_key()

    # Encrypt a file
    file_to_encrypt = 'file_to_encrypt.txt'
    encrypted_file = encrypt_file(file_to_encrypt, key)
    print(f"File encrypted: {encrypted_file}")

    # Decrypt the encrypted file
    decrypted_file = decrypt_file(encrypted_file, key)
    print(f"File decrypted: {decrypted_file}")
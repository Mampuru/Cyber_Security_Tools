from cryptography.fernet import Fernet
from PIL import Image
import io

# function that generates an encryption key
def generate_key():
    return Fernet.generate_key()

# function that takes an image and encrypts its
def encrypt_image(image_path, key):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(image_data)

    encrypted_image = Image.open(io.BytesIO(encrypted_data))
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.' + image_path.split('.')[-1]
    encrypted_image.save(encrypted_image_path)

    return encrypted_image_path

# function that takes an image and decrypts it 
def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_image_data = encrypted_image_file.read()

    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_image_data)

    original_format = encrypted_image_path.split('.')[-1]
    decrypted_image = Image.open(io.BytesIO(decrypted_data))
    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.' + original_format
    decrypted_image.save(decrypted_image_path)

    return decrypted_image_path
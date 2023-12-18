from cryptography.fernet import Fernet
from PIL import Image
import io

# function that generates an encryption key
def generate_key():
    return Fernet.generate_key()


# Use the zipfile library to work with zip files and itertools for generating combinations.
import zipfile
import itertools

zip_file = "path/to/your/zipfile.zip"

def crack_zip(zip_file):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?,./;:'\"[]{}\\|`~"
    max_length = 8  # Maximum password length to attempt

    zip_file = zipfile.ZipFile(zip_file)

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"Password found: {password}")
                return password
            except Exception as e:
                continue

    print("Password not found.")
    return None

crack_zip(zip_file)

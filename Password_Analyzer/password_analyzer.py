def analyze_password(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(not char.isalnum() for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if uppercase:
        strength += 1
    if lowercase:
        strength += 1
    if digit:
        strength += 1
    if special_char:
        strength += 1

    return {
        "Length": length,
        "Uppercase": uppercase,
        "Lowercase": lowercase,
        "Digit": digit,
        "Special Character": special_char,
        "Strength": strength
    }

# Example usage
if __name__ == "__main__":
    password_to_analyze = input("Enter a password to analyze: ")
    analysis_result = analyze_password(password_to_analyze)

    print("\nPassword Analysis:")
    for key, value in analysis_result.items():
        print(f"{key}: {value}")
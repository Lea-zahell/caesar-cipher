"""
Caesar Cipher - A simple encryption/decryption tool
Learn: strings, loops, functions, modulo operator, ASCII values
"""

def encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher
    
    Args:
        text (str): The message to encrypt
        shift (int): How many positions to shift each letter (1-25)
    
    Returns:
        str: The encrypted message
    """
    result = ""
    
    # Loop through each character in the text
    for char in text:
        # Check if it's an uppercase letter
        if char.isupper():
            # Shift it and wrap around using modulo (%)
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        
        # Check if it's a lowercase letter
        elif char.islower():
            # Same logic but for lowercase
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        
        # If it's not a letter (space, number, punctuation), keep it as is
        else:
            result += char
    
    return result


def decrypt(text, shift):
    """
    Decrypts Caesar Cipher text
    
    Args:
        text (str): The encrypted message
        shift (int): The shift value used to encrypt
    
    Returns:
        str: The decrypted message
    """
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)


def main():
    """
    Main program - interactive menu
    """
    print("=" * 50)
    print("CAESAR CIPHER TOOL")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        if choice == "1":
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    encrypted = encrypt(message, shift)
                    print(f"\nOriginal:  {message}")
                    print(f"Encrypted: {encrypted}")
                    print(f"Shift:     {shift}")
                else:
                    print("Shift value must be between 1 and 25!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value used to encrypt (1-25): "))
                if 1 <= shift <= 25:
                    decrypted = decrypt(message, shift)
                    print(f"\nEncrypted: {message}")
                    print(f"Decrypted: {decrypted}")
                    print(f"Shift:     {shift}")
                else:
                    print("Shift value must be between 1 and 25!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "3":
            print("\nGoodbye! Happy coding! 🔐")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# This runs the program when you execute the file
if __name__ == "__main__":
    main()

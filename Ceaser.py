def caesar_cipher(text, shift, mode):
    """
    Encrypt or decrypt a text using the Caesar cipher algorithm.

    :param text: The input text to encrypt or decrypt.
    :param shift: The shift value for the cipher.
    :param mode: 'encrypt' to encrypt or 'decrypt' to decrypt the text.
    :return: The resulting text after encryption or decryption.
    """
    result = ""

    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift

    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around using modulo
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result


def save_to_file(output):
    """
    Save the result/output to a text file.

    :param output: The text to save into the file.
    """
    filename = "caesar_cipher_output.txt"
    with open(filename, "w") as file:
        file.write(output)
    print(f"Result has been saved to {filename}")


# Main program
if __name__ == "__main__":
    print("Caesar Cipher Program")
    print("Options:")
    print("1. Encrypt")
    print("2. Decrypt")
    mode_input = input("Choose an option (1/2 or 'encrypt'/'decrypt'): ").strip().lower()

    # Determine the mode based on input
    if mode_input == "1" or mode_input == "encrypt":
        mode = "encrypt"
    elif mode_input == "2" or mode_input == "decrypt":
        mode = "decrypt"
    else:
        print("Invalid option. Please enter '1', '2', 'encrypt', or 'decrypt'.")
        exit()

    message = input("Enter your message: ")
    try:
        shift_value = int(input("Enter the shift value (integer): "))
        result = caesar_cipher(message, shift_value, mode)
        print(f"Result: {result}")
        save_to_file(result)
    except ValueError:
        print("Invalid shift value. Please enter an integer.")

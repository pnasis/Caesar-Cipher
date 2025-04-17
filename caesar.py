def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_bruteforce(text):
    print("\nBrute-force results (trying all possible shifts):")
    for shift in range(1, 26):  # Skip shift=0 as it's the same as original
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")

def main():
    print("Caesar Cipher Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid option.")
        return

    text = input("Enter the text: ")
    shift_input = input("Enter the shift value (integer or 'n' to brute-force): ")

    if choice == '1':
        try:
            shift = int(shift_input)
            encrypted = caesar_encrypt(text, shift)
            print("Encrypted text:", encrypted)
        except ValueError:
            print("Encryption requires an integer shift.")
    else:  # Decrypt
        if shift_input.lower() == 'n':
            caesar_bruteforce(text)
        else:
            try:
                shift = int(shift_input)
                decrypted = caesar_decrypt(text, shift)
                print("Decrypted text:", decrypted)
            except ValueError:
                print("Decryption requires an integer shift or 'n' to brute-force.")

if __name__ == "__main__":
    main()

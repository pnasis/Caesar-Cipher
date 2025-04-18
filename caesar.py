from pyfiglet import Figlet

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
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")

def main():
    try:
        print(Figlet(font='slant').renderText("Caesar Cipher"))
        print("Created by: pnasis\nVersion: v1.0\n")
        choice = input("Choose an option (1(Encrypt) or 2(Decrypt)): ")

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
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()

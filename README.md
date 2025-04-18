# Caesar Cipher Tool

A simple Python program that implements the **Caesar Cipher** for both **encryption** and **decryption**. It also includes a **brute-force mode** to automatically try all possible keys when the shift is unknown.

## Features

- Encrypt text using a given shift.
- Decrypt text using a known shift.
- Brute-force decryption if the shift is unknown.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters are preserved.

## How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage

### Run the Program

```bash
python3 caesar_cipher.py
```

## Options

1. **Encrypt** - Provide a shift value (e.g., 3) to encrypt your message.

2. **Decrypt** - Provide a known shift value or enter n to try all possible shifts (brute-force).

## Example
```bash
   ______                              _______       __             
  / ____/___ ____  _________ ______   / ____(_)___  / /_  ___  _____
 / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ /  __(__  ) /_/ / /     / /___/ / /_/ / / / /  __/ /    
\____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/     
                                          /_/                       

Created by: pnasis
Version: v1.0

Choose an option (1(Encrypt) or 2(Decrypt)):
Enter the text: Wklv lv d whvw phvvdjh
Enter the shift value (integer or 'n' to brute-force): n

Brute-force results (trying all possible shifts):
Shift  1: Vjku ku c sguu ogrrzcig
Shift  2: Uijt jt b rftt nqqybxhf
...
Shift  3: This is a test message
...
```

## Requirements

- Python 3.x
- pyfiglet

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

# encryptor.py -- handles Vigenère cipher ENCRYPT/DECRYPT via stdin/stdout. To be implemented.
import sys

key = None

def vigenere(text, password, encrypt=True):
    text = text.upper()
    password = password.upper()
    res = []
    for i, char in enumerate(text):
        if not char.isalpha():
            res.append(char)
            continue
        p = ord(password[i % len(password)]) - ord('A')
        t = ord(char) - ord('A')
        if encrypt:
            res.append(chr((t + p) % 26 + ord('A')))
        else:
            res.append(chr((t - p + 26) % 26 + ord('A')))
    return ''.join(res)

while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    if line.upper() == "QUIT":
        break
    cmd, *args = line.split(" ", 1)
    arg = args[0] if args else ""
    if cmd.upper() == "PASS":
        key = arg.strip()
        print("RESULT Password set")
        sys.stdout.flush()
    elif cmd.upper() == "ENCRYPT":
        if key is None:
            print("ERROR Password not set")
        elif not arg.isalpha():
            print("ERROR Only letters allowed")
        else:
            print(f"RESULT {vigenere(arg, key, True)}")
        sys.stdout.flush()
    elif cmd.upper() == "DECRYPT":
        if key is None:
            print("ERROR Password not set")
        elif not arg.isalpha():
            print("ERROR Only letters allowed")
        else:
            print(f"RESULT {vigenere(arg, key, False)}")
        sys.stdout.flush()
    else:
        print("ERROR Invalid command")
        sys.stdout.flush()

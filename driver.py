# driver.py -- runs logger & encryptor as subprocesses, user menu. To be implemented.
import sys
import subprocess

def print_menu():
    print("\nChoose an action:")
    print("1. password (set password)")
    print("2. encrypt")
    print("3. decrypt")
    print("4. history")
    print("5. quit")

def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py logfile")
        sys.exit(1)
    logfile = sys.argv[1]
    logger = subprocess.Popen([sys.executable, "logger.py", logfile], stdin=subprocess.PIPE, text=True)
    encryptor = subprocess.Popen([sys.executable, "encryptor.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    history = []
    logger.stdin.write("START Driver Started.\n")
    logger.stdin.flush()
    password_set = False
    while True:
        print_menu()
        choice = input("Select action: ").strip().lower()
        if choice == "1" or choice == "password":
            val = input("Enter a password (letters only): ").strip()
            if not val.isalpha():
                print("ERROR: Only letters allowed.")
                continue
            encryptor.stdin.write(f"PASS {val}\n")
            encryptor.stdin.flush()
            res = encryptor.stdout.readline().strip()
            print(res)
            logger.stdin.write("PASSWORD Password set.\n")
            logger.stdin.flush()
            password_set = True
        elif choice == "2" or choice == "encrypt":
            val = input("Enter string to encrypt (letters only): ").strip()
            if not val.isalpha():
                print("ERROR: Only letters allowed.")
                continue
            history.append(val)
            encryptor.stdin.write(f"ENCRYPT {val}\n")
            encryptor.stdin.flush()
            res = encryptor.stdout.readline().strip()
            print(res)
            logger.stdin.write(f"ENCRYPTED {val} => {res}\n")
            logger.stdin.flush()
            history.append(res.split(" ", 1)[-1])
        elif choice == "3" or choice == "decrypt":
            val = input("Enter string to decrypt (letters only): ").strip()
            if not val.isalpha():
                print("ERROR: Only letters allowed.")
                continue
            history.append(val)
            encryptor.stdin.write(f"DECRYPT {val}\n")
            encryptor.stdin.flush()
            res = encryptor.stdout.readline().strip()
            print(res)
            logger.stdin.write(f"DECRYPTED {val} => {res}\n")
            logger.stdin.flush()
            history.append(res.split(" ", 1)[-1])
        elif choice == "4" or choice == "history":
            print("History of this session:")
            for i, item in enumerate(history):
                print(f"{i+1}: {item}")
            logger.stdin.write("HISTORY Viewed.\n")
            logger.stdin.flush()
        elif choice == "5" or choice == "quit":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            encryptor.wait()
            logger.wait()
            print("Exiting.")
            break
        else:
            print("Invalid option. Enter 1-5 or their names.")
    sys.exit(0)

if __name__ == "__main__":
    main()

from curses.ascii import isalpha
import sys
from sys import argv

def encrypt(f, key):
    """Encrypts the contents of the file object (assumed to be ASCII text)"""
    while True:
        c = f.read(1)
        if not c: break     # legal syntax, useful for this situation

        if c.isalpha():
            c = c.lower()
            c = ord(c)
            c -= ord('a')
            c += key
            c %= 26
            c += ord('a')
            c = chr(c)
        print(c,end="")

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python3 encrypt.py key input_file_name")
        sys.exit(1)

    key = 0
    try:
        key = int(argv[1])
        if (key == 0):
            raise ValueError("invalid key: "+argv[1])
    except:
        print("Invalid key: Must be a non-zero integer")
        sys.exit(1)
    
    with open(argv[2]) as f:
        encrypt(f, key)

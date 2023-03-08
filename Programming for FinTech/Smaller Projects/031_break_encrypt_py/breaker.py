import sys
from sys import argv
import os

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def CountFrequency(myList):
    freq = {}
    for item in myList:
        if item in LETTERS.lower() or item in LETTERS:
            if (item in freq):
                freq[item.lower()] += 1
            else:
                freq[item.lower()] = 1

    if len(freq) == 0:
        sys.exit(1)
    
    test_val = list(freq.values())[0]
    result = True
    for s in freq:
        if freq[s] != test_val:
            result = False
            break

    if result:
        sys.exit(1)
    else:
        caesar_cipher(freq)


def caesar_cipher(freq):
    fin_max = max(freq, key=freq.get)
    letterE = ord('e')
    fin_max = ord(fin_max)
    
    if(abs(fin_max - letterE) == 1 and fin_max == 100):
        print(25)
    else:
        print(abs(fin_max - letterE), end="")
    
    
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 breaker.py input_file_name")
        sys.exit(1)

            
    key = 0
    try:
        if os.stat(argv[1]).st_size == 0:
            print("File is empty")
            sys.exit(1)
            
        key = argv[1]
        if (key == 0):
            raise ValueError("invalid key: " + argv[1])
    except:
        print("Error: Input correct name")
        sys.exit(1)
        

    with open(argv[1]) as f:
        lines = f.read()
        CountFrequency(lines)
import os
import string
import random
from tqdm import tqdm
import sys
from difflib import SequenceMatcher
import vuhash

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    a = 0
    rn = 100000
    for i in tqdm(range(1000000)):
        if len(sys.argv) > 1:
            rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst, sys.argv[1]))
            rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst, sys.argv[1]))
        else:
            rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst).read())
            rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst).read())
        if similar(st1, st2) == 1:
            print("collision")
        a += similar(st1, st2)
    print(a / 100)

if __name__ == "__main__":
    main()

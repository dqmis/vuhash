import os
import string
import random
from difflib import SequenceMatcher
from tqdm import tqdm
import vuhash

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    a = 0
    rn = 100000
    for i in tqdm(range(1000000)):
        rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
        st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst).read())
        rs = list(rst)
        c = rst
        rs[random.randint(0, rn - 1)] = ' '
        rst = ''.join(rs)
        st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(rst).read())
        if similar(st1, st2) == 1:
            print(similar(c, rst))
            print("collision")
        a += similar(st1, st2)
    print(a / 100)

if __name__ == "__main__":
    main()

import os
import string
import random
from tqdm import tqdm
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    a = 0
    rn = 1000
    for i in tqdm(range(1000000)):
        rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
        st1 = ''.join(format(ord(x), 'b') for x in os.popen("./vuhash {}".format(rst)).read())
        rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
        st2 = ''.join(format(ord(x), 'b') for x in os.popen("./vuhash {}".format(rst)).read())
        if similar(st1, st2) == 1:
            print("colission")
        a += similar(st1, st2)
    print(a / 100)

if __name__ == "__main__":
    main()

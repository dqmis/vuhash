import os
import string
import random
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    a = 0
    rn = 1000
    for i in range(0, rn):
        rst = ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))
        st1 = ''.join(format(ord(x), 'b') for x in os.popen("./vuhash {}".format(rst)).read())
        rs = list(rst)
        rs[random.randint(0, rn - 1)] = ' '
        rst = ''.join(rs)
        st2 = ''.join(format(ord(x), 'b') for x in os.popen("./vuhash {}".format(rst)).read())
        if similar(st1, st2) == 1:
            print("colission")
        a += similar(st1, st2)
    print(a / 100)

if __name__ == "__main__":
    main()

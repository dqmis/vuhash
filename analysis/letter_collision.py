import sys
import string
import random
from difflib import SequenceMatcher
from tqdm import tqdm
import vuhash

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_word(rn):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))

def main():
    similar_avg = 0
    rn = 100000
    for i in tqdm(range(1000000)):
        if len(sys.argv) > 1:
            w_ = get_word(rn)
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn), sys.argv[1]))
            rs = list(w_)
            rs[random.randint(0, rn - 1)] = ' '
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(''.join(rs), sys.argv[1]))
        else:
            w_ = get_word(rn)
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn)))
            rs = list(w_)
            rs[random.randint(0, rn - 1)] = ' '
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(''.join(rs)))
        if similar(st1, st2) == 1:
            print("collision")
        similar_avg += similar(st1, st2)
    print(similar_avg / 1000000)

if __name__ == "__main__":
    main()

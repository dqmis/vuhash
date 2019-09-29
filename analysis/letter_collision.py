import sys
import string
import random
from difflib import SequenceMatcher
from tqdm import tqdm
import vuhash
from time import time

random.seed(42)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_word(rn):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))

def main():
    similar_avg = 0
    rn = 5
    coll_ = 0
    all_start = time()
    for i in tqdm(range(100000)):
        if len(sys.argv) > 1:
            w_ = get_word(rn)
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(w_, sys.argv[1]))
            rs = list(w_)
            rs[random.randint(0, rn - 1)] = ' '
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(''.join(rs), sys.argv[1]))
        else:
            w_ = get_word(rn)
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(w_))
            rs = list(w_)
            rs[random.randint(0, rn - 1)] = ' '
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(''.join(rs)))
        if similar(st1, st2) == 1:
            coll_ += 1
        similar_avg += similar(st1, st2)
    print('It took: {}'.format(all_start - time()))
    print(similar_avg / 100000)
    print('Found {} collisions'.format(coll_))

if __name__ == "__main__":
    main()

import string
import random
from tqdm import tqdm
import sys
from difflib import SequenceMatcher
import vuhash

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_word(rn):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=rn))

def main():
    similar_avg = 0
    rn = 10000
    for i in tqdm(range(100000)):
        if len(sys.argv) > 1:
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn), sys.argv[1]))
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn), sys.argv[1]))
        else:
            st1 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn)))
            st2 = ''.join(format(ord(x), 'b') for x in vuhash.hash(get_word(rn)))
        if similar(st1, st2) == 1:
            print("collision")
        similar_avg += similar(st1, st2)
    print(similar_avg / 100000)

if __name__ == "__main__":
    main()

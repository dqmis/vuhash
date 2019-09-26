import os
import string
from time import time
from tqdm import tqdm
from difflib import SequenceMatcher
from hashlib import sha256
import vuhash
import sys

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    all_time = 0
    with open("./konstitucija.txt") as fp:
        cnt = 0
        for line in fp:
            start = time()
            if len(sys.argv) > 1:
                hash_ = vuhash.hash(line.strip(), sys.argv[1])
            else:
                hash_ = vuhash.hash(line.strip())
            all_time += (time() - start)
            cnt += 1

    print("Average hashing time: {}".format(all_time / cnt))


if __name__ == "__main__":
    main()

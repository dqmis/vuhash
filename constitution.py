import os
import string
from time import time
from tqdm import tqdm
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    all_time = 0
    with open("./konstitucija.txt") as fp:
        cnt = 0
        for line in fp:
            start = time()
            hash_ = os.popen('./vuhash "{}"'.format(line.strip()))
            cnt += 1
            all_time += (time() - start)

    print("Average hashing time: {}".format(all_time / cnt))


if __name__ == "__main__":
    main()

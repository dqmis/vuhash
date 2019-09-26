# VU ISI Blockchain hashing function

This is a repository for VU ISI Blockchain course's [hashing function's](https://github.com/blockchain-group/Blockchain-technologijos/blob/master/pratybos/1uzduotis-Hashavimas.md) sollution.

![](https://media.giphy.com/media/eCqFYAVjjDksg/giphy.gif)

### Introduction
My hasing function is completed in multiple steps:
* Initializing 16 32bit size key vectors.
* Converting string or file content parsed to string to ascii.
* Converting ascii to binary vector.
* Padding vector so that its size would be divisible by 512.
* Shuffling bits so that beggining of binary array would affect the ending of it and vice versa.
* Making `XOR` operations on keys initialized int the beggining.
* Converting binary string to hex.

### Analysis
I am analysing my hash with `python3`. I believe that it is a really easy way to combine performace of C++ and versatility of Python. You can find out more about them in the file structure definition below.

### File structure
* `HASH/` - place where C++ hashing function code is held.
* `analysis/`:
    * `vuhash.py` - hasing function parser. It uses my vuhash or sha256.
    * `constitution.py` - file where performace of hasing every line of Lithuania's constitution is made.
    * `letter_collision.py` - file where collision analysis when changing one letter in random string is made.
    * `word_collision.py` - file where collision analysis between two radom string pairs is made. 

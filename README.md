# VU ISI Blockchain hashing function

This is a repository for VU ISI Blockchain course's [hashing function's](https://github.com/blockchain-group/Blockchain-technologijos/blob/master/pratybos/1uzduotis-Hashavimas.md) sollution.

![](https://media.giphy.com/media/eCqFYAVjjDksg/giphy.gif)

### Introduction
My hasing function is completed in multiple steps:
* Initializing 16 `32bit` size key vectors.
* Converting string or file content parsed to string to ascii.
* Converting ascii to binary vector.
* Padding vector so that its size would be divisible by 512.
* Shuffling bits so that beggining of binary array would affect the ending of it and vice versa.
* Making `XOR` operations on keys initialized int the beggining.
* Converting binary string to hex.

### Analysis
I am analysing my hash with `python3`. I believe that it is a really easy way to combine performace of C++ and versatility of Python. You can find out more about them in the file structure definition below.

### Analysis results
#### Constitution
* Average time to hash a line: `0.0051`s.
* Time to hash file line by line: `4.11`s.
#### Word collision
* Time it took: `18`min.
* Average similarity score: `0.0055`
* Found `0` collisions
#### Letter collision
* Time it took: `19`min.
* Average similarity score: `0.0054`
* Found `0` collisions
### My hashing algorithm vs `SHA256`
I made every test with my algorithm and `sha256`. Below are the results of `sha256`:
#### Constitution
* Average time to hash a line: `2.24e-06`s.
* Time to hash file line by line: `0.002`s.
#### Word collision
* Time it took: `55`s.
* Average similarity score: `0.0095`
* Found `0` collisions
#### Letter collision
* Time it took: `57`s.
* Average similarity score: `0.0096`
* Found `0` collisions

You can see that `sha256` is about 22 times faster than mine algorithm when hasing short strings. When hashing strings that are as long as 100000 chars the results are different:

* Letter collision test gives `41`it/s and mine algorithms gives `3.1`it/s. That is a `13x` difference.

### File structure
* `HASH/` - place where C++ hashing function code is held.
* `analysis/`:
    * `vuhash.py` - hasing function parser. It uses my vuhash or sha256.
    * `constitution.py` - file where performace of hasing every line of Lithuania's constitution is made.
    * `letter_collision.py` - file where collision analysis when changing one letter in random string is made.
    * `word_collision.py` - file where collision analysis between two radom string pairs is made. 

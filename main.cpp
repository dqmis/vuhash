#include <iostream>
#include "./HASH/HASH.h"

int main(int argc, char** argv) {
    HASH hash_(42);
    hash_.hash(argv[1]);

    return 0;
}
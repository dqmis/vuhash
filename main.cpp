#include <iostream>
#include "./HASH/HASH.h"

int main() {
    std::string st;
    std::cin >> st;

    HASH hash_(2);

    hash_.hash(st);
    return 0;
}
#include <iostream>
#include <string>
#include <fstream>
#include "./HASH/HASH.h"

int main(int argc, char** argv) {
    std::ifstream t(argv[1]);
    if (!t.fail()) {
        std::string str((std::istreambuf_iterator<char>(t)),(std::istreambuf_iterator<char>()));
        std::cout << vuhash(str) << std::endl;
    } else std::cout << vuhash(argv[1]) << std::endl;

    return 0;
}
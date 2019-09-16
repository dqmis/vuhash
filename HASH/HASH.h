//
// Created by Dominykas  on 14/09/2019.
//

#ifndef VUHASH_HASH_H
#define VUHASH_HASH_H

#include <string>
#include <vector>
#include <cmath>
#include <bitset>
#include <iostream>

class HASH {
private:
    int mul_const;

    std::vector<int> binary;
    std::vector<int> ascii;
    void to_ascii(std::string sat);
    void to_binary();
    void padding(std::vector<int>& bin);
    int encoded_sum();

    std::vector<int> has
public:
    HASH(int mul_const_ = 42) {
        mul_const = mul_const_;
    }
    int hash(const std::string st) {
        to_ascii(st);
        to_binary();
        padding(binary);
        for(int& a: binary) {
            std::cout << a;
        }
        return encoded_sum();
    }
};

#endif //VUHASH_HASH_H

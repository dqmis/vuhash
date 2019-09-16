//
// Created by Dominykas  on 14/09/2019.
//

#include "HASH.h"

void HASH::to_ascii(std::string st) {
    for(char& c : st)
        ascii.push_back(int(c));
}

void HASH::to_binary() {
    std::string bin;
    for(int& i: ascii) {
        bin = std::bitset<8>(i).to_string();
        for(char& c: bin)
            binary.push_back(int(c) - 48);
    }
};

void HASH::padding(std::vector<int>& bin) {
    std::string binary_val = std::bitset<8>(bin.size()).to_string();
    std::vector<int> len_bin(64 - binary_val.length(), 0);
    for(char& c: binary_val)
        len_bin.push_back(int(c) - 48);

    bin.push_back(1);
    while(bin.size() != 448)
        bin.push_back(0);

    bin.insert(bin.end(), len_bin.begin(), len_bin.end());
}

int HASH::encoded_sum() {
    int enc_sum = 0;
    for(int i = 0; i < ascii.size(); i++)
       enc_sum += pow(mul_const, i) * ascii[i];
    return  enc_sum;
}

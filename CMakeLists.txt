cmake_minimum_required(VERSION 3.14)
project(vuhash)

set(CMAKE_CXX_STANDARD 17)

add_executable(vuhash main.cpp HASH/HASH.cpp HASH/HASH.h)


#include <cstdio>
//#include <cerr>
#include <cmath>
#include <cstring>

#include <string>
#include <iostream>
#include <algorithm>
#include <random>

#define MAXLEN 300000
#define MINLEN 10
// Solve the minimum number of coins that adds up to x

const int INF = 987654321;
int length[MAXLEN] = {0,};

void
count_longest
(const int array[], const int len)
{
    for (int k=0; k<len; ++k) {
        length[k] = 1;
        for (int i=0; i<k; ++i) {
            if (array[i] < array[k]) {
                length[k] = std::max(length[k], length[i]+1);
            }
        }
    }
}


int arr[MAXLEN];
int 
main
(int argc, char* argv[]) 
{
    if (argc != 2) {
        fprintf(stderr, "usage: %s <target number[int < %d]>\n", argv[0], MAXLEN);
        exit(EXIT_FAILURE);
    }
    int target = std::stoi(argv[1]);
    if (target >= MAXLEN || target < MINLEN) {
        fprintf(stderr, "target should be smaller than %d\n", MAXLEN);
        exit(EXIT_FAILURE);
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis_value(0, MAXLEN); 

    for (int i=0; i<target; ++i) {
        arr[i] = dis_value(gen);
    }
    count_longest(arr, target);
    int* max_pos = std::max_element(length, length+target);
    long int max_index = max_pos - length;
    printf("The longest ends at %ld with %d length\n", max_index, *max_pos);

    std::cout << " * Array : ";
    for (int i=0; i<target; ++i) {
        std::cout << arr[i] << ", ";
    }
    std::cout << std::endl;

    std::cout << " * Maximal Array : ";
    for (int i=max_index - *max_pos; i<=max_index; ++i) {
        std::cout << arr[i] << ", ";
    }
    std::cout << std::endl;

    return 0;
}

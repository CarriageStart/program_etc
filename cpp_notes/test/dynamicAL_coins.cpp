
#include <cstdio>
//#include <cerr>
#include <cmath>
#include <cstring>

#include <string>
#include <iostream>

#define MAXLEN 300000
#define MODULAR 10e9+7
// Solve the minimum number of coins that adds up to x

const int coins[3] = {11, 7, 5};
const int INF = 987654321;

char first_selection[MAXLEN] = {0,};
int 
naive_solve
(int target) 
{
    if (target < 0) return INF;
    if (target == 0) return 0;
    int best = INF;
    for (auto c: coins) {
        int trial = naive_solve(target-c);
        if (best > trial + 1) {
            best = trial;
            first_selection[target] = c;
        }
    }
    return best;
}


bool sheet_ready[MAXLEN] = {false,};
int sheet_answer[MAXLEN];

int
memoization_solve
(int target)
{
    if (target < 0) return INF;
    if (target == 0) return 0;
    if (sheet_ready[target]) return sheet_answer[target];

    int best = INF;
    for (auto c: coins) {
        if (best > memoization_solve(target-c) + 1) {
            best = sheet_answer[target-c] + 1;
            first_selection[target] = c;
        }
    }
    sheet_ready[target] = true;
    sheet_answer[target] = best;
    return best;
}


int op_sheet_answer[MAXLEN] = {-1,};
int
optimized_solve
(int target)
{
    if (op_sheet_answer[target] >= 0) 
        return op_sheet_answer[target];
    
    for (int x=1; x<=target; ++x) {
        if (op_sheet_answer[x] >= 0) continue;
        op_sheet_answer[x] = INF;
        for (auto c: coins) {
            if (x-c >= 0 && op_sheet_answer[x] > op_sheet_answer[x-c]+1) {
                //op_sheet_answer[x] = std::min(op_sheet_answer[x], op_sheet_answer[x-c]+1);
                op_sheet_answer[x] = op_sheet_answer[x-c] + 1;
                first_selection[x] = c;
            }
        }
    }
    return op_sheet_answer[target];
}

int count[MAXLEN] = {0,};
int approx_count[MAXLEN] = {0,};
void
count_possibilities
(int target)
{
    count[0] = 1;
    approx_count[0] = count[0] % (int)MODULAR;
    for (int x=1; x<=target; ++x) {
        for (auto c: coins) {
            if (x-c >= 0) {
                count[x] += count[x-c];
                approx_count[x] = count[x] % (int)MODULAR;
            }
        }
    }
}


int 
main
(int argc, char* argv[]) 
{
    if (argc != 3) {
        fprintf(stderr, "usage: %s <target number[int < %d]> <option[int]>\n", argv[0], MAXLEN);
        fprintf(stderr, "option \n 1: naive recursion\n 2: with memoization\n 3: optimized memo\n");
        exit(EXIT_FAILURE);
    }
    int target = std::stoi(argv[1]);
    if (target >= MAXLEN) {
        fprintf(stderr, "target should be smaller than %d\n", MAXLEN);
        exit(EXIT_FAILURE);
    }
    count_possibilities(target);
    printf("All possible combinations : %d\n", count[target]);
    printf("    Approximately : (%d -7) * 10E7\n", approx_count[target]);
    int option = std::stoi(argv[2]);
    int answer = 0;
    switch (option) {
        case 1:
            answer = naive_solve(target);
            printf("Target : %d, Naive Answer : %d\n", target, answer);
            if (answer == INF) exit(EXIT_FAILURE);
            break;
        case 2:
            answer = memoization_solve(target);
            printf("Target : %d, Memo Answer : %d\n", target, answer);
            if (answer == INF) exit(EXIT_FAILURE);
            break;
        case 3:
            memset(op_sheet_answer, -1, sizeof(op_sheet_answer));
            op_sheet_answer[0] = 0;
            answer = optimized_solve(target);
            printf("Target : %d, Op Answer : %d\n", target, answer);
            if (answer == INF) exit(EXIT_FAILURE);
            break;
    }
    std::cout << "Section : ";
    while ( target >0 ) {
        std::cout << (int)first_selection[target] << ", ";
        target -= (int)first_selection[target];
    }
    std::cout << std::endl;
    return 0;
}



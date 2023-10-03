
#include <string>
#include <cerr>

// Solve the minimum number of coins that adds up to x

int coins[3] = {1, 3, 4};

int 
naive_solve
(int target) 
{
    if (x < 0) return INF;
    if (x == 0) return 0;

    int best = INF;
    for (auto c : coins) {
        best = min(best, solve(x-c) + 1);
    }
    return best;
}

int 
main
(int argc, char* argv[]) 
{
    if (argc != 2) {
        fprintf(stderr, "usage: %s <target number[int]>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    int target = stoi(argv[1]);

    int naive_sol = naive_solve(target);
}



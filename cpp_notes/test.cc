
#include <cstdio>
#include <string>
#include <cmath>

const int INF = 987654321;

int 
min
(int x, int y) 
{
    if (x <= y) return x;
    else return y;
}

int 
solve
(int target) 
{
    if (target < 0) return INF;
    if (target == 0) return 0;
    int best = INF;
    int coins[] = {1, 3, 4};
    for (auto c: coins) {
        best = min(best, solve(best - c) + 1);
    }
    printf("Current Best : %d\n", best);
    return best;
}

int 
main
(int argc, char* argv[]) 
{
    //if (argc != 2 ) fprintf(stderr, "Please enter the number\n");
    //int target = std::stoi(argv[1]);
    int target = 10;
    int answer = solve(target);
    printf("Target : %d, Answer : %d\n", target, answer);
    return 0;
}



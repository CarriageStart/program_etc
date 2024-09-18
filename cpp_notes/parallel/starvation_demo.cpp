
#include <cstdio>
#include <thread>
#include <mutex>

int sushi_count = 5000;

void philosopher(std::mutex &chostick) {
    int sushi_eaten = 0;
    while (sushi_count > 0) {
        std::scoped_lock lock(chostick);    // Use RAII to prevent running out
        if (sushi_count) {
            --sushi_count;
            ++sushi_eaten;
        }
    }
    printf(" Philosopher %u are %d.\n", std::this_thread::get_id(), sushi_eaten);
}

// Set chostic_a > chopstick_b (Lock Ordering)
int main() {
    std::mutex chopstick;
    std::array<std::thread, 300> philosophers;
    for (int i=0; i<philosophers.size(); ++i) {
        philosophers[i] = std::thread(philosopher, std::ref(chopstick));
    }
    for (int i=0; i<philosophers.size(); ++i) {
        philosophers[i].join();
    }
    printf("Two philosophers are done eating.\n");
    return 0;
}




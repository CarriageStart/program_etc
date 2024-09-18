
#include <cstdio>
#include <thread>
#include <mutex>

int sushi_count = 5000;

void bad_philosopher(std::mutex &chostick) {
    while (sushi_count > 0) {
        chostick.lock();
        if (sushi_count) {
            sushi_count--;
        }
        if (sushi_count == 10) {
            printf("This philosopher has had enough!\n");
            break;  // Some thread can escape without unlocking
        }
        chostick.unlock();
    }
}

void philosopher(std::mutex &chostick) {
    while (sushi_count > 0) {
        std::scoped_lock lock(chostick);    // Use RAII to prevent running out
        if (sushi_count) {
            sushi_count--;
        }
        if (sushi_count == 10) {
            printf("This philosopher has had enough!\n");
            break;  
        }
    }
}

// Set chostic_a > chopstick_b (Lock Ordering)
int main() {
    std::mutex chopstick;
    std::thread barron(philosopher, std::ref(chopstick));
    std::thread olivia(philosopher, std::ref(chopstick));
    barron.join();
    olivia.join();
    printf("Two philosophers are done eating.\n");
    return 0;
}


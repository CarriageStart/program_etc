
#include <cstdio>
#include <thread>
#include <mutex>

int sushi_count = 5000;

void philosopher(std::mutex &first_chopstick, std::mutex &second_chopstick) {
    while (sushi_count > 0) {
        first_chopstick.lock();
        second_chopstick.lock();
        if (sushi_count) {
            sushi_count--;
        }
        second_chopstick.unlock();
        first_chopstick.unlock();
    }
}

// Set chostic_a > chopstick_b (Lock Ordering)
int main() {
    std::mutex chopstick_a, chopstick_b;
    std::thread barron(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    //std::thread olivia(philosopher, std::ref(chopstick_b), std::ref(chopstick_a)); == Doesn't keep the priority
    std::thread olivia(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    barron.join();
    olivia.join();
    printf("Two philosophers are done eating.\n");
    return 0;
}



#include <cstdio>
#include <thread>
#include <mutex>

int sushi_count = 5000;

void philosopher(std::mutex &first_chopstick, std::mutex &second_chopstick) {
    while (sushi_count > 0) {
        first_chopstick.lock();
        if (!second_chopstick.try_lock()) {
            first_chopstick.unlock(); // Yield to other threads. but it is too fast
            std::this_thread::yield(); // Put this thread as "busy sleep" so that os schedule this behind of others.
        } else {
            if (sushi_count) {
                sushi_count--;
            }
            second_chopstick.unlock();
            first_chopstick.unlock();
        }
    }
}

// Set chostic_a > chopstick_b (Lock Ordering)
int main() {
    std::mutex chopstick_a, chopstick_b;
    std::thread barron(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread olivia(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve2(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki2(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve3(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki3(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve4(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki4(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve5(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki5(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve6(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki6(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve7(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki7(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve8(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki8(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    std::thread steve9(philosopher, std::ref(chopstick_a), std::ref(chopstick_b));
    std::thread nikki9(philosopher, std::ref(chopstick_b), std::ref(chopstick_a));
    barron.join();
    olivia.join();
    steve.join();
    nikki.join();
    steve2.join();
    nikki2.join();
    steve3.join();
    nikki3.join();
    steve4.join();
    nikki4.join();
    steve5.join();
    nikki5.join();
    steve6.join();
    nikki6.join();
    steve7.join();
    nikki7.join();
    steve8.join();
    nikki8.join();
    steve9.join();
    nikki9.join();
    printf("Two philosophers are done eating.\n");
    return 0;
}


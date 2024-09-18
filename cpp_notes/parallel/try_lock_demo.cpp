

#include <cstdio>
#include <thread>
#include <mutex>
#include <chrono>

unsigned int items_on_notepad = 0;
std::mutex pencil;

void shopper(const char* name) {
    int items_to_add = 0;
    while (items_on_notepad <= 20) {
        if (items_to_add && pencil.try_lock()) { // try_lock should be calculated only when items_to_add != 0! Sequence is credential..
            items_on_notepad += items_to_add;
            printf("%s Added %u item(s) to notepad.\n", name, items_to_add);
            items_to_add = 0;
            std::this_thread::sleep_for(std::chrono::milliseconds(300));
            pencil.unlock();
        } else {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            items_to_add++;
            printf("%s found something else to buy\n", name);
        }
    }
}

int main() {
    auto start_time = std::chrono::steady_clock::now();
    std::thread barron(shopper, "Barron");
    std::thread olivia(shopper, "olivia");
    barron.join();
    olivia.join();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - start_time).count();
    printf("Elapsed Time : %.2f\n", elapsed_time/1000.0);
    return 0;
}



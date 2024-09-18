
#include <cstdio>
#include <thread>
#include <chrono>
auto pgm_time = std::chrono::steady_clock::now();

void kitchen_cleaner() {
    // Infinite loop
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - pgm_time).count();
    printf("Thread %u starts function at %.2f\n", std::this_thread::get_id(), elapsed_time/1000.);
    while (true) {
        printf("Olivia cleaned the kitchen\n");
        std::this_thread::sleep_for(std::chrono::seconds(100000)); // This thread is terminated waiting
    }
    elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - pgm_time).count();
    printf("Thread %u outs function at %.2f\n", std::this_thread::get_id(), elapsed_time/1000.);
}

int main() {
    std::thread olivia(kitchen_cleaner);
    std::thread steve(kitchen_cleaner);
    olivia.detach();        // Detach the infinite loop thread.
    for (int i=0; i<3; i++) {
        printf("Barron is cooking...\n");
        std::this_thread::sleep_for(std::chrono::milliseconds(600));
    }
    printf("Barron is done.\n");
    steve.join();
    //olivia.join();        // Detached thread is not joinable, anymore.
    // since detached threads are left, the progam will finish
    return 0;
}


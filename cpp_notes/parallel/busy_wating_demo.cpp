
#include <cstdio>
#include <thread>
#include <mutex>
#include <chrono>
#include <ctime>

unsigned int garlic_count = 0;
std::mutex mu_garlic_count;
auto pgm_time = std::chrono::steady_clock::now();

void shopper() {
    auto spot_time =  std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - pgm_time).count();
    printf("Thread %u checked the mutex status at %.2f\n", std::this_thread::get_id(), spot_time/1000.);
    mu_garlic_count.lock(); // Note busy-waiting occurs within the lock() function mutex.
    auto start_time = std::chrono::steady_clock::now();
    spot_time =  std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - pgm_time).count();
    printf("Thread %u possesed the mutex status at %.2f\n", std::this_thread::get_id(), spot_time/1000.);
    for (int i=0; i<10; ++i) {
        garlic_count += 1;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - start_time).count();
    printf("garlic count : %u\n time %.2f\n", garlic_count, elapsed_time/1000.);
    mu_garlic_count.unlock();
}

int main() {
    pgm_time = std::chrono::steady_clock::now();

    std::thread persons[10];
    for (int i=0 ;i<10; ++i) {
        persons[i] = std::thread(shopper);
    }
    for (int i=0 ;i<10; ++i) {
        persons[9-i].join();
    }
    return 0;
}



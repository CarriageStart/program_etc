
#include <cstdio>
#include <thread>
#include <mutex>
#include <chrono>

unsigned int garlic_count = 0;
unsigned int apple_count = 0;
unsigned int potato_count = 0;
std::mutex pencil;  // Mutex wrapper  
std::mutex pencil2;  // Mutex wrapper  
std::mutex pencil3;  // Mutex wrapper  

void shopper() {
    pencil.lock();  // When the 
    for (unsigned int i=0; i<10000000; ++i) {
        ++garlic_count;
    }
    pencil.unlock();
}

void slowshopper() {
    pencil2.lock();
    for (unsigned int i=0; i<5; ++i) {
        printf("Shopper %u is thinking...\n", std::this_thread::get_id());
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        ++apple_count;
    }
    pencil2.unlock();
}

void bettershopper() {
    for (unsigned int i=0; i<5; ++i) {
        printf("Shopper %u is thinking...\n", std::this_thread::get_id());
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        pencil3.lock();
        ++potato_count;
        pencil3.unlock();
    }
}


int main() {
    std::thread barron(shopper);
    std::thread olivia(shopper);

    barron.join();
    olivia.join();
    printf("We should buy %u garlics.\n", garlic_count);

    for (unsigned int i=0; i<5; ++i) {
        std::thread barron2(slowshopper);
        std::thread olivia2(slowshopper);

        barron2.join();
        olivia2.join();
    }

    printf("We should buy %u apples.\n", apple_count);

    for (unsigned int i=0; i<5; ++i) {
        std::thread barron2(bettershopper);
        std::thread olivia2(bettershopper);

        barron2.join();
        olivia2.join();
    }
    printf("We should buy %u potatos.\n", potato_count);
    return 0;
}


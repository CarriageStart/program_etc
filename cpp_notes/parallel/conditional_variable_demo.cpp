
#include <thread>
#include <mutex>

int soup_servings = 100;
std::mutex slow_cooker_lid;

void hungry_person(int id) {
    int put_lid_back = 0;
    while (soup_servings > 0) {
        std::unique_lock<std::mutex> lid_lock(slow_cooker_lid);
        if ((id == soup_servings % 2) && (soup_servings > 0)) { // Even processor is forced to skip
            --soup_servings;                                    //  => Simulation of the case the condition is not met
        } else {
            ++put_lid_back;
        }
    }
    printf( "Person %d put the lid back %u times.\n", id, put_lid_back);
}

int main() {
    std::thread hungry_threads[2];  // Initialized already...
    for (int i=0; i<2; ++i) {
        hungry_threads[i] = std::thread(hungry_person, i); // Why do you make another one and copy it?
    }
    for (auto& thread: hungry_threads) {
        thread.join();
    }
    return 0;
}





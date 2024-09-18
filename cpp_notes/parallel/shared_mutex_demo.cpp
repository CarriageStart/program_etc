
#include <cstdio>
#include <thread>
#include <shared_mutex>
//#include <mutex>
#include <chrono>

char WEEKDAYS[7][10] = {
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
};

int today = 0;
std::shared_mutex marker;

void calender_reader(const int id) {
    for (int i=0; i<7; ++i) {
        marker.lock_shared();
        printf("Reader %d sees today is %s\n", id, WEEKDAYS[today]);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        marker.unlock_shared();
    }
}
void calendar_writer(const int id) {
    for (int i=0; i<7; ++i) {
        marker.lock();
        today = ++today % 7;
        printf("Writer %d sees today is %s\n", id, WEEKDAYS[today]);
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        marker.unlock();
    }
}


int main() {
    std::array<std::thread, 10> readers;
    for (unsigned int i=0; i<readers.size(); ++i) {
        readers[i] = std::thread(calender_reader, i);
    }
    std::array<std::thread, 2> writers;
    for (unsigned int i=0; i<writers.size(); ++i) {
        writers[i] = std::thread(calendar_writer, i);
    }

    for (unsigned int i=0; i<readers.size(); ++i) {
        readers[i].join();
    }
    for (unsigned int i=0; i<writers.size(); ++i) {
        writers[i].join();
    }
    return 0;

}

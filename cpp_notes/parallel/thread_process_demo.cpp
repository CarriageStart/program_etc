
#include <cstdio>
#include <thread>
#include <chrono>
#include <unistd.h>

void cpu_waster() { 
    printf("CPU Waster Process ID: %u\n", getpid());
    printf("CPU Waster Thread  ID: %u\n", std::this_thread::get_id());
    while(true) continue;
}

int main() {
    printf("Main Process ID : %u\n", getpid());
    printf("Main Thread ID  : %u\n", std::this_thread::get_id());

    std::thread thread1(cpu_waster);
    std::thread thread2(cpu_waster);

    while(true) {
         std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    return 0;
}




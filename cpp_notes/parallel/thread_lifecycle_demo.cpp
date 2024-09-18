
#include <cstdio>
#include <thread>
#include <chrono>

void chef_olivia() {
    printf( "Olivia Started & Waiting for sausage to thaw....\n" );
    std::this_thread::sleep_for(std::chrono::seconds(3));
    printf("Olivia is done cutting sausage.\n");
}

int main() {
    printf("Barron requests Olivia's help.\n");
    std::thread olivia(chef_olivia);    // Wrapper class of 

    printf("  Olivia is joinable? %s\n", olivia.joinable() ? "true" : "false"); // True

    printf("Barron continues cooking soup.\n");
    std::this_thread::sleep_for(std::chrono::seconds(1));
    printf("  Olivia is joinable? %s\n", olivia.joinable() ? "true" : "false"); // True
    
    printf("Barron patiently waits for Olivia to finish and join...\n");
    printf("  Olivia is joinable? %s\n", olivia.joinable() ? "true" : "false"); // True
    // Since the main thread can't operate on the child thread, it ask for it to child thread wrapper.
    if (olivia.joinable())
        olivia.join();  
    printf("  Olivia is joinable? %s\n", olivia.joinable() ? "true" : "false"); // False

    printf("Barron and Olivia are both done!\n");
    return 0;
}


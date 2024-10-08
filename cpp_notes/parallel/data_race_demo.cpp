
#include <cstdio>
#include <thread>

unsigned int garlic_count = 0;

void shopper() {
    for (unsigned int i=0; i<10000000u; ++i) {
        garlic_count++;
    }
}

int main() {
    std::thread barron(shopper);
    std::thread olivia(shopper);
    barron.join();
    olivia.join();
    printf("We Should buy %u garlic.\n", garlic_count);

    return 0;
}


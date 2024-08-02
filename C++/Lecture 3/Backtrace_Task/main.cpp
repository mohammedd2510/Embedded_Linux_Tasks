#include <iostream>
#include "Backtrace.hpp"


void functionC() {
    PRINT_BT();
}

void functionB() {
    functionC();
}

void functionA() {
    functionB();
}

int main() {
    functionA();
    return 0;
}

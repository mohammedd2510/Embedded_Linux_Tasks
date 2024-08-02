#include <csignal>
#include <iostream>
#include <unistd.h>

void signal_callback_handler(int signum) {
   std::cout << "\nCaught signal "<< std::endl;
   // Terminate program
   exit(signum);
}

int main(int argc, const char** argv) 
{
    std::signal(SIGINT,signal_callback_handler);
    while (true) {
        std::cout << "running" << std::endl;
        sleep(1);
    }
    return 0;
}
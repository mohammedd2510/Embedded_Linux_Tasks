#include <iostream>
#include "led.hpp"
using namespace std;

int main()
{
led ledblue(13,3,false,12);
ledblue.Display();

const led ledgreen = led();

ledgreen.Display();
led::number = 999;
led::SayHello(10);
ledblue.SayHello(1234);
    return 0;
}
#include <iostream>
using namespace std;
#include "led.hpp"

int led::number =20;

led::led() : x(0){

}
led::led(int pin,int count , bool state , int x) : pin(pin),count(count),state(state),x(x)
{

}
void led::Print(){
    cout << "the const number is" << x << endl;
    cout << "hello world" <<pin <<" " << count << " " << state << endl;
}
void led::Display() const
{
    cout << "const method " << endl;
    
}
void led::SayHello(int temp){
    int temp2 = 10;
    number++;
    temp++;
    temp2++;
    cout << "Hello " << number << " " << temp2 << " " << temp << endl;
}
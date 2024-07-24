#include <iostream>
int main(int argc, const char** argv) 
{
    auto square = [](int number){return number*number;};
    int Number= 0;
    std::cout << "Enter Number :  ";
    std::cin>>Number;
    std::cout << "The Square of "<<Number<< " = " << square(Number)<< std::endl;
 
    return 0;
}
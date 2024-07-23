#include <iostream>
int main() 
{
    int num = 0;
    int Sum =0;
    std::cout << "Enter The Number to Calculate The Sum of it's Digits" << std::endl;
    std::cin>>num;
    while (num) 
    {
    Sum+= num%10;
    num/=10;
    }
    std::cout << "The Sum of the digits = "<<Sum<< std::endl;
    return 0;
}
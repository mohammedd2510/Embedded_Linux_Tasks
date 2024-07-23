#include <iostream>
#include <ostream>
int main() 
{
    int num = 0;
    std::cout << "Enter the Number to Show its Multiplication Table"<<std::endl;
    std::cin>>num;
    for (int i = 0;i<=10;i++) 
    {
        std::cout << num <<" * "<<i<<" = "<<num*i<<std::endl;
    
    }
    return 0;
}
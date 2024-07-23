#include <iostream>
#include <bitset>
int main() 
{
    int Decimal_Number=0 ;
    std::cout << "Enter a Decimal Number : ";
    std::cin>>Decimal_Number;
    std::bitset<8>b(Decimal_Number);
    std::cout<<"Binary Representation : "<<b.to_string()<<std::endl;
    std::string binary_Number="" ;
    std::cout << "Enter a binary Number : ";
    std::cin>>binary_Number;
    std::bitset<8>b2(binary_Number);
    std::cout<<"Decimal Representation : "<<b2.to_ulong()<<std::endl;

    return 0;
}
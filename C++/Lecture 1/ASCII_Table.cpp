#include <iomanip>
#include <iostream>
#include <string>
int main() 
{
                
std::string line = "+" + std::string(6,'-') + "+" + std::string(7,'-')+ "+";
std::cout <<line<<std::endl<<"| Char | ASCII | \n"<<line <<std::endl;
for (int i = 0; i < 256; i++)
{
    
    char ascii=static_cast<char>(i);
    if (i<33|| i>126)
    {
        ascii =' ';
    } 
    
    std::cout<<"|"<<std::setw(6)<<ascii<<" |"<<std::setw(6)<<i<<" |\n";
}

    return 0;
}
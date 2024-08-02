#include <cctype>
#include <iostream>

bool check_char_is_digit(char c){
    return std::isdigit(c);
}
int main(int argc, const char** argv) 
{

std::cout << check_char_is_digit('a') << std::endl;

    return 0;
}
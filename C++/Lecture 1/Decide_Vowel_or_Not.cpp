#include <cctype>
#include <iostream>
int main() 
{
    char letter = ' ';
    std::cout<<"Enter The Letter to Decide Vowel or Not\n";
    std::cin>> letter;
    letter= std::tolower(letter);
    if (letter == 'a' || letter == 'e' || letter == 'u' || letter == 'i' || letter == 'o') 
    {
        std::cout<<"The Letter is a Vowel";
    
    }
    else {
        std::cout<<"The Letter is not vowel";
    }

    return 0;
}
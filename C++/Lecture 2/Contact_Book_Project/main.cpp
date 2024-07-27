#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include "Contact_Book.hpp"


int main(int argc, const char** argv) 
{
   std::string Decision="";
   Contact_Book CB;
   

    while (true)
    {
        CB.Print_Menu();
        std::getline(std::cin,Decision);
            std::transform(Decision.begin(), Decision.end(), Decision.begin(), [](unsigned char c) {
        return std::tolower(c);
    });
        if (Decision == "add")
        {
            std::string username , number;
            std::cout << "Enter username you want to add : ";
            std::cin>>username;
            std::cout<<"Enter username number : ";
            std::cin>>number;
            CB.Add_User(username, number); 
            std::cin.ignore();
            std::cin.get();
        }
        else if (Decision == "list") 
        {
            CB.List_All_Users();
            std::cin.ignore();
        }
        else if (Decision == "delete") {
            std::string username;
            std::cout << "Enter username you want to Delete : ";
            std::cin>>username;
            CB.Delete_User(username);
            std::cin.ignore();
            std::cin.get();
        }
        else if (Decision == "delete all") 
        {
            CB.Delete_All_Users();
            std::cin.ignore();
        }
        else if (Decision == "search") 
        {
            std::string username;
            std::cout << "Enter username you want to Search : ";
            std::cin>>username;
            CB.Search_User(username);
            std::cin.ignore();
            std::cin.get();
        }
        else if (Decision == "close") {
            break;
        }
        else 
        {
            std::cout << "Invalid Command Try Again" << std::endl;
            std::cin.ignore();
        }
        system("clear");
    }

   
    return 0;
}
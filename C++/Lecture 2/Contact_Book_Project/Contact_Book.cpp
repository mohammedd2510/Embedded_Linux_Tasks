/************************************************/
//
//              CopyRight Mohamed Osama
//
/************************************************/
/*
author: Mohamed Osama
date: 25/07/2024 17:47:39
breif:
*/
#include "Contact_Book.hpp"
#include <iomanip>
#include <ios>

Contact_Book::Contact_Book()
{
    std::cout<<"Welcome to your favourite address book"<<std::endl;
};
Contact_Book::~Contact_Book()
{
    std::cout << "Closing Address Book ....." << std::endl;
};
void Contact_Book::Print_Menu(){
    std::cout << "What do you want to do ?" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"List"<<"| List all users" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"Add"<<"| Adds new user" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"Delete"<<"| Delete an user" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"Delete all"<<"| Removes all users" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"Search"<<"| Search for a user" << std::endl;
    std::cout << "\t| "<<std::left<<std::setw(11)<<"Close"<<"| Close the address book" << std::endl;
}            
void Contact_Book::Add_User(std::string username , std::string Number)
{
    Contact_Book_Map[username]=Number;
    std::cout << "User " <<username<<" with number "<<Number<<" is added successfully"<< std::endl;
}
void Contact_Book::Search_User(std::string username)
{
    if (!Contact_Book_Map.count(username))
    {
        std::cout << "User: " <<username<<" Not Found"<< std::endl;
    }
    else {
        std::cout << "User " <<username<<" with number "<<Contact_Book_Map[username]<<" is found"<< std::endl;
    }
        
}
void Contact_Book::Delete_User(std::string username)
{
    if (!Contact_Book_Map.count(username))
    {
        std::cout << "User:" <<username<<" Not Found"<< std::endl;
    }
    else 
    {
        Contact_Book_Map.erase(username);
        std::cout << "User: " <<username<<" is deleted Successfully"<< std::endl;
    }   
}
void Contact_Book::Delete_All_Users(){
    Contact_Book_Map.clear();
    std::cout << "All Users Are Deleted Successfully" << std::endl;
}
void Contact_Book::List_All_Users()
{
    std::cout<<std::endl;
    if (Contact_Book_Map.empty())
    {
        std::cout << "No Contacts Found" << std::endl;
    }
    for (auto pair : Contact_Book_Map) 
    {
        std::cout <<"Username: " <<std::left<<std::setw(10)<<pair.first<<"|\t"<<"Number: "<<pair.second<< std::endl;
    }
}
         
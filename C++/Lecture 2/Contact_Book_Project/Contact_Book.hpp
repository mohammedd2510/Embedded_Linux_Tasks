#pragma once
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
#include <map>
#include <string>
#include <iostream>
class Contact_Book
{
public:
    Contact_Book();
    ~Contact_Book();
    void Add_User(std::string username , std::string Number);
    void Search_User(std::string username);
    void Delete_User(std::string username);
    void Delete_All_Users();
    void List_All_Users();
    void Print_Menu();
private:
    std::map<std::string, std::string > Contact_Book_Map;
};
               
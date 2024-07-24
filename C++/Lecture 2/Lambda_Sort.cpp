#include <algorithm>
#include <iostream>
#include <vector>
int main(int argc, const char** argv) {
   auto sort_array = [](std::vector<int>&arr,std::string order)
   {
    std::sort(arr.begin(),arr.end(),[order](int a , int b)
    {
        if (order ==  "ascending")return a<b;
        else if(order=="descending")return a>b;
        else return a<b;
     });
     };
   
    std::vector<int>arr{5,3,2,4,8,1,10};
    sort_array(arr,"ascending");
    for (int i : arr) {
        std::cout << i << " | ";
    }
    sort_array(arr,"descending");
    std::cout  << std::endl;
    for (int i : arr) {
        std::cout << i << " | ";
    }
    return 0;
}
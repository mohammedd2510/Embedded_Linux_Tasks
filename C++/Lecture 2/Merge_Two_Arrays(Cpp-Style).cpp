
#include <algorithm>
#include <vector>
#include <iostream>

std::vector<int> Merge_2_Arrays(std::vector<int>&arr1,std::vector<int>&arr2)
{
    std::vector<int>new_arr(arr1.size()+arr2.size());   
    std::merge(arr1.begin(),arr1.end(),arr2.begin(),arr2.end(),new_arr.begin());
    return new_arr;
}

int main(int argc, const char** argv) 
{

    std::vector<int> arr1 {1,2,3,4,5} ;
    std::vector<int> arr2  {6,7,8,9,10} ;
    std::vector<int>new_arr;
    new_arr=Merge_2_Arrays(arr1, arr2);
    std::cout << "First Array  : | ";
    for (int i : arr1) 
    {
        std::cout << i << " | ";
    }

    std::cout << "\nSecond Array : | ";
    for (int i : arr2) 
    {
        std::cout << i << " | ";
    }
    
    std::cout << "\nMerged Array : | ";
    for (int i :new_arr) 
    {
        std::cout << i << " | ";
    }
    
    return 0;
}
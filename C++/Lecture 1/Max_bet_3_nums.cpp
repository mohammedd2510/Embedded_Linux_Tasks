#include <algorithm>
#include <array>
#include <iostream>

int main() 
{

    std::array<int,3>nums;
    std::cout<<"Enter 3 Numbers to get their maximum"<<std::endl;
    for (int i=0; i<nums.size();i++)
    {
        std::cin>>nums[i];
    }
    std::cout <<"The maximum of 3 numbers is : "<<*std::max_element(nums.begin(),nums.end()) << std::endl;
} 
#include <algorithm>
#include <array>
#include <cmath>
#include <iostream>

int main() 
{

    std::array<int,3>nums;
    std::cout<<"Enter The Length of each side of the triangle : "<<std::endl;
    for (int i=0; i<nums.size();i++)
    {
        std::cin>>nums[i];
    }
    std::sort(nums.begin(),nums.end());
    if ((std::pow(nums[0],2)+std::pow(nums[1],2))== std::pow(nums[2],2))
    {
        std::cout<<"It's a Right Angle Triangle";
    }
    else {
        std::cout<<"It's Not a Right Angle Triangle";
    }
} 
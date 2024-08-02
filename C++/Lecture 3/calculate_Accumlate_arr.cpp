#include <iostream>
#include <numeric>
#include <vector>
int main(int argc, const char** argv) 
{
    std::vector<int>v{1,2,3,4,5};
    int sum = std::accumulate(v.begin(),v.end(),0);
    std::cout << "The sum =  "<< sum << std::endl;
    return 0;
}
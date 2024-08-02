#include <algorithm>
#include <iostream>
#include <vector>

bool check_all_array_is_even(std::vector<int>& v){
 return std::all_of(v.begin(),v.end(),[](int v){return (v%2==0);}); 
}
int main(int argc, const char** argv) 
{
std::vector<int>v{4,3,6,8};
std::cout<<check_all_array_is_even(v);
    return 0;
}
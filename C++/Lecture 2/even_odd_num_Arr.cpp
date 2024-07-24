#include <iostream>
#include <vector>

void print_even_odd_numbers_of_arr(std::vector<int>&arr)
{
    std::cout << "Even number of Array : | " ;
    for (int i : arr) 
    {
        if (i%2==0)
        {
            std::cout << i << " | ";
        }
    }
     std::cout << "\nOdd number of Array : | " ;
    for (int i : arr) 
    {
        if (i%2!=0)
        {
            std::cout << i << " | ";
        }
    }
}

int main(int argc, const char** argv) {

    std::vector<int> arr {1,2,3,4,5,6,7,8,9,10} ;
    print_even_odd_numbers_of_arr(arr);
    
    return 0;
}
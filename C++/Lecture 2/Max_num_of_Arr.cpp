#include <algorithm>
#include <iostream>

int Max_Num_Of_Array(int* arr,int size)
{
    return *std::max_element(arr,arr+size);

}

int main() {
    
    int arr[]={1,20,3,4,5};
    std::cout << Max_Num_Of_Array(arr,5) << std::endl;

 
    return 0;
}
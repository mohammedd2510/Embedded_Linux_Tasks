#include<iostream>
#include <numeric>
int main(int argc, const char** argv) 
{
    int arr[9991]={0};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    std::iota(arr,arr+arr_size, 10);
    for (int i : arr) {
        std::cout << i << " -> ";
    }
    return 0;
}
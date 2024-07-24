#include <algorithm>
#include <iostream>

int Search_For_Number(int*arr,int size,int num){
    return std::find(arr,arr+size,num)-arr; 
}

int main(int argc, const char** argv) {
    int arr[]={1,2,3,20,5,20,7,8,9,10};
    int num = 0;
    std::cout << "Enter The Number To Search For" << std::endl;
    std::cin>> num;
    std::cout << "The number index in the Array is : " << Search_For_Number(arr, 10, num)<< std::endl;
    return 0;
}
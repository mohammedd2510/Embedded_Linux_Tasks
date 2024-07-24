#include <algorithm>
#include <iostream>


int Delete_Number_From_Array(int*arr,int size,int num)
{
    int * arr_ptr = nullptr;
    while (true) 
    {
       arr_ptr=std::find(arr,arr+size,num);
        if (arr_ptr == arr+size)
        {
            break;
        }
        else
        {
            for (int i = arr_ptr-arr;i<size-1;i++) 
            {
                arr[i]=arr[i+1];
            }
            size--;
        } 
    }
    return size;
}
    

int main(int argc, const char** argv) {
    int arr[]={1,2,3,20,5,20,7,8,9,10};
    int num = 0;
    int arr_size = sizeof(arr)/sizeof(arr[0]);
    std::cout << "The array before Deleting : ";
    for (int i :arr) {
        std::cout << i <<" | ";
    }
    std::cout << "\nEnter The Number To Delete From Array" << std::endl;
    std::cin>> num;
    std::cout << "The array After Deleting : ";
    int arr_new_size = Delete_Number_From_Array(arr, arr_size, num);
    for (int i = 0; i<arr_new_size;i++) {
        std::cout << arr[i] <<" | ";
    }
    return 0;
}
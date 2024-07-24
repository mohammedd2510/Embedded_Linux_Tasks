#include <iostream>
#include <cstring>
int* Merge_2_Arrays(int*arr1,int n1,int*arr2,int n2 , int * arr_new_size)
{
    int* arr_new = new int[n1+n2];
    * arr_new_size = n1+n2;
    memcpy(arr_new, arr1, n1*sizeof(int));
    memcpy(arr_new+n1, arr2, n2*sizeof(int));
    return arr_new;
}

int main(int argc, const char** argv) 
{
    int arr1[5]={1,2,3,4,5};
    int arr2[5]={6,7,8,9,10};

    int n1 = sizeof(arr1)/sizeof(arr1[0]);
    int n2 = sizeof(arr2)/sizeof(arr2[0]);
    int new_size = 0;

    int *new_arr = nullptr;
    new_arr = Merge_2_Arrays(arr1, n1, arr2, n2, &new_size);

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
    for (int i = 0 ; i<new_size; i++) 
    {
        std::cout << new_arr[i] << " | ";
    }
    
    return 0;
}
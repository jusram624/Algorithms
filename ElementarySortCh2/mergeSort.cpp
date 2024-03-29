#include <iostream>
#include <vector>
using namespace std;

/*
void merge(vector<int>& nums, int low, int mid, int high){
// copying nums[low:high] => aux[low:high]
    vector<int> aux;
    for(int i =low; i<=high; i++){
        aux[i] = nums[i];
    }
    // these variables will refer to where we are in sub-array
    // initially, both point to the first element in respective sub-arrays
    int left_ind = low;
    int right_ind = mid+1;
    int curr_ind = low;
    // iterate through all position and pick the correct element
    for(int ptr = low; ptr <= high; ptr++){
    // if left subarray exhausted then use right one
        if(left_ind > mid){
            nums[ptr] = aux[right_ind];
            right_ind += 1;
        }
    // if right subarray exhausted then use left one
        else if(right_ind > high){
            nums[ptr] = aux[left_ind];
            left_ind += 1;
        }
    // if we have elements on both subarrays
    //choose the left if its smaller
        else if(aux[left_ind] < aux[right_ind]){
                nums[ptr] = aux[left_ind];
                left_ind += 1;
        }
        // choose right if its smaller
        else{
                nums[ptr] = aux[right_ind];
                right_ind += 1;
        }
    }
}
void merge_sort(vector<int>& nums, int low, int high){
// check if the bounds are correct
    if (low >= high) return;
// finding the split index
    int mid = (low + high)/2;
// recursively sorting two sub-arrays
    merge_sort(nums, low, mid);
    merge_sort(nums, mid+1, high);
// merge the two sorted arrays
    merge(nums, low, mid, high);
}*/

int main(int argc, char const *argv[])
{
    //vector<int> array{8,4,2,5,7,2};
    //merge_sort(array, array.at(0), array.at(5));
    cout<<"Hello";

}



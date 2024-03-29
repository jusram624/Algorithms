def ternary_search(arr, target):
    # Implement your code here
    low = 0
    high = len(arr) -1
    while low <= high:
        mid1 = low + (high-low) //3
        mid2 =  high - (high-low)//3

        if target == arr[mid1]:
            return mid1
        if target == arr[mid2]:
            return mid2
        
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        elif target > arr[mid1] and target < arr[mid2]:
            low = mid1 + 1
            high = mid2 - 1

    return -1


    
test_arr = [1,3,4,8,10,15,18,29,78]
print(ternary_search(test_arr, 29))


        
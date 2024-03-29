def binSearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1

    return -1

def binSearchRec(arr, target):
    low = 0
    high = len(arr)- 1

    if (low > high):
        return False
    mid = (low + high) // 2

    if(target < arr[mid]):
        return binSearchRec(arr[: mid ], target)
    elif(target > arr[mid]):
        return binSearchRec(arr[mid+1: ], target)
    
    return True

def lowBound(arr, target):
    low = 0 
    high = len(arr) - 1

    currLeftMost = -1

    while(low <= high):
        mid = (low + high) //2

        if(target < arr[mid]):
            high = mid -1 
        elif(target > arr[mid]):
            low = mid + 1
        else:
             currLeftMost = mid
             high = mid - 1

    return currLeftMost

def upperBound(arr, target):
    low = 0
    high = len(arr) - 1
    currRightMost = -1

    while(low <= high):
        mid = (low + high) // 2

        if target < arr[mid]:
            high = mid -1
        elif target > arr[mid]:
            low = mid + 1
        else:
            currRightMost = mid
            low = mid + 1
    return currRightMost


#Find Least element Greater than the Target
def leastGreater(arr, target):
    low = 0 
    high = len(arr)- 1
    ans = -1
    while (low <= high):
        mid = (low + high) // 2
        if target < arr[mid]:
            ans = mid
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            low = mid + 1 #if the target equals arr[mid]'s value then continue 
                          #finding the least element greater than target
    return ans

def greatestLess(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) //2
        if target < arr[mid]:
            high = mid -1
        elif target > arr[mid]:
            ans = mid
            low = mid +1
        else:
            high = mid - 1
    return ans
        
def oneSided(arr, target):
    low = 1
    high =1 

    while high < len(arr) and target > arr[high]:
        low = high
        high *= 2
    
    binSearch(arr, target)
    


test_arr = [1,3,4,8,10,10,10,15,18,29,78]
print("Binary Search Recursive: ")
print(binSearchRec(test_arr,10 ))
print()
print("Binary Search lower bound: ")
print(lowBound(test_arr, 10))
print()
print("Binary Search upper bound: ")
print(upperBound(test_arr, 10))
print()
print(leastGreater(test_arr, 8))
print()
print(greatestLess(test_arr, 8))
print()

        
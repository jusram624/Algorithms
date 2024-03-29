def maximumCount(nums):
    arrHigh= len(nums) -1
    arrLow = 0

    #Finding least idx greater than 0, finding the start of pos numbers if any
    low = 0
    high = len(nums) - 1
    leastGreatestAns= -1
    while(low <= high):
        mid = low + (high - low) // 2
        if(0 < nums[mid]):
            leastGreatestAns = mid
            high = mid - 1
        elif(0 > nums[mid]):
            low = mid + 1
        else:
            low = mid + 1

    if nums[len(nums) - 1] <= 0:
        posCount = 0 
    else:       
        posCount = (arrHigh - leastGreatestAns) +1


    #finding the greatest number less than 0 index if it exist, then arr[0] -> this idx are all neg.
    low = 0
    high = len(nums) - 1
    greatestLessAns = -1
    while(low <= high):
        mid = low + (high - low) // 2
        if(0 < nums[mid]):
            high = mid - 1
        elif(0 > nums[mid]):
            greatestLessAns = mid
            low = mid + 1
        else:
            high = mid - 1
    if nums[0] >= 0:
        negCount = 0
    else:
        negCount = (greatestLessAns - arrLow) +1

    return max(negCount,posCount)
    #least Ans should be the the left most index greater than 0 
    
    pass


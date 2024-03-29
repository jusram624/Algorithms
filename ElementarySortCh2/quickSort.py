def quickSort(arr):
    if len(arr) == 0:
        return []
    #partition
    left = []
    right = []
    pivot = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    #---------------------------

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

tmpArr = [5,3,8,4,2,1,9,7,6]
print (quickSort(tmpArr))


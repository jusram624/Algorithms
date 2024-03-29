def partition(arr):
    if len(arr) == 0:
        return
    
    left = []
    right = []
    piv = arr[0]
    
    for i in range(len(arr)):
        if arr[i] < piv:
            left.append(arr[i])
        else:
            right.append(arr[i])
    #tempArr = left + [piv] + right
    arr = left + right
    return len(left)
    


def quickSelect(arr, i):
    low = 0
    high = len(arr) -1

    if(low == high):
        return arr[low]
    
    #---------------
    left = []
    right = []
    piv = arr[0]
    
    for j in range(len(arr)):
        if arr[j] < piv:
            left.append(arr[j])
        else:
            right.append(arr[j])
    #tempArr = left + [piv] + right
    arr = left + right
    pos = len(left)
    #=----------------------------
    k = pos - low + 1
    if i == k:
        return arr[pos]
    if i < k:
        return quickSelect(arr[:(pos)], i)
    elif i > k:
        return quickSelect(arr[(pos+1):], i - k)

tmpArr = [30,50,31,60,27,29]
print(quickSelect(tmpArr, 5))

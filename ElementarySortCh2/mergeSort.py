def merge(arr, low, mid, high):
    aux = []
    for i in range(low, high + 1):
        aux.append(arr[i])
    left = low
    right = mid + 1

    for ptr in range(low , high + 1):
        if left > mid:
            arr[ptr] = aux[right]
            right += 1
        elif right > high:
            arr[ptr] = aux[left] 
            left += 1
        elif aux[left] < aux[right]:
            arr[ptr] = aux[left]
            left += 1
        else:
            arr[ptr] = aux[right]
            right += 1


def mergeSort( arr, low, high):
    if(low >= high):
        return
    mid = (low + high) // 2

    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

tmpArr = [6,8,2,9,3,1,7,4]
mergeSort(tmpArr, 0, len(tmpArr) - 1 )
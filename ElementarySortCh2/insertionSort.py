def insertionSort(array):
    for i in range (len(array)):
        curr = array[i]
        prev = i-1
        while prev >=0 and array[prev] > curr:
            array[prev + 1] = array[prev]
            prev = prev -1
        array[prev + 1] = curr
    return array
tmpArr = [6,8,2,9,3,1,7,4]
print(insertionSort(tmpArr))

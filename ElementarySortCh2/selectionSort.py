def selectionSort(array):
    for i in range(len(array)):
        minIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j

        temp = array[i]
        array[i] = array[minIdx]
        array[minIdx] = temp
    return array

tmpArr = [6,8,2,9,3,1,7,4]
print(selectionSort(tmpArr))
import countSort

def radixSort(arr):
    maxNum = max(arr)
    numsPlace = 1

    while (maxNum // numsPlace) > 0:
        
        countSort.countSort(tmpArr, 10)
        numsPlace *= 10
    


def radixSort1(arr):
    radArr = [[] for _ in range(10)]
    maxNum = max(arr)
    numsPlace = 1
    while maxNum // numsPlace > 0:
        for i in range(len(arr)):
            idx = ((arr[i]//numsPlace) % 10)
            elem = arr[i]

            if radArr[(arr[i]//1) % 10] == elem:
                radArr[(arr[i]//1) % 10].pop
            radArr[idx].append(elem)

        numsPlace *= 10



tmpArr = [25,553,821,43,2,13,96,7,6]
radixSort(tmpArr)
print(tmpArr)

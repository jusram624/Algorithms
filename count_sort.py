def sort(arr, valueEnd):
    posCounts = [0] * (valueEnd + 1)

    for i in range(len(arr)):
        currValue = arr[i]
        posCounts[currValue] += 1

    ans = []
    for i in range(valueEnd + 1):
        while posCounts[i] > 0:
            ans.append(i)
            posCounts[i] -= 1
    return ans


#Seperates negative integers and postive integers then combines final sorted array
def count_sort(array, valueEnd):
    sortedArray = [] 
    positiveArray = [] 
    negativeArray = [] 

    for i in range(len(array)):                     #finds negative ints and stores them as postive in negativeArray
        if array[i] < 0:
            negativeArray.append(-array[i])
    
    for i in range(len(array)):                     #finds positive ints and stores them in postiveArray
        if array[i] >= 0:
            positiveArray.append(array[i])


    if negativeArray:        
      negativeArray = sort(negativeArray, valueEnd)       #Sorts converted postive integers in negativeArray then reverses the array
      negativeArray = negativeArray[::-1]
      for i in range(len(negativeArray)):             #converts the ints back to negative
          negativeArray[i] *= -1
    
    if positiveArray:
      positiveArray = sort(positiveArray, valueEnd)       #sorts positive ints array


    for i in range(len(negativeArray)):             #appends the two sorted arrays in order and into sortedArray
       sortedArray.append(negativeArray[i])
    for i in range(len(positiveArray)):
        sortedArray.append(positiveArray[i])

    return sortedArray

    pass





def countSort(array, valueEnd):
    countArr = [0] * (valueEnd + 1)

    for i in range(len(array)):
        currVal = array[i]
        countArr[currVal] += 1

    ans = []
    for i in range(valueEnd + 1):
        while countArr[i] > 0:
            ans.append(i)
            countArr[i] -= 1
#=========================================================
            
            
    #just to sort the array 
    for i in range(0,len(array)): 
        array[i] = ans[i]
#-----------------------------------------------
        
#tmpArr = [5,3,8,4,2,1,9,7,6]
#countSort(tmpArr, 9)
#print(tmpArr)
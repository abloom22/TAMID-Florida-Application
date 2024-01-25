def sortArrays(arr1, arr2, k):
    temp = []
    while(k!=0):   #loops exactly k times or until lists are empty
        if(arr1==[]):
            if(arr2==[]):   #checks if arrays are empty, breaks out of loop
                break
            temp.append(arr2.pop(0))
        elif (arr2==[] or arr1[0]<=arr2[0]):    #compares smaller values and appends them to list
            temp.append(arr1.pop(0))
        else:
            temp.append(arr2.pop(0))
        k -= 1              #decrement k
    return temp




first = [2, 3, 8, 15, 30]
second = [1,2,3]
num = 4
output = sortArrays(first, second, num)
[print(x) for x in output]
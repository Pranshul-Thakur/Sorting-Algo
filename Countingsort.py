def count_sort(arr):
    
    #finding the maximum element of the array
    m = max(arr)
    
    #creating a count array with maximum size of +1 and inti
    count = [0] * (m + 1)
    
    #initialize count array with all 0s so that it can be filled up later on
    for num in arr:
        count[num] += 1
    
    #find the count of ever unique element and store them at the ith position in the count array    
    for i in range(1, m + 1):
        count[i] += count[i - 1]
    
    #creates a new array list and fills it with 0 
    result = [0] * len(arr)
    
    #restoring the array elements and return it
    for num in reversed(arr):
        result[count[num] - 1] = num
        count[num] -= 1
        
    return result

#print the list 
arr = [4,3,5,6,7,82,1,4,334,67]
sorted_arr = count_sort(arr)
print(sorted_arr)

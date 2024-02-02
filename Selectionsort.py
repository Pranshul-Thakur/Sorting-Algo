def selection_sort(arr):
    n = len(arr)
    
    for i in range(n): #traverse through the list
        
        min_index = i #assigning the value of minimum index to i
        for j in range(i+1, n): #traversing through the list from the second element onwards
            if arr[min_index] > arr[j]: #checking if the i is greater than j
                min_index = j #if greater then assign the value of minimum index to j
                
        arr[i], arr[min_index] = arr[min_index], arr[i] #inter switching the position of elements
        
#printing the list        
my_list = [4,34,123,2,0,78]
selection_sort(my_list)
print("Sorted array is : ", my_list)            
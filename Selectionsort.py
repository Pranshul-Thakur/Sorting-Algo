def selection_sort(arr):
    n = len(arr)

    #traverse through the list
    for i in range(n):

        #assigning the value of minimum index to i
        min_index = i

        #traversing through the list from the second element onwards
        for j in range(i+1, n):

            #checking if the i is greater than j
            if arr[min_index] > arr[j]:

                #if greater then assign the value of minimum index to j
                min_index = j

        #inter switching the position of elements
        arr[i], arr[min_index] = arr[min_index], arr[i]


#printing the list        
my_list = [4,34,123,2,0,78]
selection_sort(my_list)
print("Sorted array is : ", my_list)            

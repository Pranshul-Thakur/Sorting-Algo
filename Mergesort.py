def merge_sort(arr):
    
    #checks if the length of the array is smaller than 1, if smaller that means array is already sorted
    if len(arr) <= 1:
        return arr
        
    #Finding the middle of the array
    mid = len(arr) // 2
        
    #dividing the array into 2 half
    left_half = arr[:mid]
    right_half = arr[mid:]

    #recursively calling both the half
    merge_sort(left_half)  
    merge_sort(right_half)

    #Merging the two sorted halves
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    #checking for any remaining elements in both halves
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

#print the list
my_array = [14, 7, 12, 3]
merge_sort(my_array)
print("Sorted array:", my_array)

def partition(array, first, last):
 
    # Choose the rightmost element as pivot
    pivot = array[last]
 
    # Pointer for greater element
    i = first - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(first, last):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[last]) = (array[last], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
 
# Function to perform quicksort
def quicksort(array, first, last):
    if first < last:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, first, last)
 
        # Recursive call on the left of pivot
        quicksort(array, first, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, last)
        
my_list = [10,20,40,7,23,45,67]
n = len(my_list)
quicksort(my_list, 0, n - 1)
print("The sorted array is : ", my_list) 

def partition(array, first, last):
 
    #choosing the last element as pivot
    pivot = array[last]
 
    #pointer for the larger element
    i = first - 1
 
    #traversing through all the elements and comparing them with the pivot
    for j in range(first, last):
        if array[j] <= pivot:
 
            #if element smaller than the pivot found, swap it with i
            i = i + 1
 
            #swapping elements at i with j
            (array[i], array[j]) = (array[j], array[i])
 
    #swap the pivot element with the i
    (array[i + 1], array[last]) = (array[last], array[i + 1])
 
    #return the position
    return i + 1
 
 
#performing quicksort
def quicksort(array, first, last):
    if first < last:
 
        #finding the pivot element and checking if the smaller element are on left and larger on the right
        pi = partition(array, first, last)
        #pi is the pivot
 
        #recursive call on left of pivot
        quicksort(array, first, pi - 1)
 
        #recursive call on right of pivot
        quicksort(array, pi + 1, last)
        

#printing the list
my_list = [10,20,40,7,23,45,67]
n = len(my_list)
quicksort(my_list, 0, n - 1)
print("The sorted array is : ", my_list) 

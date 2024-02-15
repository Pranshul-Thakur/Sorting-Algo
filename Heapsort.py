def heapify(arr, n, i):
    
    #declaring the largest element
    largest = i
    
    #to go through the left half of bst
    left = 2 * i + 1
    
    #to go through the right half of bst
    right = 2 * i + 2
    
    #checking if the left side exists and is greater than root 
    if left < n and arr[largest] < arr[left]:
        largest = left
    
    #checking if the right side exists and is greater than root    
    if right < n and arr[largest] < arr[right]:
        largest = right
        
    #swapping largest if not equal to i    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        #heapify the root
        heapify(arr, n, largest)
        
#function to sort the array of any size
def heapsort(arr):
    
    #checking for the length
    n = len(arr)
    
    #traversing the array from back to build the max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    #extracting the elements for the new sorted array and sorting them   
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#print the list
arr = [10,34,23,1,520,76,7,8]
heapsort(arr)
print(arr)

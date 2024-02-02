def ins_sort(arr):
    n = len(arr)
    
    #traverse through the list
    for i in range(1,n):
        
        #assign key to current element
        key = arr[i]
        j = i-1
        
        #sift elements greater than i to right
        while j >= 0 and key < arr[j]:
             arr[j+1] = arr[j]
             j -= 1
             
         #assigning the value of key to the larger element    
        arr[j + 1] = key
               
                
#print the list                
my_list = [54,34,2,1,68,456,34]
ins_sort(my_list)
print("The sorted list is : ", my_list)
def bubble_sort(arr):
    n = len(arr)
    
    #traverse through the list
    for i in range(n):

        #traversing through the list to find the next elements
        for j in range(0, n-i-1):

            #checking if the current element bigger than the previous element
            if arr[j]>arr[j+1]:

                #switch the 2 elements
                arr[j], arr[j+1] = arr[j+1], arr[j]


#printing the list                
my_list = [3,5,7,9,1,9,0,3,2]
bubble_sort(my_list)
print("The sorted list is : ", my_list)

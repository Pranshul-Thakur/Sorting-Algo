'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
my_list = [3,5,7,9,1,9,0,3,2]
bubble_sort(my_list)
print("The sorted list is : ", my_list)
'''

def bubble_sort(arr):
    
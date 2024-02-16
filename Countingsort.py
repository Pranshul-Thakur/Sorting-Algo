def count_sort(arr):
    m = max(arr)
    count = [0] * (m + 1)
    for num in arr:
        count[num] += 1
        
    for i in range(1, m + 1):
        count[i] += count[i - 1]
        
    result = [0] * len(arr)
    
    for num in reversed(arr):
        result[count[num] - 1] = num
        count[num] -= 1
        
    return result

arr = [4,3,5,6,7,82,1,4,334,67]
sorted_arr = count_sort(arr)
print(sorted_arr)

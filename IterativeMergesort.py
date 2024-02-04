def IterativeMergeSortAlgorithm(arr):
    # Initialize the array size
    n = len(arr)

    # Set the step size for the merging process
    step = 1

    # Continue merging until step size is less than the array size
    while step < n:
        # Iterate over the array in steps
        for left in range(0, n - step, 2 * step):
            mid = left + step - 1
            right = min(left + 2 * step - 1, n - 1)

            # Merge the subarrays
            merge(arr, left, mid, right)

        # Double the step size for the next iteration
        step *= 2
    
    return arr

def merge(arr, left, mid, right):
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
my_array = [14, 7, 12, 3]
sorted_array = IterativeMergeSortAlgorithm(my_array)
print("Sorted array:", sorted_array)

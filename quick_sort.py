def quick_sort(arr):
    # ends when there is 1 or 0 elements in array
    if len(arr) <= 1:
        return arr
    
    # pivot selection (element in middle)
    pivot = arr[len(arr) // 2]

    leftArray = [x for x in arr[1:] if x < pivot]
    rightArray = [x for x in arr[1:] if x >= pivot]
    return quick_sort(leftArray) + [pivot] + quick_sort(rightArray)

# Test Case with at least 2 elements
unsorted_list = [3, 6, 9, 8, 7, 10, 1, 2, 4, 5]
print("multiple element array (unsorted): " + str(unsorted_list))
sorted_list = quick_sort(unsorted_list)
print("multiple element array (sorted):" + str(sorted_list))

# Test case with 1 or 0 elements
unsorted_list = [4]
print("single element array (unsorted): " + str(unsorted_list))
sorted_list = quick_sort(unsorted_list)
print("single element array (sorted):" + str(sorted_list))

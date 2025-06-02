def merge_sort(arr):
    # ends when there is 1 or 0 elements in array
    if len(arr) <= 1:
        return arr

    # Divide the array into two arrays, split down the middle
    middleIndex = len(arr) // 2
    leftArray = merge_sort(arr[:middleIndex])
    rightArray = merge_sort(arr[middleIndex:])

    sortedArray = []
    x = 0 
    y = 0

    # Merge the split arrays while comparing elements
    while x < len(leftArray) and y < len(rightArray):
        if leftArray[x] <= rightArray[y]:
            sortedArray.append(leftArray[x])
            x += 1
        else:
            sortedArray.append(rightArray[y])
            y += 1

    # Add any remaining elements
    sortedArray.extend(leftArray[x:])
    sortedArray.extend(rightArray[y:])
    return sortedArray

# Test Case with at least 2 elements
unsorted_list = [3, 6, 9, 8, 7, 10, 1, 2, 4, 5]
print("multiple element array (unsorted): " + str(unsorted_list))
sorted_list = merge_sort(unsorted_list)
print("multiple element array (sorted):" + str(sorted_list))

# Test case with 1 or 0 elements
unsorted_list = [4]
print("single element array (unsorted): " + str(unsorted_list))
sorted_list = merge_sort(unsorted_list)
print("single element array (sorted):" + str(sorted_list))
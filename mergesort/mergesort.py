def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)   # continously splitting array until single element arrays
    right_half = merge_sort(right_half) # time complexity for the splitting is O(logn) because it constructs a tree

    return merge(left_half, right_half) # the first merge will only be called once splitting finishes
                                        # starts at the leaves of the tree

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):  # place pointers on each subarray
        if left[left_index] < right[right_index]:               # compare with elements of the other array
            result.append(left[left_index])                     # once it is put inside temporary merged array 
            left_index += 1                                     # move pointer of the current subarray to next element
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])                            # if one pointer reaches the end of its subarray
    result.extend(right[right_index:])                          # put all the elements of the other array into temporary merged array
    return result                                               # since no elements to compare and the remaining elements are
                                                                # already sorted
# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)

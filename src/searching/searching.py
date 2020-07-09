def linear_search(arr, target):
    # traverse the list one item at a time
    for i in range(0, len(arr)):
        # if current item is the same as the target, return the index of the item
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while high >= low:
        # get the middle index (average low and high)
        middle_index = (low + high) // 2
        # compare middle value with target
        # if they are the same, return the middle index
        if arr[middle_index] == target:
            return middle_index
        # if middle is less than target, item left of middle becomes new low (look to RHS)
        elif arr[middle_index] < target:
            low = middle_index + 1
        # if middle is greater than target, middle becomes new high (look to LHS)
        else:
            high = middle_index - 1
    return -1  # not found


list_a = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print(linear_search(list_a, -6))

list_b = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(list_b, 1))

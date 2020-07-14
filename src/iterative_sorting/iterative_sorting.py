# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # loop through list to the right of the first element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                # TO-DO: swap
                smallest_index = j
        if smallest_index != cur_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through array until no swaps are performed
    was_swapped = True
    while was_swapped:
        was_swapped = False
        for i in range(0, len(arr) - 1):
            current_item = arr[i]
            j = i + 1
            next_item = arr[j]
            # compare current item to next item
            # if current item is greater than next item, swap
            if current_item > next_item:
                was_swapped = True
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# list_a = [8, 5, 2, 4, 1, 3]
# print(selection_sort(list_a))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?
BECAUSE ZERO INDEXING). 

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # create an array of zeros with length of maximum + 1
    count_arr = [0] * (maximum + 1)
    # loop through array, storing the count of each number in the count array
    for i in range(0, len(arr)):
        # for each value in the original array, increment the counting array at that index
        count_arr[arr[i]] += 1
    # loop through the count array and modify so each value is the sum of previous values
    for j in range(0, maximum + 1):
        # modify the count array so each index stores the sum of previous counts
        count_arr[j] += count_arr[j-1]
    # for each index, add the correct value the requisite number of times to the original array
    # initiate the count at the last index in the original array
    count = len(arr) - 1
    # create an array of zeros the length of the original array
    empty_arr = [0] * len(arr)
    while count >= 0:
        # fill the empty array by finding the index of each original array item in the modified count array and placing in that index
        empty_arr[count_arr[arr[count]] - 1] = arr[count]
        count_arr[arr[count]] -= 1
        count -= 1
    # copy the sorted elements into original array
    for k in range(0, len(arr)):
        arr[k] = empty_arr[k]

    return arr


list_b = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(list_b, 9))

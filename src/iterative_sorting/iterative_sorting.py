# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        """
        1. Start with current index = 0

        2. For all indices EXCEPT the last index:

            a. Loop through elements on right-hand-side 
            of current index and find the smallest element

            b. Swap the element at current index with the
            smallest element found in above loop
        """
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        

        # TO-DO: swap
        # Your code here
        temp = arr[cur_index]     
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    """
    1. Loop through the array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
    2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    """

    # keep track of whether or not there were any swaps
    swaps = True

    while swaps:
        # keep track of swaps per iteration
        swaps_this_round = 0
        # iterate over each array element
        for i in range(len(arr) - 1):
            # compare the element to the element to its right
            # if the elemenent to the right is greater, 
            # swap them
            if arr[i] > arr[i + 1]:
                swaps_this_round += 1
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        # if a whole round goes without swaps,
        # bubble sort is complete 
        if swaps_this_round == 0:
            swaps = False

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

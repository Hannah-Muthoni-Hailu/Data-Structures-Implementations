# The bubble sort function could have been optimised by reducing the number of iterations made in the inner loop after every lap since the end of each iteration would cause the end of the array to be sorted
def swap(nums, i, j):
    holder = nums[i]
    nums[i] = nums[j]
    nums[j] = holder

def bubbleSort(nums):
    n = len(nums)
    i = 0
    swaps = 0
    sorted_part = 0

    while True:
        while i < n - 1 - sorted_part:
            if nums[i] > nums[i + 1]:
                swap(nums, i, i + 1)
                swaps += 1
            i += 1

        if swaps == 0:
            break
        else:
            i = 0
            swaps = 0
            sorted_part += 1
    
    return nums

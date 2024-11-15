def binary_search(arr, val):
    high = len(arr) - 1
    low = 0

    while high > low:
        mid = (high + low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1

    return -1

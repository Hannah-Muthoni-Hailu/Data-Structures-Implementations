def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i

    return -1

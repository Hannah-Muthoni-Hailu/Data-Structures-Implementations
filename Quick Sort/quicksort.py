def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    j = 0
    i = j - 1

    while j < len(arr) - 1:
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1
    
    i += 1
    temp = arr[i]
    arr[i] = pivot
    arr[-1] = temp

    left_sub_array = quick_sort(arr[0:i])
    rigth_sub_array = quick_sort(arr[i + 1:])

    return left_sub_array + [pivot] + rigth_sub_array

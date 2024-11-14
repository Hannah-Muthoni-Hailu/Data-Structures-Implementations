def insertion_sort(arr):
    i = 1

    while i < len(arr):
        j = i - 1
        temp = arr[i]
        while j >= 0:
            if temp < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = temp
        i += 1
    
    return arr

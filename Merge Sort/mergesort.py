def merge(arr1, arr2):
    new_arr = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            new_arr.append(arr2[j])
            j += 1
        else:
            new_arr.append(arr2[j])
            new_arr.append(arr1[i])
            j += 1
            i += 1

    new_arr.extend(arr1[i:])
    new_arr.extend(arr2[j:])
    
    return new_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    return merge(merge_sort(arr[0:mid]), merge_sort(arr[mid:]))

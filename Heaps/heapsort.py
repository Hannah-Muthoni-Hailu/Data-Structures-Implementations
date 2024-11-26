def maxHeap(arr, i, n):
    left = (2 * i) + 1
    right = (2 * i) + 1
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        maxHeap(arr, largest, n)

def heapify(arr):
    n = len(arr)

    for i in range(n//2, 0, -1):
        maxHeap(arr, i-1, n)

    return arr

def HeapSort(arr):
    sorted_arr = []
    n = len(arr)

    while len(sorted_arr) < n:
        arr = heapify(arr)
        sorted_arr.append(arr.pop(0))

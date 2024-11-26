function maxHeap(arr, i) {
    var largest = i
    var left = (2 * i) + 1
    var right = (2 * i) + 2

    if (left < arr.length && arr[left] > arr[largest]){
        largest = left
    }
    if (right < arr.length && arr[right] > arr[largest]) {
        largest = right
    }

    if (largest != i) {
        var temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxHeap(arr, largest)
    }
}

function heapify(arr) {
    n = arr.length

    for (var i = Math.floor(n / 2); i >= 0; i--){
        maxHeap(arr, i)
    }
    return arr
}

function heapSort(arr) {
    var n = arr.length
    var sorted_arr = []

    while (sorted_arr.length < n) {
        arr = heapify(arr)
        sorted_arr.push(arr[0])
        arr.splice(0, 1);
    }
    return sorted_arr
}

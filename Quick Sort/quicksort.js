function quickSort(arr) {
    if (arr.length <= 1){
        return arr
    }
    
    var pivot = arr[arr.length - 1];
    var j = 0
    var i = j - 1
    while (j < arr.length - 1) {
        if (arr[j] < pivot) {
            i += 1
            var temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
        j += 1
    }
    i += 1
    var temp = arr[i]
    arr[i] = pivot
    arr[arr.length - 1] = temp

    var left_sub_array = quickSort(arr.slice(0, i))
    var right_sub_array = quickSort(arr.slice(i + 1, arr.length))

    return left_sub_array.concat([pivot].concat(right_sub_array))
}

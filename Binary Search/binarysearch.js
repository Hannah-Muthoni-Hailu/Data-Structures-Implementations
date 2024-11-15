function binarySearch(arr, val) {
    var l = 0
    var h = arr.length - 1

    while (h > l) {
        var m = Math.floor((h + l) / 2)
        if (arr[m] == val) {
            return m
        }
        else if (arr[m] > val) {
            h = m - 1
        }
        else {
            l = m + 1
        }
    }
    return -1
}

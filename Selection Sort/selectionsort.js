function selectionSort(arr) {
    for (var i = 0; i < arr.length; i++){
        var m = arr[i];
        var m_ind = i
        for (var j = i; j < arr.length; j++){
            if (arr[j] < m) {
                m = arr[j]
                m_ind = j
            }
        }
        holder = arr[i]
        arr[i] = m
        arr[m_ind] = holder
    }
    return arr
}

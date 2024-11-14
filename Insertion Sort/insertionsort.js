function insertionSort(arr) {
    for (var i = 1; i < arr.length; i++){
        temp = arr[i];
        var j = i - 1;
        while (j >= 0) {
            if(arr[j] > temp){
                arr[j + 1] = arr[j]
                j -= 1
            }
            else{
                break
            }
        }
        arr[j + 1] = temp
    }
    return arr
}

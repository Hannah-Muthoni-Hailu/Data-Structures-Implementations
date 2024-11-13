function swap(arr, i , j){
    var holder = arr[i];
    arr[i] = arr[j]
    arr[j] = holder
}

function bubbleSort(arr) {
    for (var i = 0; i < arr.length; i ++){
        for (var j = 0; j < arr.length - 1 - i; j++){
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
    }
    return arr
}

function merge(arr1, arr2) {
    var new_arr = [];
    var i = 0;
    var j = 0;

    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            new_arr.push(arr1[i])
            i += 1
        }
        else if (arr1[i] > arr2[j]) {
            new_arr.push(arr2[j])
            j += 1
        }
    }

    new_arr = new_arr.concat(arr1.slice(i , arr1.length))
    new_arr = new_arr.concat(arr2.slice(j, arr2.length))

    return new_arr
}

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    var mid = Math.floor(arr.length / 2);
    return merge(mergeSort(arr.slice(0, mid)), mergeSort(arr.slice(mid, arr.length)));
}

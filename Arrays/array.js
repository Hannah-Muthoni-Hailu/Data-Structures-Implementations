class Arr {
    constructor(arr=[]) {
        this.arr = arr
    }

    read(ind){
        for(let i = 0; i < this.arr.length; i++){
            if (i == ind) {
                return this.arr[i]
            }
        }
    }

    update(ind, val) {
        for (let i = 0; i < this.arr.length; i++){
            if (i == ind) {
                this.arr[i] = val
                return
            }
        }
        return "Index out of range"
    }

    ins(ind, val) {
        for (let i = 0; i < this.arr.length; i++){
            if (i == ind) {
                let holder = this.arr.slice(i, this.arr.length)
                this.arr[i] = val
                this.arr = this.arr.slice(0, i+1).concat(holder)
            }
        }
        return "Index out of range"
    }

    rem(val){
        for (let i = 0; i < this.arr.length; i++) {
            if (this.arr[i] == val) {
                if (i == 0){
                    this.arr = this.arr.slice(1, this.arr.length)
                } else if (i == 1) {
                    this.arr = this.arr.slice(0, 1).concat(this.arr.slice(2, this.arr.length))
                } else if (i == this.arr.length -1) {
                    this.arr = this.arr.slice(0, this.arr.length - 1 )
                }
                else {
                    this.arr = this.arr.slice(0, i).concat(this.arr.slice(i+1, this.arr.length))
                }
                return
            }
        }
        return "Value not in array"
    }

    loop() {
        for (let i = 0; i < this.arr.length; i++){
            // yield this.arr[i]
        }
    }

    quickSort(arr){
        // Base case
        if (arr.length <= 1) {
            print(arr)
            return arr
        }

        // Identify the pivot
        let pivot_ind = Math.floor(arr.length / 2)
        let pivot_val = arr[pivot_ind]

        // Identify left and right pointers
        let left = 0
        let right = arr.length - 1

        while (right > left) {
            // Step
            while (arr[left] < pivot_val) {
                left += 1
            }

            while (right > 0 && arr[right] > pivot_val){
                right -= 1
            }

            // Swap
            let holder = arr[right]
            arr[right] = arr[left]
            arr[left] = holder

            // Check if pivot has been shifted
            if (arr[right] == pivot_val) {
                pivot_ind = right
            } else if (arr[left] == pivot_val) {
                pivot_ind = left
            }
        }


        let left_part = this.quickSort(arr.slice(0, pivot_ind))
        let right_part = this.quickSort(arr.slice(pivot_ind + 1, arr.length))

        return left_part.concat([pivot_val].concat(right_part))
    }

}

let my_array = new Arr([4, 3, 1, 2, 5], 1)
console.log(my_array.quickSortAdvanced(my_array.arr))
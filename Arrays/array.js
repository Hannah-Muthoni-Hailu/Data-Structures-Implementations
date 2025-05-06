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
            yield this.arr[i]
        }
    }

}

my_array = new Arr([1, 2, 3, 4])
my_array.rem(3)
console.log(my_array.arr)
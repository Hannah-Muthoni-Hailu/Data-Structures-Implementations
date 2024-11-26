class MaxHeap{
    constructor() {
        this.heap = []
    }

    heapify(i) {
        var left = (2 * i) + 1
        var right = (2 * i) + 2

        if (left >= this.heap.length && right >= this.heap.length) {
            return
        }

        if (left < this.heap.length) {
            this.heapify(left)
        }
        if (right < this.heap.length) {
            this.heapify(right)
        }

        while (True) {
            var largest = i
            if (left < this.heap.length && this.heap[left] > this.heap[i]) {
                largest = left
            }
            if (right < this.heap.length && this.heap[right] > this.heap[i]) {
                largest = right
            }
            if (largest != i) {
                var temp = this.heap[i]
                this.heap[i] = this.heap[largest]
                this.heap[largest] = temp
            }
            else {
                break
            }
        }
    }

    insert(val) {
        this.heap.push(val)
        this.heapify(0)
    }

    delete() {
        this.heap[0] = this.heap[this.heap.length - 1]
        this.heap = this.heap.slice(0, this.heap.length - 1)
        this.heapify(0)
    }
}

class MinHeap {
    constructor() {
        this.heap = []
    }

    heapify(i) {
        var left = (2 * i) + 1
        var right = (2 * i) + 2

        if (left >= this.heap.length && right >= this.heap.length) {
            return
        }

        if (left < this.heap.length) {
            this.heapify(left)
        }
        if (right < this.heap.length) {
            this.heapify(right)
        }

        while (True) {
            var smallest = i
            if (left < this.heap.length && this.heap[left] < this.heap[i]) {
                smallest = left
            }
            if (right < this.heap.length && this.heap[right] < this.heap[i]) {
                smallest = right
            }
            if (smallest != i) {
                var temp = this.heap[i]
                this.heap[i] = this.heap[smallest]
                this.heap[smallest] = temp
            }
            else {
                break
            }
        }
    }

    insert(val) {
        this.heap.push(val)
        this.heapify(0)
    }

    delete() {
        this.heap[0] = this.heap[this.heap.length - 1]
        this.heap = this.heap.slice(0, this.heap.length - 1)
        this.heapify(0)
    }
}

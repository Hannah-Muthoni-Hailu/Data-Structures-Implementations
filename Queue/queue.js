class Queue {
    constructor(max_size) {
        this.queue = [];
        this.max_size = max_size;
    };

    enqueue(val) {
        if (!this.isFull()) {
            this.queue.push(val);
        }
        else {
            console.log("Queue is Full");
        }
    };

    dequeue() {
        val = this.queue[0];
        this.queue.splice(0, 1);
        return val;
    };

    peek() {
        return this.queue[0];
    };

    rear(){
        return this.queue[this.queue.length - 1];
    };

    isFull() {
        return this.queue.length == this.max_size;
    };

    isEmpty() {
        return this.queue.length == 0;
    };
};

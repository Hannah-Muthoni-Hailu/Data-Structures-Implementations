// Stack implementation in JavaScript
class Stack {
    constructor(max_size) {
        this.stack = [];
        this.max_size = max_size;
    };

    push_stack(val) {
        if (!this.isFull()) {
            this.stack.push(val);
        }
        else {
            console.log("Stack Full")
        }
    };

    pop_stack() {
        return this.stack.pop();
    };

    top_stack() {
        return this.stack[this.stack.length - 1];
    };

    isFull() {
        return this.stack.length == this.max_size;
    };

    isEmpty() {
        return this.stack.length == 0;
    };
}

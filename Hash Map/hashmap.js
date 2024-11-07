class HashMap {
    constructor(capacity) {
        this.hashmap = {};
        for (var i = 0; i < capacity; i++){
            this.hashmap[i] = [];
        }
        this.capacity = capacity;
    }

    hashfunction(key) {
        return key % this.capacity;
    }

    insertion(key, val) {
        var index = this.hashfunction(key);

        this.hashmap[index].push([key, val]);
    }

    lookup(key) {
        var index = this.hashfunction(key);
        for (var i = 0; i < this.hashmap[index].length; i++){
            if (this.hashmap[index][i][0] == key) {
                return this.hashmap[index][i][1]
            }
        }
        return "Could not find key"
    }

    deletion(key) {
        var index = this.hashfunction(key);
        var found = false
        for (var i = 0; i < this.hashmap[index].length; i++) {
            if (this.hashmap[index][i][0] == key) {
                this.hashmap[index].splice(i, 1)
                found = true
            }
        }
        if (!found) {
            console.log("Could not find key")   
        }
    }
}

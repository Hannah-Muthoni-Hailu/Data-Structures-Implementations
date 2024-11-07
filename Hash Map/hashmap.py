class HashMap():
    def __init__(self, capacity):
        self.hashmap = {x:[] for x in range(capacity)}
        self.capacity = capacity

    def hashfunction(self, x):
        return x % self.capacity

    def insertion(self, x, val):
        index = self.hashfunction(x)

        # Collision resolution using seperate chaining
        self.hashmap[index].append((x, val))

        
    def lookup(self, key):
        index = self.hashfunction(key)
        for k, val in self.hashmap[index]:
            if k == key:
                return val

        return "Could not find key"

    def deletion(self, key):
        index = self.hashfunction(key)
        found = False
        for k, val in self.hashmap[index]:
            if k == key:
                self.hashmap[index].remove((k, val))
                found = True
                break

        if not found:
            print("Could not find key")

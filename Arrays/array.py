class Arr:
    def __init__(self, arr=[]):
        self.arr = arr

    def arr_read(self, index):
        for ind, item in enumerate(self.arr):
            if ind == index:
                return item
    
    def arr_update(self, index, value):
        for ind, _ in enumerate(self.arr):
            if ind == index:
                self.arr[ind] = value
                break

    def arr_insert(self, index, value):
        for ind, _ in enumerate(self.arr):
            if ind == index:
                rem = self.arr[ind:]
                self.arr[ind] = value
                self.arr += rem
                break

    def arr_remove(self, value):
        for ind, item in enumerate(self.arr):
            if item == value:
                self.arr[ind:-1] = self.arr[ind+1:]
                self.arr = self.arr[:-1]
                break

    def arr_length(self):
        counter = 0
        for item in self.arr:
            counter += 1

        return counter
    
    def arr_loop(self):
        for item in self.arr:
            yield item


my_arr = Arr([1, 2, 3, 4, 5])
my_arr.arr_remove(3)
print(my_arr.arr)

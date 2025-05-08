import math

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

    def quick_sort(self, arr, counter =0):
        #Base case
        if len(arr) <= 1:
            return arr
        
        # Pivot
        pivot_ind = len(arr) // 2
        pivot_val = arr[pivot_ind]

        # Left and right pointers
        left = 0
        right = len(arr) - 1

        while right > left:
            while arr[left] < pivot_val:
                left += 1

            while right > 0 and arr[right] > pivot_val:
                right -= 1

            # Swap
            holder = arr[right]
            arr[right] = arr[left]
            arr[left] = holder

            # Check if the pivot has been shifted
            if arr[right] == pivot_val:
                pivot_ind = right
            elif arr[left] == pivot_val:
                pivot_ind = left

        left_part = self.quick_sort(arr[0:pivot_ind])
        right_part = self.quick_sort(arr[pivot_ind+1:])

        return left_part + [pivot_val] + right_part


my_arr = Arr([2, 5, 1, 3, 6])
# print(my_arr.arr)
print(my_arr.quick_sort(my_arr.arr))

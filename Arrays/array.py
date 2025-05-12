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
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort(arr[0:mid])
        right = self.merge_sort(arr[mid:])

        res = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                res.append(left[0])
                left = left.pop()
            elif right[0] < left[0]:
                res.append(right[0])
                right = right.pop()
            else:
                res.append(right[0])
                res.append(left[0])
                right = right.pop()
                left = left.pop()

        if len(left) > 0:
            res.extend(left)
        if len(right) > 0:
            res.extend(right)

        return res
    
    def binary_search(self, arr, val, start=0, end=None, counter = 5):
        if counter == 0:
            return "Failed"
        if start == end:
            if arr[start] == val:
                return start
            else:
                return False
        
        if not end:
            end = len(arr) - 1

        if end < start:
            return False

        mid = (start + end) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return self.binary_search(arr, val, start, mid-1, counter - 1)
        else:
            return self.binary_search(arr, val, mid+1, end, counter - 1)


def two_pointer(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        yield start, end
        start += 1
        end -= 1



my_arr = Arr([0, 1, 3, 4])
# print(my_arr.arr)
print(my_arr.binary_search(my_arr.arr, 2))

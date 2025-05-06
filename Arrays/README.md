# Arrays
Arrays are a collection of values with each value having an index assigned to it.
When creating an array, we must specify the name and the values inside it.
The following operations can be performed on an array:
+ **read** - takes in an index and returns the value stored there
+ **update** - changes the value stored at a given index to a new one
+ **insert** - places a value at a specific index while shifting the values at indexes greater than it to the right
+ **remove** - removes a value at a given index
+ **length** - returns the number of elements stored in an array
+ **loop** - goes through each value in the array

## Sorting
### QuickSort
This is a Divide and Conquer algorithm.
It selects a pivot in the array then partitions the array based on this pivot, with the pivot eventually being placed at its correct position in the array.
It is a recursive algorithm
The following steps are involved in the QuickSort algorithm:
1. Identify the pivot (this could be the middle, start or end index)
2. Place a left pointer at the leftmost index of the array
3. Place a right pointer at the rightmost index of the array
4. Move the left pointer to the right until it lands on a value greater than or equal to the pivot value then stop
5. Move the right pointer to the left until it lands on a value less than or equal to the pivot value then stop
6. Swap the values at the left and right pointers
7. Repeat steps 4 through 6 until the left and right pointers cross each other
8. Repeat the entire process (recursively) on the left and right sub partitions created by the pivot
9. The base case of the recursion is reached when an array of length 1 is passed
 
Below is my pseudocode implementation of the Quick sort algorithm
```
function QuickSort(array)
  // Base case
  if LEN(array) == 1
    return array

  // Identify the pivot
  pivot_ind = floor(LEN(array) / 2)
  pivot_val = array[pivot_ind]

  // Initialize the left and right pointers
  left_pointer = 0
  right_pointer = LEN(arr) - 1

  // Loop until the left and right pointers cross
  while right_pointer > left_pointer do
    left_val = array[left_pointer]
    // Step right until the left pointer points at a value greater than or equal to the pivot
    while left_val < pivot do
      left_pointer += 1
      left_val = array[left_pointer]
    end while

    right_val = array[right_pointer]
    // Step left until the right pointer points at a value less than or equal to the pivot
    while right_val > pivot do
      right_pointer -= 1
      right_val = array[right_pointer]
    end while

    // Swap the values at the left and right pointers
    array[left_pointer] = right_val
    array[right_pointer] = left_val
  end while

  left_part = Quicksort(array[0 : pivot_ind])
  right_part = Quicksort(array[pivot_ind + 1 : LEN(array)])
  return left_part + pivot_val + right_part
end function
```

Here is a more optimized pseudocode from <a href="https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm">Tutorials Point</a>
```
function partitionFunc(left, right, pivot)
   leftPointer = left
   rightPointer = right - 1

   while True do
      while A[++leftPointer] < pivot do
      //do-nothing            
      end while
		
      while rightPointer > 0 && A[--rightPointer] > pivot do
         //do-nothing         
      end while
		
      if leftPointer >= rightPointer
         break
      else                
         swap leftPointer,rightPointer
      end if
   end while 
	
   swap leftPointer,right
   return leftPointer
end function
```

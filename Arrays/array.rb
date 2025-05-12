class Arr
  attr_accessor :arr
  def initialize(arr=[])
    @arr = arr
  end

  def read(ind)
    @arr.each_with_index do |x, idx|
      if idx == ind
        return x
      end
    end
    return "Index out of range"
  end

  def update(ind, val)
    @arr.each_with_index do |x, idx|
      if idx == ind
        @arr[ind] = val
      end
    end
  end

  def ins(ind, val)
    @arr.each_with_index do |x, idx|
      if idx == ind
        holder = arr[idx...]
        @arr[idx] = val
        @arr = @arr[0,idx+1] + holder
      end
    end
  end

  def rem(val)
    @arr.each_with_index do |x, idx|
      if x == val
        first_part = @arr[0,idx]
        second_part = @arr[idx+1...]
        @arr = first_part + second_part
      end
    end
  end

  def quickSort(arr)
    if arr.length <= 1
      return arr
    end

    # Identify pivot
    pivot_ind = arr.length / 2
    pivot_val = arr[pivot_ind]

    # Initialize pointers
    left = 0
    right = arr.length - 1

    while right > left do
      # Step
      while arr[left] < pivot_val do
        left += 1
      end

      while arr[right] > pivot_val do
        right -= 1
      end

      # Swap
      holder = arr[right]
      arr[right] = arr[left]
      arr[left] = holder

      # Check if pivot has been swapped
      if arr[right] == pivot_val
        pivot_ind = right
      elsif arr[left] == pivot_val
        pivot_ind = left  
      end
    end

    left_part = quickSort arr[0, pivot_ind]
    right_part = quickSort arr[pivot_ind + 1...]

    return left_part + [pivot_val] + right_part
  end

  def mergeSort(arr)
    if arr.length <= 1
      return arr
    end

    mid = arr.length / 2
    left = mergeSort(arr[0,mid])
    right = mergeSort(arr[mid...])

    res = []

    while left.length > 0 && right.length > 0 do
      if left[0] < right[0]
        res << left[0]
        left.shift
      elsif right[0] < left[0]
        res << right[0]
        right.shift
      else
        res << left[0]
        res << right[0]
        left.shift
        right.shift
      end
    end

    if left.length > 0
      res += left
    end

    if right.length > 0
      res += right
    end

    return res
  end

  def binarySearch(arr, val, s=0, e=nil)
    if s == e
      if arr[s] == val
        return s
      else
        return false
      end
    end

    if e == nil
      e = arr.length - 1
    end

    mid = (s + e) / 2

    if arr[mid] == val
      return mid
    elsif arr[mid] > val
      return binarySearch(arr, val, s, mid-1)
    else
      return binarySearch(arr, val, mid+1, e)
    end
  end
end

my_arr = Arr.new([0, 3])
p my_arr.binarySearch my_arr.arr, 2
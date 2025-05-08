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
end

my_arr = Arr.new([4, 3, 1, 2])
p my_arr.quickSort my_arr.arr
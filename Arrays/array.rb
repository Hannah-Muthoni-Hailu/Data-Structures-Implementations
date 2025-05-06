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
end

my_arr = Arr.new([1, 2, 3, 4])
my_arr.rem(4)
p my_arr.arr
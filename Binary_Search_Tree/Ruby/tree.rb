require_relative 'node'

class Tree
  attr_accessor :array
  def initialize(array)
    @array = quickSort(array.uniq)
    @root = build_tree(@array, 0, @array.length - 1)
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

  def build_tree(arr, start_point, end_point)
    if end_point < start_point
      return nil
    end

    mid = (start_point + end_point) / 2

    data = arr[mid]
    left = build_tree(arr, start_point, mid - 1)
    right = build_tree(arr, mid + 1, end_point)

    tree = Node.new(data, left, right)
    return tree
  end

  def pretty_print(node = @root, prefix = '', is_left = true)
    pretty_print(node.right, "#{prefix}#{is_left ? '│   ' : '    '}", false) if node.right
    puts "#{prefix}#{is_left ? '└── ' : '┌── '}#{node.data}"
    pretty_print(node.left, "#{prefix}#{is_left ? '    ' : '│   '}", true) if node.left
  end

  def insert(value)
    new_node = Node.new(value)
    pointer = @root

    loop do
      if value < pointer.data
        if pointer.left.nil?
          pointer.left = new_node
          break
        else
          pointer = pointer.left
          next
        end
      end
      if value > pointer.data
        if pointer.right.nil?
          pointer.right = new_node
          break
        else
          pointer = pointer.right
          next
        end
      end
      if value == pointer.data
        break
      end
    end
  end

  def delete(value, root=@root, parent=@root)
    pointer = root

    until pointer.nil?
      if pointer.data > value
        parent = pointer
        pointer = pointer.left
      elsif pointer.data < value
        parent = pointer
        pointer = pointer.right
      else
        # If pointer is a leaf node
        if pointer.left.nil? && pointer.right.nil?
          if pointer == @root
            @root = nil
            break
          end
          if pointer == parent.left then parent.left = nil else parent.right = nil end
          break
        # If pointer only has a left child
        elsif pointer.left && pointer.right.nil?
          if pointer == @root
            @root = pointer.left
            break
          end
          if pointer == parent.left then parent.left = pointer.left else parent.right = pointer.left end
          break
        # If pointer only has a right child
        elsif pointer.left.nil? && pointer.right
          if pointer == @root
            @root = pointer.right
            break
          end
          if pointer == parent.left then parent.left = pointer.right else parent.right = pointer.right end
          break
        # If pointer has both children
        else
          successor = pointer.right
          successor = successor.left while !successor.left.nil?
          pointer.data = successor.data
          delete(successor.data, pointer.right, pointer)
          return
        end
      end
    end
  end
  
  def find(value)
    pointer = @root

    until pointer.nil?
      if pointer.data == value
        return pointer
      elsif pointer.data > value
        pointer = pointer.left
      else
        pointer = pointer.right
      end
    end
    return "Value not found!"
  end

  def height(value)
    pointer = @root

    until pointer.nil?
      if pointer.data > value
        p pointer.data
        pointer = pointer.left
      elsif pointer.data < value
        pointer = pointer.right
      elsif pointer.data == value
        return count_height(pointer)
      end
    end
    return "Value not found"
  end

  def count_height(node)
    if node.nil? || (node.left.nil? && node.right.nil?)
      return 0
    end

    left = count_height(node.left)
    right = count_height(node.right)

    return 1 + (left > right ? left : right)
  end

  def depth(value)
    pointer = @root
    counter = 0

    until pointer.nil?
      if pointer.data > value
        pointer = pointer.left
        counter += 1
      elsif pointer.data < value
        pointer = pointer.right
        counter += 1
      elsif pointer.data == value
        return counter
      end
    end
    return "Value not found"
  end

  def balanced?(node=@root)
    if node.nil? || (node.left.nil? && node.right.nil?)
      return 0
    end

    left = balanced?(node.left)
    right = balanced?(node.right)

    if !left || !right || left > right + 1 || right > left + 1
      return false
    else
      return 1 + left + right
    end
  end

  def level_order
    arr = [@root]
    pointer = 0

    until pointer == arr.length
      if block_given?
        yield arr[pointer]
      end
      arr << arr[pointer].left unless arr[pointer].left.nil?
      arr << arr[pointer].right unless arr[pointer].right.nil?
      pointer += 1
    end

    return arr.map { |item| item.data } unless block_given?
  end

  def rebalance
    arr = level_order
    @root = build_tree(arr, 0, arr.length - 1)
  end

  def inorder(node=@root, &block)
    if node.left.nil? && node.right.nil?
      if block
        block.call(node)
      else
        return [node.data]
      end
    end

    left = node.left ? inorder(node.left, &block) : []
    if block
      block.call(node)
    end
    right = node.right ? inorder(node.right, &block) : []

    return left + [node.data] + right unless block_given?
  end

  def preorder(node=@root, &block)
    if node.left.nil? && node.right.nil?
      if block
        block.call(node)
        return
      else
        return [node.data]
      end
    end

    if block
      block.call(node)
    end

    left = node.left ? preorder(node.left, &block) : []
    right = node.right ? preorder(node.right, &block) : []

    return [node.data] + left + right unless block_given?
  end

  def postorder(node=@root, &block)
    if node.left.nil? && node.right.nil?
      if block
        block.call(node)
        return
      else
        return [node.data]
      end
    end

    left = node.left ? postorder(node.left, &block) : []
    right = node.right ? postorder(node.right, &block) : []

    if block
      block.call(node)
    end

    return left + right + [node.data] unless block_given?
  end
end

tree = Tree.new([5, 3, 7, 2, 4, 6, 8, 9, 11])
tree.pretty_print
tree.postorder { |node| p node.data }


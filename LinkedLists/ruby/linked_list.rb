require_relative 'node'

class LinkedList
  def initialize(head=nil)
    @head = head
  end

  def append(value)
    node = Node.new
    node.value = value
    node.next_node = nil

    if @head == nil
      @head = node
      return
    end

    holder = @head

    until holder.next_node == nil
      holder = holder.next_node
    end

    holder.next_node = node
  end

  def prepend(value)
    node = Node.new(value)

    holder = @head

    @head = node

    node.next_node = holder
  end

  def size
    counter = 0

    holder = @head

    until holder == nil
      counter += 1
      holder = holder.next_node
    end

    counter
  end

  def head
    @head.value
  end

  def tail
    t = @head

    until t.next_node == nil
      t = t.next_node
    end

    t.value
  end

  def at(index)
    counter = 0
    holder = @head

    loop do
      return "Index out of range" if holder == nil
      return holder.value if counter == index

      counter += 1
      holder = holder.next_node
    end
  end

  def pop
    holder = @head

    if holder.next_node == nil
      @head = nil
      return holder.value
    end

    until holder.next_node.next_node == nil
      holder = holder.next_node
    end

    last_val = holder.next_node.value
    holder.next_node = nil
    return last_val
  end

  def contains?(value)
    holder = @head

    until holder == nil
      return true if holder.value == value
      holder = holder.next_node
    end
    return false
  end

  def find(value)
    holder = @head
    counter = 0

    until holder == nil
      return counter if holder.value == value
      counter += 1
      holder = holder.next_node
    end
  end

  def insert_at(value, index)
    return 'Index out of range' if index > size || index < 0
    node = Node.new(value)
    holder = @head
    counter = 0

    if index == 0
      @head = node
      node.next_node = holder
      return
    end

    until holder == nil
      if counter + 1 == index
        temp_holder = holder.next_node
        holder.next_node = node
        node.next_node = temp_holder
        return
      end
      counter += 1
      holder = holder.next_node
    end
  end

  def remove_at(index)
    return 'Index out of range' if index >= size || index < 0
    if index == 0
      @head = @head.next_node
      return
    end

    holder = @head
    counter = 0

    until holder == nil
      if counter + 1 == index
        holder.next_node = holder.next_node.next_node
        return
      end
      counter += 1
      holder = holder.next_node
    end
  end

  def to_s
    s = ""

    holder = @head

    until holder == nil
      s += "( #{holder.value} ) -> "
      holder = holder.next_node
    end

    s += "nil"

    puts s
  end
end

list = LinkedList.new

list.append('dog')
list.append('cat')
list.append('parrot')
list.append('hamster')
list.append('snake')
list.append('turtle')

puts list

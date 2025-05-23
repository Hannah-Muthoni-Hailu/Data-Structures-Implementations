require_relative '../LinkedLists/ruby/linked_list'

class HashMap
  attr_accessor :capacity, :entries_num, :hash_map
  def initialize(load_factor, capacity)
    @load_factor = load_factor
    @capacity = capacity
    @hash_map = {}
    @entries_num = 0
    @capacity.times do |i|
      @hash_map[i] = LinkedList.new
    end
  end

  def hash(key)
    hash_code = 0
    prime_number = 31

    key.each_char { |char| hash_code = prime_number * hash_code + char.ord }

    hash_code
  end

  def set(key, value)
    hash_code = hash(key)
    bucket = hash_code % @capacity

    # Check if key exists in bucket
    head = @hash_map[bucket].head

    # Replace the value if key exists
    until head.nil?
      val = head.value
      if val[0] == key
        val[1] = value
        head.value = val
        return
      end
      head = head.next_node
    end

    # Add value to bucket if key doesn't exist
    @hash_map[bucket].append([key, value])
    @entries_num += 1
    check_capacity
  end

  def check_capacity
    if @entries_num > @capacity * @load_factor
      p "Capacity full"
      # Double the capacity
      @capacity *= 2

      # Reset the number of entries
      @entries_num = 0

      # Save the old entries
      old_entries = entries
      
      # Reset hashmap
      @hash_map = {}
      @capacity.times do |i|
        @hash_map[i] = LinkedList.new
      end

      old_entries.each do |node|
        set(node[0], node[1])
      end
    end
  end

  def get(key)
    # Determine the key's hash code
    hash_code = hash(key)

    # Identify its bucket's position
    bucket = hash_code % @capacity

    # Find it in the linked list
    head = @hash_map[bucket].head

    until head.nil?
      return head.value[1] if head.value[0] == key
      head = head.next_node
    end
    return "Value not found"
  end

  def has?(key)
    hash_code = hash(key)
    bucket = hash_code % @capacity

    head = @hash_map[bucket].head

    until head.nil?
      return true if head.value[0] == key
      head = head.next_node
    end

    return false
  end

  def remove(key)
    hash_code = hash(key)
    bucket = hash_code % @capacity

    head = @hash_map[bucket].head

    return nil if head.nil?

    if head.next_node.nil?
      return if head.value[0] == key ? 0 : nil
    end

    until head.next_node.nil?
      if head.next_node.value[0] == key
        val = head.next_node.value[1]
        head.next_node = head.next_node.next_node
        return val
      end
      head = head.next_node
    end
  end

  def length
    sum = 0
    @hash_map.each do |_, value|
      sum += value.size
    end
    sum
  end

  def clear
    @hash_map.each do |key, _|
      @hash_map[key] = LinkedList.new
    end
  end

  def keys
    keys_array = []
    @hash_map.each do |_, value|
      head = value.head
      until head.nil?
        keys_array.push(head.value[0])
        head = head.next_node
      end
    end
    keys_array
  end

  def values
    values_array = []
    @hash_map.each do |_, value|
      head = value.head
      until head.nil?
        values_array.push(head.value[1])
        head = head.next_node
      end
    end
    values_array
  end

  def entries
    entries_array = []
    @hash_map.each do |_, value|
      head = value.head
      until head.nil?
        entries_array.push(head.value)
        head = head.next_node
      end
    end
    entries_array
  end
end

test = HashMap.new(0.75, 16)

 test.set('apple', 'red')
 test.set('banana', 'yellow')
 test.set('carrot', 'orange')
 test.set('dog', 'brown')
 test.set('elephant', 'gray')
 test.set('frog', 'green')
 test.set('grape', 'purple')
 test.set('hat', 'black')
 test.set('ice cream', 'white')
 test.set('jacket', 'blue')
 test.set('kite', 'pink')
 test.set('lion', 'golden')
 test.set('ice cream', 'brown')

p test.hash_map.size
p test.length

test.set('moon', 'silver')

p test.hash_map.size
p test.length

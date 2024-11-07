class Node():
    def __init__(self, val, pointer):
        self.val = val
        self.pointer = pointer

class LinkedList():
    def __init__(self):
        self.linkedlist = []
        self.head = None
        self.head_pointer = None
        # set the pointer to always start by pointing at the head of the list
        self.next = self.head_pointer

    # Find the index of the node with a particular pointer
    def traversal(self, pointer):
        # Check if there are any elements in the linked list
        if self.next == None:
            print("There are no elements to traverse")
            return "null"

        while self.linkedlist[self.next].pointer != "end":
            if self.linkedlist[self.next].pointer == pointer:
                index = self.next
                self.next = self.head_pointer
                return index
            self.next = self.linkedlist[self.next].pointer

        if self.linkedlist[self.next].pointer == "end" and pointer == "end":
            index = self.next
            self.next = self.head_pointer
            return index
        else:
            self.next = self.head_pointer
            return "null"

    # Assign a node to the head of the list
    def insertAtHead(self, val):
        if self.head != None:
            # Set the new node's pointer to the index of the current head
            pointer = self.head_pointer

            new_node = Node(val, pointer)
            self.linkedlist.append(new_node)

            # Set the new node's position as the new head position
            self.head_pointer = self.linkedlist.index(new_node)
            self.head = new_node
            self.next = self.head_pointer
        else:
            new_node = Node(val, "end")
            self.linkedlist.append(new_node)

            # Set the new node's position as the new head position
            self.head_pointer = self.linkedlist.index(new_node)
            self.head = new_node
            self.next = self.head_pointer

    def insertAtPointer(self, val, pointer):
        # Find the previous node
        prev_node_ind = self.traversal(pointer)

        # Check if previous node exists
        if prev_node_ind == "null":
            print("Could not insert new node. Previous node pointer not found")
        else:
            # Create the new node and append it to the list with the pointer pointing to whatever node the previous node was pointing to
            new_node = Node(val, pointer)
            self.linkedlist.append(new_node)

            # Change the previous node to point to the new node
            self.linkedlist[prev_node_ind].pointer = self.linkedlist.index(new_node)

    def deletion(self, pointer):
        if pointer == self.head_pointer:
            new_head = self.linkedlist[self.head.pointer]
            new_head_pointer = self.head.pointer
            self.linkedlist.remove(self.head)

            self.head = new_head
            self.head_pointer = new_head_pointer
            self.next = self.head_pointer

        else:
            prev_node_ind = self.traversal(pointer)

            node_to_delete = self.linkedlist[self.linkedlist[prev_node_ind].pointer]

            self.linkedlist[prev_node_ind].pointer = node_to_delete.pointer

            self.linkedlist.remove(node_to_delete)

            #Update new pointers due to shift in index starting at the pointer before node that has been removed
            i = 0
        for i in range(len(self.linkedlist)):
            if self.linkedlist[i].pointer >= pointer and self.linkedlist[i].pointer != "end":
                self.linkedlist[i].pointer -= 1

    def displayList(self):
        display = [(node.val, node.pointer) for node in self.linkedlist]
        return display

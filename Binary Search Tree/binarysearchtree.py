class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, val):
        if self.root == None:
            return -1

        def iterate(root, val):
            if root is None:
                return -1

            if root.val == val:
                return root
            
            if root.val > val:
                return iterate(root.left, val)
            if root.val < val:
                return iterate(root.right, val)

        return iterate(self.root, val)

    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    # Struggles when the values are duplicated
    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return

        parent = self.root

        while True:
            if val < parent.val:  # Traverse to the left subtree
                if parent.left is None:  # Insert if left child is empty
                    parent.left = new_node
                    return
                parent = parent.left  # Move to the left child
            elif val > parent.val:  # Traverse to the right subtree
                if parent.right is None:  # Insert if right child is empty
                    parent.right = new_node
                    return
                parent = parent.right  # Move to the right child
            else:  # Duplicate value detected
                print("Duplicate values are not supported")
                return

    def deletion(self, val):
        if self.root is None:
            print("Could not find value")
            return

        # Search for value
        parent = self.root

        if val < parent:
            node = self.root.left
            pointing = "Left"
        else:
            node = self.root.right
            pointing = "Right"

        while node is not None:
            if val > node.val:
                parent = node
                node = node.right
                pointing = "Right"
            elif val < node.val:
                parent = node
                node = node.left
                pointing = "Left"
            else:
                # Deleting a leaf node
                if node.left is None and node.right is None:
                    if pointing == "Left":
                        parent.left = None
                    else:
                        parent.right = None
                    return

                # Deleting a node with only one left child
                if node.right is None:
                    if pointing == "Left":
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    if pointing == "Left":
                        parent.left = node.right
                    else:
                        parent.right = node.right

                # Deleting a node with only one right child
                if node.left is None:
                    if pointing == "Left":
                        parent.left = node.right
                    else:
                        parent.right = node.right
                else:
                    if pointing == "Left":
                        parent.left = node.left
                    else:
                        parent.right = node.left

                # Deleting a node with 2 children
                if node.left is not None and node.right is not None:
                    if pointing == "Left":
                        node.right.left = node.left
                        parent.left = node.right
                    else:
                        node.left.right = node.right
                        parent.right = node.right
                return
            print("Value not in tree")
            return
            

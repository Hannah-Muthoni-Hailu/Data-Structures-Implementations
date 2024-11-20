# This code has a lot of errors that will be fixed later

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def preorder(self, root):
        if root is None:
            return
        
        yield root.val
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        
        self.preorder(root.left)
        self.preorder(root.right)
        yield root.val

    def inorder(self):
        if root is None:
            return
        
        self.preorder(root.left)
        yield root.val
        self.preorder(root.right)

    def bfs(self, root):
        if root is None:
            return

        queue = [root]
        while queue:
            # Obtain the last item in the queue
            node = queue.pop(0)
            print(node.val)

            # Add the left node to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.left == None:
                node.left = val
                return
            if node.right == None:
                node.right = val
                return

            queue.append(node.left)
            queue.append(node.right)

    def search(self, val):
        if self.root is None:
            return False

        for node_val in self.preorder(self.root):
            if node_val == val:
                return True
        return False

    def deletion(self, val):
        if self.root is None:
            return False

        # Find value in tree
        queue = [self.root]
        target = None

        while queue:
            node = queue.pop(0)

            if node.val == val:
                target = node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


        if target is None:
            print("Value not found")
            return False

        last_node = None
        last_parent = None
        queue = deque([(root, None)])

        while queue:
            curr, parent = queue.popleft()
            last_node = curr
            last_parent = parent

            if curr.left:
                queue.append((curr.left, curr))
            if curr.right:
                queue.append((curr.right, curr))

        # Replace target's value with the last node's value
        target.data = last_node.data

        if last_parent:
            if last_parent.left == last_node:
                last_parent.left = None
            else:
                last_parent.right = None
        else:
            return None

binary_tree = Binary_Tree()

binary_tree.insert(1)
binary_tree.inorder()

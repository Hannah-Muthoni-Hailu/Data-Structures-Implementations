class Node {
    constructor(val) {
        this.val = val;
        this.right = null;
        this.left = null;
    }
}

class BinarySearchTree{
    constructor() {
        this.root = null;
    }

    traverse(root) {
        if (root == null) {
            return
        }
        this.traverse(root.left);
        console.log(root.val);
        this.traverse(root.right);
    }

    search(val) {
        if (this.root == null) {
            console.log("The tree has no values");
            return
        }
        var node = this.root
        while (node != null) {
            if (val < node) {
                node = node.left;
                continue
            }
            else if (val > node) {
                node = node.right
                continue
            }
            else {
                return node
            }
        }
        console.log("Value was not found in tree")
        return
    }

    insert(val) {
        var new_node = new Node(val)
        if (this.root == null) {
            this.root = new_node
            return
        }

        var parent = this.root

        while (true) {
            if (val < parent.val) {
                if (parent.left == null) {
                    parent.left = new_node;
                    return
                }
                else {
                    parent = parent.left
                }
            }
            else if (val > parent.val) {
                if (parent.right == null) {
                    parent.right = new_node;
                    return
                }
                else {
                    parent = parent.right
                }
            }
            else {
                console.log("Function does not support duplicates");
                return
            }
        }
    }

    delete(val) {
        if (this.root == null) {
            console.log("Tree does not contain value");
            return
        }

        var parent = self.root;
        var node = self.root;

        while (node != null) {
            if (val < node.val) {
                parent = node;
                node = node.left;
            }
            else if (val > node.val) {
                parent = node
                node = node.right
            }
            else {
                if (node.left == null && node.right == null) {
                    if (parent.left == node) {
                        parent.left = null
                        return
                    }
                    else {
                        parent.right = null
                        return
                    }
                }
                else if (parent.left == node) {
                    if (node.left == null) {
                        parent.left = node.right
                    }
                    else if (node.right == null) {
                        parent.left = node.left
                    }
                    else {
                        parent.left = node.right
                    }
                }
                else if (parent.right == node) {
                    if (node.left == null) {
                        parent.right = node.right
                    }
                    else if (node.right == null) {
                        parent.right = node.left
                    }
                    else {
                        parent.right = node.left
                    }
                }
            }
        }

    }
}

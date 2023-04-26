class Tree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        node = Tree.Node(val=val)

        if self.root == None:
            self.root = node
            return

        current = self.root
        while True:
            if current.val > val:
                if current.left == None:
                    current.left = node
                    break
                current = current.left

            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

    def equal(self, other):
        return Tree.__equal(self.root, other.root)

    @staticmethod
    def __equal(self_root, other_root):
        if self_root is None and other_root is None:
            return True

        if self_root is not None and other_root is not None:
            return self_root.val == other_root.val and \
                Tree.__equal(self_root.left, other_root.left) and \
                Tree.__equal(self_root.right, other_root.right)

        return False


tree1 = Tree()
tree1.insert(7)
tree1.insert(1)
tree1.insert(8)

tree2 = Tree()
tree2.insert(7)
tree2.insert(1)
tree2.insert(8)

print(tree1.equal(tree2))

class DoctorNode:
    """One doctor in the reporting tree."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """Stores doctors and provides three recursive traversals."""

    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        """Add a doctor under a parent; return False if the spot is invalid."""
        if side not in ("left", "right"):
            return False

        parent = self._find(self.root, parent_name)
        if parent is None:
            return False

        if side == "left":
            if parent.left is not None:
                return False
            parent.left = DoctorNode(employee_name)
        else:
            if parent.right is not None:
                return False
            parent.right = DoctorNode(employee_name)
        return True

    def _find(self, node, name):
        """Find the first doctor with this name."""
        if node is None:
            return None
        if node.name == name:
            return node
        found = self._find(node.left, name)
        if found is not None:
            return found
        return self._find(node.right, name)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

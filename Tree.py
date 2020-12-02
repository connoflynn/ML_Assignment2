import Tree as tree

# class to make the decision tree

class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        out = "Root: %s" % self.root
        if self.left:
            out += "\n Left: %s" % self.left
        if self.right:
            out += "\n\t Right: %s" % self.right
        return out
# 1 Check for the above base cases.
# 2 For each attribute a, find the normalized information gain ratio from splitting on a.
# 3 Let a_best be the attribute with the highest normalized information gain.
# 4 Create a decision node that splits on a_best.
# 5 Recurse on the sublists obtained by splitting on a_best, and add those nodes as children of node.

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

def create_tree():
    return tree
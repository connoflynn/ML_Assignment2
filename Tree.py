# 1 Check for the above base cases.
# 2 For each attribute a, find the normalized information gain ratio from splitting on a.
# 3 Let a_best be the attribute with the highest normalized information gain.
# 4 Create a decision node that splits on a_best.
# 5 Recurse on the sublists obtained by splitting on a_best, and add those nodes as children of node.

import Tree as tree
from InformationGain import find_split_indexes, choose_best_attribute
from Data import split_for_branches, get_class_count

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

# recursive function to build the tree
def create_tree(data, attributes, target):
    training = data.loc[:, attributes] # set the dataset to only include the attributes given
    training[target] = data.loc[:, target] # add target column to dataset
    
    target_column = training.loc[:, target] # get target column in the training data
    target_val = target_column.iloc[0] 
    if all(value == target_val for value in target_column):
        return tree.Tree(target_val) # if all the target values are one type, creates a leaf node

    if len(attributes) == 1: # if we run out of attributes to split by, we take the majority target value in the remaining data
        num_classes = get_class_count(training, target)
        most_class = 0
        majority_class = ""
        for target_value in num_classes:
            if num_classes[target_value] > most_class:
               most_class = num_classes[target_value]
               majority_class = target_value
        return tree.Tree(majority_class)


    split_values, split_indexes = find_split_indexes(training, target)
    split_attribute = choose_best_attribute(training, target, split_values, split_indexes)

    split_attribute_value = training[split_attribute[0]][split_attribute[1]]
    
    attributes.remove(split_attribute[0])
    
    #split the data for left and right branches
    split_left = training[training[split_attribute[0]] < split_attribute_value]
    split_right = training[training[split_attribute[0]] >= split_attribute_value]

    split_left.drop(columns = split_attribute[0])
    split_right.drop(columns = split_attribute[0])
    # print("-----------------")
    # print(split_left)
    # print("11111111111111111")
    # print(split_right)
    # print("-----------------")
    return tree.Tree({split_attribute[0]: split_attribute_value}, create_tree(split_left, attributes, target),
                     create_tree(split_right, attributes, target))

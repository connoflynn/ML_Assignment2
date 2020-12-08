from Data import get_data, split_data, remove_beerid, get_class_count, split_for_branches
from Entropy import get_entropy
from InformationGain import get_information_gain, find_split_indexes, choose_best_attribute
from Tree import create_tree

def main():
    data = get_data("beer.csv")
    data = remove_beerid(data)

    training_data, testing_data = split_data(data, 0.666)

    target_feature_value = "style"
    attributes = data.columns.values.tolist()
    
    tree = create_tree(data, attributes, target_feature_value)
    print(tree)
main()
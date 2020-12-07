from Data import get_data, split_data, remove_beerid, get_class_count
from Entropy import get_entropy
from InformationGain import get_information_gain, find_split_indexes, choose_best_attribute

def main():
    data = get_data("beer.csv")
    data = remove_beerid(data)

    training_data, testing_data = split_data(data, 0.666)

    target_feature_value = "style"

    alcohol = training_data[["alcohol", target_feature_value]]
    
    #print(get_information_gain(data,target_feature_value,"alcohol", 46))

    split_values, split_indexes = find_split_indexes(data, target_feature_value)
    first_split = choose_best_attribute(data, target_feature_value, split_values, split_indexes)
    print(first_split)
    data = data.drop(columns = "nitrogen")
    split_values, split_indexes = find_split_indexes(data, target_feature_value)
    first_split = choose_best_attribute(data, target_feature_value, split_values, split_indexes)
    print(first_split)
main()
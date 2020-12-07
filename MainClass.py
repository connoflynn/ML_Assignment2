from Data import get_data, split_data, remove_beerid, get_class_count
from Entropy import get_entropy
from InformationGain import get_information_gain, find_split_indexes

def main():
    data = get_data("beer.csv")
    data = remove_beerid(data)

    training_data, testing_data = split_data(data)

    target_feature_value = "style"

    alcohol = training_data[["alcohol", target_feature_value]]
    
    #print(get_information_gain(data,target_feature_value,"alcohol", 46))

    find_split_indexes(data, target_feature_value)
main()
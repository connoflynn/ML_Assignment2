from Data import get_data, split_data, get_number_classes, remove_beerid, get_class_count
from Entropy import entropy_calc

def main():
    data = get_data("beer.csv")

    data = remove_beerid(data)

    training, testing = split_data(data)
    target_feature_value = "style"

    num = entropy_calc(data, target_feature_value)

    print(num)
    #print(training)
    #print("+++++++++++++++++++++++++++++++++++")
    #print(num)

main()
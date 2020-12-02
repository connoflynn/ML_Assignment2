from Data import get_data, split_data, remove_beerid, get_class_count
from Entropy import get_entropy

def main():
    data = get_data("beer.csv")

    data = remove_beerid(data)

    training_data, testing_data = split_data(data)
    target_feature_value = "style"

    entropy = get_entropy(data, target_feature_value)
    print(entropy)
    #print(training)
    #print("+++++++++++++++++++++++++++++++++++")
    #print(num)

main()
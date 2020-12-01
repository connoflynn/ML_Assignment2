import pandas as pd

from Data import get_data, split_data

def main():
    data = get_data("beer.csv")

    training, testing = split_data(data)
    target_feature_value = "style"

    print(training)
    print("+++++++++++++++++++++++++++++++++++")
    print(testing)

main()
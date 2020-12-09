from Data import get_data, split_data, remove_beerid, get_class_count, split_for_branches
from Entropy import get_entropy
from InformationGain import get_information_gain, find_split_indexes, choose_best_attribute, predict_attributes
from Tree import create_tree

def main():

    test_results = dict()
    

    #perform the algorithm test
    for i in range(0,10):
        data = get_data("beer.csv")
        data = remove_beerid(data)
        split = 0.666

        target_feature_value = "style"
        attributes = data.columns.values.tolist()
        
        
        training_data, testing_data = split_data(data, split)
        tree = create_tree(training_data, attributes, target_feature_value)
        print("Decision Tree:")
        print(tree)

        correct_predictions = 0.0 # will count number of correst predictions 
        num_rows = 0.0 # will count number of rows in test data
        incorrect_guesses = list()
        for index, row in testing_data.iterrows():
            num_rows += 1.0
            predicted_attribute = predict_attributes(row, tree)
            actual_attribute = row[target_feature_value]
            
            if predicted_attribute == actual_attribute:
                correct_predictions += 1.0
            else:
                incorrect_guesses.append((index, predicted_attribute , actual_attribute))
            
        accuracy_percent = '{0:.2f}'.format((float(correct_predictions) / float(num_rows)) * 100)
        test_results[i+1] = accuracy_percent
        print("\nAccuracy Percent: ", accuracy_percent, "%")
        print("\nIncorrect Guesses:")
        for index, predicted, actual in incorrect_guesses:
            print("Index: ", index, "\tPredicted: ", predicted, "\tActual: ", actual)
        print("------------------------")
    
    accuracy_average = 0.0
    for i in test_results:
        accuracy_average = accuracy_average + float(test_results[i])
    
    accuracy_average = accuracy_average / len(test_results)
    print("Average accurate percentage: ", accuracy_average, "%")

main()
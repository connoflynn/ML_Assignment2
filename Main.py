import datetime
from Data import get_data, split_data, remove_beerid, get_class_count, split_for_branches
from Entropy import get_entropy
from InformationGain import get_information_gain, find_split_indexes, choose_best_attribute, predict_attributes
from Tree import create_tree

def main():
    begin_time = datetime.datetime.now()

    test_results = dict()
    all_incorrect_guesses = list() # will be a list of lists containing the incorrect guesses for each iteration
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
        test_results[i+1] = accuracy_percent # add accuracy to test_results
        print("\nAccuracy Percent: ", accuracy_percent, "%")
        print("\nIncorrect Guesses:")
        for index, predicted, actual in incorrect_guesses:
            print("Index: ", index, "\tPredicted: ", predicted, "\tActual: ", actual)
        all_incorrect_guesses.append(incorrect_guesses)
        print("------------------------")
    
    accuracy_average = 0.0
    for i in test_results:
        accuracy_average = accuracy_average + float(test_results[i])
    
    accuracy_average = accuracy_average / len(test_results)
    print("Average accurate percentage: ", accuracy_average, "%")
    
    print("Writing results to file.") 
    # write a summary of the results to a csv file
    with open("test_results.txt",'w') as f:
        for result in test_results.items():
            f.write("Test: %s" % str(result[0]))
            f.write("\nAccuracy: %s" % str(result[1]))
            f.write("\nIncorrect Guesses:")
            for i in range(0,len(all_incorrect_guesses[result[0]-1])):
                f.write("\nIndex: %s" % str(all_incorrect_guesses[result[0]-1][i][0]))
                f.write("\tPredicted: %s" % str(all_incorrect_guesses[result[0]-1][i][1]))
                f.write("\tActual: %s" % str(all_incorrect_guesses[result[0]-1][i][2]))
            f.write("\n\n")
        f.close()
    
    endtime = datetime.datetime.now()
    time_taken = endtime - begin_time
    print("Time taken to run: ", time_taken)

main()
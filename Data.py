import pandas as pd
import numpy as np

# A class for working with the input data 

# function to get the data from the csv file
def get_data(filename):
    return pd.read_csv(filename, header=0, delimiter=",")
    
# function to split data into training and test data    
def split_data(data):
    #shuffle data
    data_after_shuffle = data.sample(frac=1)

	#assign ratio for data split 2/3 for train 1/3 for test
    split_ratio = 0.666
	#assign training data using shuffled from top of data from bottom 2 thirds
    training = data_after_shuffle[0:int(np.ceil(len(data)*split_ratio))]
	#assign test data using shuffled from top of data from top 1 third
    testing = data_after_shuffle[int(np.ceil(len(data)*split_ratio))+1:len(data)]

    return training, testing

# function to return the number of classes in the dataset
def get_number_classes(data):
    return len(data.columns)

# function that removes beer_id from the data set as it is irrelevant 
def remove_beerid(data):
    return data.drop(columns = "beer_id")

# counts instances of each target option in the data and returns result in a dictionary
def get_class_count(data, target):
    results = dict()
    target_col = data.loc[:, target] # get location of target column
    
    for target_result in target_col:   # counts number of instances of each target type
        if target_result not in results:
            results[target_result] = 0
        results[target_result] += 1

    return results
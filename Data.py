import pandas as pd
import numpy as np

# A class for working with the input data 

# function to get the data from the csv file
def get_data(filename):
    return pd.read_csv(filename, header=0, delimiter=",")

# function that removes beer_id from the data set as it is irrelevant 
def remove_beerid(data):
    return data.drop(columns = "beer_id")
    
# function to split data into training and test data    
def split_data(data, ratio):
    #shuffle data
    shuffled_data = data.sample(frac=1)
    split_ratio = ratio  

    #add first portion of data to training variable
    training = shuffled_data[0:int(np.ceil(len(data)*split_ratio))]

    # add everything after first portion to testing variable
    testing = shuffled_data[int(np.ceil(len(data)*split_ratio))+1:len(data)]

    return training, testing

# counts instances of each target option in the data and returns result in a dictionary
def get_class_count(data, target):
    results = dict()
    target_col = data.loc[:, target] # get target column
    
    for target_result in target_col:   # counts number of instances of each target type
        if target_result not in results:
            results[target_result] = 0
        results[target_result] += 1

    return results
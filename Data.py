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
	#assign training data using shuffled from top of data from bottmo 2 thirds
    training = data_after_shuffle[0:int(np.ceil(len(data)*split_ratio))]
	#assign test data using shuffled from top of data from top 1 third
    testing = data_after_shuffle[int(np.ceil(len(data)*split_ratio))+1:len(data)]
    
    return training, testing

import math

from Data import get_class_count

# class to calculate the entropy of the training data

def entropy_calc(data, target):
    # Calculate the entropy for all of data
	# This is the measure of how messy the data set is
    # The entropy formula is the occurance of each target result divided by the total number of samples,
    # multiplied by the log base 2 of that result, all multiplied by -1
    
    results = get_class_count(data, target)
    log2 = lambda x: math.log(x) / math.log(2)
    
	#formula calculation
    entropy = 0.0
    for result in results.keys():
        proportion_of_class = float(results[result]) / len(data)
        entropy -= proportion_of_class * log2(proportion_of_class)

    return entropy
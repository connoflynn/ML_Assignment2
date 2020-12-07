import math

from Data import get_class_count

# class to calculate the entropy of the training data
def get_entropy(data, target):

    results = get_class_count(data, target)
    log2 = lambda x: math.log(x) / math.log(2)
    
	#formula calculation
    entropy = 0.0
    for result in results.keys():
        proportion_of_class = float(results[result]) / len(data)
        entropy -= proportion_of_class * log2(proportion_of_class)

    return entropy
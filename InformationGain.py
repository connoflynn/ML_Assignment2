
from Entropy import get_entropy

# class to calculte information gain of the training data

def get_information_gain(data, target, attribute, attribute_index):
    # Information Gain formula:
    # Ent(S) - sum(|Sv|/|S| * Ent(Sv))
    data_length = len(data)
    split_value = data[attribute][attribute_index]

    #splits data into less than and greater than or equal of value at index given
    left_split = data[data[attribute] < split_value]
    right_split = data[data[attribute] >= split_value]

    entropy = get_entropy(data,target)

    # information gain calculation 
    information_gain = entropy - ((len(left_split) / float(data_length)) * get_entropy(left_split, target)) - ((len(right_split) / float(data_length)) * get_entropy(right_split, target))
    
    return information_gain

# given data, will find split value and index number for each attribute
def find_split_indexes(data, target):
    split_value = 0.0

    # will create a dictionary with each attribute and the index to split the data at
    split_values = dict()
    split_indexes = dict()

    for (columnName, columnData) in data.iteritems():
        if columnName != target:
            #sort the values lowest to highest
            sorted_values = columnData.sort_values()
            information_gain = 0.0
            # for loop to iterate through the sorted values and finds the information gain if each item was the split value
            # the item with the highest information gain is chosen as the split value
            for (index, value) in sorted_values.iteritems():
                if get_information_gain(data, target, columnName, index) > information_gain:
                    information_gain = get_information_gain(data, target, columnName, index)
                    split_values[columnName] = value
                    split_indexes[columnName] = index

    return split_values, split_indexes 


# function to choose the attribute with highest information gain
def choose_best_attribute(data, target, split_values, split_indexes):
    best_info_gain = ()
    info_gain = 0.0
    for (attribute, index) in split_indexes.items():
        info = get_information_gain(data, target, attribute, index)
        if info > info_gain :
            info_gain = info
            best_info_gain = (attribute, index, split_values[attribute], info)
    
    # will return a tuple containing the name of the attribute and the info gain value
    return best_info_gain

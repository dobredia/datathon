import numpy as np

def one_hot(value, vocab):
    one_hot_array = np.full(len(vocab), '0')
    one_hot_bool_mask = np.array(vocab) == value
    one_hot_array[one_hot_bool_mask] = 1
    return one_hot_array.tolist()
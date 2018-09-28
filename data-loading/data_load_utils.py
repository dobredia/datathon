import numpy as np

def one_hot(value, vocab):
    one_hot_array = np.full(len(vocab), '0')
    one_hot_bool_mask = np.array(vocab) == value
    one_hot_array[one_hot_bool_mask] = 1
    return one_hot_array.tolist()

def process_date_air_official(date_string):
    split = date_string.split(' ')
    date, time, time_zone = split[0], split[1], split[2]
    date_split = date.split('-')
    year, month, day = date_split[0], date_split[1], date_split[2]
    time_split = time.split(':')
    hour = time_split[0]
    time_zone_delay = int(time_zone[1:3])
    hour += time_zone_delay
    
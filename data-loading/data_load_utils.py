import numpy as np
from dateutil.parser import parse

year_vocab = [2017, 2018]

def one_hot(value, vocab):
    one_hot_array = np.full(len(vocab), '0')
    one_hot_bool_mask = np.array(vocab) == value
    one_hot_array[one_hot_bool_mask] = 1
    return one_hot_array.tolist()

def time_hash(year, month, day, hour):
    return hour + day * 24 + month * 24 * 30 + year * 24 * 30 * 12

def date_hash(year, month, day):
    return day + month * 30 + year * 30 * 12

def process_date_air_official(date_string):
    dt = parse(date_string)
    t = dt.utctimetuple()
    year, month, day, hour = t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour
    return year, month, day, hour

from os import listdir
from os.path import isfile, join
import codecs
from geohash.geohashdecode import decode1
from data_loading.data_load_utils import time_hash, process_date_str

'''
    0.  time,
    1.  geohash,
    2.  P1 PM10,
    3.  P2 PM2.5,
    4.  temperature,
    5.  humidity,
    6.  pressure
'''

def rewrite_lines_0(new_file_path = '../../datathlon data/air-quality-citizen/Processed_sample_data_bg_2018.csv', file_to_read_path = '../../datathlon data/air-quality-citizen/sample_data_bg_2018.csv'):
    new_file = open(new_file_path, "w")
    f = codecs.open(file_to_read_path, "r", "utf-8")
    lines = f.readlines()

    for line in lines[:1]:
        split = line.split(',')
        array = [
            split[0], # time
            'lon', # geohash / lon
            'lat', # geohash / lat
            split[2], # P1 PM10
            # split[3], # P2 PM2.5
            split[4], # temperature
            split[5],  # humidity
            split[6][:-1],  # pressure
        ]
        new_file.write(','.join(array))

def rewrite_lines(new_file_path = '../../datathlon data/air-quality-citizen/Processed_sample_data_bg_2018.csv', file_to_read_path = '../../datathlon data/air-quality-citizen/sample_data_bg_2018.csv'):
    new_file = open(new_file_path, "a")
    f = codecs.open(file_to_read_path, "r", "utf-8")
    lines = f.readlines()

    for line in lines[1:]:
        split = line.split(',')
        lon, lat = decode1(split[1])
        array = [
            split[0], # time
            str(lon), # geohash / lon
            str(lat), # geohash / lat
            split[2], # P1 PM10
            # split[3], # P2 PM2.5
            split[4], # temperature
            split[5],  # humidity
            split[6][:-1],  # pressure
        ]
        new_file.write(','.join(array))

def rewrite_lines_for_heat_map(
        new_file_path = '../../datathlon data/air-quality-citizen/Processed_sample_data_bg_2018.csv',
        file_to_read_path = '../../datathlon data/air-quality-citizen/sample_data_bg_2018.csv',
        write_mode = 'w',
        include_header = False):

    new_file = open(new_file_path, write_mode)
    f = codecs.open(file_to_read_path, "r", "utf-8")
    lines = f.readlines()
    if include_header:
        new_file.write('DatetimeEndHash,Longitude,Latitude,Concentration\n')
    count = 0
    for line in lines[1:]:
        split = line.split(',')
        year, month, day, hour = process_date_str(split[0])
        _time_hash = time_hash(year, month, day, hour)
        try:
            lon, lat = decode1(split[1])
        except:
            print('skipped record because can not decode location hash : ', split[1])
            continue
        pm_10 = split[2]
        array = [
            str(_time_hash),
            str(lon),
            str(lat),
            pm_10 + '\n'
        ]
        new_file.write(','.join(array))
        count += 1
        if count % 100000 == 0:
            print(count / len(lines) * 100, '%')

def merge_all_files_for_heatmap(
        new_file_path = '../../datathlon data/air-quality-citizen/Processed_heatmap_all_citizen.csv',
        file_paths = ['../../datathlon data/air-quality-citizen/data_bg_2017.csv/data_bg_2017.csv', '../../datathlon data/air-quality-citizen/data_bg_2018.csv/data_bg_2018.csv']):
    new_file = open(new_file_path, 'a')
    new_file.write('DatetimeEndHash,Longitude,Latitude,Concentration\n')
    for path in file_paths:
        rewrite_lines_for_heat_map(new_file_path = new_file_path, file_to_read_path = path, write_mode = 'a')

if __name__ == "__main__":
    # rewrite_lines_0()
    # rewrite_lines()
    # rewrite_lines_for_heat_map(include_header = True)
    merge_all_files_for_heatmap()
import codecs
from geohash.geohashdecode import decode1

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
            #split[2], # P1 PM10
            split[3], # P2 PM2.5
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
            #split[2], # P1 PM10
            split[3], # P2 PM2.5
            split[4], # temperature
            split[5],  # humidity
            split[6][:-1],  # pressure
        ]
        new_file.write(','.join(array))

if __name__ == "__main__":
    rewrite_lines_0()
    rewrite_lines()
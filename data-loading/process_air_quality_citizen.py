import codecs

'''
    0.  time,
    1.  geohash,
    2.  P1 PM10,
    3.  P2 PM2.5,
    4.  temperature,
    5.  humidity,
    6.  pressure
'''

def rewrite_lines(new_file_path = '../../datathlon data/air-quality-citizen/Processed_sample_data_bg_2018.csv', file_to_read_path = '../../datathlon data/air-quality-citizen/sample_data_bg_2018.csv'):
    new_file = open(new_file_path, "w")
    f = codecs.open(file_to_read_path, "r", "utf-8")
    lines = f.readlines()
    for line in lines:
        split = line.split(',')
        array = [
            split[0], # time
            split[1], # geohash
            split[2], # P1 PM10
            split[3], # P2 PM2.5
            split[4], # temperature
            split[5],  # humidity
            split[6][:-1],  # pressure
        ]
        new_file.write(','.join(array) )

if __name__ == "__main__":
    rewrite_lines()
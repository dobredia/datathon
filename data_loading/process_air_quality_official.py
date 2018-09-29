import codecs
from data_loading.data_load_utils import one_hot, process_date_air_official, time_hash, process_date_air_official

AirQualityStationVocab = ['STA-BG0040A', 'STA-BG0050A', 'STA-BG0052A', 'STA-BG0054A', 'STA-BG0073A', 'STA-BG0079A']
SamplingProcessVocab = ['SPP-BG_A_BETA_andersenFH62IR', 'SPP-BG_A_BETA_thermo5030SHARP']

'''
    0.  Countrycode,
    1.  Namespace,
    2.  AirQualityNetwork,
    3.  AirQualityStation,
    4.  AirQualityStationEoICode,
    5.  SamplingPoint,
    6.  SamplingProcess,
    7.  Sample,
    8.  AirPollutant,
    9.  AirPollutantCode,
    10. AveragingTime,
    11. Concentration,
    12. UnitOfMeasurement,
    13. DatetimeBegin,
    14. DatetimeEnd,
    15. Validity,
    16. Verification
'''

def rewrite_lines(new_file_path = '../../datathlon data/air-quality-official/Processed_BG_5_9421_2013_timeseries.csv', file_to_read_path = '../../datathlon data/air-quality-official/BG_5_9421_2013_timeseries.csv'):
    new_file = open(new_file_path, "w")
    f = codecs.open(file_to_read_path, "r", "utf-16")
    lines = f.readlines()
    for line in lines[1:]:
        split = line.split(',')
        array = []
        array += one_hot(split[3], AirQualityStationVocab) # AirQualityStation
        array += one_hot(split[6], SamplingProcessVocab)   # SamplingProcess
        array += [
            split[11], # Concentration
            split[13], # DatetimeBegin
            split[14]  # DatetimeEnd
        ]
        process_date_air_official(split[13])
        new_file.write(','.join(array) + '\n')

def long_lat_of_official_air_station(air_station_name):
    if air_station_name == 'STA-BG0040A':
        return 23.310972, 42.732292
    elif air_station_name == 'STA-BG0050A':
        return 23.296786, 42.680558
    elif air_station_name == 'STA-BG0052A':
        return 23.400164, 42.666508
    elif air_station_name == 'STA-BG0054A':
        return 23.33605, 42.690353
    elif air_station_name == 'STA-BG0073A':
        return 23.268403, 42.669797
    elif air_station_name == 'STA-BG0079A':
        return 23.383271, 42.655488

def rewrite_lines_for_heatmap(new_file_path = '../../datathlon data/air-quality-official/Processed_heatmap_BG_5_9421_2013_timeseries.csv', file_to_read_path = '../../datathlon data/air-quality-official/BG_5_9421_2013_timeseries.csv'):
    new_file = open(new_file_path, "w")
    f = codecs.open(file_to_read_path, "r", "utf-16")
    lines = f.readlines()
    for line in lines[1:]:
        split = line.split(',')
        year, month, day, hour = process_date_air_official(split[14]) # DatetimeEnd
        _time_hash = time_hash(year, month, day, hour)
        long, lat = long_lat_of_official_air_station(split[3])
        array = [
            str(_time_hash), # DatetimeEnd hash
            str(long),       # Longitude
            str(lat),        # Latitude
            split[11],       # Concentration
        ]
        new_file.write(','.join(array) + '\n')

if __name__ == "__main__":
    rewrite_lines_for_heatmap()


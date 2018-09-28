import codecs

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
    for line in lines:
        split = line.split(',')
        array = [
            split[3], # AirQualityStation
            split[6], # SamplingProcess
            split[11], # Concentration
            split[13], # DatetimeBegin
            split[14] # DatetimeEnd
        ]
        new_file.write(','.join(array) + '\n')

if __name__ == "__main__":
    rewrite_lines()
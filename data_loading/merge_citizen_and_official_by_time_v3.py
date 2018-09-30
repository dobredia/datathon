from os import listdir
from os.path import isfile, join
import codecs
from geohash.geohashdecode import decode1
from data_loading.data_load_utils import time_hash, process_date_str
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data_loading.process_air_quality_official import data_for_heatmap as data_for_heatmap_official
from scipy import stats

'''
    0. DatetimeEndHash	
    1. Longitude	
    2. Latitude	
    3. Concentration
'''

def merge_citize_and_official():
    official = pd.read_csv('../../datathlon data/air-quality-official/Processed_heatmap_all.csv').as_matrix()
    citizen = pd.read_csv('../../datathlon data/air-quality-citizen/Processed_heatmap_all_citizen.csv').as_matrix()
    by_time = {}

    for i in range(len(official)):
        if by_time.__contains__(official[i][0]):
            by_time[official[i][0]] += [official[i]]
        else:
            by_time[official[i][0]] = [official[i]]

    for key in by_time:
        matrix = by_time[key]
        for passnum in range(len(matrix) - 1, 0, -1):
            for i in range(passnum):
                if matrix[i][2] > matrix[i + 1][2]:
                    temp = matrix[i]
                    matrix[i] = matrix[i + 1]
                    matrix[i + 1] = temp
        by_time[key] = matrix

    citizen_enriched_with_official = []
    for i in range(len(citizen)):
        if by_time.__contains__(citizen[i][0]):
            try:
                official_by_time = by_time[citizen[i][0]]
                official_concentrations = [official_by_time[0][3], official_by_time[1][3], official_by_time[2][3], official_by_time[3][3]]
                if len(official_by_time) == 5:
                    official_concentrations += [ official_by_time[4][3]]
                else:
                    official_concentrations += [0]
                enriched = citizen[i].tolist() + official_concentrations
                citizen_enriched_with_official.append(enriched)
            except:
                # print('recored skipped beacuse of error')
                print(official_by_time)

    '''
        0. DatetimeEndHash	
        1. Longitude	
        2. Latitude	
        3. Concentration
        4. Concentration Official 1
        5. Concentration Official 2
        6. Concentration Official 3
        7. Concentration Official 4
        8. Concentration Official 5
    '''

    np_citizen_enriched_with_official = np.asanyarray(citizen_enriched_with_official)
    print(np_citizen_enriched_with_official.shape)
    citizen_concentrations = np.squeeze(np_citizen_enriched_with_official[:, 3:4])
    official_concentration_1 = np.squeeze(np_citizen_enriched_with_official[:, 4:5])
    official_concentration_2 = np.squeeze(np_citizen_enriched_with_official[:, 5:6])
    official_concentration_3 = np.squeeze(np_citizen_enriched_with_official[:, 6:7])
    official_concentration_4 = np.squeeze(np_citizen_enriched_with_official[:, 7:8])
    official_concentration_5 = np.squeeze(np_citizen_enriched_with_official[:, 8:9])

    pearson_r_1 = stats.pearsonr(citizen_concentrations, official_concentration_1)[0]
    pearson_r_2 = stats.pearsonr(citizen_concentrations, official_concentration_2)[0]
    pearson_r_3 = stats.pearsonr(citizen_concentrations, official_concentration_3)[0]
    pearson_r_4 = stats.pearsonr(citizen_concentrations, official_concentration_4)[0]
    pearson_r_5 = stats.pearsonr(citizen_concentrations, official_concentration_5)[0]

    print('Pearson R', pearson_r_1, pearson_r_2, pearson_r_3, pearson_r_4, pearson_r_5)

if __name__ == "__main__":
    merge_citize_and_official()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data_loading.process_air_quality_official import data_for_heatmap as data_for_heatmap_official

if __name__ == "__main__":

    '''
        OFFICIAL DATA
    '''

    data_official = pd.read_csv('../../datathlon data/air-quality-official/Processed_heatmap_all.csv')
    # print(data.head())
    # print(data.shape)
    # print(data.columns)
    couple_columns_official = data_official[['Concentration', 'Longitude', 'Latitude']]
    # print(couple_columns.head())
    # print(data.ix[:, ['Concentration', 'Longitude', 'Latitude']].head())
    data_lat_long_official = couple_columns_official.groupby(['Latitude', 'Longitude']).mean()
    # print(data_lat_long.shape)
    # print(data_lat_long.head(10))

    data_lat_long_official = data_lat_long_official.reset_index()
    # print(data_lat_long.head())
    # major_ticks = np.arange(0.2, 0.5, 0.01)
    # minor_ticks = np.arange(0, 50, 1)

    '''
        CITIZEN DATA
    '''

    data_citizen = pd.read_csv('../../datathlon data/air-quality-citizen/Processed_heatmap_all_citizen.csv')
    # print(data.head())
    # print(data.shape)
    # print(data.columns)
    couple_columns_citizen = data_citizen[['Concentration', 'Longitude', 'Latitude']]
    # print(couple_columns.head())
    # print(data.ix[:, ['Concentration', 'Longitude', 'Latitude']].head())
    data_lat_long_citizen = couple_columns_citizen.groupby(['Latitude', 'Longitude']).mean()
    # print(data_lat_long.shape)
    # print(data_lat_long.head(10))

    data_lat_long_citizen = data_lat_long_citizen.reset_index()
    # print(data_lat_long.head())
    # major_ticks = np.arange(0.2, 0.5, 0.01)
    # minor_ticks = np.arange(0, 50, 1)

    '''
        PLOT
    '''

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(1, 1, 1)
    s_1 = ax.scatter('Latitude', 'Longitude', c = 'Concentration', data = data_lat_long_official, cmap = 'RdYlGn_r', marker = 's', s = 190)
    ax.axis([
        data_lat_long_official['Latitude'].min() - 0.05,
        data_lat_long_official['Latitude'].max() + 0.05,
        data_lat_long_official['Longitude'].min() - 0.05,
        data_lat_long_official['Longitude'].max() + 0.05
    ])
    ax.grid(which='both', alpha = 0.3)
    ax.grid(which='major', alpha = 0.3)
    ax.set_xlabel('Latitude', fontsize = 10);
    ax.set_ylabel('Longitude', fontsize = 10);
    ax.set_title('Concentration', size = 15)

    clip_config = {
        'Concentration': data_lat_long_official['Concentration'].max(),
        'Latitude': data_lat_long_citizen['Latitude'].max(),
        'Longitude': data_lat_long_citizen['Longitude'].max()
    }
    data_lat_long_citizen = data_lat_long_citizen.clip(upper = pd.Series(clip_config), axis=1)

    cbar = plt.colorbar(mappable = s_1, ax = ax)

    s_2 = ax.scatter('Latitude', 'Longitude', c='Concentration', data=data_lat_long_citizen, cmap='RdYlGn_r', marker='.', s=50)
    # cbar = plt.colorbar(mappable=s_2, ax=ax)

    plt.show()
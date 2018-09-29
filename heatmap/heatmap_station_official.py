import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data_loading.process_air_quality_official import data_for_heatmap as data_for_heatmap_official

if __name__ == "__main__":
    # data = data_for_heatmap_official()
    # time_hash, long, lat, concentration = data.__next__()

    data = pd.read_csv('../../datathlon data/air-quality-official/Processed_heatmap_BG_5_9421_2013_timeseries.csv')
    # print(data.head())
    # print(data.shape)
    # print(data.columns)
    couple_columns = data[['Concentration', 'Longitude', 'Latitude']]
    # print(couple_columns.head())
    # print(data.ix[:, ['Concentration', 'Longitude', 'Latitude']].head())
    data_lat_long = couple_columns.groupby(['Latitude', 'Longitude']).mean()
    # print(data_lat_long.shape)
    # print(data_lat_long.head(10))

    data_lat_long = data_lat_long.reset_index()
    print(data_lat_long.head())
    major_ticks = np.arange(0, 50, 5)
    minor_ticks = np.arange(0, 50, 1)

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(1, 1, 1)
    s = ax.scatter('Latitude', 'Longitude', c = 'Concentration', data = data_lat_long, cmap = 'Blues_r', marker = 's', s = 190)
    ax.axis([
        data_lat_long['Latitude'].min() - 10,
        data_lat_long['Latitude'].max() + 10,
        data_lat_long['Longitude'].min() - 10,
        data_lat_long['Longitude'].max() + 10
    ])
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor = True)
    ax.set_yticks(major_ticks)
    ax.grid(which='both', alpha = 0.3)
    ax.grid(which='major', alpha = 0.3)
    ax.set_xlabel('Latitude', fontsize = 10);
    ax.set_ylabel('Longitude', fontsize = 10);
    ax.set_title('Concentration', size = 15)

    cbar = plt.colorbar(mappable = s, ax = ax)

    plt.show()


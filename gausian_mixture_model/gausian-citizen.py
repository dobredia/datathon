import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from sklearn import mixture
import pandas as pd

'''
    0. Latitude  
    1. Longitude  
    2. Concentration
'''

data = pd.read_csv('../../datathlon data/air-quality-citizen/Processed_heatmap_all_citizen.csv')
couple_columns = data[['Concentration', 'Longitude', 'Latitude']]
data_lat_long = couple_columns.groupby(['Latitude', 'Longitude']).mean()
data_lat_long = data_lat_long.reset_index()
np_data = data_lat_long.as_matrix()
X_train = np_data[:, 0:2]

# fit a Gaussian Mixture Model with two components
clf = mixture.GaussianMixture(n_components=8, covariance_type='full')
clf.fit(X_train)

# display predicted scores by the model as a contour plot
x = np.linspace(data_lat_long['Latitude'].min() - 0.05, data_lat_long['Latitude'].max() + 0.05)
y = np.linspace(data_lat_long['Longitude'].min() - 0.05, data_lat_long['Longitude'].max() + 0.05)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

# CS = plt.contour(X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0),
#                  levels=np.logspace(0, 3, 10))

CS = plt.contour(X, Y, Z)

# CB = plt.colorbar(CS, shrink=0.8, extend='both')
CB = plt.colorbar(CS)

plt.scatter(X_train[:, 0], X_train[:, 1], .8)

plt.title('Negative log-likelihood predicted by a GMM')
plt.axis('tight')
plt.show()
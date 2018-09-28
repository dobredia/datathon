import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
helix = pd.read_csv('./helix_parameters.csv')
helix.head()
helix.shape
helix.columns
couple_columns = helix[['Energy','helix 2 phase', 'helix1 phase']]
couple_columns.head()
helix.ix[:,['Energy','helix 2 phase', 'helix1 phase']].head()
phase_1_2 = couple_columns.groupby(['helix1 phase', 'helix 2 phase']).mean()
phase_1_2.shape
phase_1_2.head(10)
phase_1_2 = phase_1_2.reset_index()
phase_1_2.head()
major_ticks = np.arange(0, 200, 20)
minor_ticks = np.arange(0, 180, 5)

fig = plt.figure(figsize = (6,5))
ax = fig.add_subplot(1,1,1)
s = ax.scatter('helix1 phase', 'helix 2 phase', c = 'Energy',data = phase_1_2, cmap = 'Blues_r', marker = 's',s = 190)
ax.axis([phase_1_2['helix1 phase'].min()-10, phase_1_2['helix1 phase'].max()+10, phase_1_2['helix 2 phase'].min()-10, phase_1_2['helix 2 phase'].max()+10])
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.grid(which='both', alpha = 0.3)
ax.grid(which='major', alpha=0.3)
ax.set_xlabel('helix1 phase', fontsize=10);
ax.set_ylabel('helix 2 phase', fontsize=10);
ax.set_title('Energy from Helix Phase Angles', size = 15)

cbar = plt.colorbar(mappable = s,ax = ax)

plt.show()
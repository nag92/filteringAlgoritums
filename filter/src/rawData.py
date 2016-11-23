'''
Created on Jul 10, 2015

@author: nathaniel
'''
import kalman_filter
import outlier_fitler
import matplotlib as mpl
mpl.rc("savefig", dpi=150)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#impoirt and save data from CSV files
df = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/filter/usbl_pose.csv', index_col=None)
#df2 = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/filter/pose_only.csv', index_col=None)

my_x = df['field.pose.position.x'].values.tolist()
my_y = df['field.pose.position.y'].values.tolist()
#my_z = df2['field.position.z'].values.tolist()
t = range(0, len(my_x))
#plot the raw and filtered data
f1 = plt.figure()
ax1 = f1.add_subplot(111)
plt.xlabel('time step')
plt.ylabel('distance (meters)')
plt.title('Raw')
ax1.scatter(t, my_x, color='b',label='Raw X')
ax1.scatter(t, my_y, color='r',label='Raw Y')
legend = ax1.legend(loc='lower left', shadow=True)

frame = legend.get_frame()
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
plt.show()

        
    
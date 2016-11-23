from matplotlib import matplotlib_fname
from mpl_toolkits.mplot3d import Axes3D
import sys
from matplotlib.pyplot import plot
from numpy import mean, std
from cairo._cairo import Matrix
from numpy.matlib import rand
import outlier_filter
print 'version is:', sys.version

import matplotlib as mpl
mpl.rc("savefig", dpi=150)

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib



filt_x = []
filt_y = []
filt_depth = [] 
out_x = []
out_y = []
out_depth = [] 
df = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/outlier_filter/usbl_data.csv', index_col=None)
#print df
my_x = df['x'].values.tolist()
my_y= df['y'].values.tolist()
my_z =  df['z'].values.tolist()
my_depth =  df['depth'].values.tolist()
n = 20
md =[random.random() for _ in range(0, n)]
#x_list = [random.normalvariate(1.9366,2.58133) for _ in range(0, n)]
#y_list =[random.normalvariate(1.9366,2.58133) for _ in range(0, n)]
x_list = [random.random() for _ in range(0, n)]
y_list =[random.random() for _ in range(0, n)]

def update(x,y,id):
   
    x_list.append(x)
    y_list.append(y)
    x_list.pop(0)
    y_list.pop(0)
    
    v = np.linalg.inv(np.cov(x_list,y_list,rowvar=0))
    r_mean = mean(x_list), mean(y_list)  
    x_diff = np.array([i - r_mean[0] for i in x_list])
    y_diff = np.array([i - r_mean[1] for i in y_list])
    diff_xy = np.transpose([x_diff, y_diff])
    dis = np.sqrt(np.dot(np.dot(np.transpose(diff_xy[n-1]),v),diff_xy[n-1]))
    md.append( dis)
    md.pop(0)
    mu  = np.mean(md)
    sigma = np.std(md)
    if dis < mu + 1.25*sigma:
        filt_x.append(my_x[id])
        filt_y.append(my_y[id])
        filt_depth.append(my_depth[id])
    else:
        out_x.append(my_x[id])
        out_y.append(my_y[id])
        out_depth.append(my_depth[id])

    
    
    
df = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/outlier_filter/usbl_data.csv', index_col=None)
#print df
my_x = df['x'].values.tolist()
my_y= df['y'].values.tolist()
my_z =  df['z'].values.tolist()
my_depth =  df['depth'].values.tolist()

#plt.ion()
fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

ax1.scatter(filt_x,filt_y,filt_depth)#,label="Good Data",color='b')
ax1.scatter(out_x,out_y,out_depth)#,label="Outliers",color='r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Outlier Rejection')

#ax1.legend()


#plt.ioff()

plt.show()





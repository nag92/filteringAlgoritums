
# -*- coding: utf-8 -*-
'''
Created on Jun 27, 2015

@author: nathaniel
'''



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

df = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/outlier_filter/usbl_data.csv', index_col=None)
#print df
my_x = df['x'].values.tolist()
my_y= df['y'].values.tolist()
my_z =  df['z'].values.tolist()
my_depth =  df['depth'].values.tolist()

d1 = (my_x[0]*my_x[0]+my_y[0]*my_y[0]+my_z[0]*my_z[0] )**.5

out_x = []
out_y = []
out_depth = [] 
filt_x = []
filt_y = []
filt_depth = [] 

delta =[]
for i in xrange(len(my_x)-1):
   
    delta.append( ( (my_x[i]-my_x[i-1])**2+ (my_y[i]-my_y[i-1])**2+ (my_z[i]-my_z[i-1])**2 )**.5)
print mean(delta)
print np.std(delta)


#cumpute the 
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

    

n = 10
md =[random.random() for _ in range(0, n)]
#x_list = [random.normalvariate(1.9366,2.58133) for _ in range(0, n)]
#y_list =[random.normalvariate(1.9366,2.58133) for _ in range(0, n)]
x_list = [random.random() for _ in range(0, n)]
y_list =[random.random() for _ in range(0, n)]

print x_list
print y_list
#outlier_filter.start()
for i in xrange(len(my_x)):
    update(my_x[i], my_y[i],i)
   # outlier_filter.filter(my_x[i], my_y[i],my_depth[i] )
std = np.std(md)
mean = np.mean(md) 
print std
print mean


    
#plt.ion()
fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

ax1.scatter(filt_x,filt_y,filt_depth,label="Good Data",color='b')
ax1.scatter(out_x,out_y,out_depth,label="Outliers",color='r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Outlier Rejection')

ax1.legend()


#plt.ioff()

plt.show()








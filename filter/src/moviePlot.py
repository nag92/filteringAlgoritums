'''
Created on Jul 3, 2015

@author: nathaniel, I&E summer 2015

This program tests the outlier and kalman filer in 3D

'''

import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import makeGraph
import outlier_fitler
import kalman_filter
import numpy as np
import random
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

mpl.rc("savefig", dpi=150)
#plt.ion()
fig = plt.figure()
ax = Axes3D(fig)
df = pd.DataFrame.from_csv('/home/nathaniel/Documents/pythonWorkSpace/outlier_filter/usbl_data.csv', index_col=None)
my_x = df['x'].values.tolist()
my_y= df['y'].values.tolist()
my_z =  df['z'].values.tolist()
my_depth =  df['depth'].values.tolist()
new_x = []
new_y = []
new_z = []

if __name__ == '__main__':
    #get data from CSV file and save it into lists
   
    #pri
    #make all the Kalman filer parameters

    dt = 1
    
    pos = np.matrix([[0],#v_x
                     [0],#v_y
                     [0],#v_z
                     [0],#x
                     [0],#y
                     [0]])#z
    
    A = np.matrix([[1,  0,  0,  0, 0, 0,],
                   [0,  1,  0,  0, 0, 0,],
                   [0,  0,  1,  0, 0, 0,],
                   [dt, 0,  0,  1, 0, 0,],
                   [0,  dt, 0,  0, 1, 0,],
                   [0,  0,  dt, 0, 0, 1, ]])
    B = np.matrix([0])
    C = np.eye(pos.shape[0])
    Q = np.eye(pos.shape[0])*.5
    R = np.eye(pos.shape[0])*5000
    P = np.eye(pos.shape[0])
    U = np.matrix( [[0]])
    Z = np.matrix( [[0],[0],[0],[0],[0],[0] ])
    
    kalman = kalman_filter.kalman_filter(A,B,C,Q,P,R,pos)
    #plt.ion()
    
  
    #loop throught data
    for i in xrange(len(my_x)):
        print i
        #if not outlier out it into kalman filter
        if(outlier_fitler.outlier(my_x[i], my_y[i],my_depth[i] )):
            #print the NOT outleirs
            #ax.scatter(my_x[i], my_y[i],-my_depth[i],color='b')
            #calculate and get the kalman points
            Z = np.matrix( [[0],[0],[0],[my_x[i]],[my_y[i]],[my_depth[i]] ])
            kalman.move(U,Z)
            pos = kalman.getState()
            #print the kalman points
            #ax.scatter(pos[3], pos[4],-pos[5],color='g')
            new_x.append(pos[3])
            new_y.append(pos[4])
            new_z.append(pos[5])
        else:
            if len(new_x) == 0:
                new_x.append( 0) 
                new_y.append( 0)
                new_z.append( 0)
            else:
                new_x.append( new_x[i-1])
                new_y.append(new_y[i-1])
                new_z.append(new_z[i-1])
        #update graph thing

print new_x

def init():
    #x = np.linspace(0, 100, 100)
    #y = np.linspace(0, 100, 100)
    #init.i+=1
    #print init.i
    ax.scatter(my_x, my_y, my_z, marker='o', c="r")
    ax.scatter(new_x, new_y, new_z, marker='o', c="b")

def animate(i):
    ax.view_init(elev=10., azim=i)
#init.i = 0  
# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init(),
                               frames=300, interval=20, blit=True)
# Save
anim.save('basic_animation3.mov', fps=24, extra_args=['-vcodec', 'libx264'])

print "done"




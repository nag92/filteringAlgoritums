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


mpl.rc("savefig", dpi=150)
mpl.rcParams.update({'font.size': 16})
# plt.ion()




if __name__ == '__main__':
    # get data from CSV file and save it into lists
    df = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/usbl_pose.csv', index_col=None)
    df2 = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/pose_only.csv', index_col=None)

    my_x = df['field.pose.position.x'].values.tolist()  
    my_y = df['field.pose.position.y'].values.tolist()
    my_depth = df2['field.position.z'].values.tolist()
    for i in xrange(len(my_depth)):
        my_depth[i] = -(1000 * my_depth[i] - 101.325) / 9.81
        print my_depth[i]
    print len(my_x)
    print len(my_depth)
    step = int(len(my_depth) / len(my_x)) + 1
    print step
    plt, ax = makeGraph.makeGraph()
    # make all the Kalman filer parameters

    dt = 1
    
    pos = np.matrix([[0],  # v_x
                     [0],  # v_y
                     [0],  # v_z
                     [0],  # x
                     [0],  # y
                     [0]])  # z
    
    A = np.matrix([[1, 0, 0, 0, 0, 0, ],
                   [0, 1, 0, 0, 0, 0, ],
                   [0, 0, 1, 0, 0, 0, ],
                   [dt, 0, 0, 1, 0, 0, ],
                   [0, dt, 0, 0, 1, 0, ],
                   [0, 0, dt, 0, 0, 1, ]])
    B = np.matrix([0])
    C = np.eye(pos.shape[0])
    Q = np.eye(pos.shape[0]) * .05
    R = np.eye(pos.shape[0]) * 5000
    P = np.eye(pos.shape[0])
    U = np.matrix([[0]])
    Z = np.matrix([[0], [0], [0], [0], [0], [0] ])
    
    kalman = kalman_filter.kalman_filter(A, B, C, Q, P, R, pos)
    # plt.ion()
    
    # plt.show()
    k = -1
    # loop throught data
    for i in xrange(len(my_depth)):
        print 'i : ' + str(i)
       # print i%step
        if(i % step == 0):
            k = int(i / step)
            # print 'k : ' + str(k)
        # if not outlier out it into kalman filter
            if(outlier_fitler.outlier(my_x[k], my_y[k], my_depth[i])):
                # print the NOT outleirs
                # ax.scatter(my_x[k], my_y[k],my_depth[i],color='b')
                # calculate and get the kalman points
            
                Z = np.matrix([[0], [0], [0], [my_x[k]], [my_y[k]], [my_depth[i]] ])
                kalman.move(U, Z)
                pos = kalman.getState()
                # print the kalman points
                ax.scatter(pos[3], pos[4], my_depth[i], color='g')
        
            # print the outliers
            #else:
                #ax.scatter(my_x[k], my_y[k],my_depth[i],color='b    ')
        # print pos
        # print 'x' +str(pos[3])
        # print 'y' +str(pos[4])
        # print 'z' +str(pos[5])
        
        # update graph thing
        #plt.draw()

    #update graph thing
    #plt.ioff()
    plt.show()






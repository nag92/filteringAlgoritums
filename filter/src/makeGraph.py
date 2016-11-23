'''
Created on Jul 3, 2015

@author: nathaniel,I&E summer 2015
make a 3D plot to print to
'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



def makeGraph():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('x(m)')
    ax.set_ylabel('y(m)')
    ax.set_zlabel('z(m)')
    ax.margins(0.1, None)
    #ax.set_title('Movement of the VideoRay in 3D with filtering')
   # ax.text(-8,-8,0, 'Blue = Raw'+ '\n' + 'Red = Outlier'  + '\n' + 'Green = Kalman',fontsize=10, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #plt.ion()
    return  plt,ax
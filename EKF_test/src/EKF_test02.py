'''
Created on Jan 2, 2016

@author: nathaniel
This program tests the EKF on a large test of non-linear data
'''

import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import EKF


df = pd.DataFrame.from_csv('/home/nathaniel/LSP/12-16-55/usbl_pose.csv', index_col=None)
my_x = df['field.pose.position.x'].values.tolist()
my_y = df['field.pose.position.y'].values.tolist()
p = lambda x,u,: x + u*.1
v = lambda x,u,: u + x*0

z1 = lambda x :  x[0] + 0*x[1]+ 0*x[2] + 0*x[3]
z2 = lambda x :0*x[0] + x[1]+ 0*x[2] + 0*x[3]
z3 = lambda x :0*x[0] + 0*x[1]+ x[2] + 0*x[3]
z4 = lambda x :0*x[0] + 0*x[1]+ 0*x[2] + x[3]
g = [ v,v,p,p ]
h = [z1,z2,z3,z4]
x = 0
loc = np.matrix( [ [x],[x],[x],[x] ] )
Q = np.eye(loc.shape[0])*2
R = np.eye(loc.shape[0])*.5
sigma = np.eye(loc.shape[0])
ekf = EKF.EKF(g,h,sigma,Q,R,loc)
real_path = []
predicted_path = []

vx = 1

for ii in xrange(len(my_x)):
    
    real_path.append(my_x[ii])
    u = [ vx,vx,vx,vx ]
    z = [[0],[0],[my_x[ii]],[my_y[ii]] ]
    temp =  np.array( ekf.update(u,z))
    predicted_path.append(temp[2][0])
    

f1 = plt.figure()
ax = f1.add_subplot(111)
plt.title("EKF")
plt.xlabel('time')
plt.ylabel('x')
time = xrange(len(my_x))
ax.plot(time, real_path,'b',label='real path' )
ax.plot(time, predicted_path,'r',label= 'Predicted path')

legend = ax.legend(loc='lower center', shadow=True)

frame = legend.get_frame()
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
    
plt.show()
    
    
 
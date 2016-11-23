'''
Created on Aug 16, 2015

@author: nathaniel
'''

from numpy import arctan2, arcsin
import numpy as np
import pandas as pd
import transformations

df = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/pose_only.csv', index_col=None)
# print df
my_x = df['field.orientation.x'].values.tolist()
my_y = df['field.orientation.y'].values.tolist()
my_z = df['field.orientation.z'].values.tolist()
my_w = df['field.orientation.w'].values.tolist()

q1 = my_x[0]
q2 = my_y[0]
q3 = my_z[0]
q0 = my_w[0]
d = 1# 180/3.14
roll = (d * arctan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)))
pitch = (d * arcsin(2 * (q0 * q2 - q3 * q1)))
yaw = (d * arctan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

print "x: " + str(my_x[0]) + " y: " + str(my_y[0]) + " z: " + str(my_z[0]) + " w: " + str(my_w[0])

print "hand: " + "roll: " + str(roll) + " pitch: " + str(pitch) + "  yaw: " +str(yaw)

(roll2, pitch2, yaw2) = transformations.euler_from_quaternion([ my_x[0],my_y[0],my_z[0],my_w[0] ])


print  "tf: " + "roll: " + str(roll2) + " pitch: " + str(pitch2) + "  yaw: " +str(yaw2)


(x,y,z,w) = transformations.quaternion_from_euler(roll, pitch, yaw)


print "x: " + str(x) + " y: " + str(y) + " z: " + str(y) + " w: " + str(w)  

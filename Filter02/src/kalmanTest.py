'''
Created on Sep 4, 2015

@author: nathaniel
'''
import kalman_filter
import numpy as np

pos = np.matrix([[1],  # v_x
                [1]])  # z
A = np.matrix([ [4, 3,],
                [ 3, 2,]])
B = A
C = A
Q = A
R = A
P = A
U = A
Z = pos
    
kalman = kalman_filter.kalman_filter(A, B, C, Q, P, R, pos)
kalman.move(Z,Z)
print kalman.getState()
'''
Created on Dec 31, 2015

@author: nathaniel
'''
import scipy.stats
import math
import numpy as np
from numpy.matlib import rand
import random
import Particle_Filter
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams.update({'font.size': 18})

model = lambda x,u,t : 0.5*x + (25*x)/(1 + x**2) + 8*np.cos(1.2*(t-1)) +  np.sqrt(1)*np.random.normal(0,.1,1)
z = lambda x :(x**2)/20 
x = .1
time = [ii for ii in xrange(0,100)]
real_path = []
predicted_path = []
particle = Particle_Filter.Particle_Filter(x,model,z,100,1,1)

         
for t in time:
    x = model(x,0,t)
    real_path.append(x)
    sensor = z(x)+np.random.normal(0,1,1)
    predicted_path.append(particle.update(0,sensor))
     
 
 
f1 = plt.figure()
ax = f1.add_subplot(111)
plt.title("Partcle Fitler")
plt.xlabel('time')
plt.ylabel('x')

ax.plot(time, real_path,'b',label='real path' )
ax.plot(time, predicted_path,'r',label= 'Predicted path')

legend = ax.legend(loc='lower center', shadow=True)

frame = legend.get_frame()
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
    
plt.show()
import numpy as np
import poly_filter
import matplotlib as mpl
mpl.rc("savefig", dpi=150)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

'''

df = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/13_30_49/usbl_pose.csv', index_col=None)
f1 = plt.figure()
ax1 = f1.add_subplot(111)
plt.title("New wieghting")
plt.xlabel('Time step')
plt.ylabel('Distance (m)')

print "start"

poly = poly_filter.poly_filter(100,3)
 
my_y = df['field.pose.position.y'].values.tolist()


 
for i in xrange(len(my_y)):
	y = my_y[i]

	if poly.update(y):
 		ax1.scatter(i, y, color='b')
 	else:
 		ax1.scatter(i, y, color='r')
 
plt.show()
	
'''



poly = poly_filter.poly_filter(3,1)

print poly.bisquare([1,2,3,3,4,5,6,7,8,9,10]) 







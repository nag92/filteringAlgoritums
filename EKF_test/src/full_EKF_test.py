
import EKF
import md_filter
import poly_filter
import matplotlib as mpl
from operator import pos
mpl.rc("savefig", dpi=150)
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams.update({'font.size': 18})


# impoirt and save data f0rom CSV files
df = pd.DataFrame.from_csv('/home/nathaniel/LSP/12-16-55/usbl_pose.csv', index_col=None)


my_x = df['field.pose.position.x'].values.tolist()
my_y = df['field.pose.position.y'].values.tolist()
t = range(0, len(my_x))

# filter parameters
alpha = 0.10
prop = 4.61
n = 10
p = lambda x, u, : x + u *2
v = lambda x, u, : u + x * 0
z1 = lambda x :  x[0] + 0 * x[1] + 0 * x[2] + 0 * x[3]
z2 = lambda x :0 * x[0] + x[1] + 0 * x[2] + 0 * x[3]
z3 = lambda x :0 * x[0] + 0 * x[1] + x[2] + 0 * x[3]
z4 = lambda x :0 * x[0] + 0 * x[1] + 0 * x[2] + x[3]
g = [ v, v, p, p ]
h = [z1, z2, z3, z4]
x = 0
pos = np.matrix([ [x], [x], [x], [x] ])
vx = 0
u = [ vx, vx, vx, vx ]
Q = np.eye(pos.shape[0]) * 2
R = np.eye(pos.shape[0]) * .5
sigma = np.eye(pos.shape[0])

# filters
ekf = EKF.EKF(g, h, sigma, Q, R, pos)
md_filter = md_filter.md_filter(2, prop, n, [0, 1])
poly_x = poly_filter.poly_filter(100, 3)
poly_y = poly_filter.poly_filter(100, 3)

# hold pos data
new_x = []
new_y = []
new_z = []
out_x = []
out_y = []
out_z = []
count = []

# varible to hold the last position to for plotting reasons
last = pos
outliers = 0
x_good = True
y_good = True

for i in xrange(len(t)):
	# if not outlier out it into kalman filter
	x_good = True
	y_good = True

	if(md_filter.update([my_x[i], my_y[i]])):
		outliers = outliers + 1
		x_good = poly_x.update(my_x[i])
		y_good = poly_y.update(my_y[i])
		if x_good and y_good :
			out_x.append(my_x[i])
			out_y.append(my_y[i])
			count.append(i)
			z = np.matrix([[0], [0], [my_x[i]], [my_y[i]] ])
			temp = np.array(ekf.update(u, z))
			pos = [temp[0][0], temp[1][0], temp[2][0], temp[3][0] ]
			
			new_x.append(temp[2][0])
			new_y.append(temp[3][0])
		else:
			if len(out_x) == 0 :
				new_x.append(pos[2])	   
				new_y.append(pos[3])
			else:   
				new_x.append(new_x[len(new_x) - 1])
				new_y.append(new_y[len(new_y) - 1])
			
	else:
				
		if(len(out_x) == 0):
			out_x.append(pos[2])
			out_y.append(pos[3])
		else:   
			# print len(new_x)
			out_x.append(out_x[len(out_x) - 1])
			out_y.append(out_y[len(out_y) - 1])
		
		
		if(len(new_x) == 0):
			new_x.append(pos[2])
			new_y.append(pos[3])
		else:   
			# print len(new_x)
			new_x.append(new_x[len(new_x) - 1])
			new_y.append(new_y[len(new_y) - 1])





f1 = plt.figure()
ax1 = f1.add_subplot(111)
plt.title("MD filter + poly filter + EKF")
plt.xlabel('Time step')
plt.ylabel('Distance (m)')
# plt.title('Depth')

ax1.scatter(t, my_x, color='b', label='Raw X')
ax1.scatter(t, my_y, color='r', label='Raw Y')
# ax1.scatter(xrange(len(my_z)), my_z, color='k',label='z')
# ax1.scatter(t, out_x, color='m', label='Outlier output X')
#
# ax1.scatter(t, out_y, color='k', label='Outlier output Y')
ax1.scatter(t, new_x, color='g', label='EKF output X')
ax1.scatter(t, new_y, color='y', label='EKF output Y')
# ax1.text(1,6, 'n = ' + str(n),fontsize=20, bbox={'facecolor':'red', 'alpha':0.5, 'pad':20})
ax1.text(-10,10 , unicode(u"\u03B1") + " =  " + str(alpha), fontsize=15)

# ax1.text(-25, 4, 'n=  ' + str(n) + '\n' + 'q = ' + str(q) + '\n' + 'r = ' + str(r) , fontsize=20, bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
# ax2.scatter(t, new_z, color='g')
legend = ax1.legend(loc='lower center', shadow=True)

frame = legend.get_frame()
for label in legend.get_texts():
	label.set_fontsize('large')

for label in legend.get_lines():
	label.set_linewidth(1.5)  # the legend line width



print "good data = " + str(100* float(outliers)/float(len(t))) + "%"
plt.show()

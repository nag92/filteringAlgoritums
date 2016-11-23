'''
Created on Sep 23, 2015
This programs grabs the XY values at a given time ranges
Then finds the mean and std of the clusters at each time 
and the depth clusters
@author: nathaniel
'''
import matplotlib as mpl

mpl.rc("savefig", dpi=150)
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/usbl_pose.csv', index_col=None)
df2 = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/pose_only.csv', index_col=None)

my_x = df['field.pose.position.x'].values.tolist()
my_y = df['field.pose.position.y'].values.tolist()
my_z = df2['field.position.z'].values.tolist()

for i in xrange(len(my_z)):
   my_z[i] = -(1000 * my_z[i] - 101.325) / 9.81
   # print my_z[i]

#depth indexes taken form KingsPointer data, manually measured
depth25 = [ [ 2700,6200], [24000,27000],[46000,50000],[66000,70000],[87000,90000] ]
depth2 = [[9000,14500 ],[26500,30500],[49000,53000],[69000,72500],[91000,94500]  ] 
depth15 = [[14500,18000],[30500, 33000 ],[40000,43000],[52000,56000],[72500,76000], [94000,99000]]
depth1 = [[17500,19500],[33000,36000],[56000,59050],[76000,80500],[98800,102000] ]
depth05= [[19500,23000],[35800,40250],[43000,45500],[59000,67000],[85000,87200],[102000,105050]] 

depths = [ depth05,depth1,depth15,depth2,depth25]

step = int(len(my_z) / len(my_x)) + 1
print len(my_z)
print len(my_x)
k = -1

points = []
allPoints = []
#extract all the points from 
for i in xrange(len(depths)):
    points = []
    for j in xrange(len(depths[i])):
          p1 = int(depths[i][j][0]/step)
          p2 = int(depths[i][j][1]/step)
          points.append( [  my_x[p1:p2],my_y[p1:p2] ]  )
    allPoints.append(points)
     
meanX = []
meanY = []
x = []
y = []
stdX = []
stdY = []
means = []
stds = []
allMeans = []
allstds = []

for i in xrange(len(allPoints)):
	for j in xrange(len(allPoints[i][0])):
		x = allPoints[i][j][0]
		y = allPoints[i][j][1]
		meanX.append(np.mean(x))
		meanY.append( np.mean(y))
		stdX.append(np.std(x))
		stdY.append(np.std(y))
		allMeans.append([meanX, meanY])
		allstds.append([stdX, stdY])
	means.append([ np.mean(meanX) ,  np.mean(meanY) ]  )
	stds.append([ np.mean(stdX) ,  np.mean(stdY) ]  )	

print 'x ' + str(len(allPoints[0][0][1]))
print 'y ' + str(len(allPoints[0][0][0]))


means = np.vstack(means)
print len(means)
t = [ .5, 1, 1.5, 2,2.5]
print  np.vstack(stds)

print np.mean(zip(*stds)[0])					
print np.mean(zip(*stds)[1])	
f1 = plt.figure()
ax1 = f1.add_subplot(111)
ax2 = f1.add_subplot(111)
plt.xlabel('x')
plt.ylabel('y')

#ax1.scatter(t, zip(*stds)[0], color='k', label='mean(std) in X')
#ax1.scatter(t, zip(*stds)[1], color='r', label='mean(std) in Y')
ax2.scatter(allPoints[0][0][0],allPoints[0][0][1],color='r', label='mean(std) in Y' )
ax2.scatter(allPoints[0][1][0],allPoints[0][1][1],color='b', label='mean(std) in Y' )
ax2.scatter(allPoints[0][2][0],allPoints[0][2][1],color='k', label='mean(std) in Y' )
ax2.scatter(allPoints[0][3][0],allPoints[0][3][1],color='m', label='mean(std) in Y' )
ax2.scatter(allPoints[0][4][0],allPoints[0][4][1],color='c', label='mean(std) in Y' )
ax2.scatter(allPoints[0][5][0],allPoints[0][5][1],color='y', label='mean(std) in Y' )
legend = ax1.legend(loc='lower center', shadow=True)

frame = legend.get_frame()
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
    
    
plt.show()
    
   
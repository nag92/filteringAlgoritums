'''
Created on Dec 7, 2015

@author: nathaniel
'''

import poly_filter
import random
import numpy as np

x = []
y = []
weights = []
poly = poly_filter.poly_filter(10,3)
for i in xrange(10):
	y.append(i)
	x.append(i) 

for i in xrange(10):
	weights.append(1)
	 
#print poly.bisquare(x)
print poly.regress(y, x, np.diag(weights))
#print poly.get_residuals(y,x,weights)
'''
poly = poly_filter.poly_filter(10,3)
for i in xrange(20):
	print poly.update(i)
'''



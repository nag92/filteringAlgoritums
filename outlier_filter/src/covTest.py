import numpy as np
import random
size = 3
var_list = []
temp = []

for i in xrange(size):
			temp = [ random.uniform(0, 1) for _ in xrange(0, 10)]
			var_list.append(temp)

print var_list
print ""
print np.vstack(var_list)
print ""
print np.cov(np.vstack(var_list))	
'''
Created on Jul 3, 2015

@author: nathaniel, I&E summer 2015

This program filters out the outlier in of the x,y coordinates 
using a Mahalanobis distance with a rolling average and standard deveation 
The crirtia for a oulier is md > mu + 1.25*sigma

'''

import numpy as np
import random

class md_filter:
	
   def __init__(self, size, weight, window, range): 
	   # get values
	   self.size = size
	   self.weight = weight  # values for weighting the tolerance  
	   self.window = window  # window size to hold values
	   self.range = range;  # range of starting values
	   self.count = 0 # count until the all the random generated numbers are out
	   # make the random list
	   self.md_list = [ random.uniform(self.range[0], self.range[1]) for _ in xrange(0, self.window)]
	   self.var_list = [ random.uniform(self.range[0], self.range[1]) for _ in xrange(0, self.window)]
 	   for i in xrange(size-1):
 		   temp = [ random.uniform(self.range[0], self.range[1]) for _ in xrange(0, self.window)]
 		   self.var_list = self.var_list, temp
	   print self.var_list
    
    def update
		

a = 3
b = [1, 2]
c = 2
d = [2, 3]
md = md_filter(a, b, c, d)
	   

'''
Created on Oct 4, 2015

@author: nathaniel
'''


import matplotlib as mpl
mpl.rc("savefig", dpi=150)
import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import md_filter
import scipy.stats as stats


usbl = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/usbl_pose.csv', index_col=None)
pos = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/pose_only.csv', index_col=None)
accel = pd.DataFrame.from_csv('/home/nathaniel/KingsPointData/15_21_23/accel.csv', index_col=None)


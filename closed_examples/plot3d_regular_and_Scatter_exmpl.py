# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:08:30 2018

@author: RAN

from
https://stackoverflow.com/questions/10572939/connecting-two-points-in-a-3d-scatter-plot-in-python-and-matplotlib#

"""

import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

dates       = [20020514, 20020515, 20020516, 20020517, 20020520]
highs       = [1135, 1158, 1152, 1158, 1163]
lows        = [1257, 1253, 1259, 1264, 1252]
upperLimits = [1125.0, 1125.0, 1093.75, 1125.0, 1125.0]
lowerLimits = [1250.0, 1250.0, 1156.25, 1250.0, 1250.0]

zaxisvalues0= [0, 0, 0, 0, 0]
zaxisvalues1= [1, 1, 1, 1, 1]
zaxisvalues2= [2, 2, 2, 2, 2]

fig = matplotlib.pyplot.figure()
ax  = fig.add_subplot(111, projection = '3d')

ax.plot(dates, zaxisvalues1, lowerLimits, color = 'b',marker = "o")
ax.plot(dates, zaxisvalues2, upperLimits, color = 'r',marker = "X")


for i,j,k,h in zip(dates,zaxisvalues0,lows,highs):
    ax.plot([i,i],[j,j],[k,h],color = 'g')
ax.scatter(dates, zaxisvalues0, highs, color = 'g', marker = "o")
ax.scatter(dates, zaxisvalues0, lows, color = 'y', marker = "^")

matplotlib.pyplot.show()
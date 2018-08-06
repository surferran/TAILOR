# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:00:50 2018

@author: RAN
from
https://stackoverflow.com/questions/42722691/python-matplotlib-update-scatter-plot-from-a-function

"""
# %matplotlib wx

import matplotlib.pyplot as plt
import numpy as np

plt.ion()
fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(0,10)
plt.ylim(0,10)

plt.draw()
for i in range(1000):
    x.append(np.random.rand(1)*10)
    y.append(np.random.rand(1)*10)
    sc.set_offsets(np.c_[x,y])
#    fig.canvas.draw_idle()
    plt.pause(0.01)

plt.waitforbuttonpress()

######################################

import numpy
import matplotlib.pyplot as plt 
fig = plt.figure()
axe = fig.add_subplot(111)
X,Y = [],[]
sp, = axe.plot([],[],label='toto',ms=10,color='k',marker='o',ls='')
fig.show()
for iter in range(5):
    X.append(numpy.random.rand())
    Y.append(numpy.random.rand())
    sp.set_data(X,Y)
    axe.set_xlim(min(X),max(X))
    axe.set_ylim(min(Y),max(Y))
#    raw_input('...')
    fig.canvas.draw()
    
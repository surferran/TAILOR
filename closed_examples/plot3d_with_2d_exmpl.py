# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 07:08:30 2018

@author: RAN
"""

import matplotlib.pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import random

#%matplotlib wx

dates       = [20020514, 20020515, 20020516, 20020517, 20020520]
highs       = [1135, 1158, 1152, 1158, 1163]
lows        = [1257, 1253, 1259, 1264, 1252]
upperLimits = [1125.0, 1125.0, 1093.75, 1125.0, 1125.0]
lowerLimits = [1250.0, 1250.0, 1156.25, 1250.0, 1250.0]

zaxisvalues0= [0, 0, 0, 0, 0]
zaxisvalues1= [1, 1, 1, 1, 1]
zaxisvalues2= [2, 2, 2, 2, 2]

#plt.style.use('dark_background')

fig = matplotlib.pyplot.figure()
"""***************************************************"""
ax  = fig.add_subplot(221, projection = '3d')

ax.plot(dates, zaxisvalues1, lowerLimits, color = 'b',marker = "o")
ax.plot(dates, zaxisvalues2, upperLimits, color = 'r',marker = "X")

op=1
if op==1:
    for i,j,k,h in zip(dates,zaxisvalues0,lows,highs):
        ax.plot([i,i],[j,j],[k,h],color = 'g',linewidth = 5)
    ax.scatter(dates, zaxisvalues0, highs, color = 'g', marker = "o")
    ax.scatter(dates, zaxisvalues0, lows, color = 'y', marker = "^")

    verts = []; fcs = []
    for i in range(len(dates)-1):
       xs = [dates[i],dates[i+1],dates[i+1],dates[i],dates[i]] # each box has 4 vertices, give it 5 to close it, these are the x coordinates
       ys = [highs[i],highs[i+1],lows[i+1],lows[i], highs[i]]  # each box has 4 vertices, give it 5 to close it, these are the y coordinates
       verts.append(list(zip(xs,ys)))
       fcs.append((random.random(),random.random(),random.random(),0.6))
    poly = PolyCollection(verts, closed = False)
    poly = PolyCollection(verts, facecolors = fcs, closed = False)
    ax.add_collection3d(poly, zs=[zaxisvalues0[0]] * len(verts), zdir='y') # in the "z" just use the same coordinate
elif op==2:
    displacements = []
    for i in lows:
        position = lows.index(i)
        disp = highs[position] - i
        displacements.append(disp)
    
    ax.bar(dates, displacements, zdir='y', bottom=lows, zs=0, width=0.2, align='center', alpha=0.6, edgecolor='k')

pnts = list(zip(dates, zaxisvalues1, lowerLimits))
pnt0 = pnts[0]
moving_point = ax.scatter(pnt0[0],pnt0[1],pnt0[2], marker="*", color = 'k')

matplotlib.pyplot.gca().patch.set_facecolor('white')
ax.w_xaxis.set_pane_color((0.31, 0.8, 0.8, 1.0))
ax.w_yaxis.set_pane_color((0.8, 0.31, 0.8, 1.0))
ax.w_zaxis.set_pane_color((0.8, 0.8, 0.31, 1.0))

ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')

ax.set_title("'some background?' style")


"""***************************************************"""
ax  = fig.add_subplot(222) #, projection = '2d') Unknown projection '2d'
matplotlib.pyplot.gca().patch.set_facecolor('lightgray')

ax.plot(dates, lowerLimits, color = 'b',marker = "o")

plt.text(20020516, 1207, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')

#ax.set_aspect(1) # works but looks bad

plt.axhline(1204)

plt.axvspan(20020516, 20020519)

plt.grid(True)

"""***************************************************"""
ax  = fig.add_subplot(223, projection = '3d')

ax.plot(dates, zaxisvalues1, lowerLimits, color = 'b',marker = "o")
ax.plot(dates, zaxisvalues2, upperLimits, color = 'r',marker = "X")


#how to do in 3d?
#plt.text(20020516, 1207,'this is\nyet another test',
#         rotation=45,
#         horizontalalignment='center',
#         verticalalignment='top',
#         multialignment='center')

"""***************************************************"""
ax  = fig.add_subplot(224)

ax.plot(dates, zaxisvalues1, lowerLimits, color = 'b',marker = "o")
ax.plot(dates, zaxisvalues2, upperLimits, color = 'r',marker = "X")

"""***************************************************"""
if 1==2:
    plt.subplots_adjust(bottom=0.25, top=0.75, left=0.3)


matplotlib.pyplot.show()



ax  = fig.add_subplot(221, projection = '3d')
for ndx,pnt in enumerate(pnts):
    moving_point.set_offsets(pnt[0])#,pnt[1],pnt[2])    
    plt.draw()
    pass
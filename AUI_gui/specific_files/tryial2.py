# -*- coding: utf-8 -*-
"""
Created on Sat May 05 10:53:38 2018

@author: Ran_the_User
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class DraggablePatch:

  def __init__(self, patch):
    self.patch = patch
    self.storedPosition = None
    self.connect()

  def getPosOfPatch(self, marker):
    ext = marker.get_extents().get_points()
    x0 = ext[0,0]
    y0 = ext[0,1]
    x1 = ext[1,0]
    y1 = ext[1,1]
    return 0.5*(x0+x1), 0.5*(y0+y1)

  def connect(self):
    'connect to all the events we need'
    self.cidpress  = self.patch.figure.canvas.mpl_connect('button_press_event',  self.onPress)
    self.cidmotion = self.patch.figure.canvas.mpl_connect('motion_notify_event', self.onMove)

  def onPress(self, event):
    'on button press we will see if the mouse is over us and store some data'
    contains, attrd = self.patch.contains(event)
    if contains:
      self.storedPosition = self.getPosOfPatch(self.patch), event.xdata, event.ydata

  def onMove(self, event):
    'how to update an circle?!'
    contains, attrd = self.patch.contains(event)
    if contains and self.storedPosition is not None:
      oldPos, oldEventXData, oldEventYData = self.storedPosition
      dx = event.xdata - oldEventXData
      dy = event.ydata - oldEventYData
      newX = oldPos[0] + dx
      newY = oldPos[1] + dy
      print "now I would like to move my patch to", newX, newY


def myPatch(x,y): 
  return patches.Circle((x,y), radius=.05, alpha=0.5)

N = 10
x = np.random.random(N)
y = np.random.random(N)
patches = [myPatch(x[i], y[i]) for i in range(N)]

fig = plt.figure()
ax = fig.add_subplot(111)
drs = []
for patch in patches:
  ax.add_patch(patch)
  dr = DraggablePatch(patch)
  drs.append(dr)

plt.show()
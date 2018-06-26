# -*- coding: utf-8 -*-
"""
Created on Sat May 05 10:52:11 2018

@author: Ran_the_User
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class InteractiveCircle(object):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.axis('equal')

        self.circ = Circle((0.5, 0.5), 0.1)
        self.ax.add_artist(self.circ)
        self.ax.set_title('Click to move the circle')

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.inaxes is None:
            return
        self.circ.center = event.xdata, event.ydata
        self.fig.canvas.draw()

    def show(self):
        plt.show()


InteractiveCircle().show()

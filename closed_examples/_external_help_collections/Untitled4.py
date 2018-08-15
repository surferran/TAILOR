from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

#draw the arrow
ax.quiver(0,0,0,1,1,1,length=1.0)

plt.show()

##############
"""
from
https://stackoverflow.com/questions/3461869/plot-a-plane-based-on-a-normal-vector-and-a-point-in-matlab-or-matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)

# create x,y
xx, yy = np.meshgrid(range(10), range(10))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

# plot the surface
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx, yy, z)
plt.show()


# point = [1,2,3];
# normal = [1,2,2];
# t=(0:10:360)';
# circle0=[cosd(t) sind(t) zeros(length(t),1)];
# r=vrrotvec2mat(vrrotvec([0 0 1],normal));
# circle=circle0*r'+repmat(point,length(circle0),1);
# patch(circle(:,1),circle(:,2),circle(:,3),.5);
# axis square; grid on;
# %add line
# line=[point;point+normr(normal)]
# hold on;plot3(line(:,1),line(:,2),line(:,3),'LineWidth',5)
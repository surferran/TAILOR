#%matplotlib wx
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('./tif/XING_T24.tif')
# draw graph without images
G =nx.Graph()
G.add_edge(0,1,image=img,size=0.1)
G.add_edge(1,2,image=img,size=0.05)
G.add_edge(2,3,image=img,size=0.02)
G.add_edge(3,4,image=img,size=0.075)

pos=nx.spring_layout(G)
nx.draw(G,pos)

# add images on edges
ax=plt.gca()
fig=plt.gcf()
label_pos = 0.5 # middle of edge, halfway between nodes
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform
imsize = 0.1 # this is the image size
for (n1,n2) in G.edges():
    (x1,y1) = pos[n1]
    (x2,y2) = pos[n2]
    (x,y) = (x1 * label_pos + x2 * (1.0 - label_pos),
             y1 * label_pos + y2 * (1.0 - label_pos))
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    imsize = G[n1][n2]['size']
    img =  G[n1][n2]['image']
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(img)
    a.set_aspect('equal')
    a.axis('off')
plt.savefig('./tif/save.png') 

""" ran addition """

axis_objects = ax.get_children()

#pathColl = axis_objects[0]
#pathColl.get_offset_position()
#pathColl.get_offsets()

#todo: make pickable for all objects
# set pickable for main axis or Rect.

#nx draw creates path collections of points and lines. (4 and 5 here)


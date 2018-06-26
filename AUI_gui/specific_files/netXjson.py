# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:23:12 2018

@author: Ran_the_User

from

https://networkx.github.io/documentation/stable/reference/readwrite/generated/networkx.readwrite.json_graph.tree_data.html

"""

from networkx.readwrite import json_graph
import networkx as nx
G = nx.DiGraph([(1,2)])
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(1,5)
G.add_edge('1','5')
G.add_edge('1',1)

data = json_graph.tree_data(G,root=1)   # dict type
data2 = json_graph.adjacency_data(G)

G.add_node('node')
G.add_nodes_from(['a','first name','c','f'])
G.remove_node('a')

import math
G.add_node('string')
G.add_node(math.cos) # cosine function
f = open('temp.txt', 'w') # file handle
G.add_node(f)
print G.nodes()
e = (2, 3)
G.add_edge(*e) # unpack tuple

# info:
print G.number_of_edges()
print G.size()
print G.order()
print G.number_of_nodes()

print G.neighbors(1)
print G.degree()
print G.degree(1)

# Keys and values can be of any data type
fruit_dict= {'apple': 1, 'orange': [0.12, 0.02], 42: True}
# Can retrieve the keys and values as Python lists (vector)
print fruit_dict.keys()
# Or (key, value) tuples
print fruit_dict.items()

G.add_node(10, time='10am',myparam='ran')
G.node[10]
G.node[10]['time']
'''
the special edge attribute weight should always be numeric and 
holds values used by algorithms requiring weighted edges.'''
G.node[10]['weight']=5
# G.node[10][1]['weight']=5 # err
G.add_edge(10,1, weight=4)
G.neighbors(10)
G[10][1]['weight']
#G[10][2]
G.nodes(data=True)
G.nodes()
G.edges()

for n1, n2, attr in G.edges(data=True): # unpacking
    if attr:
        print attr.keys()
        if 'weight' in attr.keys():
            print n1, n2, attr['weight']
''''''
dg = nx.DiGraph()
dg.add_weighted_edges_from([ (3, 1, 0.75), (1, 4, 0.5)])
print dg.out_degree(1, weight='weight')

print dg.degree(1, weight='weight')

print dg.successors(1)
print dg.predecessors(1)

dgU = dg.to_undirected()
''''''
dg.neighbors(1)
dgS = dg.subgraph([1,4])
dgS.edges()

red = nx.random_lobster(100, 0.9, 0.9)
nx.draw(red)
red.nodes()

nx.write_gml(red, 'redX.txt')
nx.write_edgelist(red, 'redX2.txt', comments='#', delimiter=' ', data=True, encoding='utf-8')
                  
N=G.order()
K=G.size()
avg_deg = float(K) / N
print N, K, avg_deg
print "Nodes: ", N
print "Edges: ", K
print "Average degree: ", avg_deg
print "SCC: ", nx.number_strongly_connected_components(G)
print "WCC: ", nx.number_weakly_connected_components(G)

cam_net = G
in_degrees= cam_net.in_degree() # dictionary node:degree
in_values= sorted(set(in_degrees.values()))
in_hist= [in_degrees.values().count(x) for x in in_values]

out_degrees= cam_net.out_degree() # dictionary node:degree
out_values= sorted(set(out_degrees.values()))
out_hist= [out_degrees.values().count(x) for x in out_values]

plt.figure() # you need to first do 'import pylabas plt'
plt.grid(True)
plt.plot(in_values, in_hist, 'ro-') # in-degree
plt.plot(out_values, out_hist, 'bv-') # out-degree
#plt.loglog(in_values, in_hist, 'ro-') # in-degree
#plt.loglog(out_values, out_hist, 'bv-') # out-degree
plt.legend(['In-degree', 'Out-degree'])
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('network of G')
#plt.xlim([0, 2*10**2])
plt.savefig('./cam_net_degree_distribution.pdf')
#plt.close()
''''''
cam_net_ud= cam_net.to_undirected()
# Clustering coefficient of node 0
print nx.clustering(cam_net_ud, 5)
# Clustering coefficient of all nodes (in a dictionary)
clust_coefficients= nx.clustering(cam_net_ud)
# Average clustering coefficient
avg_clust= sum(clust_coefficients.values()) / len(clust_coefficients)
print avg_clust
# Or use directly the built-in method
print nx.average_clustering(cam_net_ud)
''''''
# Connected components are sorted in descending order of their size
cam_net_components= nx.connected_component_subgraphs(cam_net_ud)
cam_net_mc= cam_net_components
# Betweennesscentrality
bet_cen= nx.betweenness_centrality(cam_net_mc)
# Closeness centrality
clo_cen= nx.closeness_centrality(cam_net_mc)
# Eigenvector centrality
eig_cen= nx.eigenvector_centrality(cam_net_mc)

defget_top_keys(dictionary, top):
    items = dictionary.items()
    items.sort(reverse=True, key=lambda x: x[1])
    return map(lambda x: x[0], items[:top])
top_bet_cen= get_top_keys(bet_cen,10)
top_clo_cen= get_top_keys(clo_cen,10)
top_eig_cent= get_top_keys(eig_cen,10)

''''''
#Compute the average degree of each node’s neighbours:
#•And the more compact version in a single line:
def avg_neigh_degree(g):
    data = {}
    for n in g.nodes():
        if g.degree(n):
            data[n] = float(sum(g.degree(i) for iin g[n]))/g.degree(n)
    return data
#
def avg_neigh_degree(g):
    return dict((n,float(sum(g.degree(i) for iin g[n]))/ g.degree(n))
for n in g.nodes() if g.degree(n))
''''''

#########################################

import json
s = json.dumps(data)
print s

with open('netConnections.json','wt') as f:
    f.write(s)

H = json_graph.tree_graph(data)
#####################################
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,4))

ax = fig.add_subplot(111)        # takes physical place in panel
ax.set_title('click on NetX points')

nx.draw(G)

plt.axis('off')
plt.grid(False)

plt.axis('on')
plt.grid(False)

#plt.axis('on')
#plt.grid(True)

axis_objects = ax.get_children()
''''''
pathObject = axis_objects[0]
pathOffsets = pathObject.get_offsets()
pathOffsets[0][0] = 0.5
#pathOffsets[1][0] = 0.5
#pathOffsets[2][0] = 0.5
#pathOffsets[3][0] = 0.5

def pick_special_func(var1, var2):
    print "got here"
    
pathObject.set_picker(pick_special_func)   
pathObject.get_picker()  # out: <function __main__.pick_special_func>
pathObject.pickable() # out: True
#pathObject.get_data() # for line obj
#pathObject.draw ?
pathObject.set_label(['a', '2', '34', '4','5'])
pathObject.get_paths()
pathProps = pathObject.properties()
''''''

linesObject = axis_objects[1]
print linesObject.get_label()
print linesObject.get_offsets()
linesObject.get_picker()
linesObjectPaths = linesObject.get_paths()
for ndx,line in enumerate(linesObjectPaths):
    print "ndx "+str(ndx)
    print line.vertices

#todo: cross data between node in G.nodes.pos
#      xy of node and its graph index
#      is G.node in G.edges , or offset[i] in lines[]
#    ..path.vertices
"""
type(path1)
Out[140]: matplotlib.path.Path

type(pathObject)
Out[141]: matplotlib.collections.PathCollection
"""

plt.get_fignums()

#plt.show()
#plt.draw()

from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
from matplotlib.artist import Path


def onpick_func2(event):
    if isinstance(event.artist, Line2D):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        print('onpick1 line:', zip(np.take(xdata, ind), np.take(ydata, ind)))
    elif isinstance(event.artist, Rectangle):
        patch = event.artist
        print('onpick1 patch:', patch.get_path())
    elif isinstance(event.artist, Text):
        text = event.artist
        print('onpick1 text:', text.get_text())  
    elif isinstance(event.artist, AxesImage):
        im = event.artist
        A = im.get_array()
        print('onpick4 image', A.shape)
    elif isinstance(event.artist, Path):
        path = event.artist
        print('onpick Path', path)
        
def onpick_func1(event):          # picker only for points
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('onpick points:', points)

def onclick1st(event):    # general picker event
    print type(event)
    print type(event.xdata)
#    onpick_func2(event)
#    if type(event.x)==("<type 'int'>"):
    if type(event.xdata) is np.float64:
        print type(event.xdata)!=("<type 'NoneType'>")
#    if type(event)!=None:
        print type(event.xdata)
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', 
               event.button,
               event.x, event.y, event.xdata, event.ydata))
#    print list(dir(event))
#    print list(dir(event.name))
#    print list(dir(event.guiEvent))
#    mouseevent = event.mouseevent  
#    artist = event.artist
#    print mouseevent
#    print artist
    # now do something with this...

#cid = fig.canvas.mpl_connect('button_press_event', onclick1st)

cid2 = fig.canvas.mpl_connect('pick_event', onpick_func1)
#cid2 = fig.canvas.mpl_connect('pick_event', onpick_func2)

for label in ax.get_xticklabels():  # make the xtick labels pickable
    label.set_picker(True)
        
for label in ax.get_yticklabels():  # make the xtick labels pickable
    label.set_picker(True)
        
def set_childrens(obj_list):
    for ndx,obj in enumerate(obj_list):
#        if ndx<5:
        if obj.get_children():  # list is not empty then:
            set_childrens(obj.get_children())
        else:
            obj.set_picker(True) # make the axis children pickable
            print str(ndx)+" "+ str(obj)

#set_childrens(axis_objects)
axis_objects[7].get_children()[0].get_children()

pathOffsets = axis_objects[0].get_offsets()
pathOffsets[0][0] = 0.5
# code ref also from  : http://matplotlib.org/users/image_tutorial.html
# and : http://www.pyimagesearch.com/2014/11/03/display-matplotlib-rgb-image/
# and : https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.readwrite.json_graph.node_link_data.html#networkx.readwrite.json_graph.node_link_data

# matplotlib reffs:
#   http://www.developersite.org/101-55137-python
# https://python.g-node.org/python-summerschool-2013/_media/wiki/datavis/matplotlib_tutorial.html
# https://matplotlib.org/api/collections_api.html

import matplotlib

import matplotlib.image as mpimg
import numpy as np
from PIL import Image

import  networkx    as nx
from    xml.dom     import minidom
import  matplotlib.pyplot as plt

from networkx.readwrite import json_graph
import json

print ("nx version : " + nx.__version__)


###############################################
matplotlib.use('WXAgg')
import matplotlib
#print (matplotlib.rc.func_globals['defaultParams'])
print (matplotlib.rc.__globals__['defaultParams'])
matplotlib.get_backend()
#matplotlib.rcdefaults() # set params back to defaults.
print (matplotlib.matplotlib_fname())
#matplotlib.rcsetup
matplotlib.rc_params()
###############################################

if __name__=='__main__':
    doc = minidom.parse("./example.xml")
    output_rel_path = "./runtime_outputs/"
else:
    doc = minidom.parse("./specific_files/example.xml")
    output_rel_path = "./runtime_outputs/"
draw_edges_labels=False#True

''' generate the graph '''

# code ref: https://networkx.github.io/documentation/networkx-1.10/reference/classes.multidigraph.html
G               = nx.MultiDiGraph(name="Simulated System Graph")
G_wVirtualEdges = nx.DiGraph(name="Graph with added virtual edges nodes")
Gimgs           = nx.Graph(name="images tree trial")

name = doc.getElementsByTagName("system")[0].getAttribute("name")
print("system name is : " + name) #.firstChild.data)

staffs = doc.getElementsByTagName("unit")
for staff in staffs:
        unit_name = staff.getAttribute("name")
        unit_img  = staff.getAttribute("img_path")

        G.add_node(unit_name,img_path=unit_img)
        G_wVirtualEdges.add_node(unit_name,img_path=unit_img,node_type="real")
        Gimgs.add_node(unit_img)

        inVars   = staff.getElementsByTagName("var_in")
        for var in inVars:
            name = var.getAttribute("var_name")
            source = var.getAttribute("var_source")
            units = var.getAttribute("data_units")
            # salary = staff.getElementsByTagName("salary")[0]
            # print("id:%s, nickname:%s, salary:%s" % (unit_name, nickname.firstChild.data, salary.firstChild.data))
            print("to unit : %s , by var name : %s, from source : %s " % (unit_name, name, source))
            G.add_edge(source, unit_name, var_name=name, units=units)
            # use the '__' double-under-line chars to sign for source-varName-target name pattern
            virtualEdgeNodeName = source + "__" + name + "__" + unit_name
            G_wVirtualEdges.add_node(virtualEdgeNodeName,node_type="VirtualEdgeNode",name=name)
            G_wVirtualEdges.add_edge(source, virtualEdgeNodeName,var_name="VirtualEdge")
            G_wVirtualEdges.add_edge(virtualEdgeNodeName, unit_name,var_name="VirtualEdge")
print ("*** G printouts: ***")
print( G)
listOfNodes = G.nodes()
filledEdges= G.edges(data='var_name')
print( filledEdges)
print( G.nodes(data=True))
print( G.edges())
print( G.edges(data=True))
#print len(G)
#print G.number_of_nodes()
#print G.order()
#print G.size()

listOfNodes_GwV = G_wVirtualEdges.nodes()
filledEdges_GwV = G_wVirtualEdges.edges(data='var_name')
#print filledEdges_GwV

#print "Gimgs nodes: "
listImgs = Gimgs.nodes()
#print listImgs

###############################################

""""""
''' deal with the graph printings '''
""""""

# drawing by : https://networkx.github.io/documentation/networkx-1.10/reference/drawing.html

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1, 2, 1)   # lines, columns, current axes

# pos=nx.spring_layout(G) # positions for all nodes
pos = nx.spectral_layout(G) # positions for all nodes
pos = nx.shell_layout(G)
pos = nx.circular_layout(G)
# pos = nx.random_layout(G)
# pos = nx.fruchterman_reingold_layout(G)

node_circle_size=3700   # unknown units
for node in listOfNodes:
    pos[node]=pos[node]*1000 + node_circle_size/20.

print (pos)

# nodes
nx.draw_networkx_nodes(G,pos,node_size=node_circle_size, node_color="white",node_shape='o',alpha=0.5) # ##ACCEPTS: [\/|- +xoO.* ]
# labels
nx.draw_networkx_labels(G,pos,font_size=15,font_family='sans-serif',font_color='k',font_weight='bold')
# edges
plotedEdges = nx.draw_networkx_edges(G,pos,edgelist=filledEdges,width=2,alpha=0.5, edge_color='b',style='dashed')  # LineCollection type returned
if draw_edges_labels==True:
    # edges labels
    nx.draw_networkx_edge_labels(G,pos,font_size=11,font_family='sans-serif')

''''''

nodesColrsDict = {'physics':0.0,
                  'quad 1':0.5,
                  'quad 2':0.5,
                  'payload':1.0 }
colorValues = [nodesColrsDict.get(node, 0.25) for node in listOfNodes]
# repeat to get axis re-scaled
plotedNodes = nx.draw_networkx_nodes(G,pos,nodelist=listOfNodes, node_size=node_circle_size, node_shape='o',alpha=0.5, node_color=colorValues) # PathCollection type returned

# search string from text search:
searchTxt = 'payload'
nx.draw_networkx_nodes(G,pos,nodelist=[searchTxt], node_size=node_circle_size, node_shape='x',alpha=0.75, node_color=colorValues, linewidths=2.)


###############################################

''''''


for node in listOfNodes:
    nodePos = pos[node]
    if node!=u'physics':
        node_img = G.node[node]['img_path']
    pass

thumb_size=1200
pos0 = pos[list(listOfNodes)[0]]-(thumb_size/20.)
pos1 = pos[list(listOfNodes)[1]]-(thumb_size/20.)

# img0 =mpimg.imread(listImgs[0])  # todo:check with this way
img0=Image.open(list(listImgs)[0])

img0.thumbnail((thumb_size, thumb_size), Image.ANTIALIAS) # resizes image in-place
# img1 =mpimg.imread(listImgs[1])
img1=Image.open(list(listImgs)[1])
img1.thumbnail((thumb_size, thumb_size), Image.ANTIALIAS) # resizes image in-place

rows0=img0.size[0]  #rows
cols0=img0.size[1]   #columns
rows1=img1.size[0]  #rows
cols1=img1.size[1]   #columns

# rows0=len(img0)  #rows
# cols0=len(img0[0])   #columns
# rows1=len(img1)  #rows
# cols1=len(img1[0])   #columns

imgplot = plt.imshow(img0, extent=[pos0[0], pos0[0]+cols1, pos0[1], pos0[1]+rows1])
imgplot = plt.imshow(img0, extent=[pos1[0], pos1[0]+cols1, pos1[1], pos1[1]+rows1])

###############################################

# nx.draw(G)

ax.set_xlim([0, 1000+node_circle_size/10.])
ax.set_ylim([0, 1000+node_circle_size/10.])

plt.axis('off')

plt.savefig(output_rel_path+"system_graph.png") # save as png
''''''

###############################################
''''''
''''''
# drawing by : https://networkx.github.io/documentation/networkx-1.10/reference/drawing.html

# fig = plt.figure(figsize=(3, 2))
ax = fig.add_subplot(1, 2, 2)
ax.autoscale()

# pos_GwV=nx.spring_layout(G_wVirtualEdges) # positions for all nodes
pos_GwV=nx.spectral_layout(G_wVirtualEdges) # positions for all nodes
pos_GwV=nx.circular_layout(G_wVirtualEdges)
pos_GwV=nx.shell_layout(G_wVirtualEdges)

for node in listOfNodes_GwV:
    pos_GwV[node]=pos_GwV[node]*1000 + node_circle_size/20.

# nodes
nx.draw_networkx_nodes(G_wVirtualEdges,pos_GwV,node_size=node_circle_size, node_color="white",node_shape='o',alpha=0.5) # ##ACCEPTS: [\/|- +xoO.* ]
# labels
nx.draw_networkx_labels(G_wVirtualEdges,pos_GwV,font_size=10,font_family='sans-serif',font_color='k',font_weight='bold')
# edges
plotedEdges_GwV = nx.draw_networkx_edges(G_wVirtualEdges,pos_GwV,width=2,alpha=0.25, edge_color='r')  # LineCollection type returned #,edgelist=filledEdges

d= nx.coloring.greedy_color(G_wVirtualEdges, strategy=nx.coloring.strategy_largest_first)

print( pos_GwV)
# nx.draw(G)
# plt.axis('off')

###############################################

specificNode = 'quad 1'
## getNode = nx.get_node_attributes(G,'node_type')
# nodesAdjList = G.adj
# nodeNeighbours = nodesAdjList[specificNode] #
nodeNeighbours = G[specificNode]
smallG = [specificNode]
for item in nodeNeighbours.keys():
    smallG.append(str(item))
newG = G_wVirtualEdges.subgraph(smallG)
newG = G.subgraph(smallG)


nodeAllNeighbours = nx.all_neighbors(G,specificNode)
# nodeCommons = nx.common_neighbors(G_wVirtualEdges,specificNode,str(nodeNeighbours.keys()[0]))  # only for UnDirected..

getNode = nx.get_node_attributes(G_wVirtualEdges,'node_type')
nodesAdjList = G_wVirtualEdges.adj

printNodes = nodesAdjList[specificNode]
nx.draw_networkx_nodes(G_wVirtualEdges,pos_GwV,nodelist=printNodes, node_size=node_circle_size, node_color="white",node_shape='o',alpha=0.5) # ##ACCEPTS: [\/|- +xoO.* ]
# labels
nx.draw_networkx_labels(G_wVirtualEdges,pos_GwV,font_size=10,font_family='sans-serif',font_color='k',font_weight='bold')
# edges
plotedEdges_GwV = nx.draw_networkx_edges(G_wVirtualEdges,pos_GwV,width=2,alpha=0.25, edge_color='r')  # LineCollection type returned #,edgelist=filledEdges

###############################################

realNodes=[]
realNodes_namesList=[]
for node in G_wVirtualEdges.nodes(data=True):
    if len(node[1]) == 0 :
        realNodes.append(node)      # assuming the 'physics' node was added because it is only ~'sourced'
        realNodes_namesList.append(node[0])
        continue
    if node[1]["node_type"]=="real":
        realNodes.append(node)
        realNodes_namesList.append(node[0])
print( realNodes)
# nodes
nx.draw_networkx_nodes(G_wVirtualEdges,pos_GwV,nodelist=realNodes_namesList,node_size=node_circle_size, node_color="blue",node_shape='o',alpha=0.25) # ##ACCEPTS: [\/|- +xoO.* ]


plt.savefig(output_rel_path+"system_graph_with_VirtEdges.png") # save as png
# how to PAN on ?

# plt.show()

# nx.draw(Gimgs)
# plt.show()

###############################################

''''''

jsonData = json_graph.node_link_data(G)
with open(output_rel_path+'jsonGout.json','w') as fJS:
    json.dump(jsonData, fJS, indent=4)

jsonData = json_graph.node_link_data(G_wVirtualEdges)
with open(output_rel_path+'jsonGwVout.json','w') as fJS:
    json.dump(jsonData, fJS, indent=4)

''''''

###############################################

# TODO
# set axis limits to 0-1000
# add text function in graph to find node by attributes
# catch user events on objects
# allow the dynamic movment of nodes in dysplay. dynamic pos change and re-draw
#   allow the extension and trim of the edges. in graph display or separate window, list
# check http://matplotlib.org/users/text_intro.html


###############################################
###############################################

# plt.axis("off")
# plt.colorbar()
def on_pick_Edges(event):
    print( "pick event Edges")
    print (event.artist)
    print (event.canvas.events)
    print (event.canvas.filetypes)
    print (plotedEdges._paths)
    print (plotedNodes._offsets)

def on_pick_Nodes(event):
    print( "pick event Nodes")
    print( event.artist)
    print( event.canvas.events)

def on_Edge_click(items):
    print ("*on_Edge_click*")
    # todo: show the list of edges in GUI
    for item in list(items):
        print (list(filledEdges)[item])  # from the input that is creating the plotedEdges

def on_Node_click(items, nodesColorsArray):
    print ("*on_Node_click*")
    # todo: highlight the node circle and edges from it
    # for item in items: print listOfNodes[item]
    selectedNode  = str(listOfNodes[items])  # the input for creating the plotedNodes
    nodeColorPrev = nodesColorsArray[items]

    print (ax.collections[0].properties())
    print (selectedNode)

    print (G[selectedNode])               # dict type
    print (G.neighbors(selectedNode))     # list type
    print (G.predecessors(selectedNode))  # list type . includes inputs

    # if isinstance(lastSelectedNode):
    #     nx.draw_networkx_nodes(G,pos,nodelist=lastSelectedNode,node_size=node_circle_size, node_color="blue",node_shape='o',alpha=0.25) # ##ACCEPTS: [\/|- +xoO.* ]

    # nodesColorsArray[[0,items]] = nodesColorsArray[[items,0]]
    # nodeColor = nodesColorsArray[items]
    # plotedNodes.set_facecolors(nodesColorsArray)
    # nodesList = [str(listOfNodes[0]),str(listOfNodes[items])]
    #
    # fig = plt.gcf()
    # nx.draw_networkx_nodes(G, pos, nodelist=nodesList, node_size=node_circle_size, node_color=nodesColorsArray,
    #                        node_shape='o', alpha=0.75, linewidths=2.0)  # ##ACCEPTS: [\/|- +xoO.* ]

    # http: // stackoverflow.com / questions / 22716161 / how - can - one - modify - the - outline - color - of - a - node - in -networkx
    axCur = plt.gca()  # to get the current axis
    axCur.collections[0].set_edgecolor("#FF0000")
    axCur.collections[1].set_edgecolor("#FFFf00")
    axCur.collections[2].set_edgecolor("#FFff00")  #self._edgecolors  is changed
    axCur.collections[3].set_edgecolor("#FFffff")
    axCur.collections[4].set_edgecolor("#FFffff")
    # todo: can change seperatly the collections by the index item??


    ##nx.draw(G, pos, node_color=range(len(pos)), node_size=800, cmap=plt.cm.Blues)
    # cmap=plt.cm.jet
    # lastSelectedNode = listOfNodes[items]

def on_Node_dblClk(items):
    print ("*on_Node_Dbl_click*")
    # todo: in separate window show the node circle and edges from it and to it with neighbours
    for item in items:
        print (listOfNodes[item])  # the input for creating the plotedNodes

def on_press(event):

    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    print ("on press")
    if event.dblclick:
        print("DBLCLICK", event) # in actual: includes also a heading 'down' event
    else:
        print("DOWN    ", event)
    print (event.inaxes)
    fig.canvas.draw_idle()
#    eventContainsEdges = plotedEdges.contains(event)
    eventContainsEdges=[]
    for pEdg in plotedEdges:
        if pEdg.contains(event)[0] :
            print(pEdg.contains(event))
            eventContainsEdges.append(pEdg)
    print ("eventContainsEdges:",eventContainsEdges)
    print("dir(plotedEdges[0])",str(dir(plotedEdges[0])))
    if (eventContainsEdges[0]):
        # print "pressed on selected edge"
    #     open other window with the selected edges/nodes
        items = eventContainsEdges[1]['ind']
        if ~event.dblclick:
           on_Edge_click(items)
    else:
        eventContainsNodes = plotedNodes.contains(event)
        print (eventContainsNodes)
        if (eventContainsNodes[0]):
            # print "pressed on selected node"
            #     open other window with the selected edges/nodes
            items = eventContainsNodes[1]['ind']
            nodesColors = plotedNodes.get_facecolors()  # result of ndArray type
            if event.dblclick:
                on_Node_dblClk(items, nodesColors)
            else:
                on_Node_click(items, nodesColors)
        else:
            print("*pressed on general item of the figure*")

    # print "plot paths len"  , len(plotedEdges._paths)
    # print "plot paths len"  , len(plotedNodes._paths)
    pass
def on_release(event):
    print ("on release")
    print (event.inaxes)
    pass
def on_motion(event):
    print ("on motion")
    print (event.inaxes)
    pass

# check plotedEdges._paths

plotedEdges[0]._picker=True
plotedEdges[0].figure.canvas.mpl_connect('button_press_event', on_press)
# plotedEdges.figure.canvas.mpl_connect('pick_event', on_pick_Edges)  ## button_release_event, motion_notify_event
plotedNodes._picker=True
plotedNodes.figure.canvas.mpl_connect('button_press_event', on_press)
# plotedNodes.figure.canvas.mpl_connect('pick_event', on_pick_Nodes)


fig = plt.gcf()
plt.gca().text(0.5, 0.5, "Click on the canvas to test mouse events.",
               ha="center", va="center")

###############################################

# fig.canvas.mpl_connect('button_press_event', on_press)
# for obj in plotedEdges:
#     makeConnect(obj)

ax.set_xlim([0, 1000+node_circle_size/10.])
ax.set_ylim([0, 1000+node_circle_size/10.])
# ax.autoscale(True) #?
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")

ax.autoscale()

# plt.savefig("weighted_graph_imgs.png") # save as png
if __name__=='__main__':
    plt.show()          # stop point. plots all delivered so far to plt.__ or nx.draw(..).
                    #  similar to Figure in matlab, but on oposite operation order. and no need in 'hold' function.

def getMeFig():
    return fig


##########################################################
# exit()

##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
if 1==2:
    plt.hist(img.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
    plt.show()

    img=Image.open(listImgs[0])
    img.thumbnail((215, 125), Image.ANTIALIAS) # resizes image in-place
    imgplot = plt.imshow(img)
    plt.show()
    imgplot = plt.imshow(img, interpolation="nearest")#,origin=[20,50]) #interpolation="bicubic")
    plt.show()

    # print(list(nx.bfs_edges(G,0)))
    ''' find the way (if possible) from source to all other nodes. with a search path.
        can see if one's node is reachable from source node. and what is the path.
    '''
    treeEdges = list(nx.bfs_edges(G,'physics'))
    print(treeEdges)
    newG = nx.MultiDiGraph(name="tree graph")
    newG.add_edges_from(treeEdges)
    nx.draw_shell(newG,arrows=True)
    plt.show()

    nx.draw_random(G)
    plt.show()


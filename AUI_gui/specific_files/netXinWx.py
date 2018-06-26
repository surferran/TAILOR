import matplotlib.pyplot as plt
import networkx as nx
import wx
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar

#######################
# addition from 
# https://andrewmellor.co.uk/blog/articles/2014/12/14/d3-networks/
# and        https://matplotlib.org/users/event_handling.html
#%matplotlib wx
import json
from networkx.readwrite import json_graph
import numpy as np
import sys

#fig, ax = plt.subplots()
#ax.plot(np.random.rand(10))

def onclick1(event):    # general picker event
    print type(event)
    print type(event.xdata)
#    if type(event.x)==("<type 'int'>"):
    if type(event.xdata) is np.float64:
        print type(event.xdata)!=("<type 'NoneType'>")
#    if type(event)!=None:
        print type(event.xdata)
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
#    print list(dir(event))
#    print list(dir(event.name))
#    print list(dir(event.guiEvent))
#    mouseevent = event.mouseevent  
#    artist = event.artist
#    print mouseevent
#    print artist
    # now do something with this...

if 0:
    G = nx.erdos_renyi_graph(30,4.0/30)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(30,4.0/30)
    fig = plt.figure(figsize=(6,4));
    
    ax = fig.add_subplot(111)        # takes physical place in panel
    ax.set_title('click on points')
    
    nx.draw(G)#, picker=5)

    cid = fig.canvas.mpl_connect('button_press_event', onclick1)
#fig.canvas.mpl_disconnect('button_press_event', onclick1)
#ax.pickable()

    sys.exit(0)
##############################################################
##############################################################

def onpick(event):          # picker only for points
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print('onpick points:', points)

if 0:
    line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance
    fig.canvas.mpl_connect('pick_event', onpick)


#    if ax is None:
#        cf = plt.gcf()
#    else:
#        cf = ax.get_figure()

#    for ix,deg in G.degree().items():
#        G.node[ix]['degree'] = deg
#        G.node[ix]['parity'] = (1-deg%2)
#    
#    for ix,katz in nx.katz_centrality(G).items():
#        G.node[ix]['katz'] = katz
#    
#    print G.nodes(data=True)[:5]
#    
#    data = json_graph.node_link_data(G)
#    with open('netx_graph.json', 'w') as f:
#        json.dump(data, f, indent=4)
    
#######################

class NetworkFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1)
        self.panel = wx.Panel(self)
        self.fig = plt.figure()
        self.canvas = FigCanvas(self.panel, -1, self.fig)
#        G=nx.house_graph()
        G=nx.dodecahedral_graph()
        edges=nx.draw_networkx_edges(G,pos=nx.spring_layout(G), arrows=False)
#        pos={0:(0,0),
#            1:(1,0),
#            2:(0,1),
#            3:(1,1),
#            4:(0.5,2.0)}

        node4 = nx.draw_networkx_nodes(G,pos,node_size=2000,nodelist=[4], picker=5, label=['4'])
        print node4
        nx.draw_networkx_nodes(G,pos,node_size=3000,nodelist=[0,1,2,3],node_color='b')
        nx.draw_networkx_labels(G, pos)
#        nx.draw_networkx_edges(G,pos,alpha=0.5,width=6)
        plt.axis('off')
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.toolbar = NavigationToolbar(self.canvas)
        self.vbox.Add(self.toolbar, 0, wx.EXPAND)
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)

        self.fig.canvas.mpl_connect('pick_event', onpick)
        #
        plt.savefig("house_with_colors.png") # save as png
        #plt.show() # display

if __name__ == '__main__':
#    if __name__ == '__main__':
  app = wx.App(False) # PySimpleApp()
  frame = NetworkFrame()
  frame.Show()
  app.MainLoop()

sys.exit(0)

def onpick2(event):

    if event.artist!=line: return True

    N = len(event.ind)
    if not N: return True


    figi = plt.figure()
    for subplotnum, dataind in enumerate(event.ind):
        ax = figi.add_subplot(N,1,subplotnum+1)
        ax.plot(X[dataind])
        ax.text(0.05, 0.9, 'mu=%1.3f\nsigma=%1.3f'%(xs[dataind], ys[dataind]),
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()
    return True


if __name__=='__main__3':
    """
    compute the mean and stddev of 100 data sets and plot mean vs stddev.
    When you click on one of the mu, sigma points, plot the raw data from
    the dataset that generated the mean and stddev
    """
    #import numpy as np
    #import matplotlib.pyplot as plt
    
    X = np.random.rand(100, 1000)
    xs = np.mean(X, axis=1)
    ys = np.std(X, axis=1)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('click on point to plot time series')
    line, = ax.plot(xs, ys, 'o', picker=5)  # 5 points tolerance
    
    
    fig.canvas.mpl_connect('pick_event', onpick2)
    
    plt.show()
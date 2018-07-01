# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:19:24 2018

@author: Ran_the_User
"""

import networkx as nx
#import matplotlib.pyplot as plt
#%matplotlib wx

G = nx.readwrite.graphml.read_graphml('bokeh_server_flow.graphml')

nx.draw(G, with_labels=True, node_size=700, node_shape='p') # one of 'so^>v<dph8'.
#G.nodes()

linefeed=chr(10) # linefeed=\n
s=linefeed.join(nx.generate_graphml(G))
s = nx.parse_graphml

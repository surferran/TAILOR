# -*- coding: utf-8 -*-
"""
Created on Fri May 04 17:13:46 2018

@author: Ran_the_User
"""
#%matplotlib wx
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
red_edges = [('A', 'C'), ('E', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = values, node_size = 500)
nx.draw_networkx_labels(G, pos)
options = {
    'node_color': 'blue',
    'node_size': 700,
    'width': 2,
    'arrowstyle': '-|>',
    'arrowsize': 7,
}
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True, **options)
nx.draw_networkx(G, pos, edgelist=black_edges, arrows=True, **options)
plt.show()

print len(G.adjacency_list())
print len(G.nodes())
nx.to_edgelist(G)
nx.to_dict_of_dicts(G)
print nx.to_dict_of_lists(G)
adjacentMat = nx.to_pandas_dataframe(G)  # shows the existing directions
print adjacentMat
col = adjacentMat['F']
row = adjacentMat.loc['F']
print col
print row
totalNeighbours = col + row

G.neighbors('F')
G.predecessors('F')
nx.predecessor(G,'F')
G.successors('F')
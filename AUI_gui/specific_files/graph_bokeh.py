"""
graph and bokeh
from
https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html#userguide-graph 
"""
def example_func_1():
    import math

    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
    from bokeh.palettes import Spectral8

    N = 8
    node_indices = list(range(N))

    # plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
    #               tools='', toolbar_location=None)
    plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1))

    graph = GraphRenderer()

    graph.node_renderer.data_source.add(node_indices, 'index')
    graph.node_renderer.data_source.add(Spectral8, 'color')
    graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

    graph.edge_renderer.data_source.data = dict(
        start=[0]*N,
        end=node_indices)

    ### start of layout code
    circ = [i*2*math.pi/8 for i in node_indices]
    x = [math.cos(i) for i in circ]
    y = [math.sin(i) for i in circ]

    graph_layout = dict(zip(node_indices, zip(x, y)))
    graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    plot.renderers.append(graph)

    output_file('graph.html')
    show(plot)

def example_func_2():
    import math

    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
    from bokeh.palettes import Spectral11, Inferno256, Category20_20

    import networkx as nx
    from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes

    from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, TapTool, BoxSelectTool
    from bokeh.palettes import Spectral4



    # N = 32 # 8
    # node_indices = list(range(N))
    # print(node_indices)
    box_limit = 2 # 1.1

    plot = figure(title="Graph Layout Demonstration" ,
                 x_range=(-box_limit, box_limit), y_range=(-box_limit, box_limit))
                # tools="", toolbar_location=None)

    plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())

    # graph = GraphRenderer()
    g = nx.karate_club_graph()
    N = (len(g.nodes()))
    g_layout = nx.spring_layout(g)
    graph_layout = g_layout

    graph = from_networkx(g, g_layout, scale=2, center=(0,0))
    
    colors = Category20_20 + Category20_20

    node_indices = list(range(N))

    graph.node_renderer.data_source.add(node_indices, 'index')
    graph.node_renderer.data_source.add(colors      , 'color') 

    graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color=Spectral4[0])  # 'color'
    graph.node_renderer.selection_glyph = Oval(height=0.1, width=0.2, fill_color=Spectral4[1])
    graph.node_renderer.hover_glyph = Oval(height=0.1, width=0.2, fill_color=Spectral4[2])

    graph.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
    graph.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
    graph.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

    graph.selection_policy  = NodesAndLinkedEdges()    
    graph.inspection_policy = EdgesAndLinkedNodes()

    if True:
        if True:  # make edges only from node 0 to all others.
            graph.edge_renderer.data_source.data = dict(
                start=[0]*N,
                end=node_indices)

        if False:  # change and make nodes positions on a circle
            ### start of layout code
            circ = [i*2*math.pi/N for i in node_indices]
            x = [math.cos(i) for i in circ]
            y = [math.sin(i) for i in circ]
            graph_layout = dict(zip(node_indices, zip(x, y)))
            graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        ### Draw quadratic bezier paths
        def bezier(start, end, control, steps):
            return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

        xs, ys = [], []
        sx, sy = graph_layout[0]
        steps = [i/100. for i in range(100)]
        # make run on all nodes. setting edges from [0] node to all others
        for node_index in node_indices:
            ex, ey = graph_layout[node_index]
            xs.append(bezier(sx, ex, 0, steps))
            ys.append(bezier(sy, ey, 0, steps))
        graph.edge_renderer.data_source.data['xs'] = xs
        graph.edge_renderer.data_source.data['ys'] = ys

    plot.renderers.append(graph)

    output_file("graph2.html")
    show(plot)

example_func_2()
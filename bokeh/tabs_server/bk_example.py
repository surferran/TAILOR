# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 06:08:47 2018

@author: Ran_the_User

example from
https://hub.mybinder.org/user/bokeh-bokeh-notebooks-cb1sq6o2/notebooks/tutorial/00%20-%20Introduction%20and%20Setup.ipynb

"""

def bk_example():
    from bokeh.models import ColumnDataSource, HoverTool
    from bokeh.plotting import figure
    from bokeh.sampledata.autompg import autompg_clean as df
#    from bokeh.transform import factor_cmap
    
#    df.cyl = df.cyl.astype(str)
#    df.yr = df.yr.astype(str)
#    
    group = df#.groupby(('cyl', 'mfr'))
    source = ColumnDataSource(group)
    
    p = figure(plot_width=800, plot_height=300, title="Mean MPG by # Cylinders and Manufacturer", x_range=group, toolbar_location=None, tools="")
    
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = "Manufacturer grouped by # Cylinders"
    p.xaxis.major_label_orientation = 1.2
    
#    index_cmap = factor_cmap('cyl', palette=['#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c'], 
#                             factors=sorted(df.cyl.unique()), end=1)
    
    p.vbar(x='cyl', top='mpg', width=1, source=source )# ,
#           line_color="white", # fill_color=index_cmap, 
#           hover_line_color="black" ) # , hover_fill_color=index_cmap)
    
#    p.add_tools(HoverTool(tooltips=[("MPG", "@mpg"), ("Cyl, Mfr", "@cyl")]))
    
    return p

def bk_full_example(doc):
    from bokeh.models import ColumnDataSource, HoverTool
    from bokeh.plotting import figure
    from bokeh.sampledata.autompg import autompg_clean as df
    from bokeh.transform import factor_cmap
    
    df.cyl = df.cyl.astype(str)
    df.yr = df.yr.astype(str)
    
    group = df.groupby(('cyl', 'mfr'))
    source = ColumnDataSource(group)
    
    p = figure(plot_width=800, plot_height=300, title="Mean MPG by # Cylinders and Manufacturer",
               x_range=group, toolbar_location=None, tools="")
    
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = "Manufacturer grouped by # Cylinders"
    p.xaxis.major_label_orientation = 1.2
    
    index_cmap = factor_cmap('cyl', palette=['#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c'], 
                             factors=sorted(df.cyl.unique()), end=1)
    
    p.vbar(x='cyl', top='mpg', width=1, source=source,
           line_color="white", fill_color=index_cmap, 
           hover_line_color="black", hover_fill_color=index_cmap)
    
#    p.add_tools(HoverTool(tooltips=[("MPG", "@mpg"), ("Cyl, Mfr", "@cyl")]))
    
    return p
#    return doc.add_root(p)
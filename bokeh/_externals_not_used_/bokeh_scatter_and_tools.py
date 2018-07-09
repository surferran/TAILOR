
# ref user : http://bokeh.pydata.org/en/latest/docs/user_guide/tools.html

import pandas
from bokeh.plotting import figure, output_file, show
from bokeh.models.tools import LassoSelectTool, BoxSelectTool, HoverTool   # for the additional way to add tools
import json

# df=pandas.read_csv("approx.csv")
df=pandas.read_csv("Sensor_record_20150810_002415_AndroSensor.csv",sep=';')
#df=pandas.read_csv("accound_details.csv",sep=',')

p=figure(plot_width=600,plot_height=400,
         tools='pan,wheel_zoom,reset,undo,redo',   # ,UndoTool,RedoTool', resize
         toolbar_location="right",  #"above","below","left","right"
         active_scroll = "wheel_zoom",
         toolbar_sticky=False)


p.add_tools(LassoSelectTool())  # possible option to add tools
#//p.add_tools(BoxSelectTool(dimensions=["width"]))    # only in 1 dimension. note: To make a multiple selection, press the SHIFT key. To clear the selection, press the ESC key.
# p.add_tools(HoverTool())

print "lof_facctor: " + str(p.lod_factor)
print "lod_interval: " + str(p.lod_interval)
print "lod_threshold: " + str(p.lod_threshold)
print "lod_timeout: " + str(p.lod_timeout)

# Bokeh toolbars can have (at most) one active tool from each kind of gesture (drag, scroll, tap).
# configure so that no drag tools are active
# p.toolbar.active_drag = None
# configure so that Bokeh chooses what (if any) scroll tool is active
# p.toolbar.active_scroll = wheel_zoom # "auto"
# configure so that a specific PolySelect tap tool is active
# p.toolbar.active_tap = poly_select

p.tools.wheel_zoom = ""         ## ? what is this line?
p.title.text="Some Title"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="x Axis Title"
p.yaxis.axis_label="Column header"               

p.circle(df[df.columns[0]],df[df.columns[1]],size=10, color="Black")
p.circle(df[df.columns[0]],df[df.columns[2]],size=5, color="Coral")
# p.circle(df[df.columns[0]],df[df.columns[0]],size=7, color="Gray")

tmpA = p.to_json('stam')
tmpB = p.to_json_string('also stam')

print tmpA
print tmpB
with open('txt4Json.txt','wt') as fJSON:
    # fJSON.write(tmpA)
    fJSON.write(tmpB)

with open('txt4Json.json','w') as fJSON:
    # fJSON.write(tmpA)
    json.dump(tmpA, fJSON)
    # fJSON.write(tmpB)


output_file("BokehDfExample.html")
show(p)

"""
bokeh application to show and open section by working steps.

dated : 21/08/18
"""
 
from os.path import dirname, join, relpath
import sys

import pandas as pd

from bokeh.layouts import row, widgetbox, layout, column
from bokeh.models import ColumnDataSource, CustomJS, BoxSelectTool, CrosshairTool  # BoxEditTool, 
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, \
                                    NumberFormatter, CheckboxGroup, RadioGroup, \
                                    Toggle, Panel, Tabs, CheckboxButtonGroup
from bokeh.io import curdoc , push_notebook, show, output_notebook

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure


DATA_PATH_NAME = 'static'
USER_FILE_NAME = 'user_definitions.json'

DATA_DIR = join(dirname(__file__), DATA_PATH_NAME)  # full abs path
rel_DATA_DIR = relpath(DATA_DIR)

rel_User_fileName = join(rel_DATA_DIR, USER_FILE_NAME)

case_test = True
case_test = False

"""**************************************************"""    
    
def my_print(str, prefix=''):
    print("************")
    print(prefix, str)
    print("************")
        
def doc_add_root(doc, obj, title=''):
    print("doc : ", doc)
    print("doc : " + str(doc))
    print("name : ",__name__)
    print("obj : " + str(obj))
    my_print(case_test, 'is it a test case ? : ')
    
    # called from console by bokeh serve, or
    # called from jupyter notebook
    if __name__.startswith('bk_script') \
       or str(doc).startswith('<function curdoc'):  
        doc().add_root(obj)
        doc().title = title
    else:   # called by  __name__=='__main__'
        doc.add_root(obj)
        doc.title = title

"""**************************************************"""    
    
def minimial_page_4_server_test(doc):
    doc.title = "**testing demo page**"
    
    if __name__=='__main__':    
        def button_reaction():
            print("stopping server (self kill. restart)")
            server1.stop()
        toggle   = Button(label='kill server', button_type='success') 
    else:
        def button_reaction():
            print("pressed button")
        toggle   = Button(label='smile:)', button_type='success')  # Options: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    toggle.on_click(button_reaction)
    
    img_paths=[]
    img_paths.append(join(rel_DATA_DIR,'logoScrnSht.png'))
    img_paths.append(join(rel_DATA_DIR,'tree.png'))
    x_range = (-20,10) # could be anything - e.g.(0,1)
    y_range = (20,30)
    factor = 1.2
    figImg = figure(x_range=x_range, y_range=y_range, width=500, height=400)
    figImg.image_url(url=[img_paths[0]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left") 
    factor=2
    figImg.image_url(url=[img_paths[1]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor) #, anchor="bottom_left") default it left-up
        
    doc_add_root(doc, toggle)
    doc_add_root(doc, figImg)

"""**************************************************"""

def make_page_flow(doc):
    
    def on_button_change():
        print("visiting on button change")
    button = Button(label="Phase #1 ", button_type="success") # button_type: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    button.on_click(on_button_change)
    
    controls = widgetbox(button) # text field
        
    total_row = row(controls)
    
    doc_add_root(doc, total_row, title = 'work flow page')

"""**************************************************"""

if __name__=='__main__':
    print("name : ",__name__)
    my_print ("main caller")

    if case_test:
        app = {'/': Application(FunctionHandler(minimial_page_4_server_test))}
        server1 = Server(app, port=5001)
        server1.start()    
        print(server1.port)
        server1.show('/')
    else:
        print("main flow continue")
    #    https://stackoverflow.com/questions/43057328/change-colour-of-bokeh-buttons#
        
        apps1 = {'/': Application(FunctionHandler(make_page_flow))}
        
        server1 = Server(apps1, port=5007)
        server1.start()
        
        server1.show('/')
    #    print(server1.port)
   
    #    # then http://localhost:5007/    
else:
    print(" caller is ", __name__)
    if case_test:
        minimial_page_4_server_test(curdoc)
    else:
        make_page_flow(curdoc)  # default is port 5006
        
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
                                    Toggle, Panel, Tabs, CheckboxButtonGroup, \
                                    Paragraph
from bokeh.io import curdoc , push_notebook, show, output_notebook

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure

import json

from functools import partial # by https://stackoverflow.com/questions/41926478/python-bokeh-send-additional-parameters-to-widget-event-handler

DATA_PATH_NAME = 'static'
USER_FILE_NAME = 'user_definitions.json'

DATA_DIR = join(dirname(__file__), DATA_PATH_NAME)  # full abs path
rel_DATA_DIR = relpath(DATA_DIR)

rel_User_fileName = join(rel_DATA_DIR, USER_FILE_NAME)

case_test = True
case_test = False

default_text =  """
                    this is an initialized text widget
                """
default_abs_script_path = join(dirname(__file__))

"""**************************************************"""    
    
def load_JSON_file_to_Dict(fileName):
    """
    :param fileName: the json file to load
    :return: dictionary object
    """
    json_dict = json.load(open(fileName))
    return json_dict

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

    user_dict = load_JSON_file_to_Dict(rel_User_fileName)
    
    p = Paragraph(text="""
                    this is an initialized text widget
                    """,
                    width=200, height=100)
    text_box = widgetbox(p)

    if __name__=='__main__':    
        def button_reaction():
            print("stopping test-server (self kill. restart)")
            p.text = "stopping server"
            server1.stop()
            p.text = "stopping server .. failed"
        toggle   = Button(label='kill test-server', button_type='success') 
    else:
        def button_reaction():
            print("pressed button")
            p.text = "json content is :\n "+ str(user_dict)
        toggle   = Button(label='smile:) with test', button_type='success')  # Options: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    toggle.on_click(button_reaction)
    
    img_paths=[]
    img_paths.append(join(rel_DATA_DIR,'logoScrnSht.png'))
    img_paths.append(join(rel_DATA_DIR,'tree.png'))
    x_range = (-20,10)
    y_range = (20,30)
    factor = 1.2
    figImg = figure(x_range=x_range, y_range=y_range, width=500, height=400, active_drag='pan', active_scroll='wheel_zoom')
    figImg.image_url(url=[img_paths[0]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left") 
    factor=2
    figImg.image_url(url=[img_paths[1]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor) #, anchor="bottom_left") default it left-up

    doc_add_root(doc, toggle)
    doc_add_root(doc, figImg)
    doc_add_root(doc, text_box)

"""**************************************************"""

def make_page_flow(doc):
    """
    create the flow diagram by json file definitions
    """    
    user_dict = load_JSON_file_to_Dict(rel_User_fileName)
    
    text_P = Paragraph(text=default_text,
                    width=600, height=100)
    # display_original_text = True

    def on_button_change(btn_info):
        print("pressed button change")
        # tmp = display_original_text
        # if display_original_text:
        #     text_P.text = default_text            
        # else:
        text_P.text = "changed text to json content : \n "+str(user_dict)+"\n by "+str(btn_info)  # how to know caller name/id?

        # execute button_data['relevant script']
        # display_original_text = not (tmp)


    flow_items=[]
    for item in user_dict['blocks']:
        if isinstance(item, type(dict())):
            button = Button(label=item['label'], button_type="success")
            button.on_click(partial(on_button_change, btn_info=item))
            control = widgetbox(button) 
            # doc_add_root(doc, control)
            flow_items.append(control)
        elif isinstance(item, type(list())):
            btns = []
            for btn in item:
                button = Button(label=btn['label'], button_type="success")
                button.on_click(partial(on_button_change, btn_info=btn))
                btns.append(widgetbox(button))
            control = row(btns) 
            # doc_add_root(doc, control)
            flow_items.append(control)
    flow_box = column(flow_items)

    text_box = widgetbox(text_P)
        
    total_row = row(flow_box, text_box)
    
    doc_add_root(doc, total_row, title = 'work flow page')

    # doc_add_root(doc, text_box, title = 'work flow page')

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
        
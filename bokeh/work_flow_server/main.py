"""
bokeh application to show and open section by working steps.

dated : 21/08/18
"""
 
from os.path import dirname, join, relpath
import sys, os, json

import pandas as pd

from bokeh.layouts import row, widgetbox, layout, column
from bokeh.models import ColumnDataSource, CustomJS, BoxSelectTool, CrosshairTool  # BoxEditTool, 
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, \
                                    NumberFormatter, CheckboxGroup, RadioGroup, \
                                    Toggle, Panel, Tabs, CheckboxButtonGroup, \
                                    Paragraph, MultiSelect, RangeSlider, TextInput
from bokeh.io import curdoc , push_notebook, show, output_notebook

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure

from bokeh.io.state import curstate
from bokeh.resources import Resources

from functools import partial # by https://stackoverflow.com/questions/41926478/python-bokeh-send-additional-parameters-to-widget-event-handler

import step_1_action

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
    figImg.toolbar.logo=None
    figImg.image_url(url=[img_paths[0]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left") 
    factor=2
    figImg.image_url(url=[img_paths[1]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor) #, anchor="bottom_left") default it left-up
    
    multi_select = MultiSelect(title="Option:", value=["foo", "quux"], size=7,
                       options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])
    def mSlct_update(attrname, old, new):
        myString = ''
        for i in multi_select.value:
            myString += '\n' + i
        myString+='\n'+ str(range_slider.value[0])
        myString+='\n'+ str(range_slider.value[1])
        myString+='\n'+ text_input_as_filter.value
        print("\n\n selected:\n",myString)
        # myText.text = myString
    multi_select.on_change('value', mSlct_update)
    
    range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Stuff")
    range_slider.on_change('value', mSlct_update)
    
    text_input_as_filter = TextInput(value="default", title="Label:") # no workable callback option 


    doc_add_root(doc, toggle)
    doc_add_root(doc, figImg)
    doc_add_root(doc, text_box)
    doc_add_root(doc, multi_select)
    doc_add_root(doc, range_slider)
    doc_add_root(doc, text_input_as_filter)

"""**************************************************"""


# class MyResources(Resources):
#     @property
#     def css_raw(self):
#         return super().css_raw + [
#             """
#             body {
#                 background-image: linear-gradient(red, yellow);
#             }
#             """
#         ]

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

        desired_script = btn_info['relevant script']

        # app_path = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs'
        # os.system(app_path + "/notepad++.exe") # as test
        
        if desired_script=='step_1_action':
            step_1_action.script_main()
        elif desired_script=='step_2_action':
            pass
        # print('desired_script: '+desired_script)
        # __import__(desired_script)  # ref by https://stackoverflow.com/questions/301134/dynamic-module-import-in-python
        # eval(desired_script).script_main()

    flow_items=[]
    for item in user_dict['blocks']:
        if isinstance(item, type(dict())):
            button = Button(label=item['label'], button_type="success")
            button.on_click(partial(on_button_change, btn_info=item))
            control = widgetbox(button) 
            flow_items.append(control)
        elif isinstance(item, type(list())):
            btns = []
            for btn in item:
                button = Button(label=btn['label'], button_type="success")
                button.on_click(partial(on_button_change, btn_info=btn))
                btns.append(widgetbox(button))
            control = row(btns) 
            flow_items.append(control)
    flow_box = column(flow_items)

    text_box = widgetbox(text_P)
        
    total_row = row(flow_box, text_box)
    
    tab1 = Panel(child=total_row, title="flow blocks")

    ''''''
    
    text_input_field = TextInput(value="just default text", title="Label:") # no workable callback option 
    tab2 = Panel(child=text_input_field, title="user parameters to/from file", closable=False)
    
    tabs = Tabs(tabs=[ tab1, tab2 ])
    ''''''
    
    # print("setting resources as mode=cdn..")
    # curstate().file['resources'] = MyResources(mode='cdn')
    # print("setting resources as mode=relative..")
    # # curstate().file['resources'] = MyResources(mode='relative')
    # print("..set resources ")

    #doc_add_root(doc, total_row, title = 'work flow page')
    doc_add_root(doc, tabs, title = 'work flow page')

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
        
        server1 = Server(apps1, port=5008)
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
        
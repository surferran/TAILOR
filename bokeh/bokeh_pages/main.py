"""
launch method reference also from 
http://matthewrocklin.com/blog/work/2017/06/28/simple-bokeh-server

todo:
    duplicate df to build df up to 100k lines. possible on html?
    
"""
 
from os.path import dirname, join

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
#from bokeh.plotting import ColumnDataSource as plt_ColumnDataSource 

import bk_example

#import bokeh
#print (bokeh.__version__)


DATA_DIR = join(dirname(__file__), 'static/')
DATA_DIR = join(dirname(__file__), 'static')

#fileName = DATA_DIR +'salary_data.csv'
fileName = join(DATA_DIR,'salary_data.csv')
    
def doc_add_root(doc,obj):
    print("doc : ", doc)
    print("doc : " + str(doc))
    print("name : ",__name__)
    print("obj : " + str(obj))
    
    # called from console, or
    # called from notebook
    if __name__.startswith('bk_script') \
       or str(doc).startswith('<function curdoc'):  
        doc().add_root(obj)
    else:
#        if __name__=='__main__':   # and for jupyter notebook (name is  bokeh.docu..)
        doc.add_root(obj)
    
    
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
    img_paths.append(join(DATA_DIR,'logoScrnSht.png'))
    img_paths.append(join(DATA_DIR,'tree.png'))
#    img_path = './static/logoScrnSht.png'
#    img_path = r'C:\Users\Ran_the_User\Documents\GitHub\TAILOR\bokeh\bokeh_pages\static\logoScrnSht.png'
#    img_path = 'tree.png'
    x_range = (-20,10) # could be anything - e.g.(0,1)
    y_range = (20,30)
#    x_range = (0,1) # could be anything - e.g.(0,1)
#    y_range = (0,1)
    factor = 1.2
    figImg = figure(x_range=x_range, y_range=y_range, width=500, height=400)
#    figImg.image_url(url=[img_path], x=x_range[0], y=y_range[1], w=x_range[1]-x_range[0], h=y_range[1]-y_range[0], anchor="bottom_left")
    figImg.image_url(url=[img_paths[0]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left") 
    factor=2
    figImg.image_url(url=[img_paths[1]], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor) #, anchor="bottom_left") default it left-up
    
    
    doc_add_root(doc, toggle)
    doc_add_root(doc, figImg)
    
#    if __name__=='__main__':   # = only for jupyter notebook      
#        print("doc : ", str(doc))
#        print("name : ",__name__)
#        doc().add_root(toggle)
#        doc().add_root(figImg)    
#    else:
#        print("doc : ", str(doc))
#        print("name : ",__name__)
#        doc.add_root(toggle)
#        doc.add_root(figImg)    

def make_document(doc):
    doc.title = "Hello, world!"
    
    df = pd.read_csv(fileName) # return dataframe
    if False:
        df = df.set_index('date')
    ''' make a copy of df. therefor changing the source will not affect df.
        using df in update() will ~reset the source to original values '''
    source = ColumnDataSource(data=df) # dict())  
        
    columns = [
        TableColumn(field="name", title="Employee Name"),
        TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="years_experience", title="Experience (years)")
    ]
    
    data_table = DataTable(source=source, columns=columns, width=800) # ,row_headers=None)
    table = widgetbox(data_table, width=880)
    
    def slider_table_update(attr, old, new):
        print ("slider update")
        print(attr)
        print(old)
        print(new)
        current = df[df['salary'] <= slider.value].dropna()  # df ## 
        source.data = {
            'name'             : current.name,
            'salary'           : current.salary,
            'years_experience' : current.years_experience
        }
        return None
    slider = Slider(title="values range", start=0, end=100000, value=21000, step=1, width=800)
    slider.on_change('value', lambda attr, old, new: slider_table_update(attr, old, new))
    
#    fig1 = figure(title='Line plot!') #, sizing_mode='scale_width')
#    fig1.line(x=[1, 2, 3], y=[1, 4, 9])
                  #, sizing_mode='scale_width') ) #  , y_range=(00000, 100000),
#    fig2.scatter(x=source.data['years_experience'], y=source.data['salary'])
#                 title="scatter  example") #, xlabel="xlable", ylabel="ylabel")
#    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    selected_tools = 'pan,wheel_zoom,xbox_select,reset'
    fig2 = figure(title='salary - vs years scatter plot', width=500, height=400, tools='pan, wheel_zoom')
    fig2.scatter(x='years_experience', y='salary', source=source)

#    https://stackoverflow.com/questions/34646270/how-do-i-work-with-images-in-bokeh-python    
#   img_path = 'https://bokeh.pydata.org/en/latest/_static/images/logo.png'
    img_path = join(DATA_DIR,'logoScrnSht.png')
#    img_path = r'C:\Users\Ran_the_User\Documents\GitHub\TAILOR\bokeh\bokeh_pages\static\logoScrnSht.png'
    
    x_range = (-20,10) # could be anything - e.g.(0,1)
    y_range = (20,30)
    factor = 1.2
    
    figImg = figure(x_range=x_range, y_range=y_range)
#    figImg = figure(x_range=x_range, y_range=y_range, width=500, height=400)
    print (img_path)
    figImg.image_url(url=[img_path], x=x_range[0], y=y_range[1], w=x_range[1]-x_range[0], h=y_range[1]-y_range[0])
#    figImg.image_url(url=[img_path], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left") 
    
    toggle_callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        
        var A   = a.value;
        var k   = b.value;
        var phi = c.value;
        var B   = d.value;
        
        var x = data['years_experience']
        var y = data['salary']
        
        for (var i = 0; i < x.length; i++) {
            y[i] =i*2.;
        }
        source.change.emit();
    """)
    
    def isToggleActive(status):
        print("toggle case")
        print(status)
    def on_chkbx_clicked(list_of_checked_options):
        print("chkbx case")
        print(list_of_checked_options)
    def on_radio_clicked(checked_option_ndx):
        print("cradio case")
        print(checked_option_ndx)
#    toggle   = Toggle(label='Some on/off', button_type='success')
    toggle   = Button(label='change table by source', button_type='success', callback=toggle_callback)
#    toggleLayout = layout([toggle])
    
    checkbox = CheckboxGroup(labels=['foo', 'bar', 'baz'])
    radio = RadioGroup(labels=['2000', '2010', '2020'])    
#    toggle.on_click(isToggleActive)
    checkbox.on_click(on_chkbx_clicked)
    radio.on_click(on_chkbx_clicked)
    
    checkbox_button_group = CheckboxButtonGroup(
            labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

    
    def set_vbar():
        fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
        
        fig3 = figure(x_range=fruits, plot_height=250, title="Fruit Counts", toolbar_location=None, tools="")
        
        fig3.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)
        
        fig3.xgrid.grid_line_color = None
        fig3.y_range.start = 0
    
        return fig3 
    
    def event_chart():
        factors = ["a","b","c,","d"]
        x = [24.3, -22.3, -25, 6]
        
        LineColor=["green" if a>=0 else "red" for a in x]
        
        Tooltips = [
            ("index", "$index"),
            ("(x,y)", "($x, $y)")
#            ("radius", "@radius"),
#            ("fill color", "$color[hex, swatch]:fill_color"),
#            ("x", "@x"),
#            ("bar", "@bar"),
        ]
        dots_fig = figure(title="exapmple", y_range = factors, x_range = [-30,30], toolbar_location="below",  toolbar_sticky=False, \
                          tools='lasso_select, poly_select, undo, redo, reset')
#                          , \
#                          tooltips=Tooltips)
        
        dots_fig.segment(0, factors, x, factors, line_width=2, line_color=LineColor)
        c1 = dots_fig.circle(x, factors, size=15, fill_color="orange", line_width=3, line_color=LineColor)
        
<<<<<<< HEAD
#        tool = BoxEditTool(renderers=[c1])
=======
#        tool = BoxEditTool(renderers=[c1]) # ERROR:bokeh.core.validation.check:E-1014 (INCOMPATIBLE_BOX_EDIT_RENDERER): BoxEditTool renderers may only reference Rect glyph models: Circle glyph type(s) found.
>>>>>>> 9abaa8691b56df7c0b9fe4dd2ca1ddf503b38305
        tool2 = BoxSelectTool(dimensions="width") # To make a multiple selection, press the SHIFT key. To clear the selection, press the ESC key
        
#        dots_fig.add_tools(tool) # disappears the points..
        dots_fig.add_tools(tool2)
        dots_fig.add_tools(CrosshairTool(dimensions='height'))
        
        return dots_fig

#    fig2.axis.visible = False
#    fig2.image

    phase1 = column(table, slider)
    phase2 = row(phase1, fig2)
    phase3 = row(event_chart(), set_vbar())
    phase4 = column(phase2, phase3 , checkbox, radio)
    
#    phase5 = bk_example.bk_example()
#    doc.add_root(phase5)
    
#    doc.add_root(phase4)
    
    tab1 = Panel(child=phase4, title="phase4 part")
    
#    doc.add_root(toggle)
#    doc.add_root(figImg)
    
    secPanelLy = column(toggle, figImg, checkbox_button_group)
    tab2 = Panel(child=secPanelLy, title="other parts", closable=False)
    
    tabs = Tabs(tabs=[ tab1, tab2 ])
    
    if __name__!='__main__':    
        print("doc : ", str(doc))
        print("name : ",__name__)
        doc().add_root(tabs)
    else:
        print("doc : ", str(doc))
        doc.add_root(tabs)

#    doc.add_root(event_chart_example())
    
    toggle_callback.args['a']=slider
    toggle_callback.args['b']=toggle
    toggle_callback.args['c']=checkbox
    toggle_callback.args['d']=radio
    
#    slider_table_update()
    
#def make_page_flow(curdoc):
def make_page_flow(doc):
    
#    return make_document(doc)
#    if __name__=='__main__':
#        df = pd.read_csv('salary_data.csv')
#    else:
#    #    df = pd.read_csv('./bokeh_pages/salary_data.csv')
    df = pd.read_csv(fileName)
#    
    source = ColumnDataSource(data=dict())

    def update():
        print ("slider update")
        current = df[df['salary'] <= slider.value].dropna()  # df ## 
        source.data = {
            'name'             : current.name,
            'salary'           : current.salary,
            'years_experience' : current.years_experience,
        }
    
    slider = Slider(title="values range", start=0, end=100000, value=20000, step=1)
    slider.on_change('value', lambda attr, old, new: update())
    
    def on_button_change():
        print("visiting on button change")
    button = Button(label="Phase #1 ", button_type="success") # button_type: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    button.on_click(on_button_change)
#    button.callback = CustomJS(args=dict(source=source),
#                               code=open(join(dirname(__file__), "download.js")).read())
    
    columns = [
        TableColumn(field="name", title="Employee Name"),
        TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="years_experience", title="Experience (years)")
    ]
    
    data_table = DataTable(source=source, columns=columns, width=800)
    
    controls = widgetbox(slider, button)
    table = widgetbox(data_table)
    if __name__!='__main__':    
        print("doc : ", str(doc))
        print("name : ",__name__)
        doc().add_root(row(controls, table))
        doc().title = "work flow page, from caller"
    elif __name__=='__main__':   
        print("doc : ", str(doc)) 
        doc.add_root(row(controls, table))
        doc.title = "work flow page, from main"
    
#    if __name__=='__main__':
    update()

case_test = True
#case_test = False

def my_print(str, prefix=''):
    print("************")
    print(prefix, str)
    print("************")
    
my_print(case_test, 'is it a test case ? : ')

if __name__=='__main__':
#    case_test = False
#    print("doc : "+ str(doc))
#    print("doc : ", doc)
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
        
        apps1 = {'/': Application(FunctionHandler(make_document))}
#        apps1 = {'/': Application(FunctionHandler(make_page_flow))}
    #    apps3 = {'/': Application(FunctionHandler(event_chart_example))}
        
        server1 = Server(apps1, port=5008)
        server1.start()
    #    server2 = Server(apps2, port=5008)
    #    server2.start()
    #    server3 = Server(apps3, port=5009)
    #    server3.start()
    #    make_document()
        
        server1.show('/')
    #    print(server1.port)
    #    server2.show('/')
    #    server3.show('/')
        
    #    # then http://localhost:5008/
        
        section=''
    #    tmp=input("Press Enter to continue...")
    #    section='special stop'
        if section=='special stop':
            server1.stop()
#            server2.stop()
    #        server3.stop()
    
else:
#    print("doc : "+ str(doc))
    print(" caller is ", __name__)
    if case_test:
        minimial_page_4_server_test(curdoc)
    else:
#        make_page_flow(curdoc)  # default is port 5006
        make_document(curdoc)
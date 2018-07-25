"""
launch method reference also from 
http://matthewrocklin.com/blog/work/2017/06/28/simple-bokeh-server

todo:
    duplicate df to build df up to 100k lines. possible on html?
    
"""
 
from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox, layout, column
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, NumberFormatter, CheckboxGroup, RadioGroup, Toggle
from bokeh.io import curdoc

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure
#from bokeh.plotting import ColumnDataSource as plt_ColumnDataSource 

import bk_example

#import bokeh
#print (bokeh.__version__)

fileName = 'C:/Users/Ran_the_User/Documents/GitHub/TAILOR/bokeh/bokeh_pages/'
    
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
    img_paths.append('./bokeh_pages/static/logoScrnSht.png')
    img_paths.append('./bokeh_pages/static/tree.png')
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
    
    if __name__!='__main__':    
        doc().add_root(toggle)
        doc().add_root(figImg)    
    else:
        doc.add_root(toggle)
        doc.add_root(figImg)    

def make_document(doc):
    doc.title = "Hello, world!"
    
    df = pd.read_csv(fileName+'salary_data.csv') # return dataframe
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
                  
    fig2 = figure(title='salary - vs years scatter plot', width=500, height=400, tools='pan, wheel_zoom')
    fig2.scatter(x='years_experience', y='salary', source=source)

#    https://stackoverflow.com/questions/34646270/how-do-i-work-with-images-in-bokeh-python    
#   img_path = 'https://bokeh.pydata.org/en/latest/_static/images/logo.png'
    img_path = 'bokeh_pages/static/logo.png'
    img_path = './static/logoScrnSht.png'
#    img_path = r'C:\Users\Ran_the_User\Documents\GitHub\TAILOR\bokeh\bokeh_pages\static\logoScrnSht.png'
    
    x_range = (-20,-10) # could be anything - e.g.(0,1)
    y_range = (20,30)
    figImg = figure(x_range=x_range, y_range=y_range)
    figImg.image_url(url=[img_path], x=x_range[0], y=y_range[1], w=x_range[1]-x_range[0], h=y_range[1]-y_range[0])

    callback = CustomJS(args=dict(source=source), code="""
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
    toggle   = Button(label='change table by source', button_type='success', callback=callback)
#    toggleLayout = layout([toggle])
    
    checkbox = CheckboxGroup(labels=['foo', 'bar', 'baz'])
    radio = RadioGroup(labels=['2000', '2010', '2020'])    
#    toggle.on_click(isToggleActive)
    checkbox.on_click(on_chkbx_clicked)
    radio.on_click(on_chkbx_clicked)
    
    def set_vbar():
        fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
        
        fig3 = figure(x_range=fruits, plot_height=250, title="Fruit Counts", toolbar_location=None, tools="")
        
        fig3.vbar(x=fruits, top=[5, 3, 4, 2, 4, 6], width=0.9)
        
        fig3.xgrid.grid_line_color = None
        fig3.y_range.start = 0
    
        return fig3 
    
    def event_chart_example():
        factors = ["a","b","c,","d"]
        x = [24.3, -22.3, -25, 6]
        
        LineColor=["green" if a>=0 else "red" for a in x]
        
        dots = figure(title="exapmple", y_range = factors, x_range = [-30,30])
        
        dots.segment(0, factors, x, factors, line_width=2, line_color=LineColor)
        dots.circle(x, factors, size=15, fill_color="orange", line_width=3,line_color=LineColor)
        
        return dots

#    fig2.axis.visible = False
#    fig2.image

    phase1 = column(table, slider)
    phase2 = row(phase1, fig2)
    phase3 = row(event_chart_example(), set_vbar())
    phase4 = column(phase2, phase3 , checkbox, radio)
    
#    phase5 = bk_example.bk_example()
#    doc.add_root(phase5)
    
    doc.add_root(phase4)
    doc.add_root(toggle)
    doc.add_root(figImg)
    
    
#    doc.add_root(event_chart_example())
    
    callback.args['a']=slider
    callback.args['b']=toggle
    callback.args['c']=checkbox
    callback.args['d']=radio
    
#    slider_table_update()
    
#def make_page_flow(curdoc):
def make_page_flow(doc):
    
#    return make_document(doc)
#    if __name__=='__main__':
#        df = pd.read_csv('salary_data.csv')
#    else:
#    #    df = pd.read_csv('./bokeh_pages/salary_data.csv')
    df = pd.read_csv(fileName+'salary_data.csv')
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
    
    slider = Slider(title="values range", start=0, end=100000, value=50000, step=1)
    slider.on_change('value', lambda attr, old, new: update())
    
    def on_button_change():
        print("visiting on button change")
    button = Button(label="phase #1 ", button_type="success") # button_type: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
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
        doc().add_root(row(controls, table))
        doc().title = "work flow page, from caller"
    elif __name__=='__main__':    
        doc.add_root(row(controls, table))
        doc.title = "work flow page, from main"
    
#    if __name__=='__main__':
    update()

case_test = True        

if __name__=='__main__':
#    case_test = False
    print ("main caller")
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
    #    apps2 = {'/': Application(FunctionHandler(make_page_flow))}
    #    apps3 = {'/': Application(FunctionHandler(event_chart_example))}
        
        server1 = Server(apps1, port=5007)
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
    print("not main caller")
    if case_test:
        minimial_page_4_server_test(curdoc)
    else:
        make_page_flow(curdoc)  # default is port 5006
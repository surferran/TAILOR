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
from bokeh.plotting import ColumnDataSource as plt_ColumnDataSource 


def make_document(doc):
    doc.title = "Hello, world!"
    
    df = pd.read_csv('salary_data.csv') 
    source = ColumnDataSource(data=df) # dict())
        
    columns = [
        TableColumn(field="name", title="Employee Name"),
        TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="years_experience", title="Experience (years)")
    ]
    
    data_table = DataTable(source=source, columns=columns, width=800) # ,row_headers=None)
    table = widgetbox(data_table, width=880)
    
#    doc.add_root(table)
    
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
    
#    doc.add_root(slider)

#    fig1 = figure(title='Line plot!') #, sizing_mode='scale_width')
#    fig1.line(x=[1, 2, 3], y=[1, 4, 9])
    fig2 = figure(title='salary - vs years scatter plot', width=500) #, sizing_mode='scale_width')
#    fig2.scatter(x=source.data['years_experience'], y=source.data['salary'])
    fig2.scatter(x='years_experience', y='salary', source=source)
    
    def special_btn_chng():
        print("special case")
    toggle = Toggle(label='Some on/off', button_type='success')
    checkbox = CheckboxGroup(labels=['foo', 'bar', 'baz'])
    radio = RadioGroup(labels=['2000', '2010', '2020'])    
#    toggle.on_click(special_btn_chng)
#    checkbox.on_change(special_btn_chng)
#    radio.on_change(special_btn_chng)

#    doc.add_root(fig1)
#    doc.add_root(fig2)
    phase1 = column(table, slider)
    phase2 = row(phase1, fig2)
    phase3 = column(toggle, checkbox, radio)
    doc.add_root(phase2)
    doc.add_root(phase3)
    
#    slider_table_update()
    
#def make_page_flow(curdoc):
def make_page_flow(doc):
    
#    return make_document(doc)
#    if __name__=='__main__':
#        df = pd.read_csv('salary_data.csv')
#    else:
#    #    df = pd.read_csv('./bokeh_pages/salary_data.csv')
    df = pd.read_csv('salary_data.csv')
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

if __name__=='__main__':
    
    apps1 = {'/': Application(FunctionHandler(make_document))}
    apps2 = {'/': Application(FunctionHandler(make_page_flow))}
    
    server1 = Server(apps1, port=5008)
    server1.start()
    server2 = Server(apps2, port=5007)
    server2.start()
#    make_document()
    
    server1.show('/')
#    print(server2.port)
#    server2.show('/')
    
#    # then http://localhost:5008/
    
    section=''
    if section=='special stop':
        server1.stop()
        server2.stop()
    
else:
    make_page_flow(curdoc)  # default is port 5006
"""
launch method reference also from 
http://matthewrocklin.com/blog/work/2017/06/28/simple-bokeh-server
"""
 
from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, NumberFormatter
from bokeh.io import curdoc

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure 
from bokeh.plotting import ColumnDataSource as plt_ColumnDataSource 


def make_document(doc):
    fig = figure(title='Line plot!', sizing_mode='scale_width')
    fig.line(x=[1, 2, 3], y=[1, 4, 9])

    doc.title = "Hello, world!"
    doc.add_root(fig)

def make_table():
    if __name__=='__main__':
        df = pd.read_csv('salary_data.csv')
    else:
    #    df = pd.read_csv('./bokeh_pages/salary_data.csv')
        df = pd.read_csv('salary_data.csv')
    
    source = ColumnDataSource(data=dict())

    def update():
        current = df[df['salary'] <= slider.value].dropna()
        source.data = {
            'name'             : current.name,
            'salary'           : current.salary,
            'years_experience' : current.years_experience,
        }
    
    slider = Slider(title="Max Salary", start=10000, end=250000, value=150000, step=1000)
    slider.on_change('value', lambda attr, old, new: update())
    
    button = Button(label="Download", button_type="success")
    button.callback = CustomJS(args=dict(source=source),
                               code=open(join(dirname(__file__), "download.js")).read())
    
    columns = [
        TableColumn(field="name", title="Employee Name"),
        TableColumn(field="salary", title="Income", formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="years_experience", title="Experience (years)")
    ]
    
    data_table = DataTable(source=source, columns=columns, width=800)
    
    controls = widgetbox(slider, button)
    table = widgetbox(data_table)
    
    curdoc().add_root(row(controls, table))
    curdoc().title = "Export CSV"
    
    update()

if __name__=='__main__':
    
    apps = {'/': Application(FunctionHandler(make_document))}
    
    server = Server(apps, port=5008)
    server.start()
#    make_document()
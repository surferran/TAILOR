"""**************************************************"""

from main_imports import *

"""**************************************************"""
def reset_and_create_demo_source():
    '''
    :return:    df , type of DataFrame()
                source , type of dict()
    '''
    fileName_csv_source = join(rel_DATA_DIR, 'salary_data.csv')
    df = pd.read_csv(fileName_csv_source)  # return dataframe
    if False:
        df = df.set_index('date')
    ''' make a copy of df. therefor changing the source will not affect df.
        using df in update() will ~reset the source to original values '''
    source = ColumnDataSource(data=df)  # dict())

    return df, source

def create_demo_table(source):
    columns = [
        TableColumn(field="name"            , title="Employee Name"),
        TableColumn(field="salary"          , title="Income",
                                    formatter=NumberFormatter(format="$0,0.00")),
        TableColumn(field="years_experience", title="Experience (years)")
    ]

    data_table  = DataTable(source=source, columns=columns, width=800)  # ,row_headers=None)
    table       = widgetbox(data_table, width=880)

    return table

def create_demo_table_slider(df, source):
    slider = Slider(title="values range", start=0, end=100000, value=21000, step=1, width=800)

    def slider_table_update():
        print("slider update")
        ''' reset dataFrame with new limit from slider new value '''
        current = df[df['salary'] <= slider.value].dropna()
        source.data = {
            'name': list(current.name),
            'salary': list(current.salary),
            'years_experience': list(current.years_experience)
        }
        return None

    slider.on_change('value', lambda attr, old, new: slider_table_update())

    slider_table_update()

    return slider


def create_demo_figure(source):
    #    fig1 = figure(title='Line plot!') #, sizing_mode='scale_width')
    #    fig1.line(x=[1, 2, 3], y=[1, 4, 9])
                      #, sizing_mode='scale_width') ) #  , y_range=(00000, 100000),
    #    fig2.scatter(x=source.data['years_experience'], y=source.data['salary'])
    #                 title="scatter  example") #, xlabel="xlable", ylabel="ylabel")
    #    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

    selected_tools = 'pan, wheel_zoom, xbox_select, reset'
    fig2 = figure(title='salary - vs years scatter plot', width=500, height=400, tools='pan, wheel_zoom')
    fig2.scatter(x='years_experience', y='salary', source=source)

    # layout needs numbers
    # fig2.add_layout(Arrow(x_start=4, y_start=15000,  x_end=7,  y_end=18000))
    # fig2.add_layout(Arrow(x_start=4, y_start=15000,  x_end=7,  y_end=15000))
    # fig2.add_layout(Arrow(x_start=4, y_start=15000,  x_end=4,  y_end=18000))
    add_axis_to_fig(fig2, [4, 15000, 7, 18000])

    # fig2.text(x=4, y=16000, text='Agriculture', text_font_style='bold', text_align=33, backgroundcolor='#f0f0f0') # color=colors[0],

    return fig2

def create_demo_img_fig():
    #    https://stackoverflow.com/questions/34646270/how-do-i-work-with-images-in-bokeh-python
    #   img_path = 'https://bokeh.pydata.org/en/latest/_static/images/logo.png'
    img_path = join(rel_DATA_DIR, 'logoScrnSht.png')
    #    img_path = r'C:\Users\Ran_the_User\Documents\GitHub\TAILOR\bokeh\bokeh_pages\static\logoScrnSht.png'
    my_print(img_path)

    x_range = (-20, 10)  # could be anything - e.g.(0,1)
    y_range = (20, 30)
    factor = 1.2

    figImg = figure(x_range=x_range, y_range=y_range)
    #    figImg = figure(x_range=x_range, y_range=y_range, width=500, height=400)
    print(img_path)
    figImg.image_url(url=[img_path], x=x_range[0], y=y_range[1],
                     w=x_range[1] - x_range[0], h=y_range[1] - y_range[0])

    add_axis_to_fig(figImg, [0, 22, 10, 26])

    figImg.circle(0, 22, size=15, fill_color="green", line_width=3, line_color="black")

    return figImg

#    figImg.image_url(url=[img_path], x=x_range[0]/factor, y=(y_range[0]+y_range[1])/2, w=(x_range[1]-x_range[0])/factor, h=(y_range[1]-y_range[0])/factor, anchor="bottom_left")

def create_more_demo_controls():
    def on_chkbx_clicked(list_of_checked_options):
        print("chkbx click case")
        print(list_of_checked_options)
    checkbox = CheckboxGroup(labels=['foo', 'bar', 'baz'])
    checkbox.on_click(on_chkbx_clicked)

    def on_radio_clicked(checked_option_ndx):
        print("radio click case")
        print(checked_option_ndx)
    radio = RadioGroup(labels=['2000', '2010', '2020'])
    radio.on_click(on_radio_clicked)

    def on_checkbox_clicked(checkbox_ndx):
        print("checkbox click case")
        print(checkbox_ndx)
    checkbox_button_group = CheckboxButtonGroup(
            labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])
    checkbox_button_group.on_click(on_checkbox_clicked)

    return column(checkbox, radio, checkbox_button_group)

def create_demo_data_table_source_and_columns():
    from datetime import date
    from random import randint

    data = dict(
        dates=[date(2014, 3, i + 1) for i in range(10)],
        downloads=[randint(0, 100) for i in range(10)],
    )
    file_data_source = ColumnDataSource(data)

    # file_data_Columns = [
    #     TableColumn(field="dates", title="Date"),
    #     TableColumn(field="downloads", title="Downloads"),
    #     TableColumn(field="downloads", title="Downloads same"),
    # ]

    file_data_Columns = [TableColumn(field=name, title="col of " + name) for name in list(data.keys())]

    return file_data_source, file_data_Columns

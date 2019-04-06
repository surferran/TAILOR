""" @package docstring
main.py
ver 12/2/19
handles bokeh server elements to construct an html server with Tabs elements:
-input seslection
-data views
-detailed selections and adjustments
    
"""
from main_imports import *
 
from main_utils import *

from demo_parts import *


def get_df_of_variables(df):
    var_df =  pd.DataFrame()

    var_df['var name'] = list(df.keys())

    if __debug__:
        print("var ds is:\n ", var_df)

    return var_df

def make_document(doc):
    doc_title = "Hello, world!"

    demo_df, demo_source = reset_and_create_demo_source()

    demo_table_widget = create_demo_table(demo_source)

    demo_slider = create_demo_table_slider(demo_df, demo_source)

    demo_fig = create_demo_figure(demo_source)

    figImg = create_demo_img_fig()

    more_demo_ctrls = create_more_demo_controls()

    demo_row1 = row(column(demo_table_widget, demo_slider), demo_fig )
    demo_panel = column(demo_row1, row(more_demo_ctrls, figImg))

    tab_demo = Panel(child=demo_panel, title="demo parts", closable=True)

    """ ##################### """

    """ define and create objects that will use through all the Tabs """
    appDataObj = appDB.myAppData()
    appDataObj.initializeDataFields()

    files_checkboxs = CheckboxGroup(labels=[])   # labels=['foo', 'bar', 'baz']  # for tab3
    csv_header_flag = CheckboxGroup(labels=["CSV has header - relate to it"])
    csv_header_flag.active = [0]   # sets indeces if which items are active

    multi_select = MultiSelect(title="selected files", value=[], size=7, options=[], width=950) # for tab2

    file_data = dict()
    file_data_source = ColumnDataSource(file_data)
    file_data_Columns = [] # [TableColumn(field=Ci, title=Ci) for Ci in file_data.columns]  # bokeh columns

    print("should update table now")
    file_data_source, file_data_Columns = create_demo_data_table_source_and_columns()
    # dfVar = get_df_of_variables
    file_data_Columns = [TableColumn(field='var name', title='col of var')]

    file_data_table = DataTable(source=file_data_source, columns=file_data_Columns, width=800)
    files_data_table_wdgt = widgetbox(file_data_table, width=880)

    def mSlct_update(attrname, old, new):
        myString = ''
        filesPaths = []
        for i in multi_select.value:
            myString += '\n' + i
            filesPaths.append(i)
        print("\n\n selected files:\n",myString)
        files_checkboxs.labels = filesPaths
    multi_select.on_change('value', mSlct_update)

# check https://stackoverflow.com/questions/34169264/how-to-add-hovertool-to-a-data-table-bokeh-python to learn
    def on_text_input_change(attr, old, new):
        print("Previous label: " + old)
        print("attribute : ", attr)
        print("Updated label: " + new)
        # check if new is path. if sow - get files list
        # print(base_path_text_Input.value, file_attr_text_Input.value)
        ret = fH.list_files_in_path(base_path=base_path_text_Input.value, filter=file_attr_text_Input.value)
        col1 = [itm[0] for itm in ret]
        col2 = [itm[1] for itm in ret]
        col3 = [itm[2] for itm in ret]
        FilteredFiles_source.data ={
            'name'      : list(col1),
            'path'      : list(col2),
            'mod date'  : list(col3)
        }
        return None

    def fTable_clicked(attr, old, new):
        # print("fTAble clicked", attr)
        # print(old)
        # print(new)
        # https://groups.google.com/a/continuum.io/forum/#!topic/bokeh/jGHbTWVqH6U
        # https: // github.com / bokeh / bokeh / wiki / Filterable - Data - Source
        try:
            selected_rows_indeces = FilteredFiles_source.selected["1d"]["indices"]
            print("selected_rows_indeces",selected_rows_indeces)
            # print(sourceFilteredFiles.data)
            for ndx in selected_rows_indeces:
                selected_full_files_str = FilteredFiles_source.data['mod date'][ndx]
                print (selected_full_files_str)
        except IndexError:
            print("index error")
            pass

        # relevant output is : selected_rows_indeces

    template_for_tooltip = """<span href="#" data-toggle="tooltip" title="<%= value %>"><%= value %></span>"""

    FilteredFiles_source = ColumnDataSource(data=pd.DataFrame()) # dict() is the returned type
    files_table_columns = [
        TableColumn(field="name", title="Name"),
        TableColumn(field="path", title="Path"),
        TableColumn(field="mod date", title="modification date", formatter=HTMLTemplateFormatter(template=template_for_tooltip))
    ]
    # edit dataTable: https://stackoverflow.com/questions/32321841/how-to-add-a-callback-to-bokeh-datatable
    # https://bokeh.pydata.org/en/latest/docs/reference/model.html#bokeh.model.Model
    # https: // bokeh.pydata.org / en / latest / docs / reference / models / widgets.tables.html
    # JS css by: https://stackoverflow.com/questions/47874323/adding-color-to-bokeh-datatable-header
    files_table = DataTable(source=FilteredFiles_source, columns=files_table_columns, width=1050, fit_columns=True)#, row_height=13)
    fTable = widgetbox(files_table, width=1050)
    FilteredFiles_source.on_change('selected', fTable_clicked)
    # files_table.on_click(fTable_clicked)
    # print(FilteredFiles_source.to_json(include_defaults=True))
    # print(files_table.to_json(include_defaults=True))

    # base_path_str = os.path.curdir  # relative path
    base_path_str = os.path.abspath(os.path.curdir) # absolute format
    base_path_text_Input = TextInput(value=base_path_str, title="base path for files:", width=750)
    base_path_text_Input.on_change("value", on_text_input_change)

    file_attr_str = '.csv'
    file_attr_text_Input = TextInput(value=file_attr_str, title="files attribute for search", width=160)
    file_attr_text_Input.on_change("value", on_text_input_change)

    on_text_input_change("","","")  # init

    def files_button_reaction():
        print("pressed files_button")
        selected_rows_indeces = FilteredFiles_source.selected["1d"]["indices"]
        print("passed selected_rows_indeces", selected_rows_indeces)
        for ndx in selected_rows_indeces:
            selected_full_files_str = FilteredFiles_source.data['mod date'][ndx]
            print(selected_full_files_str)
            multi_select.value.append(selected_full_files_str)
            multi_select.options.append((selected_full_files_str, selected_full_files_str))
        print("added relevent selections to trimmed list")

    files_toggle = Button(label='mark file(s)', button_type='success')  # Options: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    files_toggle.on_click(files_button_reaction)

    inPanel = column(base_path_text_Input, file_attr_text_Input, fTable, files_toggle, multi_select)
    tab2 = Panel(child=inPanel, title="inputs selections", closable=False)

    """ ##################### """

    def on_files_chkbx_clicked(list_of_checked_options):
        print("files chkbx click case")
        print(list_of_checked_options)
    files_checkboxs.on_click(on_files_chkbx_clicked)

    def update_file_data_table(file_data_source, file_data_Columns, givenDF):
        """
        :param givenDF: pd.dataframe of the file read
        :return: new source setting for
        file_data_source
        file_data_Columns
        """

        givenDict = dict(givenDF)

        print("should update table now")

        if False:
            from datetime import date
            from random import randint

            data = dict(
                dates=[date(2014, 3, i + 1) for i in range(10)],
                downloads=[randint(0, 100) for i in range(10)],
            )
            file_data_source.data = data

            file_data_Columns = [
                TableColumn(field="dates", title="Date"),
                TableColumn(field="downloads", title="Downloads"),
                TableColumn(field="downloads", title="Downloads sm"),
            ]
            file_data_Columns = [TableColumn(field=name, title="col of "+name) for name in list(data.keys())]
        else:
            file_data_source.data = dict(get_df_of_variables(givenDF))
            #todo: change data table width accordingly

        file_data_table.update()
        print("data_table updated. hope it is.")

    def load_button_reaction():
        if len(files_checkboxs.active)<1:
            print("no file name has been chosen. please reTry")
            return
        """""""""""" """"""""""""
        print("files_checkboxs.labels", files_checkboxs.labels)
        # fPaths = [files_checkboxs.labels[ndx] for ndx in files_checkboxs.active]
        # fPaths = map(lambda ndx: files_checkboxs.labels[ndx], files_checkboxs.active)
        fPaths=[]
        for ndx in files_checkboxs.active:
            fPaths.append(files_checkboxs.labels[ndx])
        if len(fPaths)>0 :
            print("should now load: ", fPaths)
        else:
            print("no file name has been chosen. please reTry")
            return
        """""""""""" """"""""""""
        useHeader = (csv_header_flag.active == [0])        # todo: useHeader sign for each item in table?
        print("useHeader request: ",useHeader)

        # todo: add button select all, clear all
        # otherwise it will reload all all the time

        """""""""get 1st file to load"""""""""
        for pth in fPaths:
            fDetail = fH.get_file_details(pth)
            fH.load_CSV_to_appData(fDetail, appDataObj, headerVar=useHeader)

        # fileDictionaries = map(lambda n: fH.get_file_details(n), fPaths)
        # print("fileDictionaries",fileDictionaries)
        # map(lambda n: fH.load_CSV_to_appData(n, appDataObj, headerVar=useHeader), fileDictionaries);

        loadedFiles = appDataObj.mainDict
        print("newly added loadedFiles.name is:\n ", loadedFiles[-1].Name)
        for item in loadedFiles:
            print(" \n loadedFiles.name is: ", item.Name)

        update_file_data_table(file_data_source, file_data_Columns, loadedFiles[-1].loadedData)

        get_correct_doc(doc).clear()

        tabNew = Panel(child=files_data_table_wdgt, title="files selections", closable=True)
        doc_add_root(doc, tabNew, title = 'new tab added ')

    load_toggle = Button(label='load file(s)', button_type='success')  # Options: ‘default’, ‘primary’, ‘success’, ‘warning’, ‘danger’, ‘link’
    load_toggle.on_click(load_button_reaction)

    def unload_button_reaction():
        appDataObj.initializeDataFields()

    unload_toggle = Button(label='unload file(s)', button_type='success')
    unload_toggle.on_click(unload_button_reaction)

    grphPnl = column(files_checkboxs, csv_header_flag, row(load_toggle, unload_toggle), files_data_table_wdgt)
    tab3 = Panel(child=grphPnl, title="graphs", closable=False)

    """ ##################### """

    # tabs = Tabs(tabs=[ tab2, tab3, tab_demo ])
    tabs = Tabs(tabs=[ tab2, tab3 ])
    
    doc_add_root(doc, tabs, title="new tabs page")

    output_bokeh_state_to_json(doc)


"""**************************************************"""

if __name__=='__main__':
    print("name : ", __name__)
    my_print("main caller")
else:
    print(" caller is ", __name__)
    make_document(curdoc)
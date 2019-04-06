'''
files handling introduction functions
'''

import os

from subprocess import call, Popen

import pandas as pd

import csv

import time

def print_errors(given_err,msg):
    print ('*********************')
    print ('** ' + str(given_err))
    print ('** ' + msg)
    print ('*********************')

def get_file_details(full_file_name):
    fileNoExt,  file_extension = os.path.splitext(full_file_name) #[1]  # [1][1:]  get only the text of the extension, without the dot.  #.lower() to look on common grounds
    print("details:",fileNoExt)
    print("details:", file_extension)
    fileDetails = {}
    fileDetails['originalGivenName'] = full_file_name
    fileDetails['absPath']           = os.path.dirname(os.path.abspath(fileNoExt))        # 
    fileDetails['relPath']           = ''       # todo: find out how to get relative path
    fileDetails['basename']          = os.path.basename(fileNoExt)       # file name , with no extension
    fileDetails['extension']         = file_extension                    # '.txt' for example
    fileDetails['isFile']            = os.path.isfile(full_file_name)    # true if the given full name is existing file
    # print os.path.dirname(fileNoExt)
    # print os.path.curdir
    print (fileDetails)   # todo: how to print or set dict without sorting?
    print ((''))
    
    return fileDetails

def list_files_in_path_TRIAL(base_path='.', include_sub_dirs=True, filter='*'):
    """
    :param base_path: default is current run? directory
    :param include_sub_dirs: : default is to include
    :param filter: default is to show all files
    default is getting list og all files from base path to the inner one.
    :return: list of string :
                file name , full path, fileinfo?, modify_date?

    by
     https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
     or
     https://www.quora.com/Whats-the-easiest-way-to-recursively-get-a-list-of-all-the-files-in-a-directory-tree-in-Python
    """
    print("list_file_in_path: ", base_path)

    import glob
    ret = glob.glob('*.csv')
    glob.glob('*.*', recursive=True)
    glob.glob('*')

    import re, os
    files = [f for f in os.listdir('.') if re.match(r'[0-9]+.*\.jpg', f)]

    import os
    os.path.abspath(os.path.curdir)
    os.listdir('.')
    relevant_path = "."
    included_extensions = ['jpg', 'csv', 'bmp', 'png', 'py']
    file_names = [fn for fn in os.listdir(relevant_path)
                  if any(fn.endswith(ext) for ext in included_extensions)]

    import os
    root = "."
    pattern = "*"
    alist_filter = ['jpg', 'bmp', 'png', 'py']
    path = os.path.join(root, "./")
    ret = os.walk('.')
    for item in ret:
        print(item)
    # for item in d:
    #     print(item)
    # for item in f:
    #     print(item)
    for r, d, f in os.walk(path):
        for file in f:
            if file[-3:] in alist_filter and pattern in file:
                print
                os.path.join(root, file)

    # find files in all path and sub paths
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                print(os.path.join(root, file))

    return ret


def list_files_in_path(base_path='.', include_sub_dirs=True, filter=''):
    """

    :param base_path:
    :param include_sub_dirs:
    :param filter:
    :return:
    """

    # find files in all path and sub paths
    ret = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(filter):
                ret.append((root, file, os.path.join(root, file)))
                print(os.path.join(root, file))

    return ret

def file_action_by_type(full_file_name, parentAppData):       # todo: act on file ? already from here and not the calling function?
    fileDict = get_file_details(full_file_name)

    if fileDict['isFile']==True:
        #todo: add file path to records
        if fileDict['extension'] == '.txt':
            # todo: ask to open as notepad and edit ?
            print ("text file is given")
            open_TXT_in_favorite_NOTEPAD(full_file_name)

        elif fileDict['extension'] == '.py':
            # todo: ask to open as notepad and edit? , or execute and from which work folder?
            print ("python file is given")
            execute_py_script(full_file_name)

        elif fileDict['extension'] == '.csv':
            # todo: import data, and display on new list of loaded files and data records.
            # open file in new table (minimized) view
            # import_csv_from_file(name_of_file) #load content into appDataBase as
            # show_table_data_on_table_view
            print ("csv data file is given")
            load_CSV_to_appData(fileDict, parentAppData)

        elif fileDict['extension'] == '.xls':
            print("xls data file is given")
            load_XLS_to_appData(fileDict, parentAppData)

        elif fileDict['extension'] == '.xml':
            # open file in new tree viewer
            # import_xml_from_file(name_of_file) #load content into appDataBase as
            # show_xml_on_tree_view
            print ("xml file is given")
        elif fileDict['extension'] == '.exe':
            pass
        elif fileDict['extension'] == '.dll':
            pass
        elif fileDict['extension'] == '.jpg' or fileDict['extension'] == '.tif' or fileDict['extension'] == '.tiff':
            pass
        # elif fileDict['extension'] == '.dll':
        #     pass
        # elif fileDict['extension'] == '.dll':
        #     pass

def execute_py_script(full_file_name):
    try:
        execfile(full_file_name)
        if __debug__==True:
            print (full_file_name + " executed")
    except Exception as e:
        print_errors(e, "some exception in trying stand-alone execution of : " + full_file_name)
    pass

def open_TXT_in_favorite_NOTEPAD(full_file_name):
    # help from : http://docs.notepad-plus-plus.org/index.php/Command_Line_Switches 
    #             https://docs.python.org/2/library/subprocess.html#module-subprocess
    # app_location = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Notepad++'
    # app_name = 'NOTEPAD++.lnk'
    # app_string = app_location + '/' + app_name
    app_string = r'C:\Program Files (x86)\Notepad++\Notepad++.exe'
    cmd_str = app_string + ' ' + full_file_name # /o ?
    print (cmd_str)
    print (app_string)
    try:
        # call (cmd_str) # Waits for command to complete
        Popen(cmd_str)
        if __debug__==True:
            print (cmd_str + " executed")
    except FileNotFoundError as e:
        print (e)
    except Exception as e:
        print_errors(e, "some exception in trying  : " + cmd_str)
    else:
        pass
    finally:
        pass


# Function to convert a csv file to a list of dictionaries.  Takes in one variable called "variables_file"
def load_CSV_to_dict(file):
    ### todo
    return None
    ### todo

    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs

    reader = csv.DictReader(open(file, 'rb'))
    dict_list = []
    for line in reader:
        dict_list.append(line)

    if __debug__==True:
        print (dict_list)
    return dict_list

def load_CSV_to_dataframe(file, headerVar = True):
    # todo: add check for udf16 instead 8
    if (headerVar == False):
        df = pd.read_csv(file, sep=',', header=None)#, usecols=[2])   #update parameters. also can check built-in for header text or not ? notify as recomndation for user approval.
    else:
        df = pd.read_csv(file, sep=',')
    if __debug__==True:
        print (df.values)
    return df

def load_XLS_to_dataframe(file):
    df = pd.read_excel(file)
    if __debug__==True:
        print (df.values)
    return df

def add_dict_to_appData(new_dict, appDataBase):
    pass

def add_df_to_appData(file_details, new_df, appDataBase):
    newObj = appDataBase.fileObjClass()
    newObj.Name         = file_details['originalGivenName']
    newObj.alias        = file_details['basename']
    newObj.loadedData   = new_df
    newObj.Path         = file_details['absPath']
    newObj.Type         = 'DataFrame' #file_details['extension']
    newObj.dataTimeStamp= time.ctime()

    appDataBase.addDataFromFile(newObj)


def load_CSV_to_appData(file_details, appDataBase, headerVar = True):
    # csv_dict = load_CSV_to_dict(full_file_name) 
    csv_df   = load_CSV_to_dataframe(file_details['originalGivenName'], headerVar)
    print (csv_df)
    if __debug__ and False:
	    print ("available DataFrame actions are: ")
    	print (dir(pd.DataFrame))
    	print (appDataBase)
    # add_dict_to_appData(csv_dict, appDataBase)
    add_df_to_appData(file_details, csv_df, appDataBase)
    if __debug__:
        print("appDataBase", appDataBase.mainDict)

    if __debug__==True:
        print ("data from csv file was loaded and added to appdata")

def load_XLS_to_appData(file_details, appDataBase):
    xls_df   = load_XLS_to_dataframe(file_details['originalGivenName'])
    if __debug__==True:
        print (xls_df)
    add_df_to_appData(file_details, xls_df, appDataBase)

    if __debug__==True:
        print ("data from csv file was loaded and added to appdata")

if __name__ == '__main__':
    # file_action_by_type('..\pyGUI\perspectives.txt', None)
    # load_CSV_to_dict('quad_sim.csv')

    # file_action_by_type('C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives.txt')
#    '''
#    print (fileNoExt)
#    print file_extension
#    print os.path.abspath(fileNoExt)
#    print os.path.basename(fileNoExt)
#    print os.path.dirname(fileNoExt)
#    print os.path.isfile(fileNoExt)
#    print os.path.isfile(full_file_name)
#    print os.path.relpath(fileNoExt)
#    print os.path.relpath(full_file_name)
#    print os.path.curdir
#    
#    expected output:
#    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives
#    .txt
#    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI\perspectives
#    perspectives
#    C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\pyGUI
#    False
#    True
#    perspectives
#    perspectives.txt
#    '''
    # sort_file_action_by_type('JsonControlPanel.json')
    # sort_file_action_by_type('AUI_MAIN.py')
    # sort_file_action_by_type('perspectives.txt')

    ret = list_files_in_path(filter='.py')
    print (ret)
    col1 = [itm[0] for itm in ret]
    print(col1)
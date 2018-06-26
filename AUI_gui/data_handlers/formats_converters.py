"""
converters for all kind of the basic formats
done:
read file to array of strings (each line)
todo:
json string
xml handling functions
"""

import pandas as pd
import json
from pprint import pprint  # used in 'load_json_file()'
import xml

"""
### file readers - direct read to certain known data format ###
"""
def load_file_to_String(fileName):
    """
    :param fileName:
    :return: list of strings. each line in seperate string element.
    """
    with open(fileName, 'r') as f:
        rslt = f.readlines()
    return rslt

def load_CSV_file_to_DataFrame(fileName, headerVar=True):
    """
    :param fileName: input file name including required .csv extension
    :param headerVar: does the file includes header line of fields names?
    :return: the pandas dataframe
    """
    if (headerVar == False):
        df = pd.read_csv(fileName, sep=',', header=None)
    else:
        df = pd.read_csv(fileName, sep=',')
    if __debug__ == True:
        print df.values
    return df

def load_JSON_file_to_Dict(fileName):
    """
    :param fileName: the json file to load
    :return: dictionary object
    """
    json_dict = json.load(open(fileName))
    if __debug__ == True:
        pprint(json_dict)
    return json_dict

"""
### specific formats converters ###
"""
# def xml_file_to_dict(file_name):
#     # get example
#     read_xml_file
#     xml_to_dict;
#     pass
#
# def xml_file_to_pd_dataframe(file_name):
#     # get example
#     read_xml_file
#     xml_to_dataframe;
#     pass
# def dict_to_dataframe():
#     pass

if __name__=='__main__':
    #todo: use unittest or mock to verify those
    test_file = 'df_data_example.csv'
    rslt = load_file_to_String(test_file)
    pass
    rslt = load_CSV_file_to_DataFrame(test_file)
    pass
    json_test_file = '../user_prefs/settings_Toolbars_Items.json'
    rslt = load_JSON_file_to_Dict(json_test_file)
    pass
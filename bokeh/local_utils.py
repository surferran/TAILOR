"""
contains general utilities and helper functions for the software
"""

import json
def get_dict_from_json_file(fileName):
    """
    returns dictionary from file
    """
    json_dict = json.load(open(fileName))
    return json_dict

import shutil
def copy_source_to_taget_paths(source, target):
    """
    will copy the files from source location 
    """
    print("check point print - entered function copy_source_to_tar_paths")
    
    pass

import os
    
""" ****************************************************************"""

if __name__=='__main__':
    print (get_dict_from_json_file('user_settings.json'))
    print (copy_source_to_taget_paths('a','s'))
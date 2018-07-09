"""
handle the copy of source code to local location
"""

import common as cmn
    
def get_source_to_local(sourcePath, local):
    print("check point print - entered function copy_source_to_tar_paths")
    """
    1.ask user for path location
    2.verify path is new 
      if new - create one and download
      if exists - don;t download. ask user to proceed to next phase (compile)
    """
#    cmn.local_utils.shutil.
    '''
    optional cases:
        0 validate inputs : no spaces in paths names. for better os support.
        1. no local dir. then create new one and then copy
        2. there is local dir. it is TOTALY empty. then copy
        3. it is not empty -> notify the user and stop the process.
    '''
    cmn.local_utils.shutil.copytree(sourcePath, local)
    print ("copied source to target")


""" ****************************************************************"""

if __name__=='__main__':
    print cmn.local_utils.get_dict_from_json_file('user_settings.json')
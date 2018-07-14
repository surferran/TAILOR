"""
this is the main operating file for bokeh server.

the software method guidlines:
    -sphinx syntax for semi-automatic documentation
    -usage of user definitions from json files
    -make unittests through the way 

todo:
    add usage of 'logging'
    
"""

import common as cmn

import bokeh_pages.main as bkPage
import _1_copy_source   as block1_module

def phase1_func(flow_steps, user_defs):
    copy_func   = flow_steps["1"]["action function"]
    src         = user_defs['source_code_location']
    trgt        = user_defs['local_storage_path']
    copy_func(src, trgt)
    
"""***************************************************"""

if __name__ == '__main__':
    sys_constants = cmn.sys_params()
    user_defs = cmn.local_utils.get_dict_from_json_file(sys_constants.user_file)
    #print user_defs
    
    flow_steps = cmn.local_utils.get_dict_from_json_file(sys_constants.phases_and_functions)
    #print flow_steps
    
    if 1==2:
        phase1_func(flow_steps, user_defs)
    
    
#    create_bokeh_page()
#    show(bkPage)
    exe = 'launch_server.bat'
    cmn.local_utils.os.system(exe)
    
    print "END of MAIN run"
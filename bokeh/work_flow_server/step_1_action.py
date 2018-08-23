"""
bokeh application to show and open section by working steps.

dated : 21/08/18
"""

print ("called script 1 from somewhere")

def script_main():
    import os
    print("action of script 1 "+str(os.path.abspath(os.path.curdir)))

if __name__=='__main__':
    script_main()
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:29:43 2019

@author: RAN
"""

"""**************************************************"""

from main_imports import *
"""**************************************************"""


def my_print(str, prefix=''):
    """ doc for a function
     print string surrounded by lines of '*'
    :param str:
    :param prefix:
    :return:
    """
    print("************")
    print(prefix, str)
    print("************")


def get_correct_doc(doc):
    # called from console, or
    # called from notebook
    if __name__.startswith('bk_script') \
       or str(doc).startswith('<function curdoc'):
        return doc()
    else:
        return doc

def doc_add_root(doc, obj, title=''):
    get_correct_doc(doc).add_root(obj)
    get_correct_doc(doc).title = title


def not_doc_add_root(doc, obj, title=''):
    if __debug__:
        print("doc : ", doc)
        print("doc : " + str(doc))
        print("name : ",__name__)
        print("obj : " + str(obj))
    
    # # called from console, or
    # # called from notebook
    # if __name__.startswith('bk_script') \
    #    or str(doc).startswith('<function curdoc'):
    #     doc().add_root(obj)
    #     doc().title = title
    # else:
    #     # if __name__=='__main__':   # and for jupyter notebook (name is  bokeh.docu..)
    #     doc.add_root(obj)
    #     doc.title = title

def output_bokeh_state_to_json(doc):
    import json
    if __name__.startswith('bk_script') \
       or str(doc).startswith('<function curdoc'):
        strJ = doc().to_json()
        with open('bokehConstructionState.json','w') as f:
            json.dump(strJ, f, indent=2)
    else:
        # if __name__=='__main__':   # and for jupyter notebook (name is  bokeh.docu..)
        # lst = doc.roots()
        print(doc.to_json())


"""
input is matplotlib figure
output is same figure with added axis-alike arrows
"""
def add_axis_to_fig(fig, xyPnts):
    fig.add_layout(Arrow(x_start=xyPnts[0], y_start=xyPnts[1], x_end=xyPnts[2], y_end=xyPnts[1], line_width=2))
    fig.add_layout(Arrow(x_start=xyPnts[0], y_start=xyPnts[1], x_end=xyPnts[2], y_end=xyPnts[3], line_color="green", line_width=2))
    fig.add_layout(Arrow(x_start=xyPnts[0], y_start=xyPnts[1], x_end=xyPnts[0], y_end=xyPnts[3], line_width=2))

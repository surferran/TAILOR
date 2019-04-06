# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:28:49 2019

@author: RAN
"""


from os.path import dirname, join

import pandas as pd

from bokeh.layouts import row, widgetbox, layout, column
from bokeh.models import ColumnDataSource, CustomJS, BoxSelectTool, CrosshairTool, Arrow # BoxEditTool,
from bokeh.models.widgets import Slider, Button, DataTable, TableColumn, \
                                    NumberFormatter, CheckboxGroup, RadioGroup, \
                                    Toggle, Panel, Tabs, CheckboxButtonGroup, TextInput, \
                                    HTMLTemplateFormatter, \
                                    MultiSelect # , RangeSlider, Paragraph
from bokeh.io import curdoc , push_notebook, show, output_notebook

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure
# from bokeh.plotting import ColumnDataSource as plt_ColumnDataSource

import sys

import os.path

util_rel_path = '../../AUI_gui'
util_path = join(dirname(__file__), util_rel_path)  # full abs path
sys.path.append(util_path)
import files_handler as fH

util_rel_path = '../../AUI_gui/data_handlers'
util_path = join(dirname(__file__), util_rel_path)  # full abs path
sys.path.append(util_path)
import AppGlobalData as appDB

# DATA_DIR = join(dirname(__file__), 'static/')
DATA_DIR = join(dirname(__file__), 'static')  # full abs path
rel_DATA_DIR = os.path.relpath(DATA_DIR)
# fileName_csv_source = join(rel_DATA_DIR, 'salary_data.csv')

from main_utils import *
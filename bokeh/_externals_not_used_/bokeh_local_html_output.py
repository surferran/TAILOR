from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
from bokeh.sampledata.iris import flowers

import pandas as pd

def plot_to_bokeh(data_frame, channels_names, desired_col_index=-1):
    '''
    :param data_frame:  pandas dataframe
    :channels_names: list of strings
    :param desired_col_index: -1 for all, i>0 for any other
    :return: non
    '''
    if desired_col_index>=0:
        header_str = data_frame._info_axis.values[desired_col_index]
        print header_str
        print channels_names[desired_col_index]
#        return 0
        col_data = data_frame._series[channels_names[desired_col_index]].values     # returns nd_array
        
        # data_frame[data_frame._info_axis.values[3]]
        print col_data
        ###################
        output_file("iris.html")

        # Create the figure object
        f = figure()

        # adding glyphs
        print len(col_data)
        print range(0,len(col_data))
        f.circle(range(0,len(col_data)), col_data)

        # Save and show the figure
        show(f)

        print f

        ###################
        return col_data


if __name__=='__main__':
    print ("in main")
    df = pd.DataFrame({"varName":[1,2,3,5,4,3,3,3,3,3,4,5,6,7,7,8,9]})    
    varNames = ["varName","stam"]    
    print df
    data = plot_to_bokeh(df, varNames, 0)
    print data

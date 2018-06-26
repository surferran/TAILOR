# handle pandas dataframe objects relevant actions

import pandas as pd

########################################
# class DFactions(pd.DataFrame):
# todo: how to add those function to built in dataframe object ?  generator ?
def get_head(pd, lines=-1):
    """
    get .head() of the DataFrame. 
    if 'lines' parameter is equel to -1 : use the deafult (usually 5),
    otherwise : use it. 
    return type : DataFrame
    """
    if lines == -1:
        return pd.head()
    else:
        return pd.head(lines)
    
def get_tail(pd, lines=-1):
    """
    get .tail() of the DataFrame. 
    if 'lines' parameter is equel to -1 : use the deafult (usually 5),
    otherwise : use it.    
    return type : DataFrame
    """
    if lines == -1:
        return pd.tail()
    else:
        return pd.tail(lines)
    
def get_only_head_and_tail(pd, lines=-1):
    """
    get .head() + .tail() of the DataFrame. 
    if 'lines' parameter is equel to -1 : use the deafult (usually 5),
    otherwise : use it.    
    return type : DataFrame
    """
    if lines == -1:
        return pd.head().append( pd.tail() )
    else:
        lines = int(lines/2)
        return pd.head(lines).append( pd.tail(lines) )
    
    pass
def get_columns_by_name(pd,req_col=None):
    """
    fetch data by label or array of labels.
    i.e : 
        print get_columns_by_name(testDF, 'a')
        print get_columns_by_name(testDF,[ 'a', 'c'])
    return type : Series or DataFrame 
    """
    return pd[req_col]
    
def get_rows_by_index(pd, req_row_start=None, req_row_end=None):
    """
    fetch values by index of line(s)
    usage example:
        print get_rows_by_index(testDF, 3)
        print get_rows_by_index(testDF, 3, 3)
        print get_rows_by_index(testDF, 3, 5)
        print get_rows_by_index(testDF, None, 5)
    return type : DataFrame 
    """
    return pd.loc[req_row_start:req_row_end]

def get_header(pd):
    """
    returns list of variables names
    return type: list(ndarray)
    """
    return list(pd.columns.values)

def print_DataFrame_info(pd):
    """
    prints basic information about the DataFrame.
    such as: range index, data columns, dtypes, 
             memory usage of the object.
    """
    return pd.info()

def get_DF_statistics(pd):
    """
    returns type of DataFrame
    """
    return testDF.describe()

def get_trimmed_DF(pd, rows, cols):
    """
    input:
        pd : the input dataframe
        rows : number of total rows to select
        cols : total Num Of Columns to select
    output:
        the trimmed DataFrame
    """
    cols = int(cols/2)
    numOfVars = len(list(pd))  # any more efficient method? 
    colRange  = range(0, cols) + range(numOfVars-cols, numOfVars)
    trimmedDF = get_only_head_and_tail(pd.iloc[:, colRange], rows)
    return trimmedDF
##################################################

if __name__=='__main__':

    print " script name : "+ __name__

    # small data
    introDict = {"index": [1,2,3,4],
                 "stamData": ["ran", "child", 0, 3]}
    testDF = pd.DataFrame(introDict)
    print introDict
    print testDF

    #bigger data
    testDF = pd.read_csv('df_data_example.csv')

#    print get_head(testDF)
    print get_head(testDF, 2)
#    print get_tail(testDF)
    print get_tail(testDF, 2)
    print get_only_head_and_tail(testDF, 2)
    
    print get_columns_by_name(testDF,[ 'a', 'c'])
    print get_rows_by_index(testDF, 3, 5)
    
    print get_header(testDF)
    
    print_DataFrame_info(testDF)
    
    tmp = get_DF_statistics(testDF)
    print tmp
    
#    testDF.plot()
    
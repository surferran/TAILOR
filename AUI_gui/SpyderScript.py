#cls 
#%clear
#%matplotlib wx

from AUI_GlobalImports import *

appDataObj  = appDB.myAppData()
appDataObj.initializeDataFields()
print appDataObj.lastPastedText

commonPath = u'C:/Users/Ran_the_User/Documents/GitHub\pyFiles\FILES\pyGUI/simOutputsData/'
#filePath = 'C:\Users\Ran_the_User\Documents\RAN\python\pandastable-master\pandastable\datasets/'
fileBaseNames = ['2018_2_5_3_28_47_quad_sim.csv'
                ,'2018_2_5_3_29_25_quad_sim.csv'
                ,'2018_2_5_3_30_33_quad_sim.csv'
                ,'2018_2_5_3_31_24_quad_sim.csv']
fileNames = map(lambda n : commonPath + n, fileBaseNames)
#fileName1 = commonPath + fileBaseNames[0]
#fileName2 = commonPath + fileBaseNames[1]
#fileName3 = commonPath + fileBaseNames[2]

fileDictionaries = map(lambda n : files_handler.get_file_details(n), fileNames)
#fileDict1 = files_handler.get_file_details(fileName1)
#fileDict2 = files_handler.get_file_details(fileName2)
#fileDict3 = files_handler.get_file_details(fileName3)
map(lambda n: files_handler.load_CSV_to_appData(n, appDataObj, headerVar = False), fileDictionaries);
#files_handler.load_CSV_to_appData(fileDict1, appDataObj, headerVar = False);
#files_handler.load_CSV_to_appData(fileDict2, appDataObj, headerVar = False);
#files_handler.load_CSV_to_appData(fileDict3, appDataObj, headerVar = False);
loadedFiles = appDataObj.mainDict
print loadedFiles
#########################################
for ndx, itm in enumerate(loadedFiles):
    print ndx
    print itm.Name
    
for ndx, itm in enumerate(loadedFiles):
    print ndx
    print itm.Name
    print itm.Type
    print itm.alias
    print itm.dataTimeStamp
    print itm.fileID
    print itm.Path
    print "*********"
#########################################

# get the DataFrames themselves :     
fileA = loadedFiles[0].loadedData
fileB = loadedFiles[3].loadedData

# specific selection, and show intro data
print fileA.info()
print fileB.info()

testDF = fileA - fileB

print testDF.describe()

print testDF.dtypes

a = testDF.head()
b = testDF.tail()
headWithTail = a.append(b)
print headWithTail
# print b.append(a)  #upside

# check specifics
#c= testDF.get_values()
#print c
headerLine = dfActions.get_header(testDF)  # get header. maybe find a better not questionable formula ??
print headerLine

##########################################
gui_plots.close_the_opened_plots()

t = dfActions.get_columns_by_name(testDF, 0) 
t = dfActions.get_columns_by_name(fileA, 0) 
y = dfActions.get_columns_by_name(testDF, 1) 
dispParams = {}
dispParams['title']    = 'Ran trial'
dispParams['lgndStr']  = ['y testDF']
dispParams['lineStyle'] = '-'
dispParams['lineColor'] = 'r'
dispParams['y-label']  = ' y var'
dispParams['x-label']  = 'time [sec]'
dispParams['alpha']    = 1
fig1 = gui_plots.plot_Var_Vs_Time(y , t, dispParams)

y = dfActions.get_columns_by_name(fileA, 1) 
dispParams['alpha']    = 0.6
dispParams['lgndStr']  = ['y fileA']
dispParams['lineStyle'] = '-.'
dispParams['lineColor'] = 'c'
fig2 = gui_plots.plot_Var_Vs_Time(y , t, dispParams,fig= fig1) # todo:

y = dfActions.get_columns_by_name(fileB, 1) 
dispParams['alpha'] = 0.3
dispParams['lgndStr'] = ['y fileB']
dispParams['lineStyle'] = 'dashed'
dispParams['lineColor'] = 'g'
fig3 = gui_plots.plot_Var_Vs_Time(y , t, dispParams, fig1) # todo:

gui_plots.show_the_constructed_plots()


# compare performance and details by : 
#  https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
a = dfActions.get_header(fileA)
b = dfActions.get_header(fileB)
set(a).intersection(b)
'''
# indexing and selections help :
#  https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
'''
fileA.head(4)
"""
example:
In [74]: range(0,3)
Out[74]: [0, 1, 2]
"""
#fileA.iloc[:,0] # 1st column
#fileA.iloc[:,0:3] # 1,2,3 columns
#numOfVars = len(list(fileA))  # any more efficient method?
#fileA.iloc[:,0:numOfVars:2] # every 2nd column. 0,2,4,6
#
#colRange = range(0,3) + range(numOfVars-3,numOfVars)
#trimmedDF = dfActions.get_only_head_and_tail(fileA.iloc[:,colRange], 10)

trimmedDF2 = dfActions.get_trimmed_DF(fileA, 15, 6)

# selection of rows, by general condition on a column value:
trimmedDF2.loc[trimmedDF2[1]>1]
trimmedDF2.loc[trimmedDF2[1]>1, 1]  # returned Series type
trimmedDF2.loc[trimmedDF2[1]>1, [1]]  # returned DataFrame type
trimmedDF2.loc[trimmedDF2[1]>1, [2,5]]  # with specific columns to return
trimmedDF2.loc[trimmedDF2[1]>1, 2:5]  # with specific columns to return


idxCnd = trimmedDF2[4].apply(lambda x: x>1) # returns bool list
# Select only the True values in 'idx' and only the 3 columns specified:
trimmedDF2.loc[idxCnd, :]

trimmedDF2[2].value_counts() # seperate values available in the data

trimmedDF2[2][trimmedDF2[1]<1] # more filtering syntax option

trimmedDF2[2].nunique()  # number of unique numbers

trimmedDF2.groupby([1]).groups.keys()
trimmedDF2.groupby([1]).first()
trimmedDF2.groupby([1])[2].sum()  # not sure what it gives..
trimmedDF2.groupby([1]).count()

############
#users.set_index('user_id', inplace=True)
#users.reset_index(inplace=True)
#pd.merge(left_frame, right_frame, on='key', how='inner') , left,right,outer
#pd.concat([left_frame, right_frame])
############
myEPS = 1E-7
boolEpsDF = (trimmedDF2> myEPS)
print boolEpsDF
EpsDFtrue = boolEpsDF.max() # True is higher then False 
EpsDFfalse = boolEpsDF.min() # False is lower then True

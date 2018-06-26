#cls 
#%clear
#%matplotlib wx

from AUI_GlobalImports import *

item_img = '../pyGUI/system_images/quad.jpg'

######################
"""
data section
"""

appDataObj  = appDB.myAppData()
appDataObj.initializeDataFields()
print appDataObj.lastPastedText

def printLoadedFilesInfo(loadedFiles):
    for ndx, itm in enumerate(loadedFiles):
        print ndx
        print itm.Name
        print itm.Type
        print itm.alias
        print itm.dataTimeStamp
        print itm.fileID
        print itm.Path
        print "*********"

def printExtraInfo(df):
    print df.info()
    print df.describe()
    print df.dtypes
    
######################################### load data files
commonPath = u'C:/Users/Ran_the_User/Documents/GitHub\pyFiles\FILES\pyGUI/simOutputsData/'

fileBaseNames = ['2018_2_5_3_28_47_quad_sim.csv'
                ,'2018_2_5_3_31_24_quad_sim.csv']
fileNames = map(lambda n : commonPath + n, fileBaseNames)
fileDictionaries = map(lambda n : files_handler.get_file_details(n), fileNames)
map(lambda n: files_handler.load_CSV_to_appData(n, appDataObj, headerVar = False), fileDictionaries);

loadedFiles = appDataObj.mainDict
printLoadedFilesInfo(loadedFiles)

#########################################
df = loadedFiles[0].loadedData
printExtraInfo(df)

headerLine = dfActions.get_header(df)  # get header. maybe find a better not questionable formula ??
print headerLine

##########################################
"""
plots setion
"""
gui_plots.close_the_opened_plots()

t = dfActions.get_columns_by_name(df, 0) 
y = dfActions.get_columns_by_name(df, 1) 
dispParams = {}
dispParams['title']    = 'Ran trial'
dispParams['lgndStr']  = ['y testDF']
dispParams['lineStyle'] = '-'
dispParams['lineColor'] = 'r'
dispParams['y-label']  = ' y var'
dispParams['x-label']  = 'time [sec]'
dispParams['alpha']    = 1
fig1 = gui_plots.plot_Var_Vs_Time(y , t, dispParams)

y = dfActions.get_columns_by_name(df, 2) 
dispParams['alpha']    = 0.6
dispParams['lgndStr']  = ['y fileA']
dispParams['lineStyle'] = '-.'
dispParams['lineColor'] = 'c'
fig2 = gui_plots.plot_Var_Vs_Time(y , t, dispParams,fig= fig1) # todo:

y = dfActions.get_columns_by_name(df, 3) 
dispParams['alpha'] = 0.3
dispParams['lgndStr'] = ['y fileB']
dispParams['lineStyle'] = 'dashed'
dispParams['lineColor'] = 'g'
fig3 = gui_plots.plot_Var_Vs_Time(y , t, dispParams, fig1) # todo:

gui_plots.show_the_constructed_plots()


####################################
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

img = scipy.misc.face()  
# img = scipy.misc.face()  # lena is not included in scipy 0.19.1
plt.figure(figsize=(12, 2))

for degree in range(5):
    plt.subplot(151+degree)
    rotated_img = ndimage.rotate(img, degree*60)
    plt.imshow(rotated_img, cmap=plt.cm.gray)
    plt.axis('off')

plt.show()

plt.imshow(cat[0])
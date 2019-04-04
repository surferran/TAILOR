# keep common data for the app
# verify : http://www.python-course.eu/python3_global_vs_local_variables.php

import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

########################################
class myAppData(dict):

    testField='a'
    lastFileID = -1

    class fileObjClass():
        Name = ''  # full file path and name
        Type = ''
        Path = ''
        alias = ''
        loadedData    = {}
        # fileID        = lastFileID       # unique integer id for the loaded data
        dataTimeStamp = -1  # time in seconds when the file or data was loaded and saved to fileObj memory

        def setFileID(self, fileID):
            self.fileID = fileID

    def __init__(self):
        pass

    def initializeDataFields(self):
        self.mainDict       = list()           # dict() ?
        self.lastPastedText = 'selfInitTest1'
        self.lastPastedUrl  = 'selfInitTest2'
        self.testField      = 'c'
        self.lastFileID     = -1
        if __debug__:
             print ("just initialized appDB (and hopefully cleared some memory")
            # print (self)

    def incFileID(self):
        self.lastFileID += 1
        return self.lastFileID

    def import_data_from_CSV(self,fileName):
        pass

    def addDataFromFile(self, fileObj):
        newFileID = self.incFileID()
        fileObj.setFileID(newFileID)
        self.mainDict.append(fileObj)


##################################################

if __name__=='__main__':
    appDict = myAppData()
    print (appDict.testField)
    appDict.initializeDataFields()
    print (appDict.testField)

    tmp1 = appDict.fileObjClass()
    tmp1.Name='rtrial.file'
    tmp1.alias='tryial'
    tmp1.loadedData=[]
    tmp1.Path='.'
    tmp1.Type='.py'

    tmp2 = appDict.fileObjClass()
    tmp2.Name = r'C:\Users\Ran_the_User\Documents\GitHub\pyFiles\FILES\myODE_case\quad_sim.csv'

    appDict.addDataFromFile(tmp1)
    appDict.addDataFromFile(tmp2)

    print ("appdict:")
    print (appDict)

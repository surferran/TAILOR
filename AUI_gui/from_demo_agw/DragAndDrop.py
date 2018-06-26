# intro to subject : https://wiki.wxpython.org/DragAndDrop
import  wx

import glob # similar or instead of 'os'  http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory
import os

import sys
sys.path.append('../')  # to find above packages
import files_handler

import ShapedWindows as ShpWin

if __name__=="__main__":
    print "activated by 1 , as : " + __name__
    sys.path.append('../specific_files/')  # to find above packages
    import interpShell
else:
    print "activated by 2 , as : " + __name__
    sys.path.append('../specific_files/')  # to find above packages
    sys.path.append('./specific_files/')  # to find above packages
    import interpShell

#----------------------------------------------------------------------
def magic_getDF(theCallerSelf):
    var1 = theCallerSelf._appDataHolder.mainDict
    var2 = theCallerSelf.text3
    print "got to magic function"
    return var1
#----------------------------------------------------------------------

class OtherDropTarget(wx.DropTarget):
    def __init__(self, window, log):
        wx.DropTarget.__init__(self)
        self.window = window
        self.log = log

        self.doComposite = wx.DataObjectComposite()  # the dataobject that gets filled with the appropriate data
        self.filedo = wx.FileDataObject()
        self.textdo = wx.TextDataObject()
        self.bmpdo  = wx.BitmapDataObject()
        self.urldo  = wx.URLDataObject(url="")
        self.doComposite.Add(self.filedo)
        self.doComposite.Add(self.textdo)
        self.doComposite.Add(self.bmpdo)
        # self.doComposite.Add(self.urldo)  # bad combination..
        self.SetDataObject(self.doComposite)

    def OnEnter(self, x, y, d):
        # self.log.WriteText\
        # print ("OnEnter: %d, %d, %d\n" % (x, y, d))
        return wx.DragCopy

    # def OnDragOver(self, x, y, d):
    #    self.log.WriteText("OnDragOver: %d, %d, %d\n" % (x, y, d))
    #    return wx.DragCopy

    def OnLeave(self):
        # self.log.WriteText("OnLeave\n")
        pass

    def OnDrop(self, x, y):
        # self.log.WriteText("OnDrop: %d %d\n" % (x, y))
        return True

    def OnData(self, x, y, result):
        """
        Handles drag/dropping files/text or a bitmap
        """
        # self.log.WriteText("OnData: %d, %d, %d\n" % (x, y, result)) #log from outside is MessaageBox like

        self.window.SetInsertionPointEnd()
        self.window.WriteText("\nOnData: %d, %d, %d\n" % (x, y, result))

        if self.GetData():
            # formatType, formatId = self.GetReceivedFormatAndId()
            formatType = self.GetReceivedFormatAndId()
            self.window.WriteText("formatType is : %s\n" % (formatType))
            # if formatId == 'text/x-moz-message':
            #     return self.OnThunderbirdDrop()
            if formatType in (wx.DF_TEXT, wx.DF_UNICODETEXT):   # type num: 13
                return self.OnTextDrop()
            elif formatType == wx.DF_FILENAME:  # type num: 15
                return self.OnFileDrop()
            elif formatType == wx.DF_BITMAP:
                return self.OnBMPDrop()
            else:
                return self.OnUrlDrop()

        return result  # you must return this


    def GetReceivedFormatAndId(self):
        format     = self.doComposite.GetReceivedFormat()
        formatType = format.GetType()
        # try:
        #     formatId = format.GetId()  # May throw exception on unknown formats
        # except:
        #     formatId = None
        # return formatType, formatId
        return formatType

    def OnThunderbirdDrop(self):
        # self.textCtrl.AppendText(self.thunderbirdDropData.GetData().decode('utf-16'))
        # self.textCtrl.AppendText('\n')
        return wx.DragCopy

    def OnUrlDrop(self):
        print "OnUrlDrop:"
        url = self.data.GetURL()
        self.window.AppendText(url + "\n")
        return wx.DragLink

    def OnTextDrop(self):
        print "OnTextDrop:"
        text = self.textdo.GetText()
        # self.textCtrl.AppendText(self.textDropData.GetText() + '\n')
        print text
        self.window.WriteText(text+'\n')
        #TODO : show popup menu to categorize the text and relate action to it.
         # either store data in lists, or links book-keeping, or issues to track (as part of my notes)
        #  zoomBar like circle action icons ?
        return wx.DragCopy

    def OnFileDrop(self):

        dragedFilesInfo = {}
        dragedFilesInfo['numOfFiles']           = 0
        dragedFilesInfo['files']                = []

        print "OnFileDrop:"

        filesNames = self.filedo.GetFilenames()
        dragedFilesInfo['numOfFiles']      = len(filesNames)

        if dragedFilesInfo['numOfFiles'] == 1:
            self.window.WriteText("1 file was dragged in\n")
        else:
            self.window.WriteText("%d files were dragged in\n" % len(filesNames))

        for ndx ,name in enumerate(filesNames):
            print name
            files_handler.file_action_by_type(name, self.window.Parent._appDataHolder) #new

            print self.window.Parent._appDataHolder.mainDict[0].loadedData
            # self.window.Parent._appDataHolder

            # self.log.WriteText("%s\n" % name)
            self.window.WriteText("%s\n" % name)

            pass

            print 'self.window.Parent.Parent.Parent.Parent.Label is : '
            print self.window.Parent.Parent.Parent.Parent.Label   #'inintial wxFrame'
            # print self.window.Parent.Parent.Parent # panel
            print self.window.Parent.Parent  # AUIFrame named 'frame'
            # print self.window.Parent  # FileDropPanel
            # print self.window # TextCtrl
            # print self  # OtherDropTarget
            # self.window.Parent.Parent._appDataRef is available

            pass

            full_path                       = os.path.dirname(name)
            fullFileName, file_extension    = os.path.splitext(name)
            allSimilarFiles                 = glob.glob(full_path + "/*" + file_extension)
            dragedFileIndexInList           = allSimilarFiles.index(name)   # same meaning as startViewIndex

            print fullFileName
            print full_path
            print file_extension
            print allSimilarFiles
            print dragedFileIndexInList

            dragedFilesInfo['files'].append({})
            dragedFilesInfo['files'][ndx]['fullName_withExt']   = name
            dragedFilesInfo['files'][ndx]['fullName_withNoExt'] = fullFileName
            dragedFilesInfo['files'][ndx]['fileExtension']      = file_extension
            dragedFilesInfo['files'][ndx]['fileFullPath']       = full_path
            dragedFilesInfo['files'][ndx]['fileIndexInList']    = dragedFileIndexInList
            dragedFilesInfo['files'][ndx]['allSimilarPathFiles']= allSimilarFiles

        return wx.DragCopy

    def OnBMPFDrop(self):
        print "OnBMPDrop:"
        bmp = self.bmpdo.GetBitmap()
        return wx.DragCopy

#----------------------------------------------------------------------

class FileDropPanel(wx.Panel):
    def __init__(self, parent, log, appData):       # extended header
        wx.Panel.__init__(self, parent, -1)
        self._appDataHolder = appData

        #self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        ''''''  #ran section addition
        # sizer.Add(
        #     wx.StaticText(self, -1, " \nother Drag&Drop here:"),
        #     0, wx.EXPAND|wx.ALL, 2
        #     )

        ### add interpreter with exampled data
        class Strct():
            a = 'a'
            b = {}
        strct = Strct()
        strct.b = {'a': 1, 'b': 12}
        passedLocals = {"__name__": "__RanConsole__", \
                        "__doc__": "None docs will be populated by ran", \
                        "varA": strct}
        I = interpShell.II(passedLocals)


        # self.text3 = interpShell.PySTC(
        self.text3 =        wx.TextCtrl(
                                        self, -1,       #"",
                                        style = wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL)
        self.text3.SetBackgroundColour('light gray')
        # sys.stdout = self.text3
        # sys.stderr = self.text3
        # todo : add apropriate handler for paste action . self.text3.Bind(wx.EVT_TEXT_PASTE, self.onPaste)
        self.text3.Bind(wx.EVT_CHAR, self.onCharPressed)
        # self.text3.SetInter(I)

        dt = OtherDropTarget(self.text3, log)
        self.text3.SetDropTarget(dt)

        sizer.Add(self.text3, 2, wx.EXPAND)
        ''''''
        self.SetAutoLayout(True)
        self.SetSizer(sizer)

    # def WriteText(self, text):
    #     self.text.WriteText(text)
    #
    # def SetInsertionPointEnd(self):
    #     self.text.SetInsertionPointEnd()

    def onCharPressed(self, evt):
        # ref : https://www.blog.pythonlibrary.org/2009/08/29/wxpython-catching-key-and-char-events/
        # https: // wxpython.org / Phoenix / docs / html / wx.TextCtrl.html
        ''' search mainly for pressed Ctrl-E '''
        keyFeatures={}
        keyFeatures['keyCode']     = evt.GetKeyCode()
        keyFeatures['controlDown'] = evt.CmdDown()
        keyFeatures['altDown']     = evt.AltDown()
        keyFeatures['shiftDown']   = evt.ShiftDown()

        # self.text3.GetScrollPos(wx.VERTICAL)  i.e 12 till back above to first line of text field
        # self.text3.GetLastPosition() end of field lenght
        selectionRange = self.text3.GetSelection() # type of tuple, len of 2. from start or end pos to pos where key was pressed
        selectedString = self.text3.GetStringSelection()
        textFiled = self.text3.GetValue()  # returns the whole text field string
        if 1==2:
            print self.text3.GetInsertionPoint()
            print self.text3.GetNumberOfLines()
            print self.text3.GetPosition()
            print selectionRange
            print selectedString
            print textFiled
        # insertionpoint
        # linelenght
        # linetext
        # getsele
            print keyFeatures

        # if keyFeatures['controlDown']==False \
        #     and keyFeatures['shiftDown'] == False \
        #     and keyFeatures['altDown'] == False \
        #     and keyFeatures['keyCode']!=5:
        #     # self.text3.WriteText("%s" % chr(keyFeatures['keyCode']))
        #     evt.Skip()
        # else:
        if keyFeatures['keyCode']==1 \
            and keyFeatures['controlDown'] == True \
            and keyFeatures['shiftDown'] == False \
            and keyFeatures['altDown'] == False:
            ''' Ctrl-A '''
            self.text3.SetSelection(-1, -1)  # it doesn't work otherwise for some reason
        elif keyFeatures['keyCode']==5 \
            and keyFeatures['controlDown'] == True \
            and keyFeatures['shiftDown'] == False \
            and keyFeatures['altDown'] == False:
            ''' all relates to ^-E '''
            # todo get selecetion data if any , or current line if presed Enter
            # evaluate contant as eval
            print ("needs selected text evaluation")
            #todo goto end of selection location
            self.text3.WriteText(chr(10)+"selection evaluation output is : " + chr(10))
            self.text3.WriteText("evalution.. %s" % chr(10))
        elif (keyFeatures['keyCode'] == 10 or keyFeatures['keyCode'] == 13) \
            and keyFeatures['controlDown'] == True \
            and keyFeatures['shiftDown'] == False \
            and keyFeatures['altDown'] == False:
            # todo get selecetion data if any , or current line if pressed Enter
            # evaluate contant as eval
            # print ("needs current line evaluation")
            #todo goto end of line
            ##self.text3.WriteText(chr(10) + "line evalution output is : " + chr(10))
            # https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python
            if selectedString!='':
                cmdToEvaluate = selectedString
            else:
                cmdToEvaluate = textFiled
            try:
                # recursion : self.text3.Value
                self.text3.WriteText( str(eval(cmdToEvaluate)) )
                self.text3.WriteText('\nused successfuly eval() function ')   # todo: update the status bar instead. and for about 3 sec. and change status to ready
                                                                                # status_bar_callback(0, "used successfuly eval() function")
            except:
                ##self.text3.WriteText(chr(10) + "exception in evaluation of : " + textFiled + chr(10))
                try:
                    exec (cmdToEvaluate)
                    self.text3.WriteText('\nused successfuly exec() function ' )
                except:
                    self.text3.WriteText(chr(10) + "exception in eval() and in exec() of : " + cmdToEvaluate + chr(10))
        else:
            # pass event to act regularly
            evt.Skip()


    def onPaste(self, evt):
        success = False
        do = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(do)
            wx.TheClipboard.Close()

        if success:
            pastedStr = do.GetText()
            # self.text3.SetValue(do.GetText())
            self.text3.SetInsertionPointEnd()
            self.text3.WriteText("\nPaste string : \n%s\n" % pastedStr)

            ## ran
            self.openImageShortcutsPanel(pastedStr)
            ## ran

        else:
            wx.MessageBox(
                "There is no data in the clipboard in the required format",
                "Error"
                )

        # evt.Skip()  # propagate to regular behaviour of the Paste action

    def openImageShortcutsPanel(self, inputString=""):

        pnl = wx.Panel(self)

        iconNames           = ["help", "smfuel", "checked"]  # todo - get from os list or user json file
        functionsToLaunch   = [ShpWin.addUrlToLinksList, None, None, None]
                    # add list of number of required parameters for each function. should pass as ~*args
        avgLoc              = (1200, 600)
        deltaLoc            = [(50, 00), (00, 50), (0, -50), (-50, 00)]
        winLocations        = [(x + avgLoc[0], y + avgLoc[1]) for (x, y) in deltaLoc]

        for icon, func, loc in zip(iconNames, functionsToLaunch, winLocations):
            # todo: get current path and add known relative
            iName = "./from_demo_agw/bitmaps/" + icon + ".ico"
            win = ShpWin.ShapedWindowByImage(pnl, imageFileName=iName, launchFunction=func, initialLocation=loc)
            win.Show(True)
    #------------------ ------------------ ------------------ ---------
    ''' local magic function. for connecting the consule to the outside world '''
    def getDFlist(self):
        print "got to inner magic func"    
#----------------------------------------------------------------------
#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        wx.Panel.__init__(self, parent, -1)

        self.SetAutoLayout(True)
        outsideSizer = wx.BoxSizer(wx.VERTICAL)

        # msg = "Clipboard / Drag-And-Drop"
        # text = wx.StaticText(self, -1, "", style=wx.ALIGN_CENTRE)
        # text.SetFont(wx.Font(24, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        # text.SetLabel(msg)
        #
        # w,h = text.GetTextExtent(msg)
        # text.SetSize(wx.Size(w,h+1))
        # text.SetForegroundColour(wx.BLUE)
        # outsideSizer.Add(text, 0, wx.EXPAND|wx.ALL, 5)
        # outsideSizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND)

        inSizer = wx.BoxSizer(wx.HORIZONTAL)
        # inSizer.Add(ClipTextPanel(self, log), 1, wx.EXPAND)
        inSizer.Add(FileDropPanel(self, log,-1), 1, wx.EXPAND)

        outsideSizer.Add(inSizer, 1, wx.EXPAND)
        self.SetSizer(outsideSizer)


#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

#----------------------------------------------------------------------

overview = """\ 
"""

if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])


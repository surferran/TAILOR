#show tif files
# possible refs:
# https://blog.philippklaus.de/2011/08/handle-16bit-tiff-images-in-python
# https://matplotlib.org/users/image_tutorial.html

import wx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_wxagg import \
        FigureCanvasWxAgg as FigCanvas, \
        NavigationToolbar2WxAgg as NavigationToolbar
import sys
sys.path.append('../from_demo_agw')
sys.path.append('../')

import glob
import os

# import DragAndDrop as DD
# import AUI_MAIN as AMain

class ShowTifInPath(wx.Panel):

    def __init__(self,parent):

        wx.Panel.__init__(self, parent)

        self.fig = plt.figure()
        self.canvas = FigCanvas(self, -1, self.fig)

        self.lastFileName = ''
        self.filesPath = ''

        self.bindKeyShortcuts()

        self.createMenuAndToolbar()

    def bindKeyShortcuts(self):

        self.canvas.Bind(wx.EVT_KEY_DOWN    , self.OnDwnKeyPress)
        self.canvas.Bind(wx.EVT_KEY_UP      , self.OnUpKeyPress)
        self.canvas.Bind(wx.EVT_ENTER_WINDOW, self.ChangeCursor)

        # Create an accelerator table
        myKeyId_1 = wx.NewId()
        myKeyId_2 = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onCtrlShiftF1, id=myKeyId_1)
        self.Bind(wx.EVT_MENU, self.onShiftAltY  , id=myKeyId_2)

        accel_tbl = wx.AcceleratorTable([
                                          (wx.ACCEL_SHIFT | wx.ACCEL_CTRL, wx.WXK_F1, myKeyId_1),
                                          (wx.ACCEL_SHIFT | wx.ACCEL_ALT , ord('Y') , myKeyId_2)
                                          ])

        self.SetAcceleratorTable(accel_tbl)

    def onCtrlShiftF1(self, event):
        """ https://www.blog.pythonlibrary.org/2010/12/02/wxpython-keyboard-shortcuts-accelerators/ """
        print "You pressed CTRL+SHIFT+F1"
    def onShiftAltY(self, event):
        """ https://www.blog.pythonlibrary.org/2010/12/02/wxpython-keyboard-shortcuts-accelerators/ """
        print "You pressed ALT+SHIFT+Y"

    def createMenuAndToolbar(self):
        '''
        ref: https://www.blog.pythonlibrary.org/2008/07/02/wxpython-working-with-menus-toolbars-and-accelerators/
        '''
        """ Create the menu bar. """
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenu.AppendSeparator()
        exitMenuItem = fileMenu.Append(wx.NewId(), "&Exit\tAlt+F4",  "Exit the application")
        self.Bind(wx.EVT_MENU,  self.OnExit, exitMenuItem)
        menuBar.Append(fileMenu, "&File")
        # exitMenuItem.Enable(False)
        # menuBar.EnableTop(0, False)
        self.GetParent().SetMenuBar(menuBar)    # add it to Frame object


        """        Create a toolbar.        """
        self.toolbar = self.GetParent().CreateToolBar()
        self.toolbar.SetToolBitmapSize((16, 16))  # sets icon size

        # Use wx.ArtProvider for default icons
        open_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16, 16))
        if 'phoenix' in wx.PlatformInfo:
            openTool = self.toolbar.AddTool(wx.ID_ANY, "Open", open_ico, "Select file to load")
        else:
            openTool = self.toolbar.AddSimpleTool(wx.ID_ANY, open_ico, "Open", "Select file to load")
        # self.Bind(wx.EVT_MENU, self.onSave, saveTool)


        # Use wx.ArtProvider for default icons
        save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16, 16))
        saveTool = self.toolbar.AddTool(wx.ID_ANY, "Save", save_ico, "Saves the Current Worksheet")
        # self.Bind(wx.EVT_MENU, self.onSave, saveTool)

        self.toolbar.AddSeparator()

        print_ico = wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_TOOLBAR, (16, 16))
        printTool = self.toolbar.AddTool(wx.ID_ANY, "Print", print_ico, "Sends Timesheet to Default Printer")
        # self.Bind(wx.EVT_MENU, self.onPrint, printTool)

        # delete_ico = wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_TOOLBAR, (16, 16))
        # deleteTool = self.toolbar.AddSimpleTool(wx.ID_ANY, delete_ico, "Delete", "Delete contents of cell")
        # # self.Bind(wx.EVT_MENU, self.onDelete, deleteTool)
        #
        # undo_ico = wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_TOOLBAR, (16, 16))
        # self.undoTool = self.toolbar.AddSimpleTool(wx.ID_UNDO, undo_ico, "Undo", "")
        # self.toolbar.EnableTool(wx.ID_UNDO, False)
        # # self.Bind(wx.EVT_TOOL, self.onUndo, self.undoTool)
        #
        # redo_ico = wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_TOOLBAR, (16, 16))
        # self.redoTool = self.toolbar.AddSimpleTool(wx.ID_REDO, redo_ico, "Redo", "")
        # self.toolbar.EnableTool(wx.ID_REDO, False)
        # # self.Bind(wx.EVT_TOOL, self.onRedo, self.redoTool)

        # This basically shows the toolbar
        self.toolbar.Realize()

    def OnExit(self):
        # SystemExit()
        self.Close()

    def ChangeCursor(self, event):
        self.canvas.SetCursor(wx.Cursor(wx.CURSOR_BULLSEYE))

    def updateTif(self,tifFullName):
        img = mpimg.imread(tifFullName)
        self.imgplot.set_data(img)
        self.canvas.draw()
        # self.vbox.Fit(self)  #bad for getting correct resize
        self.canvas.Refresh()

        return self.imgplot

    def showTif(self,tifFullName):
        img = mpimg.imread(tifFullName)
        self.imgplot = plt.imshow(img)

        self.cBar = plt.colorbar()
        self.toolbar = NavigationToolbar(self.canvas)
        # plt.axis('off')

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.vbox.Add(self.toolbar, 0, wx.EXPAND)

        self.SetSizer(self.vbox)

        self.vbox.Fit(self)

        return self.imgplot, self.cBar

    def OnDwnKeyPress(self, event):
        pass
        # print "dwnKey"

    def OnUpKeyPress(self, event):
        print "onUpKey"
        pressedKey = event.GetKeyCode()
        if (pressedKey==wx.WXK_LEFT) | (pressedKey==wx.WXK_DOWN):
            print"left / down key"
            #currentIndex % len(relevant items)
            filesList = list(panel.filesInfo)
            if (filesList[3] > 0):
                filesList[3] = (filesList[3]) - 1
            else:
                filesList[3] = len(filesList[2])-1;
            panel.filesInfo = tuple(filesList)
            newFileName = panel.filesInfo[2][filesList[3]]
            panel.updateTif(newFileName)

        elif (pressedKey==wx.WXK_RIGHT) | (pressedKey==wx.WXK_UP):
            print "right / up key"
            #currentIndex % len(relevant items)
            filesList = list(panel.filesInfo)
            if (filesList[3] < (len(filesList[2])-1)):
                filesList[3]= (filesList[3]) + 1
            else:
                filesList[3] = 0;
            panel.filesInfo = tuple(filesList)
            newFileName = panel.filesInfo[2][filesList[3]]
            panel.updateTif(newFileName)

        elif (pressedKey == wx.WXK_NUMPAD_ADD) :
            print "+ key"
        elif (pressedKey == wx.WXK_NUMPAD_SUBTRACT):
            print "- key"
        else :
            print pressedKey

        return pressedKey


class MinimumDropTarget(wx.DropTarget):
    ''' handles ony file types '''
    def __init__(self):
        wx.DropTarget.__init__(self)

        self.doComposite = wx.DataObjectComposite()
        self.filedo = wx.FileDataObject()

        self.doComposite.Add(self.filedo)
        self.SetDataObject(self.doComposite)

    def OnData(self, x, y, result):
        """
        Handles drag/dropping files/text or a bitmap
        """

        if self.GetData():
            # formatType, formatId = self.GetReceivedFormatAndId()
            formatType = self.GetReceivedFormatAndId()
            if formatType == wx.DF_FILENAME:
                return self.OnFileDrop()

        return result  # you must return this


    def GetReceivedFormatAndId(self):
        format     = self.doComposite.GetReceivedFormat()
        formatType = format.GetType()
        return formatType

    def OnFileDrop(self):
        print "OnFileDrop:"
        filesNames = self.filedo.GetFilenames()
        # for name in filesNames:
        #     print name

        firstDropedFileFullName         = filesNames[0]

        panel.updateTif(firstDropedFileFullName)

        # panel.filesInfo = panel.getSimilarFilesInfo(firstDropedFileFullName)
        panel.filesInfo = self.getSimilarFilesInfo(firstDropedFileFullName)

        return wx.DragCopy

    def getSimilarFilesInfo(self,firstDropedFileFullName):
        full_path = os.path.dirname(firstDropedFileFullName)
        fullFileName, file_extension = os.path.splitext(firstDropedFileFullName)
        allSimilarFiles = glob.glob(full_path + "\\*" + file_extension)
        fileIndexInList = allSimilarFiles.index(firstDropedFileFullName)
        print firstDropedFileFullName
        # print fullFileName
        # print full_path
        print file_extension
        print allSimilarFiles
        print fileIndexInList

        return (full_path, file_extension, allSimilarFiles, fileIndexInList)


if __name__=='__main__':
    tiff_file = '.\\tif\\CCITT_2.TIF'

    app     = wx.App()#PySimpleApp()
    fr      = wx.Frame(None, title='main test')
    panel   = ShowTifInPath(fr)

    # log = AMain.Log()
    # obj =  DD.OtherDropTarget(panel, log)
    # obj =  DD.FileDropPanel(panel, log)
    obj=MinimumDropTarget()
    fr.SetDropTarget(obj)

    # panel.draw()
    panel.showTif(tiff_file)
    # panel.filesInfo = panel.getSimilarFilesInfo(tiff_file)
    panel.filesInfo = obj.getSimilarFilesInfo(tiff_file)

    app.SetTopWindow(fr)
    fr.Show()
    app.MainLoop()

    #from PIL import Image
    #im = Image.open(tiff_file)
    ##im.show()
    #
    #import matplotlib.pyplot as plt
    #I = plt.imread(tiff_file)   #ndarray type
    #plt.show()


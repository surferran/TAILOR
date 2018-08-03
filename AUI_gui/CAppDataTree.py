# ---------------------------------------------------------------------------- #
# Class UserPanels
# ---------------------------------------------------------------------------- #
import wx
import time

import specific_files.dfgui


import data_handlers.DataFrames_actions    	as dfActions

class AppData_TreeCtrl(wx.TreeCtrl):
    def __init__(self, parent):#, appData):
#        wx.TreeCtrl.__init__(self, parent, -1, 
#                             wx.Point(0, 0), wx.Size(160, 250),
#                             wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        
        wx.TreeCtrl.__init__(self, parent, -1
                             , wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                               | wx.TR_EDIT_LABELS
                               | wx.TR_MULTIPLE
                               | wx.TR_DEFAULT_STYLE 
                               | wx.NO_BORDER
                               #| wx.TR_HIDE_ROOT
                               #, self.log
                             )

        # def Create_AppData_TreeCtrl(parent, appData):
        """
        todo:
         1. verify if already opened window like this - and update content. (will be in parenting caller).
            other option - pressing 'show app data' will toggle window off ?
         2. capture double click on dataType, and accordingly open window of table or list of vars or some graph or text editor or run excecutable
         3. verify if data is copied or referenced..
    
         4. when loaded file - add time tag for file reading time (will be in OnDrag..)
    
         chcek http://www.java2s.com/Tutorial/Python/0380__wxPython/Treenodebegineditevent.htm
    
        """

        frame_title = "Loaded data files"

        # tree = wx.TreeCtrl(parent, -1, wx.Point(0, 0), wx.Size(160, 250),
        #                    wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
        #
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        self.AssignImageList(imglist)

        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.treeItemActivated) # will catch mouse double click only if the above is not binded
#        self.Bind(wx.EVT_RIGHT_DOWN         , self.onRightClick)  # catch mouse right click
        
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp)
        
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT,   self.OnEndEdit)

        self.root = self.AddRoot(frame_title, 0)  #todo: init with None and replace if appData not empty
        self.items = []
###################################################

    def OnBeginEdit(self, event):
        print("OnEdit Begin\n")
        item = event.GetItem()
        if item and self.GetItemText(item) == "The Root Item":
            wx.Bell() 
            print ("You can't edit this one...\n")
            event.Veto()
            
    def OnEndEdit(self, event):
#        self.log.WriteText
        print("OnEdit end: %s %s\n" %
                           (event.IsEditCancelled(), event.GetLabel()) )
        # todo : allow label edit only for main label
        item = event.GetItem()
        label = event.GetLabel()
        if item and ("(#" in label):
#        if label == '':
            print("You can't change this property...\n")
            event.Veto()
###################################################


    def populateTree(self, appData):
        for ndx, item in enumerate(appData.mainDict):
            prefix = "(#" + str(ndx) + ") "
            self.items.append(self.AppendItem(self.root, prefix + item.alias, 0))
            sub_item = self.items[-1]
            self.AppendItem(sub_item, item.Name, 1)
            self.AppendItem(sub_item, item.Path, 1)
            self.AppendItem(sub_item, item.Type, 1)
            self.AppendItem(sub_item, str(item.fileID), 1)
            self.AppendItem(sub_item, item.dataTimeStamp, 1)
            ''''''
            self.AppendItem(sub_item, str(item.loadedData.shape), 1)
            ''''''
            # tree.SetItemData(sub_item, item)  # will create copy also of the data
            self.SetItemData(sub_item, item.fileID)

        self.Expand(self.root)
    
    def deleteItemFromTree(self, itemID = None):
#        self.items
        if (itemID):
            print (self.items[itemID])
            del self.items[itemID]
        pass

    def treeItemActivated(self, event=None):
        """
        activated when user presses double click on the item
        """
        if __debug__:
            print ("tree dbl clk")

        # print (time.time())
        # print (time.ctime())
        treeItem            = event.EventObject
        selectedItem        = event.EventObject.Selections[0]
        selectedItemLabel   = treeItem.GetItemText(selectedItem)
        selectedItemParent  = treeItem.GetItemParent(selectedItem)

        appDataRelevantFileID = treeItem.GetItemData(selectedItem)
        if appDataRelevantFileID == None:
            print ("appDataRelevantFileID == None")
            print ("treeItem")
            print (treeItem)
            print ("selectedItem")
            print (selectedItem)
            print ("selectedItemLabel")
            print (selectedItemLabel)
            print ("selectedItemParent:")
            print (selectedItemParent)
            if selectedItemLabel!="Loaded data files":
                appDataRelevantFileID = treeItem.GetItemData(selectedItemParent)
                selectedItemLabel   = treeItem.GetItemText(selectedItemParent)

        # treeItem.SelectItem(selectedItem)

        print ("valid tree id? : " + str(event.EventObject.Selections[0].IsOk()))
        print ("number of items in whole tree: " + str(treeItem.GetCount()))

        # if (treeItem.Children):
        #     treeItem.SelectChildren()

        # treeItem.CollapseAll()
        # treeItem.ExpandAll()

        # treeRoot = treeItem.GetRootItem()
        # treeItem.SelectItem(treeRoot)

        if appDataRelevantFileID > -1:  #todo: change -1 to some app constant
            print ('appDataRelFileID gt -1')
            #todo  if self.Parent.Parent. is valid only when tree is not docked.
            # otherwise relate to other parent
            if self.Parent.Parent._appDataRef.mainDict[appDataRelevantFileID].Type == 'DataFrame':
                parentWindowCtrl = self.Parent.Parent
                DFdata = parentWindowCtrl._appDataRef.mainDict[appDataRelevantFileID].loadedData

                # show data in wx table under parent, with stored identification related to main appData
                ##                 specific_files.dfgui.show(DFdata)
                trimmedDF = DFdata
                ###
                trimmedDFrows = min(15, len(DFdata)) # todo: put as constants from INI
                trimmedDFcols = min(6, len(list(DFdata))) # todo: put as constants from INI
                trimmedDF = dfActions.get_trimmed_DF(DFdata, trimmedDFrows, trimmedDFcols)
                wxPnl = specific_files.dfgui.show_tabel_panel(trimmedDF, parentWindowCtrl)
                panelTitle = selectedItemLabel + " data table"
                parentWindowCtrl.Create_DFtable(wxPnl, panelTitle)

                headersList = list(DFdata.columns.values) # or list(DFdata)  # can tty also sorted(DFdata)
                print (headersList)
        ##
        pieces = []
        # todo: condition with .not. multi selection tree
        # item = treeItem.GetSelection()
        items = treeItem.GetSelections()
        for item in items:
            while item:
                piece = treeItem.GetItemText(item)
                pieces.insert(0, piece)
                item = treeItem.GetItemParent(item)
        print ("item path tree : ")
        print (pieces)
        ##
        # wx.MessageBox("msg box")
###################################################


    def OnRightDown(self, event):
        
        pt = event.GetPosition()
        item, flags = self.HitTest(pt)

        if item:
            self.item = item
#            self.log.write
            print("OnRightDown: %s, %s, %s" % (self.GetItemText(item), type(item), item.__class__) + "\n")
            self.SelectItem(item)
            ########
            self.OnRightUp(event)
            ########

    def OnRightUp(self, event):
        """
        create the pop up menu for the application db items tree.
        """

        # item is dependend on creation in 'OnRightDown()'
        if not self.item:
            print ("item is nan.. (in OnRightUp)")
            event.Skip()
            return

        item = self.item

        # Item Text Appearance
        back   = self.GetItemBackgroundColour(item)
        fore   = self.GetItemTextColour(item)
        isbold = self.IsBold(item)
        font   = self.GetItemFont(item)

        # Generic Item's Info
        children  = self.GetChildrenCount(item)
        text      = self.GetItemText(item)
        itemdata    = self.GetItemData(item)
        
        self.current = item
        # todo: read from json i.e 'appDBtreePopUpItems.json'
        self.itemdict = {"back": back, "fore": fore, "isbold": isbold, "font": font,
                         "children": children, "text": text, "itemdata": itemdata}
        
        ''''''
        menu = wx.Menu()

        # item1 = menu.Append(wx.ID_ANY, "Change item background colour")
        # item2 = menu.Append(wx.ID_ANY, "Modify item text colour")
        # menu.AppendSeparator()

        if isbold:
            boldStr = "Make item text not bold"
        else:
            boldStr = "Make item text bold"
        item3 = menu.Append(wx.ID_ANY, boldStr)
        # item4 = menu.Append(wx.ID_ANY, "Change item font")
        menu.AppendSeparator()

        item10 = menu.Append(wx.ID_ANY, "show list of variables")
        item11 = menu.Append(wx.ID_ANY, "show trimmed table")
        item12 = menu.Append(wx.ID_ANY, "print full table to console")
        item13 = menu.Append(wx.ID_ANY, "show table summary (.info and .describe)")
        menu.AppendSeparator()

        # if len(item)>1:
        #     item14 = menu.Append(wx.ID_ANY, "compare tables list of variables")
        #     item15 = menu.Append(wx.ID_ANY, "compare tables")
        #     menu.AppendSeparator()

        item5 = menu.Append(wx.ID_ANY, "Delete item")
        if item == self.GetRootItem():
            item5.Enable(False)

#        self.Bind(wx.EVT_MENU, self.OnItemBackground, item1)
#        self.Bind(wx.EVT_MENU, self.OnItemForeground, item2)
        self.Bind(wx.EVT_MENU, self.OnItemBold, item3)
#        self.Bind(wx.EVT_MENU, self.OnItemFont, item4)

        self.Bind(wx.EVT_MENU, self.OnObjVarList, item10)
        self.Bind(wx.EVT_MENU, self.OnObjShowTrimmed, item11)
        self.Bind(wx.EVT_MENU, self.OnObjPrintTable, item12)
        self.Bind(wx.EVT_MENU, self.OnObjShowSummary, item13)
        # self.Bind(wx.EVT_MENU, self.OnObjsCompareVars, item14)
        # self.Bind(wx.EVT_MENU, self.OnObjsCompare, item15)
        
        self.Bind(wx.EVT_MENU, self.OnItemDelete, item5)

        self.PopupMenu(menu)
        menu.Destroy()

    def OnObjVarList(self, event):
        """ 
        show list of variables of selected DataFrame item

        event here is CommandEvent
        """

        if __debug__:
            print ("show item var list")

        treeItem            = event.EventObject.Window # type of Menu->Tree
        selectedItem        = event.EventObject.Window.Selections[0]
        selectedItemParent  = treeItem.GetItemParent(selectedItem)
        selectedItemLabel   = treeItem.GetItemText(selectedItem)

        appDataRelevantFileID = treeItem.GetItemData(selectedItem)
        if appDataRelevantFileID == None and selectedItemLabel!="Loaded data files":
                appDataRelevantFileID = treeItem.GetItemData(selectedItemParent)
                selectedItemLabel     = treeItem.GetItemText(selectedItemParent)

        print ("valid tree id? : " + str(selectedItem.IsOk()))
        print ("number of items in whole tree: " + str(treeItem.GetCount()))

        if appDataRelevantFileID > -1:  #todo: change -1 to some app constant
            print ('appDataRelFileID gt -1')
            if self.Parent.Parent._appDataRef.mainDict[appDataRelevantFileID].Type == 'DataFrame':
                parentWindowCtrl = self.Parent.Parent
                DFdata = parentWindowCtrl._appDataRef.mainDict[appDataRelevantFileID].loadedData

                # show data in wx table under parent, with stored identification related to main appData
                ##                 specific_files.dfgui.show(DFdata)
#                trimmedDF = DFdata.keys()
                trimmedDF = specific_files.dfgui.pd.DataFrame( {"keys":list(DFdata.columns.values)} ) # .transpose()
                print (trimmedDF)
                wxPnl = specific_files.dfgui.show_tabel_panel(trimmedDF, parentWindowCtrl)
                panelTitle = selectedItemLabel + " variables"
                parentWindowCtrl.Create_DFtable(wxPnl, panelTitle)

#        pieces = []
#        # todo: condition with .not. multi selection tree
#        # item = treeItem.GetSelection()
#        items = treeItem.GetSelections()
#        for item in items:
#            while item:
#                piece = treeItem.GetItemText(item)
#                pieces.insert(0, piece)
#                item = treeItem.GetItemParent(item)
#        print "item path tree : "
#        print pieces
        ##
        # wx.MessageBox("msg box")
###################################################

        pass
    def OnObjShowTrimmed(self, event):
        pass
    def OnObjPrintTable(self, event):
        pass
    def OnObjShowSummary(self, event):
        pass
    def OnObjsCompareVars(self, event):
        pass
    def OnObjsCompare(self, event):
        pass

    def OnItemBold(self, event):

        self.SetItemBold(self.current, not self.itemdict["isbold"])


    def OnItemDelete(self, event):

        print ("item selected is : " )
        print (self.current)
        selectedIndex = self.current  # type of TreeItemId
        # todo: itemDBid = get field of item ID in appData object
        
        strs = "Are You Sure You Want To Delete Item " + self.GetItemText(self.current) + "?"
        dlg = wx.MessageDialog(None, strs, 'Deleting Item', wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_QUESTION)

        if dlg.ShowModal() in [wx.ID_NO, wx.ID_CANCEL]:
            dlg.Destroy()
            return

        dlg.Destroy()

        self.DeleteChildren(self.current)
        self.Delete(self.current)
        self.current = None
        
        # delete item for appObj
#        self.deleteItemFromTree(itemDBid)
        
        # refresh all other app_db_tree windows if any
                

    def onRightClick(self, event):
        if __debug__:
            print("right clicked ")

        print (time.ctime())
        treeItem        = event.EventObject
        selectedItem    = event.EventObject.Selections[0]
        selectedItemLabel   = treeItem.GetItemText(selectedItem)
        selectedItemParent  = treeItem.GetItemParent(selectedItem)

        appDataRelevantFileID = treeItem.GetItemData(selectedItem)
        if appDataRelevantFileID == None:
            appDataRelevantFileID = treeItem.GetItemData(selectedItemParent)

        if appDataRelevantFileID > -1:  # todo: change -1 to some app constant
            parentWindowCtrl = self.Parent.Parent
            DFdata = parentWindowCtrl._appDataRef.mainDict[appDataRelevantFileID].loadedData
            headersList = list(DFdata.columns.values)  # or list(DFdata)  # can tty also sorted(DFdata)

        pieces = []
        # item = treeItem.GetSelection()
        item = treeItem.GetSelections()
        while item:
            piece = treeItem.GetItemText(item)
            pieces.insert(0, piece)
            item = treeItem.GetItemParent(item)
        print ("item path tree : ")
        print (pieces)
        pass
        list(parentWindowCtrl._appDataRef.mainDict[0].loadedData)
###################################################

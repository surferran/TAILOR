
import  sys
import  wx

from xml.parsers import expat

#----------------------------------------------------------------------

class XMLTree(wx.TreeCtrl):
    def __init__(self, parent, ID):
        # consider ID as tID = wx.NewId()
        wx.TreeCtrl.__init__(self, parent, ID
                             , wx.DefaultPosition, wx.DefaultSize,
                               wx.TR_HAS_BUTTONS
                               | wx.TR_EDIT_LABELS
                               | wx.TR_MULTIPLE
                               #| wx.TR_HIDE_ROOT
                               #, self.log
                             )
        self._root = self.AddRoot("Root")
        self.nodeStack = [self._root]

        # Trees need an image list to do DnD...
        self.il = wx.ImageList(16,16)
        self.SetImageList(self.il)

        # event handlers for DnD
        self.Bind(wx.EVT_TREE_BEGIN_DRAG,       self.OnBeginDrag)
        self.Bind(wx.EVT_TREE_END_DRAG,         self.OnEndDrag)

        # event handlers for tree items
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED,    self.OnItemExpanded)#,  self.tree)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED,   self.OnItemCollapsed)#, self.tree)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,      self.OnSelChanged)#,    self.tree)
        self.Bind(wx.EVT_TREE_BEGIN_LABEL_EDIT, self.OnBeginEdit)#,     self.tree)
        self.Bind(wx.EVT_TREE_END_LABEL_EDIT,   self.OnEndEdit)#,       self.tree)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,   self.OnActivate)#,      self.tree)

        self.Bind(wx.EVT_LEFT_DCLICK,      self.OnLeftDClick)
        self.Bind(wx.EVT_RIGHT_DOWN,       self.OnRightDown)
        self.Bind(wx.EVT_RIGHT_UP,         self.OnRightUp)

###################################################

    def OnRightDown(self, event):
        pt = event.GetPosition();
        item, flags = self.HitTest(pt)
        if item:
#            self.log.WriteText
            print ("OnRightClickDown: %s, %s, %s\n" %
                               (self.GetItemText(item), type(item), item.__class__))
            self.SelectItem(item)

    def OnRightUp(self, event):
        pt = event.GetPosition();
        item, flags = self.HitTest(pt)
        if item:        
#            self.log.WriteText
            print ("OnRightUp: %s (manually starting label edit)\n"
                               % self.GetItemText(item))
            self.EditLabel(item)  #todo:replace with pop up menu

    def OnBeginEdit(self, event):
#        self.log.WriteText
        print("OnEdit Begin\n")
        # show how to prevent edit...
        item = event.GetItem()
        if item and self.GetItemText(item) == "The Root Item":
            wx.Bell()
#            self.log.WriteText
            print ("You can't edit this one...\n")

#            # Lets just see what's visible of its children
#            cookie = 0
#            root = event.GetItem()
#            (child, cookie) = self.GetFirstChild(root)
#
#            while child.IsOk():
##                self.log.WriteText
#                print ("Child [%s] visible = %d" %
#                                   (self.GetItemText(child),
#                                    self.IsVisible(child)))
#                (child, cookie) = self.GetNextChild(root, cookie)

            event.Veto()

    def OnEndEdit(self, event):
#        self.log.WriteText
        print("OnEdit end: %s %s\n" %
                           (event.IsEditCancelled(), event.GetLabel()) )
#        # show how to reject edit, we'll not allow any digits
#        for x in event.GetLabel():
#            if x in string.digits:
##                self.log.WriteText
#                print("You can't enter digits...\n")
#                event.Veto()
#                return

    def OnLeftDClick(self, event):
        pt = event.GetPosition();
        item, flags = self.HitTest(pt)
        # sort childrens items . todo: activate self.EditLabel(item)
        if item:
#            self.log.WriteText
            print("OnLeftDClick: %s\n" % self.GetItemText(item))
            parent = self.GetItemParent(item)
            if parent.IsOk():
                self.SortChildren(parent)
        event.Skip()

    def OnSize(self, event):
        print ("size event visit")
        pass
#        w,h = self.GetClientSizeTuple()
#        self.SetDimensions(0, 0, w, h)

    def OnItemExpanded(self, event):
        item = event.GetItem()
#        if item:
#            self.log.WriteText("OnItemExpanded: %s\n" % self.tree.GetItemText(item))

    def OnItemCollapsed(self, event):
        item = event.GetItem()
#        if item:
#            self.log.WriteText("OnItemCollapsed: %s\n" % self.tree.GetItemText(item))

    def OnSelChanged(self, event):
        pass
#        self.item = event.GetItem()
#        if self.item:
#            self.log.WriteText("OnSelChanged: %s\n" % self.tree.GetItemText(self.item))
#            if wx.Platform == '__WXMSW__':
#                self.log.WriteText("BoundingRect: %s\n" %
#                                   self.tree.GetBoundingRect(self.item, True))
#            #items = self.tree.GetSelections()
#            #print map(self.tree.GetItemText, items)
#        event.Skip()

    def OnActivate(self, event):
        if self.item:
#            self.log.WriteText
            print("OnActivate: %s\n" % self.GetItemText(self.item))

###################################################
    def OnBeginDrag(self, event):
        item = event.GetItem()

        if item != self.GetRootItem():
            self.draggingItem = item
            event.Allow()  # if DnD of this item is okay Allow it.

    def IsDescendant(self, firstItem, secondItem):
        "Recursive check if firstItem is a descendant of a secondItem."
        if firstItem == self._root:
            return False
        parentItem = self.GetItemParent(firstItem)
        if parentItem == secondItem:
            return True
        else:
            return self.IsDescendant(parentItem, secondItem)

    def OnEndDrag(self, evt):
        itemSrc = self.draggingItem
        itemDst = evt.GetItem()
        self.draggingItem = None

        if not itemDst.IsOk():
            print ("Can't drag to here...")
            return

        if self.IsDescendant(itemDst, itemSrc):
            print ("Can't move item to its descendant")
            return

        # For this simple example just take the text of the source item
        # and append it to the destination item.  In real life you would
        # possibly want to copy subtrees...
        text = self.GetItemText(itemSrc)
        self.AppendItem(itemDst, text)
        self.Delete(itemSrc)


    # Define a handler for start element events
    def StartElement(self, name, attrs ):
        name = name.encode()

        id = self.AppendItem(self.nodeStack[-1], name)
        self.nodeStack.append(id)

    def EndElement(self,  name ):
        self.nodeStack = self.nodeStack[:-1]

    def CharacterData(self, data ):
        if data.strip():
            data = data.encode()

            self.AppendItem(self.nodeStack[-1], data)

#####################################################
    def LoadTree(self, filename):
        # Create a parser
        Parser = expat.ParserCreate()

        # Tell the parser what the start element handler is
        Parser.StartElementHandler = self.StartElement
        Parser.EndElementHandler = self.EndElement
        Parser.CharacterDataHandler = self.CharacterData

        # Parse the XML File
        ParserStatus = Parser.Parse(open(filename,'r').read(), 1)   # todo: giev option to get ready xml data structure

    def SaveTree(self,output_file_name):
        # todo ..  and search for ready made example
        pass
"""
@file : AUO_MAIN.py

@description 

main AUI creation.
the manager of all gui .

major reference of gui applications and tutorials (Hands-on wxPython, 2.9.4):
http://www.infinity77.net/pycon/tutorial/pybr/wxpython.html (full zip: http://bit.ly/TgyfRN)



31/03/18, 25/4/19:
OBJECTIVES:
...TBD...

LITERATURE REVIEW (background references before getting to this project):

    http://docs.enthought.com/chaco/ - building interactive and custom 2-D plots and visualizations

    http://doc.frapp.fr/doku.php?id=en:programmation:python:boa:help:boagettingstarted - boa tutorial
    https://bitbucket.org/cwt/boa-constructor/downloads/ - Boa aims to be a simple Delphi for wxPython.
    https://wiki.wxpython.org/Boa%20Constructor

    AvoPlot : https://openresearchsoftware.metajnl.com/articles/10.5334/jors.ai/

"""

from AUI_GlobalImports import *

# def focusFollowsMouse(window):
#     window.Bind(wx.EVT_ENTER_WINDOW, lambda event: window.SetFocus())
#
class AuiFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos= wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style = wx.DEFAULT_FRAME_STYLE
                        |wx.SUNKEN_BORDER,
                        #|wx.STAY_ON_TOP,       #ran : todo: set only for minimal template. not all
                 log=None):

        global appDataObj

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager()

        # tell AuiManager to manage this frame
        self._mgr.SetManagedWindow(self)
        
        # set frame icon
        self.SetIcon(images.Mondrian.GetIcon()) #TODO: set to relevant icon file

        # set up default notebook style
        self._notebook_style = aui.AUI_NB_DEFAULT_STYLE | aui.AUI_NB_TAB_EXTERNAL_MOVE | wx.NO_BORDER
        self._notebook_theme = 0
        # Attributes
        self._textCount = 1
        self._transparency = 255
        self._snapped = False
        self._custom_pane_buttons = False
        self._custom_tab_buttons = False
        self._pane_icons = False
        self._veto_tree = self._veto_text = False

        self.log = log

        self.CreateStatusBar()
        self.status_bar_callback(0, "Ready by new BAR")

        self.BuildPanes()
        self.CreateMenuBar()
        self.BindEvents()

        self._appDataRef = appDataObj

    def status_bar_callback(self, i, new_text):
        self.GetStatusBar().SetStatusText(new_text, i)

    def setViewMenu(self):
        view_menu = wx.Menu()
        view_menu.Append(ID_CreateText, "Create Text Control")
        view_menu.Append(ID_CreateHTML, "Create HTML Control")
        view_menu.Append(ID_CreateTree, "Create Tree")
        view_menu.Append(ID_CreateRanTree, "Create Ran Tree")#ran
        view_menu.Append(ID_CreateGrid, "Create Grid")
        view_menu.Append(ID_CreateNotebook, "Create Notebook")
        view_menu.Append(ID_CreateSizeReport, "Create Size Reporter")
        view_menu.AppendSeparator()
        view_menu.Append(ID_GridContent, "Use a Grid for the Content Pane")
        view_menu.Append(ID_TextContent, "Use a Text Control for the Content Pane")
        view_menu.Append(ID_HTMLContent, "Use an HTML Control for the Content Pane")
        view_menu.Append(ID_TreeContent, "Use a Tree Control for the Content Pane")
        view_menu.Append(ID_NotebookContent, "Use a AuiNotebook control for the Content Pane")

        view_menu.Append(ID_RanDDContent,
                         "Use a ID_RanDDContent control for the Content Pane")  # todo: replace with min layout commnad

        view_menu.Append(ID_SizeReportContent, "Use a Size Reporter for the Content Pane")
        view_menu.AppendSeparator()

        ##        if wx.Platform == "__WXMAC__":
        ##            switcherAccel = "Alt+Tab"
        ##        elif wx.Platform == "__WXGTK__":
        ##            switcherAccel = "Ctrl+/"
        ##        else:
        ##            switcherAccel = "Ctrl+Tab"
        ##
        ##        view_menu.Append(ID_SwitchPane, _("S&witch Window...") + "\t" + switcherAccel)
        return view_menu

    def setOptionsMenu(self):

        options_menu = wx.Menu()
        options_menu.AppendRadioItem(ID_TransparentHint, "Transparent Hint")
        options_menu.AppendRadioItem(ID_VenetianBlindsHint, "Venetian Blinds Hint")
        options_menu.AppendRadioItem(ID_RectangleHint, "Rectangle Hint")
        options_menu.AppendRadioItem(ID_NoHint, "No Hint")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_HintFade, "Hint Fade-in")
        options_menu.AppendCheckItem(ID_AllowFloating, "Allow Floating")
        options_menu.AppendCheckItem(ID_NoVenetianFade, "Disable Venetian Blinds Hint Fade-in")
        options_menu.AppendCheckItem(ID_TransparentDrag, "Transparent Drag")
        options_menu.AppendCheckItem(ID_AllowActivePane, "Allow Active Pane")
        options_menu.AppendCheckItem(ID_LiveUpdate, "Live Resize Update")
        options_menu.AppendCheckItem(ID_NativeMiniframes, "Use Native wx.MiniFrames")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_MinimizePosSmart, "Minimize in Smart mode").Check()
        options_menu.AppendRadioItem(ID_MinimizePosTop, "Minimize on Top")
        options_menu.AppendRadioItem(ID_MinimizePosLeft, "Minimize on the Left")
        options_menu.AppendRadioItem(ID_MinimizePosRight, "Minimize on the Right")
        options_menu.AppendRadioItem(ID_MinimizePosBottom, "Minimize at the Bottom")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_MinimizeCaptSmart, "Smart Minimized Caption")
        options_menu.AppendRadioItem(ID_MinimizeCaptHorz, "Horizontal Minimized Caption")
        options_menu.AppendRadioItem(ID_MinimizeCaptHide, "Hidden Minimized Caption").Check()
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_PaneIcons, "Set Icons On Panes")
        options_menu.AppendCheckItem(ID_AnimateFrames, "Animate Dock/Close/Minimize Of Floating Panes")
        options_menu.AppendCheckItem(ID_SmoothDocking, "Smooth Docking Effects (PyQT Style)")
        options_menu.AppendSeparator()
        options_menu.Append(ID_TransparentPane, "Set Floating Panes Transparency")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_DefaultDockArt, "Default DockArt")
        options_menu.AppendRadioItem(ID_ModernDockArt, "Modern Dock Art")
        options_menu.AppendSeparator()
        options_menu.Append(ID_SnapToScreen, "Snap To Screen")
        options_menu.AppendCheckItem(ID_SnapPanes, "Snap Panes To Managed Window")
        options_menu.AppendCheckItem(ID_FlyOut, "Use Fly-Out Floating Panes")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_CustomPaneButtons, "Set Custom Pane Button Bitmaps")
        options_menu.AppendSeparator()
        options_menu.AppendRadioItem(ID_NoGradient, "No Caption Gradient")
        options_menu.AppendRadioItem(ID_VerticalGradient, "Vertical Caption Gradient")
        options_menu.AppendRadioItem(ID_HorizontalGradient, "Horizontal Caption Gradient")
        options_menu.AppendSeparator()
        options_menu.AppendCheckItem(ID_PreviewMinimized, "Preview Minimized Panes")
        options_menu.AppendSeparator()
        options_menu.Append(ID_Settings, "Settings Pane")

        return options_menu

    def setNotebookMenu(self):
        notebook_menu = wx.Menu()
        notebook_menu.AppendRadioItem(ID_NotebookArtGloss, "Glossy Theme (Default)")
        notebook_menu.AppendRadioItem(ID_NotebookArtSimple, "Simple Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC71, "VC71 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtFF2, "Firefox 2 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtVC8, "VC8 Theme")
        notebook_menu.AppendRadioItem(ID_NotebookArtChrome, "Chrome Theme")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookNoCloseButton, "No Close Button")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButton, "Close Button At Right")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonAll, "Close Button On All Tabs")
        notebook_menu.AppendRadioItem(ID_NotebookCloseButtonActive, "Close Button On Active Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookCloseOnLeft, "Close Button On The Left Of Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendRadioItem(ID_NotebookAlignTop, "Tab Top Alignment")
        notebook_menu.AppendRadioItem(ID_NotebookAlignBottom, "Tab Bottom Alignment")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabMove, "Allow Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabExternalMove, "Allow External Tab Move")
        notebook_menu.AppendCheckItem(ID_NotebookAllowTabSplit, "Allow Notebook Split")
        notebook_menu.AppendCheckItem(ID_NotebookTabFloat, "Allow Single Tab Floating")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookDclickUnsplit, "Unsplit On Sash Double-Click")
        notebook_menu.AppendCheckItem(ID_NotebookTabDrawDnd, "Draw Tab Image On Drag 'n' Drop")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookScrollButtons, "Scroll Buttons Visible")
        notebook_menu.AppendCheckItem(ID_NotebookWindowList, "Window List Button Visible")
        notebook_menu.AppendCheckItem(ID_NotebookTabFixedWidth, "Fixed-Width Tabs")
        notebook_menu.AppendSeparator()
        notebook_menu.AppendCheckItem(ID_NotebookHideSingle, "Hide On Single Tab")
        notebook_menu.AppendCheckItem(ID_NotebookSmartTab, "Use Smart Tabbing")
        notebook_menu.AppendCheckItem(ID_NotebookUseImagesDropDown, "Use Tab Images In Dropdown Menu")
        notebook_menu.AppendCheckItem(ID_NotebookCustomButtons, "Show Custom Buttons In Tab Area")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(ID_NotebookMinMaxWidth, "Set Min/Max Tab Widths")
        notebook_menu.Append(ID_NotebookMultiLine, "Add A Multi-Line Label Tab")
        notebook_menu.AppendSeparator()
        notebook_menu.Append(ID_NotebookPreview, "Preview Of All Notebook Pages")

        return notebook_menu

    def setPerspectivesMenu(self):

        perspectives_menu = wx.Menu()

        self._perspectives_menu = wx.Menu()
        self._perspectives_menu.Append(ID_CreatePerspective, "Create Perspective")
        self._perspectives_menu.Append(ID_CopyPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._perspectives_menu.AppendSeparator()
        self._perspectives_menu.Append(ID_FirstPerspective+0, "Default Startup")
        self._perspectives_menu.Append(ID_FirstPerspective+1, "All Panes")
        self._perspectives_menu.Append(ID_FirstPerspective + 2, "Minimum for DragAndDrop") #ran
        self._perspectives_menu.Append(ID_FirstPerspective + 3, "Minimum 2") #ran

        self._nb_perspectives_menu = wx.Menu()
        self._nb_perspectives_menu.Append(ID_CreateNBPerspective, "Create Perspective")
        self._nb_perspectives_menu.Append(ID_CopyNBPerspectiveCode, "Copy Perspective Data To Clipboard")
        self._nb_perspectives_menu.AppendSeparator()
        self._nb_perspectives_menu.Append(ID_FirstNBPerspective+0, "Default Startup")

        guides_menu = wx.Menu()
        guides_menu.AppendRadioItem(ID_StandardGuides, "Standard Docking Guides")
        guides_menu.AppendRadioItem(ID_AeroGuides, "Aero-Style Docking Guides")
        guides_menu.AppendRadioItem(ID_WhidbeyGuides, "Whidbey-Style Docking Guides")

        perspectives_menu.Append(wx.ID_ANY, "Frame Perspectives", self._perspectives_menu)
        perspectives_menu.Append(wx.ID_ANY, "AuiNotebook Perspectives", self._nb_perspectives_menu)
        perspectives_menu.AppendSeparator()
        perspectives_menu.Append(wx.ID_ANY, "Docking Guides", guides_menu)

        return perspectives_menu

    def setActionMenu(self):

        action_menu = wx.Menu()
        action_menu.AppendCheckItem(ID_VetoTree, "Veto Floating Of Tree Pane")
        action_menu.AppendCheckItem(ID_VetoText, "Veto Docking Of Fixed Pane")
        action_menu.AppendSeparator()

        attention_menu = wx.Menu()

        self._requestPanes = {}
        for indx, pane in enumerate(self._mgr.GetAllPanes()):
            if pane.IsToolbar():
                continue
            if not pane.caption or not pane.name:
                continue
            ids = wx.ID_HIGHEST + 12345 + indx
            self._requestPanes[ids] = pane.name
            attention_menu.Append(ids, pane.caption)

        action_menu.Append(wx.ID_ANY, "Request User Attention For", attention_menu)

        return action_menu

    def CreateMenuBar(self):

        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "Exit")

        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "About...")

        mb.Append(file_menu, "&File")
        mb.Append(self.setViewMenu(), "&View")
        mb.Append(self.setPerspectivesMenu(), "&Perspectives")
        mb.Append(self.setOptionsMenu(), "&Options")
        mb.Append(self.setNotebookMenu(), "&Notebook")
        mb.Append(self.setActionMenu(), "&Actions")
        mb.Append(help_menu, "&Help")

        self.SetMenuBar(mb)

    def BuildToolBar(self, tb_prop):

        # tb_prop = user_ToolBars['tb_2']  current_tBar
        tbar = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                              agwStyle=eval(tb_prop['tb_properties']))

        for ndx, btn_props in enumerate(tb_prop['buttons']):
            key = list(btn_props.keys())[0]
            if key != 'seperator':
                btn = btn_props[key]
                tbar.AddSimpleTool(eval(btn['ID_string']), btn['btn_label'], eval(btn['btn_icon']), btn['btn_tooltip'])
                self.Bind(wx.EVT_MENU, eval(btn['action_to_be_evaluated']), id=eval(btn['ID_string']))
            else:
                tbar.AddSeparator()

        # tbar.Realize()

        return tbar

    def BuildPanes(self):
        '''
        create and add all desired panes windows .
        created in stock, only some are shown by hidden or show property.
        '''
        # min size for the frame itself isn't completely done.
        # see the end up AuiManager.Update() for the test
        # code. For now, just hard code a frame minimum size
        # self.SetMinSize(wx.Size(400, 300))
        self.SetMinSize(wx.Size(300, 150)) #ran

        # prepare a few custom overflow elements for the toolbars' overflow buttons

        prepend_items, append_items = [], []
        item = aui.AuiToolBarItem()

        item.SetKind(wx.ITEM_SEPARATOR)
        append_items.append(item)

        item = aui.AuiToolBarItem()
        item.SetKind(wx.ITEM_NORMAL)
        item.SetId(ID_CustomizeToolbar)
        # item.SetShortHelp("this is a short help string ")  running over the Label string..
        item.SetLabel("Customize...")
        append_items.append(item)


        # create some toolbars
        tb1 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb1.SetToolBitmapSize(wx.Size(48, 48))
        tb1.AddSimpleTool(ID_SampleItem+1, "Test", wx.ArtProvider.GetBitmap(wx.ART_ERROR))
        tb1.AddSeparator()
        tb1.AddSimpleTool(ID_SampleItem+2, "Test", wx.ArtProvider.GetBitmap(wx.ART_QUESTION))
        tb1.AddSimpleTool(ID_SampleItem+3, "Test", wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        tb1.AddSimpleTool(ID_SampleItem+4, "Test", wx.ArtProvider.GetBitmap(wx.ART_WARNING))
        tb1.AddSimpleTool(ID_SampleItem+5, "Test", wx.ArtProvider.GetBitmap(wx.ART_MISSING_IMAGE))
        tb1.SetCustomOverflowItems(prepend_items, append_items)
        # tb1.Realize()

        tb2 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb2.SetToolBitmapSize(wx.Size(16, 16))

        tb2_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))
        tb2.AddSimpleTool(ID_SampleItem+6, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+7, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+8, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+9, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+10, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+11, "Test", tb2_bmp1)
        tb2.AddSeparator()
        tb2.AddSimpleTool(ID_SampleItem+12, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+13, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+14, "Test", tb2_bmp1)
        tb2.AddSimpleTool(ID_SampleItem+15, "Test", tb2_bmp1)
        tb2.SetCustomOverflowItems(prepend_items, append_items)
        # tb2.Realize()

        tb3 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_DEFAULT_STYLE | aui.AUI_TB_OVERFLOW)
        tb3.SetToolBitmapSize(wx.Size(16, 16))
        tb3_bmp1 = wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16))
        tb3.AddSimpleTool(ID_SampleItem+16, "Check 1", tb3_bmp1, "Check 1", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+17, "Check 2", tb3_bmp1, "Check 2", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+18, "Check 3", tb3_bmp1, "Check 3", aui.ITEM_CHECK)
        tb3.AddSimpleTool(ID_SampleItem+19, "Check 4", tb3_bmp1, "Check 4", aui.ITEM_CHECK)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+20, "Radio 1", tb3_bmp1, "Radio 1", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+21, "Radio 2", tb3_bmp1, "Radio 2", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+22, "Radio 3", tb3_bmp1, "Radio 3", aui.ITEM_RADIO)
        tb3.AddSeparator()
        tb3.AddSimpleTool(ID_SampleItem+23, "Radio 1 (Group 2)", tb3_bmp1, "Radio 1 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+24, "Radio 2 (Group 2)", tb3_bmp1, "Radio 2 (Group 2)", aui.ITEM_RADIO)
        tb3.AddSimpleTool(ID_SampleItem+25, "Radio 3 (Group 2)", tb3_bmp1, "Radio 3 (Group 2)", aui.ITEM_RADIO)

        tb3.SetCustomOverflowItems(prepend_items, append_items)
        # tb3.Realize()

        """
        build from json user definitions file.
        TODO: it still depends deeply on function 'OnButtonPress' content 
        """
        ''''''
        self._user_settings_file = './user_prefs/settings_Toolbars_Items.json'
        user_ToolBars = fConverters.load_JSON_file_to_Dict(self._user_settings_file)

        print (user_ToolBars)
        print (user_ToolBars['tb_1'])
        
        tb_prop = user_ToolBars['tb_1']
        favorites_tbar = self.BuildToolBar(tb_prop)  # tb4

        tb_prop = user_ToolBars['tb_2']
        vertical_tbar = self.BuildToolBar(tb_prop)  # tb5
        ''''''

        tb6 = aui.AuiToolBar(self, -1, wx.DefaultPosition, wx.DefaultSize,
                             agwStyle=aui.AUI_TB_OVERFLOW | aui.AUI_TB_VERT_TEXT)
        tb6.SetToolBitmapSize(wx.Size(48, 48))
        tb6.AddSimpleTool(ID_SampleItem+35, "Clockwise 1", wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.AddSeparator()
        tb6.AddSimpleTool(ID_SampleItem+36, "Clockwise 2", wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.AddSimpleTool(ID_DropDownToolbarItem, "Clockwise 3", wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_OTHER, wx.Size(16, 16)))
        tb6.SetCustomOverflowItems(prepend_items, append_items)
        tb6.SetToolDropDown(ID_DropDownToolbarItem, True)
        # tb6.Realize()

        # add a bunch of panes

        self._mgr.AddPane(self.CreateRan_PanelCtrl(), aui.AuiPaneInfo().Name("RAN_name").Caption("RAN_caption").MaximizeButton(True))

        self.OnCreateRanTree(name="RAN_name2", caption="RAN_caption2", update=False, option=1)

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Name("test1").Caption("Pane Caption").Top().MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().Name("test8").Caption("Tree Pane").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).
                          MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("autonotebook").Caption("Auto NB").
                          Bottom().Layer(1).Position(1).MinimizeButton(True))

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Name("thirdauto").Caption("A Third Auto-NB Pane").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))  # ran note: using target creates tabs collection

        wnd10 = self.CreateTextCtrl("This pane will prompt the user before hiding.")
        self._mgr.AddPane(wnd10, aui.AuiPaneInfo().
                          Name("test10").Caption("Text Pane with Hide Prompt").
                          Bottom().MinimizeButton(True), target=self._mgr.GetPane("autonotebook"))

        # self._mgr.AddPane(SettingsPanel(self,self), aui.AuiPaneInfo().
        #                   Name("settings").Caption("Dock Manager Settings").
        #                   Dockable(False).Float().Hide().MinimizeButton(True))

        self._mgr.AddPane(JsonControlPanel(self,self), aui.AuiPaneInfo().
                          Name("new settings").Caption("Dock Manager new Settings").
                          Dockable(False).Float().Hide().MinimizeButton(True))

        # create some center panes
        self._mgr.AddPane(self.CreateRan_DandDCtrl(), aui.AuiPaneInfo().Name("DandD_content").
                          CenterPane().Hide().MinimizeButton(True))

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().Name("notebook_content").
                          CenterPane().PaneBorder(False))

        # add the toolbars to the manager
        self._mgr.AddPane(favorites_tbar, aui.AuiPaneInfo().Name("favorites_tbar").Caption("Sample Bookmark Toolbar").
                          # ToolbarPane().Top().Row(2))
                          ToolbarPane().Top().Row(1))

        self._mgr.AddPane(vertical_tbar, aui.AuiPaneInfo().Name("vertical_tbar").Caption("Sample Vertical Toolbar").
                          ToolbarPane().Left().GripperTop())

        if 1==1:    #choosing toolbars to add
            # pass
            self._mgr.AddPane(tb1, aui.AuiPaneInfo().Name("tb1").Caption("Big Toolbar").
                              ToolbarPane().Top())

            self._mgr.AddPane(tb2, aui.AuiPaneInfo().Name("tb2").Caption("Toolbar 2").
                              ToolbarPane().Top().Row(1))

            self._mgr.AddPane(tb3, aui.AuiPaneInfo().Name("tb3").Caption("Toolbar 3").
                              ToolbarPane().Top().Row(1).Position(1))


            self._mgr.AddPane(tb6, aui.AuiPaneInfo().
                              Name("tb6").Caption("Sample Vertical Clockwise Rotated Toolbar").
                              ToolbarPane().Right().GripperTop().TopDockable(False).BottomDockable(False));

            self._mgr.AddPane(wx.Button(self, -1, "Test Button"),
                              aui.AuiPaneInfo().Name("tb7").ToolbarPane().Top().Row(2).Position(1))

        # Show how to add a control inside a tab
        notebook = self._mgr.GetPane("notebook_content").window
        # self.gauge = ProgressGauge(notebook, size=(55, 15))   #ran
        # notebook.AddControlToPage(4, self.gauge) #ran : it is annoying..

        self._main_notebook = notebook

        self.handle_perspectives()

        # Show how to get a custom minimizing behaviour, i.e., to minimize a pane
        # inside an existing AuiToolBar
        tree = self._mgr.GetPane("test8")
        tree.MinimizeMode(aui.AUI_MINIMIZE_POS_TOOLBAR)

        toolbarPane = self._mgr.GetPane(favorites_tbar)
        tree.MinimizeTarget(toolbarPane)

        # "commit" all changes made to AuiManager
        self._mgr.Update()

    def hide_all_available_panes(self):
        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if not pane.IsToolbar():
                pane.Hide()
            else:  # ran added - hide toolbars as well:
                # print 
                pane.Hide()
                # print " is toolbar "

    def set_manual_hide_and_show_for_deafult_panes(self):
        # manual display configurations for setting the default one:
        self._mgr.GetPane("DandD_content").Hide()
        # self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), "Minimum layout")
        # self._perspectives.append(perspective_min)
        #        self.SetSize(previousSize)
        if 3 == 4:
            self._mgr.GetPane("tb1").Hide()
            self._mgr.GetPane("tb7").Hide()
        self._mgr.GetPane("favorites_tbar").Show()  # ran

        self._mgr.GetPane("test8").Show().Left().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("__notebook_%d" % self._mgr.GetPane("test10").notebook_id).\
                                   Show().Bottom().Layer(0).Row(0).Position(0)
        self._mgr.GetPane("autonotebook").Show()
        self._mgr.GetPane("thirdauto").Show()
        self._mgr.GetPane("test10").Show()
        self._mgr.GetPane("notebook_content").Show()

    def handle_perspectives(self):
        ''' perspective settings and keeping '''
        ''' set also frame size and position '''

        # todo: 1. set/load perspectives strings.
        #         2. set buttons to run py file (simulatino) and get csv results file
        #         3. check to allow running external 32bit dll (like in matlab)

        # keep the current setting, where most of the panes are created visible
        # assuming most are set to show(). those that are created with hide() are not included
        perspective_all = self._mgr.SavePerspective()

        # now hide all panes and show only those neede for new perspective
        self.hide_all_available_panes()
        self._mgr.GetPane("DandD_content").Show()

        # print sizes and locations
        if 1 == 2:
            # prnt = self.GetParent()     # get the parent panel
            # prnt2 = prnt.GetParent()    # get the frame window
            # prnt2.ToggleWindowStyle(wx.STAY_ON_TOP)

            # self.SetWindowStyle(wx.STAY_ON_TOP)
            # prnt.SetWindowStyle(wx.STAY_ON_TOP)
            # prnt2.SetWindowStyle(wx.STAY_ON_TOP)
            #:todo: set win size to min. set as external win.
            # get screen resolution

            print (self)
            print (self.GetSize())
            print (self.GetParent())
            print (self.GetParent().GetSize())
            print (self.GetParent().GetParent())
            print (self.GetParent().GetParent().GetSize())

            print (self)
            print (self.GetPosition())
            print (self.GetParent())
            print (self.GetParent().GetPosition())
            print (self.GetParent().GetParent())
            print (self.GetParent().GetParent().GetPosition())
        # set locations
        if 2==21:
            # desiredFramePos = wx.Point(1200,100)
            desiredFramePos = wx.Point(683, 384) #todo: take from config file / user preffs.
            previousSize = self.GetParent().GetParent().GetPosition()  #todo: check to relate self. or global
            self.GetParent().GetParent().SetPosition(desiredFramePos)
            # self.pos = (700,900)

            desiredFrameSize = wx.Size(400, 300)  #todo: take from config file
            # print 
            self.GetParent().GetParent().SetSize(desiredFrameSize)
            # print 
            self.SetSize(desiredFrameSize)

            if 2==1:
                print (self)
                print (self.GetPosition())
                print (self.GetParent())
                print (self.GetParent().GetPosition())
                print (self.GetParent().GetParent())
                print (self.GetParent().GetParent().GetPosition())

            # self.CenterOnScreen()
            # set size  , previousSize =
            # self.GetStartPosition()
            # self.GetParent().GetParent().SetSize(wx.Size(750, 150))
            w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
            h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
            centerPos = (w / 2, h / 2)
            print ("screen centerPos : " + str(centerPos[0]) + "," + str(centerPos[1]))

        # "commit" all changes made to AuiManager
        self._mgr.Update()
        perspective_min = self._mgr.SavePerspective()  # ran note: consider using 'Config' class and 'LoadPerspective' method

        self.set_manual_hide_and_show_for_deafult_panes()
        perspective_default = self._mgr.SavePerspective()  # ran note: consider using 'Config' class and 'LoadPerspective' method

        # add more perspective . ran
        self._mgr.LoadPerspective(perspective_min)
        self._mgr.GetPane("favorites_tbar").Show()
        self._mgr.GetPane("vertical_tbar").Show()
        perspective_min2 = self._mgr.SavePerspective()

        self._perspectives = []
        self._perspectives.append(perspective_default)
        self._perspectives.append(perspective_all)
        self._perspectives.append(perspective_min)  # ran
        self._perspectives.append(perspective_min2)  # ran
        self.keepPerspectivesToFile()

        self._nb_perspectives = []
        auibook = self._mgr.GetPane("notebook_content").window
        nb_perspective_default = auibook.SavePerspective()
        self._nb_perspectives.append(nb_perspective_default)

        self._mgr.LoadPerspective(perspective_default)  ##
        if 1==2:  # todo: condition with user input from file
            self._mgr.LoadPerspective(perspective_min2)  ## ran
        ''''''''''''''''''''''''

    def keepPerspectivesToFile(self):
        # todo: might use config instead
        # http: // www.pythonforbeginners.com / cheatsheet / python - file - handling
        filename = "perspectives.txt"
        file = open(filename, "w")
        file.writelines(self._perspectives)
        file.close()
        pass

    def BindEvents(self):
        '''
        set all revenat actions allowed to user interactions.
        by the 'options' text menu. or other
        '''

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MENU, self.OnCreateTree, id=ID_CreateTree)
        self.Bind(wx.EVT_MENU, self.OnCreateRanTree, id=ID_CreateRanTree)#ran
        self.Bind(wx.EVT_MENU, self.OnCreateGrid, id=ID_CreateGrid)
        self.Bind(wx.EVT_MENU, self.OnCreateText, id=ID_CreateText)
        self.Bind(wx.EVT_MENU, self.OnCreateHTML, id=ID_CreateHTML)
        self.Bind(wx.EVT_MENU, self.OnCreateSizeReport, id=ID_CreateSizeReport)
        self.Bind(wx.EVT_MENU, self.OnCreateNotebook, id=ID_CreateNotebook)
##        self.Bind(wx.EVT_MENU, self.OnSwitchPane, id=ID_SwitchPane)
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective, id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyPerspectiveCode, id=ID_CopyPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnCreateNBPerspective, id=ID_CreateNBPerspective)
        self.Bind(wx.EVT_MENU, self.OnCopyNBPerspectiveCode, id=ID_CopyNBPerspectiveCode)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_StandardGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_AeroGuides)
        self.Bind(wx.EVT_MENU, self.OnGuides, id=ID_WhidbeyGuides)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowFloating)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_RectangleHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoHint)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_HintFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_TransparentDrag)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_LiveUpdate)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_SmoothDocking)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_NativeMiniframes)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosTop)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosLeft)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosRight)
        self.Bind(wx.EVT_MENU, self.OnMinimizePosition, id=ID_MinimizePosBottom)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptSmart)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHorz)
        self.Bind(wx.EVT_MENU, self.OnMinimizeCaption, id=ID_MinimizeCaptHide)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AnimateFrames)
        self.Bind(wx.EVT_MENU, self.OnSetIconsOnPanes, id=ID_PaneIcons)
        self.Bind(wx.EVT_MENU, self.OnTransparentPane, id=ID_TransparentPane)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_MENU, self.OnDockArt, id=ID_ModernDockArt)
        self.Bind(wx.EVT_MENU, self.OnSnapToScreen, id=ID_SnapToScreen)
        self.Bind(wx.EVT_MENU, self.OnSnapPanes, id=ID_SnapPanes)
        self.Bind(wx.EVT_MENU, self.OnFlyOut, id=ID_FlyOut)
        self.Bind(wx.EVT_MENU, self.OnCustomPaneButtons, id=ID_CustomPaneButtons)
        self.Bind(wx.EVT_MENU, self.OnManagerFlag, id=ID_AllowActivePane)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtGloss)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtSimple)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC71)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtFF2)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtVC8)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookArtChrome)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_MENU, self.OnNotebookFlag, id=ID_NotebookCloseOnLeft)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignTop)
        self.Bind(wx.EVT_MENU, self.OnTabAlignment, id=ID_NotebookAlignBottom)
        self.Bind(wx.EVT_MENU, self.OnCustomTabButtons, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_MENU, self.OnMinMaxTabWidth, id=ID_NotebookMinMaxWidth)
        self.Bind(wx.EVT_MENU, self.OnPreview, id=ID_NotebookPreview)
        self.Bind(wx.EVT_MENU, self.OnAddMultiLine, id=ID_NotebookMultiLine)

        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_NoGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_VerticalGradient)
        self.Bind(wx.EVT_MENU, self.OnGradient, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_MENU, self.OnSettings, id=ID_Settings)
        self.Bind(wx.EVT_MENU, self.OnPreviewMinimized, id=ID_PreviewMinimized)
        self.Bind(wx.EVT_MENU, self.OnCustomizeToolbar, id=ID_CustomizeToolbar)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_GridContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TreeContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_TextContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_SizeReportContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_HTMLContent)
        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_NotebookContent)

        self.Bind(wx.EVT_MENU, self.OnChangeContentPane, id=ID_RanDDContent) #ran

        self.Bind(wx.EVT_MENU, self.OnVetoTree, id=ID_VetoTree)
        self.Bind(wx.EVT_MENU, self.OnVetoText, id=ID_VetoText)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_MENU, self.OnRequestUserAttention, id=ids)

        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)

        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestoreNBPerspective, id=ID_FirstNBPerspective,
                  id2=ID_FirstNBPerspective+1000)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AllowFloating)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HintFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_TransparentDrag)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VerticalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_HorizontalGradient)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VenetianBlindsHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_RectangleHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoHint)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NoVenetianFade)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_LiveUpdate)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_PaneIcons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AnimateFrames)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_DefaultDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_ModernDockArt)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_SnapPanes)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_FlyOut)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_CustomPaneButtons)

        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFixedWidth)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookNoCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButton)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonAll)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCloseButtonActive)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabExternalMove)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookAllowTabSplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabFloat)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookDclickUnsplit)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookTabDrawDnd)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookScrollButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookWindowList)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookHideSingle)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookSmartTab)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookUseImagesDropDown)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_NotebookCustomButtons)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoTree)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_VetoText)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_StandardGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_AeroGuides)
        self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ID_WhidbeyGuides)

        for ids in self._requestPanes:
            self.Bind(wx.EVT_UPDATE_UI, self.OnUpdateUI, id=ids)

        self.Bind(aui.EVT_AUITOOLBAR_TOOL_DROPDOWN  , self.OnDropDownToolbarItem, id=ID_DropDownToolbarItem) #todo: use it. ran
        self.Bind(aui.EVT_AUI_PANE_CLOSE            , self.OnPaneClose)
        self.Bind(aui.EVT_AUINOTEBOOK_ALLOW_DND     , self.OnAllowNotebookDnD)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE    , self.OnNotebookPageClose)

        # self.Bind(aui.EVT_AUI_PANE_BUTTON           , self.onButtonPress        , id=ID_SampleItem+23) #ran
        # self.Bind(wx.EVT_BUTTON           , self.onButtonPress        , id=ID_SampleItem+24) #ran
        # self.Bind(wx.EVT_MENU, self.OnButtonPress, id=ID_SampleItem+23)  # ran
        # self.Bind(wx.EVT_MENU, self.OnButtonPress, id=ID_SampleItem+24)  # ran
        # self.Bind(wx.EVT_MENU, self.OnButtonPress, id=ID_SampleItem+25)  # ran
        # self.Bind(aui.EVT_AUI_PANE_BUTTON           , self.onButtonPress        , id=ID_SampleItem+26) #ran

        # ran removed those Alarm bindings
        # self.Bind(aui.EVT_AUI_PANE_FLOATING, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_FLOATED, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_DOCKING, self.OnFloatDock)
        # self.Bind(aui.EVT_AUI_PANE_DOCKED, self.OnFloatDock)

        # self.Bind(wx.EVT_CLOSE, self.OnClose)  # already set above in 755

        self.Bind(wx.EVT_TIMER, self.TimerHandler)
        self.timer = wx.Timer(self)
        self.timer.Start(100)


    def OnButtonPress(self, event):
        print  ("onBtnPrs")
        # ref: https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html?highlight=filedialog%20style

        # This is how you pre-establish a file filter so that the dialog
        # only shows the extension(s) you want it to.
        files_wildcard = "Python source (*.py)|*.py|" \
                         "CSV files (*.csv)|*.csv|" \
                         "All files (*.*)|*.*"
        # '''
        # # xls
        # # csv
        # # mat
        # # txt
        # # log
        # '''
        #                  "Compiled Python (*.pyc)|*.pyc|" \
        #                  "SPAM files (*.spam)|*.spam|" \
        #                  "Egg file (*.egg)|*.egg|" \

        print ("CWD: %s\n" % os.getcwd())

        # print event.EventObject
        if event.EventObject._tip_item.label=="Open":
            # print "found the correct label:)"
            # event.EventObject._tip_item.long_help="ran d was here "
            #todo: open dialog to select file nmae.
            #      load the file
            # Create the dialog. In this case the current directory is forced as the starting
            # directory for the dialog, and no default file name is forced. This can easilly
            # be changed in your program. This is an 'open' dialog, and allows multitple
            # file selections as well.
            #
            # Finally, if the directory is changed in the process of getting files, this
            # dialog is set up to change the current working directory to the path chosen.
            dlg = wx.FileDialog(
                self, message="Choose a file",
                defaultDir=os.getcwd(),
                defaultFile="",
                wildcard=files_wildcard,
                style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            )

            # Show the dialog and retrieve the user response. If it is the OK response,
            # process the data.
            if dlg.ShowModal() == wx.ID_OK:
                # This returns a Python list of files that were selected.
                paths = dlg.GetPaths()

                # self.log.WriteText('You selected %d files:' % len(paths))
                print('You selected %d files:' % len(paths))

                for path in paths:
                    print('           %s\n' % path)
                    # sort_file_action_by_type
                    files_handler.file_action_by_type(path, self._appDataRef)

            # Compare this with the debug above; did we change working dirs?
            print ("CWD: %s\n" % os.getcwd())

            # Destroy the dialog. Don't do this until you are done with it!
            # BAD things can happen otherwise!
            dlg.Destroy()

        elif event.EventObject._tip_item.label=="Save":

            # Create the dialog. In this case the current directory is forced as the starting
            # directory for the dialog, and no default file name is forced. This can easilly
            # be changed in your program. This is an 'save' dialog.
            #
            # Unlike the 'open dialog' example found elsewhere, this example does NOT
            # force the current working directory to change if the user chooses a different
            # directory than the one initially set.
            dlg = wx.FileDialog(
                self, message="Save file as ...", defaultDir=os.getcwd(),
                defaultFile="", wildcard=wildcard, style=wx.SAVE
            )

            # This sets the default filter that the user will initially see. Otherwise,
            # the first filter in the list will be used by default.
            dlg.SetFilterIndex(2)

            # Show the dialog and retrieve the user response. If it is the OK response,
            # process the data.
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                print ('You selected "%s"' % path)

                # Normally, at this point you would save your data using the file and path
                # data that the user provided to you, but since we didn't actually start
                # with any data to work with, that would be difficult.
                #
                # The code to do so would be similar to this, assuming 'data' contains
                # the data you want to save:
                #
                # fp = file(path, 'w') # Create file anew
                # fp.write(data)
                # fp.close()
                #
                # You might want to add some error checking :-)
                #

            # Note that the current working dir didn't change. This is good since
            # that's the way we set it up.
            print("CWD: %s\n" % os.getcwd())

            # Destroy the dialog. Don't do this until you are done with it!
            # BAD things can happen otherwise!
            dlg.Destroy()
        elif event.EventObject._tip_item.label == "Show App Data":
            print ("build app data tree")
            self.OnCreate_AppDataTree()
        elif event.EventObject._tip_item.label == "Reload CSV":
            print ("reloading")
#            basePath = './simOutputsData/'   
            basePath = '../bokeh/_externals_not_used_/bokeh_app/data/'
            fileDict1 = files_handler.get_file_details(basePath + 'quad_sim.csv')            
            fileDict2 = files_handler.get_file_details(basePath + 'titanic3.csv')
            fileDict3 = files_handler.get_file_details(basePath + 'tips.csv')
            files_handler.load_CSV_to_appData(fileDict1, self._appDataRef)
            files_handler.load_CSV_to_appData(fileDict2, self._appDataRef)
            files_handler.load_CSV_to_appData(fileDict3, self._appDataRef)

        pass

    def __del__(self):

        self.timer.Stop()


    def OnClose(self, event):

        self.timer.Stop()
        self._mgr.UnInit()
        event.Skip()


    def TimerHandler(self, event):

        try:
            self.gauge.Pulse()
        except RuntimeError:   # wx.PyDeadObjectError:
            print ("TimerHandler event : wx.PyDeadObjectError exception ")
            self.timer.Stop()
        except:
            print ("TimerHandler event : no gauge.Pulse() object - stopping the timer")
            self.timer.Stop()


    def GetDockArt(self):

        return self._mgr.GetArtProvider()


    def DoUpdate(self):

        self._mgr.Update()
        self.Refresh()


    def OnEraseBackground(self, event):

        event.Skip()


    def OnSize(self, event):

        event.Skip()


    def OnSettings(self, event):

        # show the settings pane, and float it
        floating_pane = self._mgr.GetPane("new settings").Float().Show()

        if floating_pane.floating_pos == wx.DefaultPosition:
            floating_pane.FloatingPosition(self.GetStartPosition())

        self._mgr.Update()


    def OnPreviewMinimized(self, event):

        checked = event.IsChecked()
        agwFlags = self._mgr.GetAGWFlags()

        if event.IsChecked():
            agwFlags ^= aui.AUI_MGR_PREVIEW_MINIMIZED_PANES
        else:
            agwFlags &= ~aui.AUI_MGR_PREVIEW_MINIMIZED_PANES

        self._mgr.SetAGWFlags(agwFlags)


    def OnSetIconsOnPanes(self, event):

        panes = self._mgr.GetAllPanes()
        checked = event.IsChecked()
        self._pane_icons = checked

        for pane in panes:
            if checked:
                randimage = random.randint(0, len(ArtIDs) - 1)
                bmp = wx.ArtProvider.GetBitmap(eval(ArtIDs[randimage]), wx.ART_OTHER, (16, 16))
            else:
                bmp = None

            pane.Icon(bmp)

        self._mgr.Update()


    def OnTransparentPane(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a transparency value (0-255):", "Pane transparency")

        dlg.SetValue("%d"%self._transparency)
        if dlg.ShowModal() != wx.ID_OK:
            return

        transparency = int(dlg.GetValue())
        dlg.Destroy()
        try:
            transparency = int(transparency)
        except:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if transparency < 0 or transparency > 255:
            dlg = wx.MessageDialog(self, 'Invalid transparency value. Transparency' \
                                   ' should be an integer between 0 and 255.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        self._transparency = transparency
        panes = self._mgr.GetAllPanes()
        for pane in panes:
            pane.Transparent(self._transparency)

        self._mgr.Update()


    def OnDockArt(self, event):

        if event.GetId() == ID_DefaultDockArt:
            self._mgr.SetArtProvider(aui.AuiDefaultDockArt())
        else:
            if self._mgr.CanUseModernDockArt():
                self._mgr.SetArtProvider(aui.ModernDockArt(self))

        self._mgr.Update()
        self.Refresh()


    def OnSnapToScreen(self, event):

        self._mgr.SnapToScreen(True, monitor=0, hAlign=wx.RIGHT, vAlign=wx.TOP)


    def OnSnapPanes(self, event):

        allPanes = self._mgr.GetAllPanes()

        if not self._snapped:
            self._captions = {}
            for pane in allPanes:
                self._captions[pane.name] = pane.caption

        toSnap = not self._snapped

        if toSnap:
            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                snap = random.randint(0, 4)
                if snap == 0:
                    # Snap everywhere
                    pane.Caption(pane.caption + " (Snap Everywhere)")
                    pane.Snappable(True)
                elif snap == 1:
                    # Snap left
                    pane.Caption(pane.caption + " (Snap Left)")
                    pane.LeftSnappable(True)
                elif snap == 2:
                    # Snap right
                    pane.Caption(pane.caption + " (Snap Right)")
                    pane.RightSnappable(True)
                elif snap == 3:
                    # Snap top
                    pane.Caption(pane.caption + " (Snap Top)")
                    pane.TopSnappable(True)
                elif snap == 4:
                    # Snap bottom
                    pane.Caption(pane.caption + " (Snap Bottom)")
                    pane.BottomSnappable(True)

        else:

            for pane in allPanes:
                if pane.IsToolbar() or isinstance(pane.window, aui.AuiNotebook):
                    continue

                pane.Caption(self._captions[pane.name])
                pane.Snappable(False)

        self._snapped = toSnap
        self._mgr.Update()
        self.Refresh()


    def OnFlyOut(self, event):

        checked = event.IsChecked()
        pane = self._mgr.GetPane("test8")

        if checked:
            dlg = wx.MessageDialog(self, 'The tree pane will have fly-out' \
                                   ' behaviour when floating.',
                                   'Message',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            pane.FlyOut(True)
        else:
            pane.FlyOut(False)

        self._mgr.Update()


    def OnCustomPaneButtons(self, event):

        self._custom_pane_buttons = checked = event.IsChecked()
        art = self._mgr.GetArtProvider()

        if not checked:
            art.SetDefaultPaneBitmaps(wx.Platform == "__WXMAC__")
        else:
            for bmp, button, active, maximize in CUSTOM_PANE_BITMAPS:
                art.SetCustomPaneBitmap(bmp.GetBitmap(), button, active, maximize)

        self._mgr.Update()
        self.Refresh()


    def OnCustomizeToolbar(self, event):

        wx.MessageBox("Customize Toolbar clicked", "AUI Test")


    def OnGradient(self, event):

        evId = event.GetId()
        if evId == ID_NoGradient:
            gradient = aui.AUI_GRADIENT_NONE
        elif evId == ID_VerticalGradient:
            gradient = aui.AUI_GRADIENT_VERTICAL
        elif evId == ID_HorizontalGradient:
            gradient = aui.AUI_GRADIENT_HORIZONTAL

        self._mgr.GetArtProvider().SetMetric(aui.AUI_DOCKART_GRADIENT_TYPE, gradient)
        self._mgr.Update()


    def OnManagerFlag(self, event):

        flag = 0
        evId = event.GetId()

        if evId in [ID_TransparentHint, ID_VenetianBlindsHint, ID_RectangleHint, ID_NoHint]:

            agwFlags = self._mgr.GetAGWFlags()
            agwFlags &= ~aui.AUI_MGR_TRANSPARENT_HINT
            agwFlags &= ~aui.AUI_MGR_VENETIAN_BLINDS_HINT
            agwFlags &= ~aui.AUI_MGR_RECTANGLE_HINT
            self._mgr.SetAGWFlags(agwFlags)

        if evId == ID_AllowFloating:
            flag = aui.AUI_MGR_ALLOW_FLOATING
        elif evId == ID_TransparentDrag:
            flag = aui.AUI_MGR_TRANSPARENT_DRAG
        elif evId == ID_HintFade:
            flag = aui.AUI_MGR_HINT_FADE
        elif evId == ID_NoVenetianFade:
            flag = aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE
        elif evId == ID_AllowActivePane:
            flag = aui.AUI_MGR_ALLOW_ACTIVE_PANE
        elif evId == ID_TransparentHint:
            flag = aui.AUI_MGR_TRANSPARENT_HINT
        elif evId == ID_VenetianBlindsHint:
            flag = aui.AUI_MGR_VENETIAN_BLINDS_HINT
        elif evId == ID_RectangleHint:
            flag = aui.AUI_MGR_RECTANGLE_HINT
        elif evId == ID_LiveUpdate:
            flag = aui.AUI_MGR_LIVE_RESIZE
        elif evId == ID_AnimateFrames:
            flag = aui.AUI_MGR_ANIMATE_FRAMES
        elif evId == ID_SmoothDocking:
            flag = aui.AUI_MGR_SMOOTH_DOCKING
        elif evId == ID_NativeMiniframes:
            flag = aui.AUI_MGR_USE_NATIVE_MINIFRAMES

        if flag:
            self._mgr.SetAGWFlags(self._mgr.GetAGWFlags() ^ flag)

        self._mgr.Update()


    def OnMinimizePosition(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizePosSmart:
            minize_mode |= aui.AUI_MINIMIZE_POS_SMART
        elif evId == ID_MinimizePosTop:
            minize_mode |= aui.AUI_MINIMIZE_POS_TOP
        elif evId == ID_MinimizePosLeft:
            minize_mode |= aui.AUI_MINIMIZE_POS_LEFT
        elif evId == ID_MinimizePosRight:
            minize_mode |= aui.AUI_MINIMIZE_POS_RIGHT
        elif evId == ID_MinimizePosBottom:
            minize_mode |= aui.AUI_MINIMIZE_POS_BOTTOM

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            if pane.name != "test8":
                pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_CAPT_MASK))


    def OnMinimizeCaption(self, event):

        minize_mode = 0
        evId = event.GetId()

        if evId == ID_MinimizeCaptSmart:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_SMART
        elif evId == ID_MinimizeCaptHorz:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HORZ
        elif evId == ID_MinimizeCaptHide:
            minize_mode |= aui.AUI_MINIMIZE_CAPT_HIDE

        all_panes = self._mgr.GetAllPanes()
        for pane in all_panes:
            pane.MinimizeMode(minize_mode | (pane.GetMinimizeMode() & aui.AUI_MINIMIZE_POS_MASK))


    def OnNotebookFlag(self, event):
        '''
        change appearance of relevant notebook by the user menu selection. or other..
        '''

        evId = event.GetId()
        unsplit = None

        if evId in [ID_NotebookNoCloseButton, ID_NotebookCloseButton, ID_NotebookCloseButtonAll, \
                    ID_NotebookCloseButtonActive]:

            self._notebook_style &= ~(aui.AUI_NB_CLOSE_BUTTON |
                                      aui.AUI_NB_CLOSE_ON_ACTIVE_TAB |
                                      aui.AUI_NB_CLOSE_ON_ALL_TABS)

            if evId == ID_NotebookCloseButton:
                self._notebook_style ^= aui.AUI_NB_CLOSE_BUTTON
            elif evId == ID_NotebookCloseButtonAll:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ALL_TABS
            elif evId == ID_NotebookCloseButtonActive:
                self._notebook_style ^= aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

        if evId == ID_NotebookAllowTabMove:
            self._notebook_style ^= aui.AUI_NB_TAB_MOVE

        if evId == ID_NotebookAllowTabExternalMove:
            self._notebook_style ^= aui.AUI_NB_TAB_EXTERNAL_MOVE

        elif evId == ID_NotebookAllowTabSplit:
            self._notebook_style ^= aui.AUI_NB_TAB_SPLIT

        elif evId == ID_NotebookTabFloat:
            self._notebook_style ^= aui.AUI_NB_TAB_FLOAT

        elif evId == ID_NotebookTabDrawDnd:
            self._notebook_style ^= aui.AUI_NB_DRAW_DND_TAB

        elif evId == ID_NotebookWindowList:
            self._notebook_style ^= aui.AUI_NB_WINDOWLIST_BUTTON

        elif evId == ID_NotebookScrollButtons:
            self._notebook_style ^= aui.AUI_NB_SCROLL_BUTTONS

        elif evId == ID_NotebookTabFixedWidth:
            self._notebook_style ^= aui.AUI_NB_TAB_FIXED_WIDTH

        elif evId == ID_NotebookHideSingle:
            self._notebook_style ^= aui.AUI_NB_HIDE_ON_SINGLE_TAB

        elif evId == ID_NotebookSmartTab:
            self._notebook_style ^= aui.AUI_NB_SMART_TABS

        elif evId == ID_NotebookUseImagesDropDown:
            self._notebook_style ^= aui.AUI_NB_USE_IMAGES_DROPDOWN

        elif evId == ID_NotebookCloseOnLeft:
            self._notebook_style ^= aui.AUI_NB_CLOSE_ON_TAB_LEFT

        all_panes = self._mgr.GetAllPanes()

        for pane in all_panes:

            if isinstance(pane.window, aui.AuiNotebook):
                nb = pane.window

                if evId == ID_NotebookArtGloss:

                    nb.SetArtProvider(aui.AuiDefaultTabArt())
                    self._notebook_theme = 0

                elif evId == ID_NotebookArtSimple:
                    nb.SetArtProvider(aui.AuiSimpleTabArt())
                    self._notebook_theme = 1

                elif evId == ID_NotebookArtVC71:
                    nb.SetArtProvider(aui.VC71TabArt())
                    self._notebook_theme = 2

                elif evId == ID_NotebookArtFF2:
                    nb.SetArtProvider(aui.FF2TabArt())
                    self._notebook_theme = 3

                elif evId == ID_NotebookArtVC8:
                    nb.SetArtProvider(aui.VC8TabArt())
                    self._notebook_theme = 4

                elif evId == ID_NotebookArtChrome:
                    nb.SetArtProvider(aui.ChromeTabArt())
                    self._notebook_theme = 5

                if nb.GetAGWWindowStyleFlag() & aui.AUI_NB_BOTTOM == 0:
                    nb.SetAGWWindowStyleFlag(self._notebook_style)

                if evId == ID_NotebookCloseButtonAll:
                    # Demonstrate how to remove a close button from a tab
                    nb.SetCloseButton(2, False)
                elif evId == ID_NotebookDclickUnsplit:
                    nb.SetSashDClickUnsplit(event.IsChecked())

                nb.Refresh()
                nb.Update()


    def OnUpdateUI(self, event):

        agwFlags = self._mgr.GetAGWFlags()
        evId = event.GetId()

        if evId == ID_NoGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_NONE)

        elif evId == ID_VerticalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_VERTICAL)

        elif evId == ID_HorizontalGradient:
            event.Check(self._mgr.GetArtProvider().GetMetric(aui.AUI_DOCKART_GRADIENT_TYPE) == aui.AUI_GRADIENT_HORIZONTAL)

        elif evId == ID_AllowFloating:
            event.Check((agwFlags & aui.AUI_MGR_ALLOW_FLOATING) != 0)

        elif evId == ID_TransparentDrag:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_DRAG) != 0)

        elif evId == ID_TransparentHint:
            event.Check((agwFlags & aui.AUI_MGR_TRANSPARENT_HINT) != 0)

        elif evId == ID_LiveUpdate:
            event.Check(aui.AuiManager_HasLiveResize(self._mgr))

        elif evId == ID_VenetianBlindsHint:
            event.Check((agwFlags & aui.AUI_MGR_VENETIAN_BLINDS_HINT) != 0)

        elif evId == ID_RectangleHint:
            event.Check((agwFlags & aui.AUI_MGR_RECTANGLE_HINT) != 0)

        elif evId == ID_NoHint:
            event.Check(((aui.AUI_MGR_TRANSPARENT_HINT |
                              aui.AUI_MGR_VENETIAN_BLINDS_HINT |
                              aui.AUI_MGR_RECTANGLE_HINT) & agwFlags) == 0)

        elif evId == ID_HintFade:
            event.Check((agwFlags & aui.AUI_MGR_HINT_FADE) != 0)

        elif evId == ID_NoVenetianFade:
            event.Check((agwFlags & aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE) != 0)

        elif evId == ID_NativeMiniframes:
            event.Check(aui.AuiManager_UseNativeMiniframes(self._mgr))

        elif evId == ID_PaneIcons:
            event.Check(self._pane_icons)

        elif evId == ID_SmoothDocking:
            event.Check((agwFlags & aui.AUI_MGR_SMOOTH_DOCKING) != 0)

        elif evId == ID_AnimateFrames:
            event.Check((agwFlags & aui.AUI_MGR_ANIMATE_FRAMES) != 0)

        elif evId == ID_DefaultDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.AuiDefaultDockArt))

        elif evId == ID_ModernDockArt:
            event.Check(isinstance(self._mgr.GetArtProvider(), aui.ModernDockArt))

        elif evId == ID_SnapPanes:
            event.Check(self._snapped)

        elif evId == ID_FlyOut:
            pane = self._mgr.GetPane("test8")
            event.Check(pane.IsFlyOut())

        elif evId == ID_AeroGuides:
            event.Check(agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES != 0)

        elif evId == ID_WhidbeyGuides:
            event.Check(agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES != 0)

        elif evId == ID_StandardGuides:
            event.Check((agwFlags & aui.AUI_MGR_AERO_DOCKING_GUIDES == 0) and (agwFlags & aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES == 0))

        elif evId == ID_CustomPaneButtons:
            event.Check(self._custom_pane_buttons)

        elif evId == ID_PreviewMinimized:
            event.Check(agwFlags & aui.AUI_MGR_PREVIEW_MINIMIZED_PANES)

        elif evId == ID_NotebookNoCloseButton:
            event.Check((self._notebook_style & (aui.AUI_NB_CLOSE_BUTTON|aui.AUI_NB_CLOSE_ON_ALL_TABS|aui.AUI_NB_CLOSE_ON_ACTIVE_TAB)) != 0)

        elif evId == ID_NotebookCloseButton:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_BUTTON) != 0)

        elif evId == ID_NotebookCloseButtonAll:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ALL_TABS) != 0)

        elif evId == ID_NotebookCloseButtonActive:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_ACTIVE_TAB) != 0)

        elif evId == ID_NotebookAllowTabSplit:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_SPLIT) != 0)

        elif evId == ID_NotebookTabFloat:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FLOAT) != 0)

        elif evId == ID_NotebookDclickUnsplit:
            event.Check(self._main_notebook.GetSashDClickUnsplit())

        elif evId == ID_NotebookTabDrawDnd:
            event.Check((self._notebook_style & aui.AUI_NB_DRAW_DND_TAB) != 0)

        elif evId == ID_NotebookAllowTabMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_MOVE) != 0)

        elif evId == ID_NotebookAllowTabExternalMove:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_EXTERNAL_MOVE) != 0)

        elif evId == ID_NotebookScrollButtons:
            event.Check((self._notebook_style & aui.AUI_NB_SCROLL_BUTTONS) != 0)

        elif evId == ID_NotebookWindowList:
            event.Check((self._notebook_style & aui.AUI_NB_WINDOWLIST_BUTTON) != 0)

        elif evId == ID_NotebookTabFixedWidth:
            event.Check((self._notebook_style & aui.AUI_NB_TAB_FIXED_WIDTH) != 0)

        elif evId == ID_NotebookHideSingle:
            event.Check((self._notebook_style & aui.AUI_NB_HIDE_ON_SINGLE_TAB) != 0)

        elif evId == ID_NotebookSmartTab:
            event.Check((self._notebook_style & aui.AUI_NB_SMART_TABS) != 0)

        elif evId == ID_NotebookUseImagesDropDown:
            event.Check((self._notebook_style & aui.AUI_NB_USE_IMAGES_DROPDOWN) != 0)

        elif evId == ID_NotebookCloseOnLeft:
            event.Check((self._notebook_style & aui.AUI_NB_CLOSE_ON_TAB_LEFT) != 0)

        elif evId == ID_NotebookCustomButtons:
            event.Check(self._custom_tab_buttons)

        elif evId == ID_NotebookArtGloss:
            event.Check(self._notebook_theme == 0)

        elif evId == ID_NotebookArtSimple:
            event.Check(self._notebook_theme == 1)

        elif evId == ID_NotebookArtVC71:
            event.Check(self._notebook_theme == 2)

        elif evId == ID_NotebookArtFF2:
            event.Check(self._notebook_theme == 3)

        elif evId == ID_NotebookArtVC8:
            event.Check(self._notebook_theme == 4)

        elif evId == ID_NotebookArtChrome:
            event.Check(self._notebook_theme == 5)

        elif evId == ID_VetoTree:
            event.Check(self._veto_tree)

        elif evId == ID_VetoText:
            event.Check(self._veto_text)

        else:
            for ids in self._requestPanes:
                if evId == ids:
                    paneName = self._requestPanes[ids]
                    pane = self._mgr.GetPane(paneName)
                    event.Enable(pane.IsShown())


    def OnPaneClose(self, event):

        if event.pane.name == "test10":

            msg = "Are you sure you want to "
            if event.GetEventType() == aui.wxEVT_AUI_PANE_MINIMIZE:
                msg += "minimize "
            else:
                msg += "close/hide "

            res = wx.MessageBox(msg + "this pane?", "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnCreatePerspective(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")

        dlg.SetValue("Perspective %u"%(len(self._perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._perspectives) == 0:
            self._perspectives_menu.AppendSeparator()

        self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), dlg.GetValue())
        self._perspectives.append(self._mgr.SavePerspective())


    def OnCopyPerspectiveCode(self, event):

        s = self._mgr.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()


    def OnRestorePerspective(self, event):

        self._mgr.LoadPerspective(self._perspectives[event.GetId() - ID_FirstPerspective])


    def OnCreateNBPerspective(self, event):

        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")

        dlg.SetValue("Perspective %u"%(len(self._nb_perspectives) + 1))
        if dlg.ShowModal() != wx.ID_OK:
            return

        if len(self._nb_perspectives) == 0:
            self._nb_perspectives_menu.AppendSeparator()

        auibook = self._mgr.GetPane("notebook_content").window
        self._nb_perspectives_menu.Append(ID_FirstNBPerspective + len(self._nb_perspectives), dlg.GetValue())
        self._nb_perspectives.append(auibook.SavePerspective())


    def OnCopyNBPerspectiveCode(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        s = auibook.SavePerspective()

        if wx.TheClipboard.Open():

            wx.TheClipboard.SetData(wx.TextDataObject(s))
            wx.TheClipboard.Close()


    def OnRestoreNBPerspective(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.LoadPerspective(self._nb_perspectives[event.GetId() - ID_FirstNBPerspective])

        self.gauge = ProgressGauge(auibook, size=(55, 15))
        auibook.AddControlToPage(4, self.gauge)


    def OnGuides(self, event):

        useAero = event.GetId() == ID_AeroGuides
        useWhidbey = event.GetId() == ID_WhidbeyGuides
        agwFlags = self._mgr.GetAGWFlags()

        if useAero:
            agwFlags ^= aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
        elif useWhidbey:
            agwFlags ^= aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
        else:
            agwFlags &= ~aui.AUI_MGR_AERO_DOCKING_GUIDES
            agwFlags &= ~aui.AUI_MGR_WHIDBEY_DOCKING_GUIDES

        self._mgr.SetAGWFlags(agwFlags)


    def OnNotebookPageClose(self, event):

        ctrl = event.GetEventObject()
        if isinstance(ctrl.GetPage(event.GetSelection()), wx.html.HtmlWindow):

            res = wx.MessageBox("Are you sure you want to close/hide this notebook page?",
                                "AUI", wx.YES_NO, self)
            if res != wx.YES:
                event.Veto()


    def OnAllowNotebookDnD(self, event):

        # for the purpose of this test application, explicitly
        # allow all noteboko drag and drop events
        event.Allow()


    def GetStartPosition(self):

        x = 20
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)


    def OnCreateTree(self, event):

        self._mgr.AddPane(self.CreateTreeCtrl(), aui.AuiPaneInfo().
                          Caption("Tree Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        self._mgr.Update()

    def OnCreate_AppDataTree(self, event=0):

        frame_title = "Loaded data files"

        treeCtrl = AppData_TreeCtrl(self)
        self._mgr.AddPane(treeCtrl, aui.AuiPaneInfo().
                          Caption(frame_title).
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))
        treeCtrl.populateTree(self._appDataRef)
        self._mgr.Update()

    def Create_DFtable(self, DFpanel, frame_title = "selected data file table"):
        """
        activated by an external CAppDataTree action
        """
        tblCtrl = DFpanel
        self._mgr.AddPane(tblCtrl, aui.AuiPaneInfo().
                          Caption(frame_title).
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(150, 300)).MinimizeButton(True))

        self._mgr.Update()
        
    def Create_Var_Plot(self, var):
        print ("called for variable named: "+str(var))
        pass

    def OnCreateRanTree(self, event=0, name="", caption="Ran Tree Control", update=True, option=2):

        if option==1:
            self._mgr.AddPane(self.CreateRan_TreeCtrl(),
                                aui.AuiPaneInfo().
                                Name(name).
                                Caption(caption).
                                MaximizeButton(True))
        else:
            self._mgr.AddPane(self.CreateRan_TreeCtrl(),
                                aui.AuiPaneInfo().
                                Caption(caption).
                                Float().FloatingPosition(self.GetStartPosition()).
                                FloatingSize(wx.Size(150, 400)).MinimizeButton(True))

        if update:
            self._mgr.Update()


    def OnCreateGrid(self, event):

        self._mgr.AddPane(self.CreateGrid(), aui.AuiPaneInfo().
                          Caption("Grid").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateHTML(self, event):

        self._mgr.AddPane(self.CreateHTMLCtrl(), aui.AuiPaneInfo().
                          Caption("HTML Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          FloatingSize(wx.Size(300, 200)).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateNotebook(self, event):

        self._mgr.AddPane(self.CreateNotebook(), aui.AuiPaneInfo().
                          Caption("Notebook").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnCreateText(self, event):

        self._mgr.AddPane(self.CreateTextCtrl(), aui.AuiPaneInfo().
                          Caption("Text Control").
                          Float().FloatingPosition(self.GetStartPosition()).
                          MinimizeButton(True))
        self._mgr.Update()


    def OnCreateSizeReport(self, event):

        self._mgr.AddPane(self.CreateSizeReportCtrl(), aui.AuiPaneInfo().
                          Caption("Client Size Reporter").
                          Float().FloatingPosition(self.GetStartPosition()).
                          CloseButton(True).MaximizeButton(True).MinimizeButton(True))
        self._mgr.Update()


    def OnChangeContentPane(self, event):

        self._mgr.GetPane("grid_content").Show(event.GetId() == ID_GridContent)
        self._mgr.GetPane("text_content").Show(event.GetId() == ID_TextContent)
        self._mgr.GetPane("tree_content").Show(event.GetId() == ID_TreeContent)
        self._mgr.GetPane("sizereport_content").Show(event.GetId() == ID_SizeReportContent)
        self._mgr.GetPane("html_content").Show(event.GetId() == ID_HTMLContent)
        self._mgr.GetPane("notebook_content").Show(event.GetId() == ID_NotebookContent)
        self._mgr.GetPane("DandD_content").Show(event.GetId() == ID_RanDDContent)   #ran
        self._mgr.Update()


    def OnVetoTree(self, event):

        self._veto_tree = event.IsChecked()


    def OnVetoText(self, event):

        self._veto_text = event.IsChecked()


    def OnRequestUserAttention(self, event):

        ids = event.GetId()
        if ids not in self._requestPanes:
            return

        paneName = self._requestPanes[ids]
        pane = self._mgr.GetPane(paneName)
        self._mgr.RequestUserAttention(pane.window)


    def OnDropDownToolbarItem(self, event):

        if event.IsDropDownClicked():

            tb = event.GetEventObject()
            tb.SetToolSticky(event.GetId(), True)

            # create the popup menu
            menuPopup = wx.Menu()
            bmp = wx.ArtProvider.GetBitmap(wx.ART_QUESTION, wx.ART_OTHER, wx.Size(16, 16))

            m1 =  wx.MenuItem(menuPopup, 10001, "Drop Down Item 1")
            m1.SetBitmap(bmp)
            menuPopup.Append(m1)

            m2 =  wx.MenuItem(menuPopup, 10002, "Drop Down Item 2")
            m2.SetBitmap(bmp)
            menuPopup.Append(m2)

            m3 =  wx.MenuItem(menuPopup, 10003, "Drop Down Item 3")
            m3.SetBitmap(bmp)
            menuPopup.Append(m3)

            m4 =  wx.MenuItem(menuPopup, 10004, "Drop Down Item 4")
            m4.SetBitmap(bmp)
            menuPopup.Append(m4)

            #todo: set bindings to those 'temporary' buttons, in order to meen somthing

            # line up our menu with the button
            rect = tb.GetToolRect(event.GetId())
            pt = tb.ClientToScreen(rect.GetBottomLeft())
            pt = self.ScreenToClient(pt)

            self.PopupMenu(menuPopup, pt)

            # make sure the button is "un-stuck"
            tb.SetToolSticky(event.GetId(), False)


    def OnTabAlignment(self, event):

        for pane in self._mgr.GetAllPanes():

            if isinstance(pane.window, aui.AuiNotebook):

                nb = pane.window
                style = nb.GetAGWWindowStyleFlag()

                if event.GetId() == ID_NotebookAlignTop:
                    style &= ~aui.AUI_NB_BOTTOM
                    style ^= aui.AUI_NB_TOP
                    nb.SetAGWWindowStyleFlag(style)
                elif event.GetId() == ID_NotebookAlignBottom:
                    style &= ~aui.AUI_NB_TOP
                    style ^= aui.AUI_NB_BOTTOM
                    nb.SetAGWWindowStyleFlag(style)

                self._notebook_style = style
                nb.Update()
                nb.Refresh()


    def OnCustomTabButtons(self, event):

        checked = event.IsChecked()
        self._custom_tab_buttons = checked
        auibook = self._mgr.GetPane("notebook_content").window

        left = CUSTOM_TAB_BUTTONS["Left"]
        for btn, ids in left:
            if checked:
                auibook.AddTabAreaButton(ids, wx.LEFT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        right = CUSTOM_TAB_BUTTONS["Right"]
        for btn, ids in right:
            if checked:
                auibook.AddTabAreaButton(ids, wx.RIGHT, btn.GetBitmap())
            else:
                auibook.RemoveTabAreaButton(ids)

        auibook.Refresh()
        auibook.Update()


    def OnMinMaxTabWidth(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        minTabWidth, maxTabWidth = auibook.GetMinMaxTabWidth()

        dlg = wx.TextEntryDialog(self, "Enter the minimum and maximum tab widths, separated by a comma:",
                                 "AuiNotebook Tab Widths")

        dlg.SetValue("%d,%d"%(minTabWidth, maxTabWidth))
        if dlg.ShowModal() != wx.ID_OK:
            return

        value = dlg.GetValue()
        dlg.Destroy()

        try:
            minTabWidth, maxTabWidth = value.split(",")
            minTabWidth, maxTabWidth = int(minTabWidth), int(maxTabWidth)
        except:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Tab widths should be' \
                                   ' 2 integers separated by a comma.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        if minTabWidth > maxTabWidth:
            dlg = wx.MessageDialog(self, 'Invalid minimum/maximum tab width. Minimum tab width' \
                                   ' should be less of equal than maximum tab width.',
                                   'Error',
                                   wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()
            return

        auibook.SetMinMaxTabWidth(minTabWidth, maxTabWidth)
        auibook.Refresh()
        auibook.Update()


    def OnPreview(self, event):

        auibook = self._mgr.GetPane("notebook_content").window
        auibook.NotebookPreview()


    def OnAddMultiLine(self, event):

        auibook = self._mgr.GetPane("notebook_content").window

        auibook.InsertPage(1, wx.TextCtrl(auibook, -1, "Some more text", wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_MULTILINE|wx.NO_BORDER), "Multi-Line\nTab Labels", True)

        auibook.SetPageTextColour(1, wx.BLUE)


    def OnFloatDock(self, event):

        paneLabel = event.pane.caption
        etype = event.GetEventType()

        strs = "Pane %s "%paneLabel
        if etype == aui.wxEVT_AUI_PANE_FLOATING:
            strs += "is about to be floated"

            if event.pane.name == "test8" and self._veto_tree:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_FLOATED:
            strs += "has been floated"
        elif etype == aui.wxEVT_AUI_PANE_DOCKING:
            strs += "is about to be docked"

            if event.pane.name == "test11" and self._veto_text:
                event.Veto()
                strs += "... Event vetoed by user selection!"
                self.log.write(strs + "\n")
                return

        elif etype == aui.wxEVT_AUI_PANE_DOCKED:
            strs += "has been docked"

        self.log.write(strs + "\n")


    def OnExit(self, event):
        """
        proper exiting is done only when choosing 'Exit' menu in the GUI
        """
        print  ("EXITING")
        self.Close(True)

    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        proper exiting and back to terminal
            is done only when choosing 'Exit' menu in the GUI
        """
        
        print  ("CLOSING")
        
        # ran
        prnt = self.GetParent()
        prnt2 = prnt.GetParent()    # 2 parents , because I know the creation of this 'self' was with panel parent and frame parent
        
        self.DestroyChildren()
        self.Destroy()

        prnt.Close(True)
        prnt.Destroy()
        
        prnt2.Close(True)
        prnt2.Destroy()

        print ("is OUT")

    def OnAbout(self, event):

        msg = "This Is The About Dialog Of The Pure Python Version Of AUI.\n\n" + \
              "Author: Andrea Gavana @ 23 Dec 2005\n\n" + \
              "Please Report Any Bug/Requests Of Improvements\n" + \
              "To Me At The Following Adresses:\n\n" + \
              "andrea.gavana@maerskoil.com\n" + "andrea.gavana@gmail.com\n\n" + \
              "Welcome To wxPython " + wx.VERSION_STRING + "!!"

        dlg = wx.MessageDialog(self, msg, "AUI Demo",
                               wx.OK | wx.ICON_INFORMATION)

        if wx.Platform != '__WXMAC__':
            try:
                #dlg.SetFont(wx.Font(8, wx.NORMAL, wx.NORMAL, wx.NORMAL, False))
#    				dlg.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, '', wx.FONTENCODING_DEFAULT))
                pass
            except: #ran
                pass

        dlg.ShowModal()
        dlg.Destroy()


    def CreateTextCtrl(self, ctrl_text=""):

        if ctrl_text.strip():
            text = ctrl_text
        else:
            text = "This is text box %d"%self._textCount
            self._textCount += 1

        return wx.TextCtrl(self,-1, text, wx.Point(0, 0), wx.Size(150, 90),
                           wx.NO_BORDER | wx.TE_MULTILINE)


    def CreateGrid(self):

        grid = wx.grid.Grid(self, -1, wx.Point(0, 0), wx.Size(150, 250),
                            wx.NO_BORDER | wx.WANTS_CHARS)
        grid.CreateGrid(50, 20)
        return grid


    def CreateTreeCtrl(self):

        tree = wx.TreeCtrl(self, -1, wx.Point(0, 0), wx.Size(160, 250),
                           wx.TR_DEFAULT_STYLE | wx.NO_BORDER)

        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16)))
        tree.AssignImageList(imglist)

        root = tree.AddRoot("AUI Project", 0)
        items = []

        #todo: how to do this with lambda instead?
        items.append(tree.AppendItem(root, "Item 1", 0))
        items.append(tree.AppendItem(root, "Item 2", 0))
        items.append(tree.AppendItem(root, "Item 3", 0))
        items.append(tree.AppendItem(root, "Item 4", 0))
        items.append(tree.AppendItem(root, "Item 5", 0))

        for ndx,item in enumerate(items):
            prefix = "#"+str(ndx)
            tree.AppendItem(item, prefix +" Subitem 1", 1)
            tree.AppendItem(item, "Subitem 2", 1)
            tree.AppendItem(item, "Subitem 3", 1)
            tree.AppendItem(item, "Subitem 4", 1)
            tree.AppendItem(item, "Subitem 5", 1)

        tree.Expand(root)

        return tree


    def CreateSizeReportCtrl(self, width=80, height=80):

        ctrl = SizeReportCtrl(self, -1, wx.DefaultPosition, wx.Size(width, height), self._mgr)
        return ctrl

    def CreateRan_DandDCtrl(self):
        # pnl = wx.Panel(self)
        # DD.TestPanel(pnl,log)
        # pnl.Show()
        # item1 = wx.DropTarget

        obj = DD.FileDropPanel(self, log, appDataObj)   # added extended header # todo: trim this pass by propagating events from DandD
        #todo: add button for 'back to previous or default layout'
                 #remove the text menu
        obj.Bind(wx.EVT_BUTTON, self.OnPaste)

        return obj
    def OnPaste(self):
        print("onPaste event reaction")

    def CreateRan_PanelCtrl(self):
        # frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
        # frame.Show(False)  # Show the frame.
        pnl = wx.Panel(self)

        ## ctrl = rNX.getMeFig()   #TODO: how to add fig to the panel
        # pnl.fig =

        zB.TestPanel(pnl, log)   #adding this example to the panel (panel type into panel parent)

        # DD.FileDropPanel(pnl,log)
        return pnl

    def CreateRan_TreeCtrl(self, file_name = "./specific_files/example.xml"):

        win = Xtr.XMLTree(self,-1)
        win.LoadTree(file_name)
        return  win

#######################

    def CreateHTMLCtrl(self, parent=None):

        if not parent:
            parent = self

        ctrl = wx.html.HtmlWindow(parent, -1, wx.DefaultPosition, wx.Size(400, 300))
        ctrl.SetPage(GetIntroText())
        return ctrl


    def CreateNotebook(self):
        """
        creates notebook of type AuiNotebook.
        sets the notebook tabs pages. 
        each is added by AddPage.
        """
        
        # create the notebook off-window to avoid flicker
        client_size = self.GetClientSize()
        ctrl = aui.AuiNotebook(self, -1, wx.Point(client_size.x, client_size.y),
                              wx.Size(430, 200), agwStyle=self._notebook_style)

        arts = [aui.AuiDefaultTabArt, aui.AuiSimpleTabArt, aui.VC71TabArt, aui.FF2TabArt,
                aui.VC8TabArt, aui.ChromeTabArt]

        art = arts[self._notebook_theme]()
        ctrl.SetArtProvider(art)

        page_bmp = wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16, 16))
        ctrl.AddPage(self.CreateHTMLCtrl(ctrl), "Welcome to AUI", False, page_bmp)

        panel = wx.Panel(ctrl, -1)
        flex = wx.FlexGridSizer(rows=0, cols=2, vgap=2, hgap=2)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.Add(wx.StaticText(panel, -1, "wxTextCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.TextCtrl(panel, -1, "", wx.DefaultPosition, wx.Size(100, -1)),
                 1, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.StaticText(panel, -1, "wxSpinCtrl:"), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add(wx.SpinCtrl(panel, -1, "5", wx.DefaultPosition, wx.Size(100, -1),
                             wx.SP_ARROW_KEYS, 5, 50, 5), 0, wx.ALL|wx.ALIGN_CENTRE, 5)
        flex.Add((5, 5))
        flex.Add((5, 5))
        flex.AddGrowableRow(0)
        flex.AddGrowableRow(3)
        flex.AddGrowableCol(1)
        panel.SetSizer(flex)
        ctrl.AddPage(panel, "Disabled-not", False, page_bmp)

        # Demonstrate how to disable a tab
#        ctrl.EnableTab(1, False)

        return ctrl


    def OnSwitchPane(self, event):

        items = ASD.SwitcherItems()
        items.SetRowCount(12)

        # Add the main windows and toolbars, in two separate columns
        # We'll use the item 'id' to store the notebook selection, or -1 if not a page

        for k in xrange(2):
            if k == 0:
                items.AddGroup(_("Main Windows"), "mainwindows")
            else:
                items.AddGroup(_("Toolbars"), "toolbars").BreakColumn()

            for pane in self._mgr.GetAllPanes():
                name = pane.name
                caption = pane.caption
                if not caption:
                    continue

                toolBar = isinstance(pane.window, wx.ToolBar) or isinstance(pane.window, aui.AuiToolBar)
                bitmap = (pane.icon.IsOk() and [pane.icon] or [wx.NullBitmap])[0]

                if (toolBar and k == 1) or (not toolBar and k == 0):
                    items.AddItem(caption, name, -1, bitmap).SetWindow(pane.window)

        # Now add the wxAuiNotebook pages
        items.AddGroup(_("Notebook Pages"), "pages").BreakColumn()

        for pane in self._mgr.GetAllPanes():
            nb = pane.window
            if isinstance(nb, aui.AuiNotebook):
                for j in xrange(nb.GetPageCount()):

                    name = nb.GetPageText(j)
                    win = nb.GetPage(j)

                    items.AddItem(name, name, j, nb.GetPageBitmap(j)).SetWindow(win)

        # Select the focused window

        idx = items.GetIndexForFocus()
        if idx != wx.NOT_FOUND:
            items.SetSelection(idx)

        if wx.Platform == "__WXMAC__":
            items.SetBackgroundColour(wx.WHITE)

        # Show the switcher dialog

        dlg = ASD.SwitcherDialog(items, self, self._mgr)

        # In GTK+ we can't use Ctrl+Tab; we use Ctrl+/ instead and tell the switcher
        # to treat / in the same was as tab (i.e. cycle through the names)

        if wx.Platform == "__WXGTK__":
            dlg.SetExtraNavigationKey('/')

        if wx.Platform == "__WXMAC__":
            dlg.SetBackgroundColour(wx.WHITE)
            dlg.SetModifierKey(wx.WXK_ALT)

        ans = dlg.ShowModal()

        if ans == wx.ID_OK and dlg.GetSelection() != -1:
            item = items.GetItem(dlg.GetSelection())

            if item.GetId() == -1:
                info = self._mgr.GetPane(item.GetName())
                info.Show()
                self._mgr.Update()
                info.window.SetFocus()

            else:
                nb = item.GetWindow().GetParent()
                win = item.GetWindow()
                if isinstance(nb, aui.AuiNotebook):
                    nb.SetSelection(item.GetId())
                    win.SetFocus()

#---------------------------------------------------------------------------

def alignToBottomRight(win):

    # posOffset = wx.Point(683, 384)
    posOffset = wx.Point(5 , 50)

    previousSize = win.GetPosition()
    dw, dh  = wx.DisplaySize()
    w, h    = win.GetSize()
    x = dw - w - posOffset.x
    y = dh - h - posOffset.y
    win.SetPosition((x, y))

def MainAUI(parent, log):

    frame = AuiFrame(parent, -1, "* Tailor *", size=(800, 600), log=log)
    # frame.CenterOnScreen()

    alignToBottomRight(frame)
    # desiredFramePos = wx.Point(683, 384)
    # desiredFramePos = wx.Point(2, 2)
    # previousSize = frame.GetPosition()
    # frame.SetPosition(desiredFramePos)

    frame.Show()

overview = GetIntroText()

class Log:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)
    write = WriteText

if __name__ == '__main__':
    # import sys,os
    # import run
    # run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
    app   = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = wx.Frame(None, wx.ID_ANY, "initial wxFrame")  # A Frame is a top-level window.
    frame.Show(False)  # Show the frame.
    pnl   = wx.Panel(frame)
    log   = Log()

    appDataObj  = appDB.myAppData()
    appDataObj.initializeDataFields()
    # print appDataObj.mainDict
    # print appDataObj.lastPastedText
    # print appDataObj.lastPastedUrl

    win         = MainAUI(pnl, log)
    app.MainLoop()

    # appDataObj
    # pass
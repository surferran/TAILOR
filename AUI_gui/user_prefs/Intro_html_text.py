
def GetIntroText():

    text = \
    "<html><body>" \
    "<h3>Welcome to AUI</h3>" \
    "<br/><b>Overview</b><br/>" \
    "<p>AUI is an Advanced User Interface library for the wxPython toolkit " \
    "that allows developers to create high-quality, cross-platform user " \
    "interfaces quickly and easily.</p>" \
    "<p><b>Features</b></p>" \
    "<p>With AUI, developers can create application frameworks with:</p>" \
    "<ul>" \
    "<li>Native, dockable floating frames</li>" \
    "<li>Perspective saving and loading</li>" \
    "<li>Native toolbars incorporating real-time, 'spring-loaded' dragging</li>" \
    "<li>Customizable floating/docking behavior</li>" \
    "<li>Completely customizable look-and-feel</li>" \
    "<li>Optional transparent window effects (while dragging or docking)</li>" \
    "<li>Splittable notebook control</li>" \
    "</ul>" \
    "<p><b>What's new in AUI?</b></p>" \
    "<p>Current wxAUI Version Tracked: wxWidgets 2.9.4 (SVN HEAD)" \
    "<p>The wxPython AUI version fixes the following bugs or implement the following" \
    " missing features (the list is not exhaustive): " \
    "<p><ul>" \
    "<li>Visual Studio 2005 style docking: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=596'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=596</a></li>" \
    "<li>Dock and Pane Resizing: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=582'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=582</a></li> " \
    "<li>Patch concerning dock resizing: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=610'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=610</a></li> " \
    "<li>Patch to effect wxAuiToolBar orientation switch: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=641'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=641</a></li> " \
    "<li>AUI: Core dump when loading a perspective in wxGTK (MSW OK): <a href='http://www.kirix.com/forums/viewtopic.php?f=15&t=627</li>'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=15&t=627</li></a>" \
    "<li>wxAuiNotebook reordered AdvanceSelection(): <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=617'>"\
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=617</a></li> " \
    "<li>Vertical Toolbar Docking Issue: <a href='http://www.kirix.com/forums/viewtopic.php?f=16&t=181'>" \
    "http://www.kirix.com/forums/viewtopic.php?f=16&t=181</a></li> " \
    "<li>Patch to show the resize hint on mouse-down in aui: <a href='http://trac.wxwidgets.org/ticket/9612'>" \
    "http://trac.wxwidgets.org/ticket/9612</a></li> " \
    "<li>The Left/Right and Top/Bottom Docks over draw each other: <a href='http://trac.wxwidgets.org/ticket/3516'>" \
    "http://trac.wxwidgets.org/ticket/3516</a></li>" \
    "<li>MinSize() not honoured: <a href='http://trac.wxwidgets.org/ticket/3562'>" \
    "http://trac.wxwidgets.org/ticket/3562</a></li> " \
    "<li>Layout problem with wxAUI: <a href='http://trac.wxwidgets.org/ticket/3597'>" \
    "http://trac.wxwidgets.org/ticket/3597</a></li>" \
    "<li>Resizing children ignores current window size: <a href='http://trac.wxwidgets.org/ticket/3908'>" \
    "http://trac.wxwidgets.org/ticket/3908</a></li> " \
    "<li>Resizing panes under Vista does not repaint background: <a href='http://trac.wxwidgets.org/ticket/4325'>" \
    "http://trac.wxwidgets.org/ticket/4325</a></li> " \
    "<li>Resize sash resizes in response to click: <a href='http://trac.wxwidgets.org/ticket/4547'>" \
    "http://trac.wxwidgets.org/ticket/4547</a></li> " \
    "<li>'Illegal' resizing of the AuiPane? (wxPython): <a href='http://trac.wxwidgets.org/ticket/4599'>" \
    "http://trac.wxwidgets.org/ticket/4599</a></li> " \
    "<li>Floating wxAUIPane Resize Event doesn't update its position: <a href='http://trac.wxwidgets.org/ticket/9773'>" \
    "http://trac.wxwidgets.org/ticket/9773</a></li>" \
    "<li>Don't hide floating panels when we maximize some other panel: <a href='http://trac.wxwidgets.org/ticket/4066'>"\
    "http://trac.wxwidgets.org/ticket/4066</a></li>" \
    "<li>wxAUINotebook incorrect ALLOW_ACTIVE_PANE handling: <a href='http://trac.wxwidgets.org/ticket/4361'>" \
    "http://trac.wxwidgets.org/ticket/4361</a></li> " \
    "<li>Page changing veto doesn't work, (patch supplied): <a href='http://trac.wxwidgets.org/ticket/4518'>" \
    "http://trac.wxwidgets.org/ticket/4518</a></li> " \
    "<li>Show and DoShow are mixed around in wxAuiMDIChildFrame: <a href='http://trac.wxwidgets.org/ticket/4567'>"\
    "http://trac.wxwidgets.org/ticket/4567</a></li> " \
    "<li>wxAuiManager & wxToolBar - ToolBar Of Size Zero: <a href='http://trac.wxwidgets.org/ticket/9724'>" \
    "http://trac.wxwidgets.org/ticket/9724</a></li> " \
    "<li>wxAuiNotebook doesn't behave properly like a container as far as...: <a href='http://trac.wxwidgets.org/ticket/9911'>" \
    "http://trac.wxwidgets.org/ticket/9911</a></li>" \
    "<li>Serious layout bugs in wxAUI: <a href='http://trac.wxwidgets.org/ticket/10620'>" \
    "http://trac.wxwidgets.org/ticket/10620</a></li>" \
    "<li>wAuiDefaultTabArt::Clone() should just use copy contructor: <a href='http://trac.wxwidgets.org/ticket/11388'>" \
    "http://trac.wxwidgets.org/ticket/11388</a></li>" \
    "<li>Drop down button for check tool on wxAuiToolbar: <a href='http://trac.wxwidgets.org/ticket/11139'>" \
    "http://trac.wxwidgets.org/ticket/11139</a></li>" \
    "<li>Rename a wxAuiNotebook tab with double-click: <a href='http://trac.wxwidgets.org/ticket/10847'>" \
    "http://trac.wxwidgets.org/ticket/10847</a></li>" \
    "</ul>" \
    "<p>Plus the following features:" \
    "<p><ul>" \
    "<li><b>AuiManager:</b></li>" \
    "<ul>" \
    "<li>Implementation of a simple minimize pane system: Clicking on this minimize button causes a new " \
    "<i>AuiToolBar</i> to be created and added to the frame manager, (currently the implementation is such " \
    "that panes at West will have a toolbar at the right, panes at South will have toolbars at the " \
    "bottom etc...) and the pane is hidden in the manager. " \
    "Clicking on the restore button on the newly created toolbar will result in the toolbar being " \
    "removed and the original pane being restored;</li>" \
    "<li>Panes can be docked on top of each other to form <i>AuiNotebooks</i>; <i>AuiNotebooks</i> tabs can be torn " \
    "off to create floating panes;</li>" \
    "<li>On Windows XP, use the nice sash drawing provided by XP while dragging the sash;</li>" \
    "<li>Possibility to set an icon on docked panes;</li>" \
    "<li>Possibility to draw a sash visual grip, for enhanced visualization of sashes;</li>" \
    "<li>Implementation of a native docking art (<i>ModernDockArt</i>). Windows XP only, <b>requires</b> Mark Hammond's " \
    "pywin32 package (winxptheme);</li>" \
    "<li>Possibility to set a transparency for floating panes (a la Paint .NET);</li>" \
    "<li>Snapping the main frame to the screen in any positin specified by horizontal and vertical " \
    "alignments;</li>" \
    "<li>Snapping floating panes on left/right/top/bottom or any combination of directions, a la Winamp;</li>" \
    "<li>'Fly-out' floating panes, i.e. panes which show themselves only when the mouse hover them;</li>" \
    "<li>Ability to set custom bitmaps for pane buttons (close, maximize, etc...);</li>" \
    "<li>Implementation of the style <tt>AUI_MGR_ANIMATE_FRAMES</tt>, which fade-out floating panes when " \
    "they are closed (all platforms which support frames transparency) and show a moving rectangle " \
    "when they are docked and minimized (Windows excluding Vista and GTK only);</li>" \
    "<li>A pane switcher dialog is available to cycle through existing AUI panes; </li>" \
    "<li>Some flags which allow to choose the orientation and the position of the minimized panes;</li>" \
    "<li>The functions <i>[Get]MinimizeMode()</i> in <i>AuiPaneInfo</i> which allow to set/get the flags described above;</li>" \
    "<li>Events like <tt>EVT_AUI_PANE_DOCKING</tt>, <tt>EVT_AUI_PANE_DOCKED</tt>, <tt>EVT_AUI_PANE_FLOATING</tt> "\
    "and <tt>EVT_AUI_PANE_FLOATED</tt> are "\
    "available for all panes <b>except</b> toolbar panes;</li>" \
    "<li>Implementation of the <i>RequestUserAttention</i> method for panes;</li>" \
    "<li>Ability to show the caption bar of docked panes on the left instead of on the top (with caption " \
    "text rotated by 90 degrees then). This is similar to what <i>wxDockIt</i> did. To enable this feature on any " \
    "given pane, simply call <i>CaptionVisible(True, left=True)</i>;</li>" \
    "<li>New Aero-style docking guides: you can enable them by using the <i>AuiManager</i> style <tt>AUI_MGR_AERO_DOCKING_GUIDES</tt>;</li>" \
    "<li>New Whidbey-style docking guides: you can enable them by using the <i>AuiManager</i> style <tt>AUI_MGR_WHIDBEY_DOCKING_GUIDES</tt>;</li>" \
    "<li>A slide-in/slide-out preview of minimized panes can be seen by enabling the <i>AuiManager</i> style" \
    "<tt>AUI_MGR_PREVIEW_MINIMIZED_PANES</tt> and by hovering with the mouse on the minimized pane toolbar tool;</li>" \
    "<li>Native of custom-drawn mini frames can be used as floating panes, depending on the <tt>AUI_MGR_USE_NATIVE_MINIFRAMES</tt> style;</li>" \
    "<li>A 'smooth docking effect' can be obtained by using the <tt>AUI_MGR_SMOOTH_DOCKING</tt> style (similar to PyQT docking style);</li>" \
    '<li>Implementation of "Movable" panes, i.e. a pane that is set as `Movable()` but not `Floatable()` can be dragged and docked into a new location but will not form a floating window in between.</li>' \
    "</ul><p>" \
    "<li><b>AuiNotebook:</b></li>" \
    "<ul>" \
    "<li>Implementation of the style <tt>AUI_NB_HIDE_ON_SINGLE_TAB</tt>, a la <i>wx.lib.agw.flatnotebook</i>;</li>" \
    "<li>Implementation of the style <tt>AUI_NB_SMART_TABS</tt>, a la <i>wx.lib.agw.flatnotebook</i>;</li>" \
    "<li>Implementation of the style <tt>AUI_NB_USE_IMAGES_DROPDOWN</tt>, which allows to show tab images " \
    "on the tab dropdown menu instead of bare check menu items (a la <i>wx.lib.agw.flatnotebook</i>);</li>" \
    "<li>6 different tab arts are available, namely:</li>" \
    "<ul>" \
    "<li>Default 'glossy' theme (as in <i>wx.aui.AuiNotebook</i>)</li>" \
    "<li>Simple theme (as in <i>wx.aui.AuiNotebook</i>)</li>" \
    "<li>Firefox 2 theme</li>" \
    "<li>Visual Studio 2003 theme (VC71)</li>" \
    "<li>Visual Studio 2005 theme (VC81)</li>" \
    "<li>Google Chrome theme</li>" \
    "</ul>" \
    "<li>Enabling/disabling tabs;</li>" \
    "<li>Setting the colour of the tab's text; </li>" \
    "<li>Implementation of the style <tt>AUI_NB_CLOSE_ON_TAB_LEFT</tt>, which draws the tab close button on " \
    "the left instead of on the right (a la Camino browser); </li>" \
    "<li>Ability to save and load perspectives in <i>wx.aui.AuiNotebook</i> (experimental); </li>" \
    "<li>Possibility to add custom buttons in the <i>wx.aui.AuiNotebook</i> tab area; </li>" \
    "<li>Implementation of the style <tt>AUI_NB_TAB_FLOAT</tt>, which allows the floating of single tabs. " \
    "<b>Known limitation:</b> when the notebook is more or less full screen, tabs cannot be dragged far " \
    "enough outside of the notebook to become floating pages. </li>" \
    "<li>Implementation of the style <tt>AUI_NB_DRAW_DND_TAB</tt> (on by default), which draws an image " \
    "representation of a tab while dragging;</li>" \
    "<li>Implementation of the <i>AuiNotebook</i> unsplit functionality, which unsplit a splitted AuiNotebook " \
    "when double-clicking on a sash (Use <i>SetSashDClickUnsplit</i>);</li>" \
    "<li>Possibility to hide all the tabs by calling <i>HideAllTAbs</i>;</li>" \
    "<li>wxPython controls can now be added inside page tabs by calling <i>AddControlToPage</i>, and they can be " \
    "removed by calling <i>RemoveControlFromPage</i>;</li>" \
    "<li>Possibility to preview all the pages in a <i>AuiNotebook</i> (as thumbnails) by using the <i>NotebookPreview</i> " \
    "method of <i>AuiNotebook</i></li>;" \
    "<li>Tab labels can be edited by calling the <i>SetRenamable</i> method on a <i>AuiNotebook</i> page;</li>" \
    "<li>Support for multi-lines tab labels in <i>AuiNotebook</i>;</li>" \
    "<li>Support for setting minimum and maximum tab widths for fixed width tabs;</li>"\
    "<li>Implementation of the style <tt>AUI_NB_ORDER_BY_ACCESS</tt>, which orders the tabs by last access time inside the "\
    "<i>Tab Navigator</i> dialog</li>;" \
    "<li>Implementation of the style <tt>AUI_NB_NO_TAB_FOCUS</tt>, allowing the developer not to draw the tab " \
    "focus rectangle on tne <i>AuiNotebook</i> tabs.</li>"\
    "</ul><p>" \
    "<li><b>AuiToolBar:</b></li>" \
    "<ul>" \
    "<li><tt>AUI_TB_PLAIN_BACKGROUND</tt> style that allows to easy setup a plain background to the AUI toolbar, " \
    "without the need to override drawing methods. This style contrasts with the default behaviour " \
    "of the <i>wx.aui.AuiToolBar</i> that draws a background gradient and this break the window design when " \
    "putting it within a control that has margin between the borders and the toolbar (example: put " \
    "<i>wx.aui.AuiToolBar</i> within a <i>wx.StaticBoxSizer</i> that has a plain background);</li>" \
    "<li><i>AuiToolBar</i> allow item alignment: <a href='http://trac.wxwidgets.org/ticket/10174'> " \
    "http://trac.wxwidgets.org/ticket/10174</a>;</li>" \
    "<li><i>AUIToolBar</i> <i>DrawButton()</i> improvement: <a href='http://trac.wxwidgets.org/ticket/10303'>" \
    "http://trac.wxwidgets.org/ticket/10303</a>;</li>" \
    "<li><i>AuiToolBar</i> automatically assign new id for tools: <a href='http://trac.wxwidgets.org/ticket/10173'>" \
    "http://trac.wxwidgets.org/ticket/10173</a>;</li>" \
    "<li><i>AuiToolBar</i> Allow right-click on any kind of button: <a href='http://trac.wxwidgets.org/ticket/10079'>" \
    "http://trac.wxwidgets.org/ticket/10079</a>;</li>" \
    "<li><i>AuiToolBar</i> idle update only when visible: <a href='http://trac.wxwidgets.org/ticket/10075'>" \
    "http://trac.wxwidgets.org/ticket/10075</a>;</li>" \
    "<li>Ability of creating <i>AuiToolBar</i> tools with [counter]clockwise rotation. This allows to propose a " \
    "variant of the minimizing functionality with a rotated button which keeps the caption of the pane as label;</li>" \
    "<li>Allow setting the alignment of all tools in a toolbar that is expanded.</li>" \
    "<li>Implementation of the <tt>AUI_MINIMIZE_POS_TOOLBAR</tt> flag, which allows to minimize a pane inside " \
     "an existing toolbar. Limitation: if the minimized icon in the toolbar ends up in the overflowing " \
     "items (i.e., a menu is needed to show the icon), this style will not work.</li>" \
    "</ul>" \
    "</ul><p>" \
    "<p>" \
    "</body></html>"

    return text


"""
ref by
https://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/
http://code.activestate.com/recipes/475155-dynamic-system-tray-icon-wxpython/

"""

import wx
print wx.__version__
from wx import adv
import os,  subprocess

TRAY_TOOLTIP    = ' -- application MyLauncher -- '  #"restore"
TRAY_ICON       = '.\IMAGES\wx.ico'
TRAY_ICONs      = [TRAY_ICON , '.\IMAGES/4x4.png']


def create_menu_item(menu, label, func, icon_ndx=0):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    item.SetBitmap(wx.Bitmap(TRAY_ICONs[icon_ndx]))
    menu.Append(item)
    return item

########################################################################
class CustomTaskBarIcon(wx.adv.TaskBarIcon):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame

        img = wx.Image(TRAY_ICON,   wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(bmp)   # = wx.IconFromBitmap(wx.Bitmap(path))
 
        self.SetIcon(self.icon, TRAY_TOOLTIP)

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
#        self.Bind(wx.EVT_CHAR_HOOK, self.func_call_2)
#        self.Bind(wx.EVT_HOTKEY, self.func_call_2)
        
 
    #----------------------------------------------------------------------

    def CreatePopupMenu(self):
        menu = wx.Menu()

        item1 = create_menu_item(menu, 'Say func1', self.func_call_1 , icon_ndx=1)
        item1 = create_menu_item(menu, 'Say func2', self.func_call_1 , icon_ndx=1)
        menu.AppendSeparator()
        item2 = create_menu_item(menu, 'Exit', self.func_call_exit, icon_ndx=0)

        # items = [item1, item2]
        # for item in items:
        #     self.bindEvents(item)

        return menu

    def bindEvents(self, item):
        """"""
        item.Bind(wx.EVT_BUTTON, self.onButton)
        # sizer.Add(btn, 0, wx.ALL, 5)

    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        button = event.GetEventObject()
        print "The button you pressed was labeled: " + button.GetLabel()
        print "The button's name is " + button.GetName()

        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print "The button you pressed was labeled: " + button_by_id.GetLabel()
        print "The button's name is " + button_by_id.GetName()

    def OnTaskBarActivate(self, evt):
        """"""
        print "ACTIVATED"
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        print "CLOSING"
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        print 'Tray icon was left-clicked.'
        if __name__ != '__main__':
            tmp = self.frame.ribbon_link.Shown
            self.frame.ribbon_link.Show(not(tmp))
        #TODO: set this icon tray. to be shown. not hidden with other win sys tray icons
        self.frame.Show()
        self.frame.Restore()

    def func_call_1(self, event):
        print "func1 entered"

        self.ShowBalloon('balllllooon','texttt')

        tmp = event.GetEventObject()
        # print "The button you pressed was labeled: " + tmp.GetLabel()
        # print "The button's name is " + tmp.GetName()

        tmp_id = event.GetId()
        # tmp_by_id = self.FindWindowById(tmp_id)
        # print "The button you pressed was labeled: " + tmp_by_id.GetLabel()
        # print "The button's name is " + tmp_by_id.GetName()

        os.startfile('notepad++')
        # # or
        # pdf = "path/to/pdf"
        # acrobatPath = r'C:\Program Files\Adobe\Reader 9.0\Reader\AcroRd32.exe'
        # subprocess.Popen("%s %s" % (acrobatPath, pdf))

    def func_call_2(self, event):
        print "func2 entered"
        pass
    
    def func_call_exit(self, event):
        print "pressed exit"
        # wx.CallAfter(self.Destroy)
        
#        self is 'CustomTaskBarIcon' object
        
        if __name__ != '__main__':
            self.Close(True)
            self.frame.Close()
#        
#        self.DestroyChildren()
        
        self.RemoveIcon()
        self.Destroy()
        self.frame.Destroy()
        
        print ("is OUT")
        
  

##
# The task bar application
#
class TaskBarApp(wx.Frame):

    ##
    # \brief the constructor
    #
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, -1, title, size = (1, 1),
            style=wx.FRAME_NO_TASKBAR|wx.NO_FULL_REPAINT_ON_RESIZE)

        self.tbicon = CustomTaskBarIcon(self)
#        self.tbicon.SetIconTimer()

        self.Show(True)

##
# The main application wx.App class
#
class MyApp(wx.App):
    def OnInit(self):
        frame = TaskBarApp(None, -1, ' ')
        frame.Center(wx.BOTH)
        frame.Show(False)
        return True

def main(argv=None):
    app = MyApp(0)
    app.MainLoop()

if __name__ == '__main__':
    main()
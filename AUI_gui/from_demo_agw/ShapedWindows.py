
import  wx
import  images

__doc__=\
"""
Top level windows now have a SetShape method that lets you set a
non-rectangular shape for the window using a wxRegion.  All pixels
outside of the region will not be drawn and the window will not be
sensitive to the mouse in those areas either.
"""
#----------------------------------------------------------------------

class ShapedWindowByImage(wx.Frame):
    def __init__(self, parent, imageFileName="", launchFunction=None, initialLocation=(0,0) ):
        wx.Frame.__init__(self, parent, -1, "Shaped Window",
                         style =
                           wx.FRAME_SHAPED
                         | wx.SIMPLE_BORDER
                         | wx.FRAME_NO_TASKBAR
                         | wx.STAY_ON_TOP
                         )

        self.hasShape       = False
        self.delta          = (0,0)        # delta from previous location

        self.winFunction    = launchFunction

        self.Bind(wx.EVT_LEFT_DCLICK,   self.OnDoubleClick)
        self.Bind(wx.EVT_LEFT_DOWN,     self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,       self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,        self.OnMouseMove)
        self.Bind(wx.EVT_PAINT,         self.OnPaint)
        self.Bind(wx.EVT_RIGHT_UP,      self.OnExit)

        img         = wx.Image(imageFileName, wx.BITMAP_TYPE_ANY) # wx._core.image return type
        self.bmp    = img.ConvertToBitmap()    # keeping the alpha ??
        # self.bmp = images.Vippi.GetBitmap() #bitmap type
        w, h        = self.bmp.GetWidth(), self.bmp.GetHeight()
        self.SetClientSize( (w, h) )

        self.SetToolTip("Right-click to close the window\n"
                        "Double-click the image to set/unset the window shape")

        if wx.Platform == "__WXGTK__":
            # wxGTK requires that the window be created before you can set its shape,
            # so delay the call to SetWindowShape until this event.
            self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        else:
            # On wxMSW and wxMac the window has already been created, so go for it.
            self.SetWindowShape()

        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)
        self.Move(initialLocation)

    def SetWindowShape(self, *evt):
        # Use the bitmap's mask to determine the region
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def OnDoubleClick(self, evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape = False
        else:
            self.SetWindowShape()

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp, 0,0, True)      # coordinates relative to window

    def OnExit(self, evt):
        self.Close()
        #TODO: set this correctly to finish closing the app . verify if activated by 'main'

    def OnLeftDown(self, evt):
        self.CaptureMouse()
        x, y = self.ClientToScreen(evt.GetPosition())
        originx, originy = self.GetPosition()
        dx = x - originx
        dy = y - originy
        self.delta = ((dx, dy))

    def OnLeftUp(self, evt):
        if self.HasCapture():
            self.ReleaseMouse()
        if self.winFunction!=None:
            self.winFunction("dummyTestUrl\n")

    def OnMouseMove(self, evt):
        if evt.Dragging() and evt.LeftIsDown():
            x, y = self.ClientToScreen(evt.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

def addUrlToLinksList(linkText):
    if __name__=='__main__':
        fileLoc = "..//user_prefs//userUrLinks.txt"
    else:
        fileLoc = ".//user_prefs//userUrLinks.txt"
    with open(fileLoc,'a') as f:
        f.write(linkText)
    #TODO: close icon window(s) after the action (when operated by external parent program)

if __name__ == '__main__':

    app     = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame   = wx.Frame(None, wx.ID_ANY, "Hello Shapes World")  # A Frame is a top-level window.
    frame.Show(False)  # Show the frame.
    pnl     = wx.Panel(frame)

    iconNames       = ["help", "smfuel","checked"]   # todo - get from os list or user json file
    functionsToLaunch = [addUrlToLinksList, None, None, None]
    # functionToLaunch = [addUrlToLinksList]
    # avgLoc = (600,400)
    avgLoc          = (1200, 600)
    deltaLoc        = [(50,00),(00,50) ,(0,-50) ,(-50,00)  ]
    winLocations    = [ (x+avgLoc[0],y+avgLoc[1]) for (x,y) in deltaLoc]

    for icon,func,loc in zip(iconNames, functionsToLaunch, winLocations):
        iName = "bitmaps/" + icon + ".ico"
        win = ShapedWindowByImage(pnl, imageFileName = iName, launchFunction = func, initialLocation=loc)
        win.Show(True)

    app.MainLoop()

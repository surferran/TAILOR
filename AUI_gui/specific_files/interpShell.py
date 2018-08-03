import wx
import wx.stc as stc
import code
import sys

print ( "entered interpShell as : " + __name__)

# other posiible usage (but very simple and not flexible) :
#   x = code.InteractiveConsole()
#   x.interact("A kind of Python interpreter")

class II(code.InteractiveInterpreter):
    def __init__(self, locals):
        code.InteractiveInterpreter.__init__(self, locals)
    def Runit(self, cmd):
        code.InteractiveInterpreter.runsource(self, cmd)
    def openInteract(self):
        code.interact(banner="Welcome to Python\n")

class PySTC(stc.StyledTextCtrl):
    def __init__(self, parent, ID, pos=(10,10), size=(700, 600), style=0):
        stc.StyledTextCtrl.__init__(self, parent, ID, pos, size, style)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        self.cmd     = ''
        self.lastpos = self.GetCurrentPos()
        # sys.stdout = self
        # sys.stderr = self
    def SetInter(self, interpreter):
        self.inter = interpreter
    def write(self, ln):
        # self.AppendTextUTF8('%s'%str(ln))
        self.GotoLine(self.GetLineCount())
    def OnKeyPressed(self, event):
        self.changed = True
        char = event.GetKeyCode() # get code of keypress
        if (self.GetCurrentPos() < self.lastpos) and (char <314) or (char > 317):
            # need to check for arrow keys in this
            pass
        elif char == 13:
            """
            What to do if <enter> is pressed? It depends if
            there are enough
            instructions
            """
            lnNo        = self.GetCurrentLine()
            ln          = self.GetLine(lnNo)
            self.cmd    = self.cmd + ln + '\r\n'
            self.NewLine()
            self.tabs   = ln.count('\t') #9
            if (ln.strip() == '') or ((self.tabs < 1) and (':' not in ln)):
                # record command in command list
                self.cmd = self.cmd.replace('\r\n','\n')
                if self.cmd == "resetSTD\n":
                    sys.stdout = sys.__stdout__
                    sys.stderr = sys.__stderr__
                    self.f.close()
                elif self.cmd == "STDtoFile\n":
                    # ref https://www.blog.pythonlibrary.org/2016/06/16/python-101-redirecting-stdout/
                    print ("redirecting to file")
                    self.f = open('stdFlie.txt', 'w')
                    sys.stdout = self.f
                    sys.stderr = self.f
                else:
                    # run command now
                    print('*' * 40)
                    print ("'" + self.cmd.replace("\n","") + "'" +" eval output is : \n")
                    self.inter.Runit(self.cmd)
                    print('*' * 40)
                self.cmd = ''
                self.lastpos = self.GetCurrentPos()
                # try:
                #     sys.stderr.flush()
                #     sys.stdout.flush()
                # except :
                #     print ("flush exception")
                #     pass
            else:
                if ':' in ln:
                    self.tabs = self.tabs + 1
                self.AppendText('\t' * self.tabs)
                # change cursor position now
                p = self.GetLineIndentPosition(lnNo + 1)
                self.GotoPos(p)
        else:
           event.Skip() # ensure keypress is shown

################################################################

class ecpintframe(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["size"] = (700,600)
        wx.Frame.__init__(self, *args, **kwds)
        self.ed = PySTC(self, -1)

if __name__ == '__main__':
    print ("activated by 3 : " + __name__)
    Ecpint = wx.PySimpleApp(0)
    class Strct():
        a='a'
        b={}
    strct = Strct()
    strct.b = {'a':1,'b':12}
    passedLocals = {"__name__": "__RanConsole__", \
                    "__doc__" : "None docs will be populated by ran",\
                    "varA"    : strct}
    I = II(passedLocals)
    # I.openInteract()
    win = ecpintframe(None, -1, "EcPint - Interactive interpreter")
    win.Show()
    win.ed.SetInter(I)
    Ecpint.MainLoop()

    print (passedLocals)
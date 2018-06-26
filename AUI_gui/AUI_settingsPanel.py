
from AUI_Agw import *

#todo: consider seperating this class. it depends on the controls IDs.
class SettingsPanel(wx.Panel):

    def __init__(self, parent, frame):

        wx.Panel.__init__(self, parent)
        self._frame = frame

        s1 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_size = wx.SpinCtrl(self, ID_PaneBorderSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE),
                                        wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100,
                                        frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.Add(wx.StaticText(self, -1, "Pane Border Size:"))
        s1.Add(self._border_size)
        s1.Add((1, 1), 1, wx.EXPAND)
        s1.SetItemMinSize(1, (180, 20))

        s2 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_size = wx.SpinCtrl(self, ID_SashSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE), wx.DefaultPosition,
                                      wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.Add(wx.StaticText(self, -1, "Sash Size:"))
        s2.Add(self._sash_size)
        s2.Add((1, 1), 1, wx.EXPAND)
        s2.SetItemMinSize(1, (180, 20))

        s3 = wx.BoxSizer(wx.HORIZONTAL)
        self._caption_size = wx.SpinCtrl(self, ID_CaptionSize, "%d"%frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE),
                                         wx.DefaultPosition, wx.Size(50, 20), wx.SP_ARROW_KEYS, 0, 100, frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.Add(wx.StaticText(self, -1, "Caption Size:"))
        s3.Add(self._caption_size)
        s3.Add((1, 1), 1, wx.EXPAND)
        s3.SetItemMinSize(1, (180, 20))

        b = self.CreateColourBitmap(wx.BLACK)

        s4 = wx.BoxSizer(wx.HORIZONTAL)
        self._background_colour = wx.BitmapButton(self, ID_BackgroundColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.Add(wx.StaticText(self, -1, "Background Colour:"))
        s4.Add(self._background_colour)
        s4.Add((1, 1), 1, wx.EXPAND)
        s4.SetItemMinSize(1, (180, 20))

        s5 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_colour = wx.BitmapButton(self, ID_SashColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.Add(wx.StaticText(self, -1, "Sash Colour:"))
        s5.Add(self._sash_colour)
        s5.Add((1, 1), 1, wx.EXPAND)
        s5.SetItemMinSize(1, (180, 20))

        s6 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_colour = wx.BitmapButton(self, ID_InactiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.Add(wx.StaticText(self, -1, "Normal Caption:"))
        s6.Add(self._inactive_caption_colour)
        s6.Add((1, 1), 1, wx.EXPAND)
        s6.SetItemMinSize(1, (180, 20))

        s7 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_gradient_colour = wx.BitmapButton(self, ID_InactiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.Add(wx.StaticText(self, -1, "Normal Caption Gradient:"))
        s7.Add(self._inactive_caption_gradient_colour)
        s7.Add((1, 1), 1, wx.EXPAND)
        s7.SetItemMinSize(1, (180, 20))

        s8 = wx.BoxSizer(wx.HORIZONTAL)
        self._inactive_caption_text_colour = wx.BitmapButton(self, ID_InactiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.Add(wx.StaticText(self, -1, "Normal Caption Text:"))
        s8.Add(self._inactive_caption_text_colour)
        s8.Add((1, 1), 1, wx.EXPAND)
        s8.SetItemMinSize(1, (180, 20))

        s9 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_colour = wx.BitmapButton(self, ID_ActiveCaptionColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.Add(wx.StaticText(self, -1, "Active Caption:"))
        s9.Add(self._active_caption_colour)
        s9.Add((1, 1), 1, wx.EXPAND)
        s9.SetItemMinSize(1, (180, 20))

        s10 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_gradient_colour = wx.BitmapButton(self, ID_ActiveCaptionGradientColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.Add(wx.StaticText(self, -1, "Active Caption Gradient:"))
        s10.Add(self._active_caption_gradient_colour)
        s10.Add((1, 1), 1, wx.EXPAND)
        s10.SetItemMinSize(1, (180, 20))

        s11 = wx.BoxSizer(wx.HORIZONTAL)
        self._active_caption_text_colour = wx.BitmapButton(self, ID_ActiveCaptionTextColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.Add(wx.StaticText(self, -1, "Active Caption Text:"))
        s11.Add(self._active_caption_text_colour)
        s11.Add((1, 1), 1, wx.EXPAND)
        s11.SetItemMinSize(1, (180, 20))

        s12 = wx.BoxSizer(wx.HORIZONTAL)
        self._border_colour = wx.BitmapButton(self, ID_BorderColour, b, wx.DefaultPosition, wx.Size(50, 25))
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.Add(wx.StaticText(self, -1, "Border Colour:"))
        s12.Add(self._border_colour)
        s12.Add((1, 1), 1, wx.EXPAND)
        s12.SetItemMinSize(1, (180, 20))

        s13 = wx.BoxSizer(wx.HORIZONTAL)
        self._gripper_colour = wx.BitmapButton(self, ID_GripperColour, b, wx.DefaultPosition, wx.Size(50,25))
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.Add(wx.StaticText(self, -1, "Gripper Colour:"))
        s13.Add(self._gripper_colour)
        s13.Add((1, 1), 1, wx.EXPAND)
        s13.SetItemMinSize(1, (180, 20))

        s14 = wx.BoxSizer(wx.HORIZONTAL)
        self._sash_grip = wx.CheckBox(self, ID_SashGrip, "", wx.DefaultPosition, wx.Size(50,20))
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.Add(wx.StaticText(self, -1, "Draw Sash Grip:"))
        s14.Add(self._sash_grip)
        s14.Add((1, 1), 1, wx.EXPAND)
        s14.SetItemMinSize(1, (180, 20))

        s15 = wx.BoxSizer(wx.HORIZONTAL)
        self._hint_colour = wx.BitmapButton(self, ID_HintColour, b, wx.DefaultPosition, wx.Size(50,25))
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.Add(wx.StaticText(self, -1, "Hint Window Colour:"))
        s15.Add(self._hint_colour)
        s15.Add((1, 1), 1, wx.EXPAND)
        s15.SetItemMinSize(1, (180, 20))

        grid_sizer = wx.GridSizer(rows=0, cols=2, vgap=5, hgap=5)
        grid_sizer.SetHGap(5)
        grid_sizer.Add(s1)
        grid_sizer.Add(s4)
        grid_sizer.Add(s2)
        grid_sizer.Add(s5)
        grid_sizer.Add(s3)
        grid_sizer.Add(s13)
        grid_sizer.Add(s14)
        grid_sizer.Add((1, 1))
        grid_sizer.Add(s12)
        grid_sizer.Add(s6)
        grid_sizer.Add(s9)
        grid_sizer.Add(s7)
        grid_sizer.Add(s10)
        grid_sizer.Add(s8)
        grid_sizer.Add(s11)
        grid_sizer.Add(s15)

        cont_sizer = wx.BoxSizer(wx.VERTICAL)
        cont_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(cont_sizer)
        self.GetSizer().SetSizeHints(self)

        self._border_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE))
        self._sash_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_SASH_SIZE))
        self._caption_size.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_CAPTION_SIZE))
        self._sash_grip.SetValue(frame.GetDockArt().GetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP))

        self.UpdateColours()

        self.Bind(wx.EVT_SPINCTRL, self.OnPaneBorderSize, id=ID_PaneBorderSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnSashSize, id=ID_SashSize)
        self.Bind(wx.EVT_SPINCTRL, self.OnCaptionSize, id=ID_CaptionSize)
        self.Bind(wx.EVT_CHECKBOX, self.OnDrawSashGrip, id=ID_SashGrip)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BackgroundColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_SashColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_InactiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionGradientColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_ActiveCaptionTextColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_BorderColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_GripperColour)
        self.Bind(wx.EVT_BUTTON, self.OnSetColour, id=ID_HintColour)


    def CreateColourBitmap(self, c):

        image = wx.Image(25, 14)
        for x in xrange(25):
            for y in xrange(14):
                pixcol = c
                if x == 0 or x == 24 or y == 0 or y == 13:
                    pixcol = wx.BLACK

                # image.SetRGB(x, y, pixcol.Red(), pixcol.Green(), pixcol.Blue())
                image.SetRGB(wx.Rect(wx.Size(25, 14)), pixcol.Red(), pixcol.Green(), pixcol.Blue())

        return image.ConvertToBitmap()


    def UpdateColours(self):

        bk = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BACKGROUND_COLOUR)
        self._background_colour.SetBitmapLabel(self.CreateColourBitmap(bk))

        cap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR)
        self._inactive_caption_colour.SetBitmapLabel(self.CreateColourBitmap(cap))

        capgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR)
        self._inactive_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(capgrad))

        captxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR)
        self._inactive_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(captxt))

        acap = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR)
        self._active_caption_colour.SetBitmapLabel(self.CreateColourBitmap(acap))

        acapgrad = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR)
        self._active_caption_gradient_colour.SetBitmapLabel(self.CreateColourBitmap(acapgrad))

        acaptxt = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR)
        self._active_caption_text_colour.SetBitmapLabel(self.CreateColourBitmap(acaptxt))

        sash = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_SASH_COLOUR)
        self._sash_colour.SetBitmapLabel(self.CreateColourBitmap(sash))

        border = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_BORDER_COLOUR)
        self._border_colour.SetBitmapLabel(self.CreateColourBitmap(border))

        gripper = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_GRIPPER_COLOUR)
        self._gripper_colour.SetBitmapLabel(self.CreateColourBitmap(gripper))

        hint = self._frame.GetDockArt().GetColour(aui.AUI_DOCKART_HINT_WINDOW_COLOUR)
        self._hint_colour.SetBitmapLabel(self.CreateColourBitmap(hint))


    def OnPaneBorderSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_PANE_BORDER_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSashSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_SASH_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnCaptionSize(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_CAPTION_SIZE,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnDrawSashGrip(self, event):

        self._frame.GetDockArt().SetMetric(aui.AUI_DOCKART_DRAW_SASH_GRIP,
                                           event.GetInt())
        self._frame.DoUpdate()


    def OnSetColour(self, event):

        dlg = wx.ColourDialog(self._frame)
        dlg.SetTitle("Colour Picker")

        if dlg.ShowModal() != wx.ID_OK:
            return

        evId = event.GetId()
        if evId == ID_BackgroundColour:
            var = aui.AUI_DOCKART_BACKGROUND_COLOUR
        elif evId == ID_SashColour:
            var = aui.AUI_DOCKART_SASH_COLOUR
        elif evId == ID_InactiveCaptionColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_COLOUR
        elif evId == ID_InactiveCaptionGradientColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_InactiveCaptionTextColour:
            var = aui.AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_ActiveCaptionColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_COLOUR
        elif evId == ID_ActiveCaptionGradientColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR
        elif evId == ID_ActiveCaptionTextColour:
            var = aui.AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR
        elif evId == ID_BorderColour:
            var = aui.AUI_DOCKART_BORDER_COLOUR
        elif evId == ID_GripperColour:
            var = aui.AUI_DOCKART_GRIPPER_COLOUR
        elif evId == ID_HintColour:
            var = aui.AUI_DOCKART_HINT_WINDOW_COLOUR
        else:
            return

        self._frame.GetDockArt().SetColour(var, dlg.GetColourData().GetColour())
        self._frame.DoUpdate()
        self.UpdateColours()

########################################################################

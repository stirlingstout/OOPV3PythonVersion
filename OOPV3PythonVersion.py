import wx

from typing import List, Callable


class OOPDraw(wx.Frame):
    """ OOPDraw is a subclass of wx.Frame which contains all the wx.Windows (labels, comboboxes and
    panel on which graphic elements are drawn """

    def __init__(self):
        def AddChoice(panel: wx.Panel, vBox: wx.BoxSizer, label: str, y: int, options: List[str], handler: Callable):
            vBox.Add(wx.StaticText(panel, wx.ID_ANY, label))
            cb = wx.ComboBox(panel, wx.ID_ANY, options[0], choices=options)
            cb.Bind(wx.EVT_COMBOBOX, handler, cb)
            vBox.Add(cb)       
           
        wx.Frame.__init__(self, None, wx.ID_ANY, 'OOPDraw in Python', size=(800, 600))
        self.SetSize(0, 0, 800, 600)

        # panel contains all the controls (label + combobox for each option)
        panel = wx.Panel(self, wx.ID_ANY)
        # vBox is responsible for sizing all the controls and placing them within panel
        vBox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vBox)

        #AddChoice(panel, vBox, "Line width:", 0, ["Thin", "Medium", "Thick"], self.OnLineWidthChanged)
        #AddChoice(panel, vBox, "Colour:", 30, ["Red", "Green", "Blue"], self.OnColourChanged)
        #AddChoice(panel, vBox, "Shape:", 60, ["Line", "Rectangle", "Ellipse", "Circle"] , self.OnShapeChanged)
        #AddChoice(panel, vBox, "Action:", 90, ["Draw", "Select", "Duplicate", "Move", "Group"] , self.OnActionChanged)

        # hBox is responsible for sizing the panel for controls and the panel for drawing on (canvas)
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(hBox)
        hBox.Add(panel, 0, wx.EXPAND)
        self.canvas = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.canvas, 1, wx.EXPAND)

        self.canvas.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Buffer = wx.Bitmap(self.canvas.GetSize())

    def OnLineWidthChanged(self, e: wx.Event):
        pass

    def OnColourChanged(self, e: wx.Event):
        pass

    def OnShapeChanged(self, e: wx.Event):
        pass

    def OnActionChanged(self, e: wx.Event):
        pass

    def OnPaint(self, event=None):
        pass

if __name__ == '__main__':
    app = wx.App()
    frame = OOPDraw()

    frame.Show()

    app.MainLoop()


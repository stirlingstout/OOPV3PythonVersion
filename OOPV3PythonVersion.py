import wx

from typing import List, Callable

# Page 15 exercise start
from Line import Line
# Page 15 exercise end

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
        self.Canvas = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.Canvas, 1, wx.EXPAND)

        # Page 6 changes start 
        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)
       
        wx.Window.SetDoubleBuffered(self, True)
        self.CurrentPen = wx.Pen(wx.BLACK)
        # Page 6 changes end

        # Page 9 changes start
        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.dragging = False
        self.startOfDrag = wx.Point()
        self.lastMousePosition = wx.Point()
        self.Lines = []

    # These events could be deleted and the user asked to put them in
    #def OnLineWidthChanged(self: wx.Frame, e: wx.Event):
    #    pass

    #def OnColourChanged(self: wx.Frame, e: wx.Event):
    #    pass

    #def OnShapeChanged(self: wx.Frame, e: wx.Event):
    #    pass

    #def OnActionChanged(self: wx.Frame, e: wx.Event):
    #    pass

    def OnPaint(self: wx.Frame, e: wx.Event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        # Page 15 exercise start
        for line in self.Lines:
            line.Draw(dc)
        # Page 15 exercise end

    # Page 9 changes start
    def OnMouseDown(self: wx.Window, e: wx.MouseEvent):
        self.dragging = True
        self.startOfDrag = lastMousePosition = e.GetPosition()
        # Page 15 exercise start
        self.Lines.append(Line(self.CurrentPen, e.GetPosition().x, e.GetPosition().y));
        # Page 15 exercise end
        e.Skip()

    def OnMouseUp(self: wx.Window, e: wx.MouseEvent):
        self.dragging = False

    def OnMouseMove(self: wx.Window, e: wx.MouseEvent):
        if self.dragging:
            # Page 15 exercise start
            currentLine = self.Lines[-1]
            currentLine.GrowTo(e.GetPosition().x, e.GetPosition().y)
            # Page 15 exercise end
            self.lastMousePosition = e.GetPosition()
            self.Refresh()
    # Page 9 changes end


if __name__ == '__main__':
    app = wx.App()
    frame = OOPDraw()

    frame.Show()

    app.MainLoop()


import wx

from typing import List, Callable

from Line import Line
from Rectangle import Rectangle

from Shape import Shape

class OOPDraw(wx.Frame):
    """ OOPDraw is a subclass of wx.Frame which contains all the wx.Windows (labels, comboboxes and
    panel on which graphic elements are drawn """

    def __init__(self):
        def AddChoice(panel: wx.Panel, vBox: wx.BoxSizer, name: str, label: str, y: int, options: List[str], handler: Callable):
            vBox.Add(wx.StaticText(panel, wx.ID_ANY, label))
            cb = wx.ComboBox(panel, wx.ID_ANY, options[0], choices=options, name=name)
            cb.Bind(wx.EVT_TEXT, handler, cb)
            vBox.Add(cb)       
           
        wx.Frame.__init__(self, None, wx.ID_ANY, 'OOPDraw in Python', size=(800, 600))
        self.Size = (0, 0, 800, 600)

        # panel contains all the controls (label + combobox for each option)
        panel = wx.Panel(self, wx.ID_ANY)
        # vBox is responsible for sizing all the controls and placing them within panel
        vBox = wx.BoxSizer(wx.VERTICAL)
        panel.Sizer = vBox

        AddChoice(panel, vBox, "LineWidth", "Line width:", 0, ["Thin", "Medium", "Thick"], self.OnLineWidthChanged)
        AddChoice(panel, vBox, "Colour", "Colour:", 30, ["Red", "Green", "Blue"], self.OnColourChanged)
        AddChoice(panel, vBox, "Shape", "Shape:", 60, ["Line", "Rectangle", "Ellipse", "Circle"] , self.OnShapeChanged)
        #AddChoice(panel, vBox, "Action:", 90, ["Draw", "Select", "Duplicate", "Move", "Group"] , self.OnActionChanged)

        # hBox is responsible for sizing the panel for controls and the panel for drawing on (canvas)
        hBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer = hBox
        hBox.Add(panel, 0, wx.EXPAND)
        self.Canvas = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.Canvas, 1, wx.EXPAND)

        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)
       
        self.DoubleBuffered = True 
        self.CurrentPen = wx.Pen(wx.BLACK)
        self.CurrentBrush = wx.Brush(wx.BLACK, style=wx.BRUSHSTYLE_TRANSPARENT)

        self.FindWindow("LineWidth").Value = "Medium"
        self.FindWindow("Colour").Value = "Green"
        self.FindWindow("Shape").Value = "Line"

        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.dragging = False
        self.startOfDrag = wx.Point()
        self.lastMousePosition = wx.Point()
        self.Shapes = []
       
    # These events could be deleted and the user asked to put them in
    def OnLineWidthChanged(self: wx.Frame, e: wx.Event):
        width = self.CurrentPen.Width
        if e.String == "Thin":
            width = 2
        elif e.String == "Medium":
            width = 4
        elif e.String == "Thick":
            width = 8
        self.CurrentPen = wx.Pen(self.CurrentPen.Colour, width)

    def OnColourChanged(self: wx.Frame, e: wx.Event):
        colour = self.CurrentPen.Colour
        if e.String == "Red":
            colour = wx.RED
        elif e.String == "Green":
            colour = wx.GREEN
        elif e.String == "Blue":
            colour = wx.BLUE
        self.CurrentPen = wx.Pen(colour, self.CurrentPen.Width)

    def OnShapeChanged(self: wx.Frame, e: wx.Event):
        pass

    #def OnActionChanged(self: wx.Frame, e: wx.Event):
    #    pass

    def OnPaint(self: wx.Frame, e: wx.Event):
        dc = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        dc.Brush = self.CurrentBrush
        for shape in self.Shapes:
            shape.Draw(dc)

    def OnMouseDown(self: wx.Window, e: wx.MouseEvent):
        self.dragging = True
        self.startOfDrag = lastMousePosition = e.Position
        if self.FindWindow("Shape").Value == "Line":
            self.Shapes.append(Line(self.CurrentPen, e.Position.x, e.Position.y));
        elif self.FindWindow("Shape").Value == "Rectangle":
            self.Shapes.append(Rectangle(self.CurrentPen, e.Position.x, e.Position.y))
        e.Skip()

    def OnMouseUp(self: wx.Window, e: wx.MouseEvent):
        self.dragging = False

    def OnMouseMove(self: wx.Window, e: wx.MouseEvent):
        if self.dragging:
            currentLine = self.Shapes[-1]
            currentLine.GrowTo(e.Position.x, e.Position.y)
            self.lastMousePosition = e.Position
            self.Refresh()


if __name__ == '__main__':
    app = wx.App()
    frame = OOPDraw()

    frame.Show()

    app.MainLoop()


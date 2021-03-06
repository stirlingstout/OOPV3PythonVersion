import wx # type: ignore

from typing import List, Callable, Optional

#from shape import Shape

from classes.circle import Circle
from classes.shape import Shape
from classes.line import Line
from classes.rectangle import Rectangle
from classes.ellipse import Ellipse
from classes.composite_shape import CompositeShape


class OOPDrawIntermediate(wx.Frame):
    """ OOPDrawIntermediate is a subclass of wx.Frame which contains all the wx.Windows (labels, comboboxes and
    panel on which graphic elements are drawn. It's used as a stepping stone to the ful OOPDraw package """

    def __init__(self):
        def AddChoice(panel: wx.Panel, vBox: wx.BoxSizer, name: str, label: str, y: int, options: List[str], handler: Callable):
            vBox.AddSpacer(10)

            hBox: wx.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
            hBox.AddSpacer(10)
            hBox.Add(wx.StaticText(panel, wx.ID_ANY, label))
            vBox.Add(hBox)

            hBox = wx.BoxSizer(wx.HORIZONTAL)
            cb: wx.ComboBox = wx.ComboBox(panel, wx.ID_ANY, options[0], choices=options, style=wx.CB_READONLY, name=name)
            cb.Bind(wx.EVT_COMBOBOX, handler, cb)

            hBox.AddSpacer(10)
            hBox.Add(cb)
            hBox.AddSpacer(10)

            vBox.Add(hBox)
           
        wx.Frame.__init__(self, None, wx.ID_ANY, 'OOPDraw in Python', size=(800, 600))
        self.Size = (0, 0, 800, 600)

        # panel contains all the controls (label + combobox for each option)
        panel: wx.Panel = wx.Panel(self, wx.ID_ANY)
        # vBox is responsible for sizing all the controls and placing them within panel
        vBox: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
        panel.Sizer = vBox

        AddChoice(panel, vBox, "LineWidth", "Line width:", 0, ["Thin", "Medium", "Thick"], self.OnLineWidthChanged)
        AddChoice(panel, vBox, "Colour", "Colour:", 30, ["Red", "Green", "Blue"], self.OnColourChanged)
        AddChoice(panel, vBox, "Shape", "Shape:", 60, ["Line", "Rectangle", "Ellipse", "Circle"] , self.OnShapeChanged)
        AddChoice(panel, vBox, "Action", "Action:", 90, ["Draw", "Select", "Duplicate", "Move", "Group", "Delete"] , self.OnActionChanged)

        # hBox is responsible for sizing the panel for controls and the panel for drawing on (canvas)
        hBox: wx.BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Sizer = hBox
        hBox.Add(panel, 0, wx.EXPAND)
        hBox.AddSpacer(10)
        self.Canvas: wx.Panel = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE, name="Canvas")
        hBox.Add(self.Canvas, 1, wx.EXPAND)

        self.Canvas.Bind(wx.EVT_PAINT, self.OnPaint)
       
        self.Canvas.SetDoubleBuffered(True) 
        panel.SetDoubleBuffered(True)
        self.CurrentPen: wx.Pen = wx.Pen(wx.GREEN, 4)
        self.CurrentBrush: wx.Brush = wx.Brush(wx.BLACK, style=wx.BRUSHSTYLE_TRANSPARENT)

        self.FindWindow("LineWidth").Value = "Medium"
        self.FindWindow("Colour").Value = "Green"
        self.FindWindow("Shape").Value = "Line"
        # These don't raise EVT_COMBOBOX

        self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
        self.Canvas.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
        self.Canvas.Bind(wx.EVT_MOTION, self.OnMouseMove)


class OOPDraw(OOPDrawIntermediate):
    def __init__(self):
        OOPDrawIntermediate.__init__(self)

        self.dragging: bool = False
        self.startOfDrag: wx.Point = wx.Point()
        self.lastMousePosition: wx.Point = wx.Point()
        self.Shapes: List[Shape] = []

        self.SelectionBox: Rectangle = None
       
    # These events could be deleted and the user asked to put them in
    def OnLineWidthChanged(self: wx.Frame, e: wx.Event):
        width: int = self.CurrentPen.Width
        if e.String == "Thin":
            width = 2
        elif e.String == "Medium":
            width = 4
        elif e.String == "Thick":
            width = 8
        self.CurrentPen = wx.Pen(self.CurrentPen.Colour, width)

    def OnColourChanged(self: wx.Frame, e: wx.Event):
        colour: wx.Colour = self.CurrentPen.Colour
        if e.String == "Red":
            colour = wx.RED
        elif e.String == "Green":
            colour = wx.GREEN
        elif e.String == "Blue":
            colour = wx.BLUE
        self.CurrentPen = wx.Pen(colour, self.CurrentPen.Width)

    def OnShapeChanged(self: wx.Frame, e: wx.Event):
        pass

    def OnActionChanged(self: wx.Frame, e: wx.Event):
        action: str = self.FindWindow("Action").Value
        if action == "Group":
            self.GroupSelectedShapes()
        elif action == "Delete":
            self.DeleteSelectedShapes()
        elif action == "Duplicate":
            self.DuplicateSelectedShapes()
            self.Refresh()

    def OnPaint(self: wx.Frame, e: wx.Event):
        dc: wx.DC = wx.BufferedPaintDC(self.Canvas)
        dc.Clear()
        dc.Brush = self.CurrentBrush
        for shape in self.Shapes:
            shape.Draw(dc)
        if self.SelectionBox:
            self.SelectionBox.Draw(dc)

    def AddShape(self, e: wx.MouseEvent):
        shapeName: str = self.FindWindow("Shape").Value
        if shapeName == "Line":
            self.Shapes.append(Line(self.CurrentPen, e.Position.x, e.Position.y));
        elif shapeName == "Rectangle":
            self.Shapes.append(Rectangle(self.CurrentPen, e.Position.x, e.Position.y))
        elif shapeName == "Ellipse":
            self.Shapes.append(Ellipse(self.CurrentPen, e.Position.x, e.Position.y))
        elif shapeName == "Circle":
            self.Shapes.append(Circle(self.CurrentPen, e.Position.x, e.Position.y))

    def OnMouseDown(self: wx.Frame, e: wx.MouseEvent):
        self.dragging = True
        self.startOfDrag = self.lastMousePosition = e.Position
        action: str = self.FindWindow("Action").Value
        if action == "Draw":
            self.AddShape(e)
        elif action == "Select":
            p = wx.Pen(wx.BLACK, 1)
            self.SelectionBox = Rectangle(p, self.startOfDrag.x, self.startOfDrag.y)

        # debug: print(f"{type(self.Shapes[-1])}Circle({self.Shapes[-1].X1()}, {self.Shapes[-1].Y1()})-({self.Shapes[-1].X2()}, {self.Shapes[-1].Y2()})")
        e.Skip()

    def OnMouseUp(self: wx.Frame, e: wx.MouseEvent):
        self.dragging = False
        self.lastMousePosition = wx.Point()
        self.SelectionBox = None
        self.Refresh()

    def OnMouseMove(self: wx.Frame, e: wx.MouseEvent):
        if self.dragging:
            action: str = self.FindWindow("Action").Value
            if action == "Move":
                self.MoveSelectedShapes(e)
            elif action == "Draw":
                currentShape: Shape = self.Shapes[-1]
                currentShape.GrowTo(e.Position.x, e.Position.y)
            elif action == "Select":
                self.SelectionBox.GrowTo(e.X,e.Y)
                self.SelectShapes()

            # debug: print(f"{type(currentShape)}({currentShape.X1()}, {currentShape.Y1()})-({currentShape.X2()}, {currentShape.Y2()})")
            self.lastMousePosition = e.Position
            self.Refresh()

    def DeselectAll(self):
        for shape in self.Shapes:
            shape.Deselect()

    def SelectShapes(self):
        self.DeselectAll()
        for s in self.Shapes:
            if self.SelectionBox.FullySurrounds(s):
                s.Select()

    def GetSelectedShapes(self) -> List[Shape]:
        return list(filter(lambda s: s.Selected(), self.Shapes))

    def MoveSelectedShapes(self, e: wx.MouseEvent):
        for s in self.GetSelectedShapes():
            s.MoveBy(e.Position.x - self.lastMousePosition.x, e.Position.y - self.lastMousePosition.y)

    def GroupSelectedShapes(self):
        members = list(self.GetSelectedShapes())
        if len(members) >= 2:
            composite = CompositeShape(members)
            composite.Select()
            self.Shapes.append(composite)
            for m in members:
                self.Shapes.remove(m)
                m.Deselect()
            self.Refresh()

    def DeleteSelectedShapes(self):
        for s in self.GetSelectedShapes():
            self.Shapes.remove(s)
        self.Refresh()

    def DuplicateSelectedShapes(self):
        duplicates = []
        for s in self.GetSelectedShapes():
            duplicates.append(s.Clone())
            s.Deselect()
        for s in duplicates:
            self.Shapes.append(s)
            s.MoveBy(50, 50)
            s.Select()
        

if __name__ == '__main__':
    app = wx.App()

    frame = OOPDraw()
    frame.Show()

    app.MainLoop()


import wx # type: ignore

from typing import List

from shape import Shape

class CompositeShape(Shape):
    """I represent a composite shape in the OOPDraw system,
    holding a collection of the shapes that I consiste of."""
    def __init__(self, components: List[Shape]):
        Shape.__init__(self, wx.Pen(wx.BLACK, 1), 0, 0, 0, 0)
        self._Shape__Pen.DashStyle = wx.PENSTYLE_SHORT_DASH
        self.__Components = components
        self.CalculateEnclosingRectangle()

    def CalculateEnclosingRectangle(self):
        # Note that min(self.Components(), lambda c: min(c.X1(), c.X2())) etc doesn't
        #   work here since it returns the c that gives the minimum, not the minimum
        #   of that c
        self._Shape__X1 = min([min(c.X1(), c.X2()) for c in self.Components()])
        self._Shape__Y1 = min([min(c.Y1(), c.Y2()) for c in self.Components()])
        self._Shape__X2 = max([max(c.X1(), c.X2()) for c in self.Components()])
        self._Shape__Y2 = max([max(c.Y1(), c.Y2()) for c in self.Components()])
        
    def Draw(self, dc: wx.DC):
        for shape in self.Components():
            shape.Draw(dc)
        if self.Selected():
            dc.Pen = self.Pen()
            dc.DrawRectangle(self.X1(), self.Y1(), self.X2() - self.X1(), self.Y2() - self.Y1())

    def MoveBy(self, xDelta: int, yDelta: int):
        for shape in self.Components():
            shape.MoveBy(xDelta, yDelta)
        self.CalculateEnclosingRectangle()

    def Components(self) -> List[Shape]:
        return self.__Components

    def Clone(self) -> Shape:
        members: List[Shape] = []
        for shape in self.Components():
            members.append(shape.Clone())
        return CompositeShape(members)

import wx # type: ignore

from typing import List

from shape import Shape

class CompositeShape(Shape):
    """I represent a composite shape in the OOPDraw system,
    holding a collection of the shapes that I consiste of."""
    def __init__(self, components: List[Shape]):
        Shape.__init__(self, wx.Pen(wx.BLACK, 1), 0, 0, 0, 0)
        self._Shape__Pen.DashStyle = wx.PENSTYLE_SHORT_DASH
        self.Components = components
        self.CalculateEnclosingRectangle()

    def CalculateEnclosingRectangle(self):
        self._Shape__X1 = min(self.Components, key=lambda c: min(c.X1(), c.X2()))
        self._Shape__Y1 = min(self.Components, key=lambda c: min(c.Y1(), c.Y2()))
        self._Shape__X1 = max(self.Components, key=lambda c: max(c.X1(), c.X2()))
        self._Shape__X1 = max(self.Components, key=lambda c: max(c.Y1(), c.Y2()))

    def Draw(self, dc: wx.DC):
        for shape in self.Components:
            shape.Draw(dc)
        if self.Selected():
            dc.DrawRectangle(self.Pen(), self.X1(), self.Y1(), self.X2() - self.X1(), self.Y2() - self.Y1)

    def MoveBy(self, xDelta: int, yDelta: int):
        for shape in self.Components:
            shape.MoveBy(xDelta, yDelta)
        self._Shape__X1 += xDelta
        self._Shape__Y1 += yDelta
        self._Shape__X2 += xDelta
        self._Shape__Y2 += yDelta



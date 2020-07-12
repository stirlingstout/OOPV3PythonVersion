from typing import Optional

import wx # type: ignore

from shape import Shape

from drawing_functions import DrawingFunctions

class Circle(Shape):
    """I represent a circle in the OOPDraw system"""

    def __init__(self, p: wx.Pen, x1: int, y1: int, x2: Optional[int]=None, y2: Optional[int]=None):
        Shape.__init__(self, p, x1, y1, x2, y2)
        self.GrowTo(self.X2(), self.Y2())

    def Draw(self, dc: wx.DC):
        DrawingFunctions.DrawClosedArc(dc, self)

    def GrowTo(self, x2: int, y2: int):
        diameter: int = max(x2 - self.X1(), y2 - self.Y1())
        self._Shape__X2 = self.X1() + diameter
        self._Shape__Y2 = self.Y1() + diameter

    def Clone(self) -> Shape:
        return Circle(self.Pen(), self.X1(), self.Y1(), self.X2(), self.Y2())

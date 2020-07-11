from typing import Optional
import wx

from Shape import Shape

class Circle(Shape):
    """I represent a circle in the OOPDraw system"""

    def __init__(self, p: wx.Pen, x1: int, y1: int, x2: Optional[int]=None, y2: Optional[int]=None):
        Shape.__init__(self, p, x1, y1, x2, y2)
        self.GrowTo(self.X2(), self.Y2())

    def Draw(self, dc: wx.DC):
        x: int = min([self.X1(), self.X2()])
        y: int = min([self.Y1(), self.Y2()])
        w: int = max([self.X1(), self.X2()]) - x
        h: int = max([self.Y1(), self.Y2()]) - y
        r: int = w // 2
        dc.Pen = self.Pen()
        dc.DrawCircle(x + r, y + r, r)

    def GrowTo(self, x2: int, y2: int):
        diameter: int = max([x2 - self.X1(), y2 - self.Y1()])
        self._Shape__X2 = self.X1() + diameter
        self._Shape__Y2 = self.Y1() + diameter

import wx # type: ignore

from classes.shape import Shape


class Line(Shape):
    """I represent a line in the OOPDraw program. I have a
    Pen, and the start and end points of the line I represent.
    The end point can be changed using my GrowTo method"""
 
    def Draw(self, dc: wx.DC):
        dc.Pen = self.Pen()
        dc.DrawLine(self.X1(), self.Y1(), self.X2(), self.Y2())

    def Clone(self) -> Shape:
        return Line(self.Pen(), self.X1(), self.Y1(), self.X2(), self.Y2())


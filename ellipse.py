import wx

from Shape import Shape


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        x: int = min([self.X1(), self.X2()])
        y: int = min([self.Y1(), self.Y2()])

        w: int = max([self.X1(), self.X2()]) - x
        h: int = max([self.Y1(), self.Y2()]) - y

        dc.Pen = self.Pen()
        dc.DrawEllipse(x, y, w, h)


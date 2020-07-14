import wx # type: ignore

from classes import shape, drawing_functions

#from drawing_functions import DrawingFunctions


class Ellipse(shape.Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        drawing_functions.DrawingFunctions.DrawClosedArc(dc, self)

    def Clone(self) -> shape.Shape:
        return Ellipse(self.Pen(), self.X1(), self.Y1(), self.X2(), self.Y2())


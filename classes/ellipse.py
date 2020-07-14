import wx # type: ignore

from classes.shape import Shape
from classes.drawing_functions import DrawingFunctions

#from drawing_functions import DrawingFunctions


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        DrawingFunctions.DrawClosedArc(dc, self)

    def Clone(self) -> Shape:
        return Ellipse(self.Pen(), self.X1(), self.Y1(), self.X2(), self.Y2())


import wx # type: ignore

from Shape import Shape

from drawing_functions import DrawingFunctions


class Ellipse(Shape):
    """I represent an ellipse in the OOPDraw system"""

    def Draw(self, dc: wx.DC):
        DrawingFunctions.DrawClosedArc(dc, self)


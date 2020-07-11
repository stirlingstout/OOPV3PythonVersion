import wx # type: ignore

from Shape import Shape

class DrawingFunctions(object):
    """I contain helper functions for OOPDraw. Note that
    there are no self parameters since these are static 
    functions"""

    def DrawClosedArc(dc: wx.DC, shape: Shape):
        (x, y, w, h) = shape.EnclosingRectangle()
        dc.Pen = shape.Pen()
        dc.DrawEllipticArc(x, y, w, h, 0, 360)

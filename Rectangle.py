import wx # type: ignore

from Shape import Shape

class Rectangle(Shape):
    """I represent a rectangle in the OOPDraw program. I have a
    Pen, and the start and end points of my top left and bottom 
    corners of the rectangle.
    My size can be changed using my GrowTo method"""

    def Draw(self, dc: wx.DC):
        (x, y, w, h) = self.EnclosingRectangle()
        dc.Pen = self.Pen()
        dc.DrawRectangle(x, y, w, h)





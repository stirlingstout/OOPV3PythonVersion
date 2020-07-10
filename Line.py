import wx

from Shape import Shape

class Line():
    """I represent a line in the OOPDraw program. I have a
    Pen, and the start and end points of the line I represent.
    The end point can be changed using my GrowTo method"""

    def __init__(self, p: wx.Pen, x1: int, y1: int, x2: int=None, y2: int=None):
        self.__Pen = p
        self.__X1 = x1
        self.__Y1 = y1
        self.__X2 = x2 if x2 else x1
        self.__Y2 = y2 if y2 else y1
        
    def Pen(self):
        return self.__Pen

    def X1(self):
        return self.__X1

    def Y1(self):
        return self.__Y1

    def X2(self):
        return self.__X2

    def Y2(self):
        return self.__Y2
 
    def Draw(self, dc: wx.DC):
        dc.SetPen(self.__Pen)
        dc.DrawLine(self.__X1, self.__Y1, self.__X2, self.__Y2)
 
    def GrowTo(self, x2: int, y2: int):
        self.__X2 = x2
        self.__Y2 = y2


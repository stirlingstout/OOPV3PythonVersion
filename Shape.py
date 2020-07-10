from abc import ABC, abstractmethod
import wx

class Shape(ABC):
    """I define members common to all the shapes that
    will be used in OOPDraw. I can't be instantiated
    myself since I'm abstract"""

    #@abstractmethod
    def Draw(self, dc: wx.DC):
        pass

    @abstractmethod
    def GrowTo(x2: int, y2: int):
        pass



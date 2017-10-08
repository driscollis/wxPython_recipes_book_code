import sys
import wx

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Image Extractor')

        self.panel = wx.Panel(self)

        loc = wx.IconLocation(sys.executable, 0)
        self.SetIcon(wx.Icon(loc))


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyForm().Show()
    app.MainLoop()
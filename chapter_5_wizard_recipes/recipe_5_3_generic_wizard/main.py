import wx

class WizardPage(wx.Panel):
    """A Simple wizard page"""

    def __init__(self, parent, title=None):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        if title:
            title = wx.StaticText(self, -1, title)
            title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
            sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)


class WizardPanel(wx.Panel):
    """"""
 
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.pages = []
        self.page_num = 0
 
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.panelSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        # add prev/next buttons
        self.prevBtn = wx.Button(self, label="Previous")
        self.prevBtn.Bind(wx.EVT_BUTTON, self.onPrev)
        btnSizer.Add(self.prevBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        self.nextBtn = wx.Button(self, label="Next")
        self.nextBtn.Bind(wx.EVT_BUTTON, self.onNext)
        btnSizer.Add(self.nextBtn, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
    
        # finish layout
        self.mainSizer.Add(self.panelSizer, 1, wx.EXPAND)
        self.mainSizer.Add(btnSizer, 0, wx.ALIGN_RIGHT)
        self.SetSizer(self.mainSizer)


    def addPage(self, title=None):
        """"""
        panel = WizardPage(self, title)
        self.panelSizer.Add(panel, 2, wx.EXPAND)
        self.pages.append(panel)
        if len(self.pages) > 1:
            # hide all panels after the first one
            panel.Hide()
            self.Layout()

    def onNext(self, event):
        """"""
        pageCount = len(self.pages)
        if pageCount-1 != self.page_num:
            self.pages[self.page_num].Hide()
            self.page_num += 1
            self.pages[self.page_num].Show()
            self.panelSizer.Layout()
        else:
            print("End of pages!")

        if self.nextBtn.GetLabel() == "Finish":
            # close the app
            self.GetParent().Close()

        if pageCount == self.page_num+1:
            # change label
            self.nextBtn.SetLabel("Finish")

    def onPrev(self, event):
        """"""
        pageCount = len(self.pages)
        if self.page_num-1 != -1:
            self.pages[self.page_num].Hide()
            self.page_num -= 1
            self.pages[self.page_num].Show()
            self.panelSizer.Layout()
        else:
            print("You're already on the first page!")

class MainFrame(wx.Frame):
    """"""
 
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Generic Wizard", size=(800,600))
 
        self.panel = WizardPanel(self)
        self.panel.addPage("Page 1")
        self.panel.addPage("Page 2")
        self.panel.addPage("Page 3")
 
        self.Show()
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

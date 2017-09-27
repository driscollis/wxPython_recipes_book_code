import wx
from wx.adv import Wizard, WizardPageSimple


class TitledPage(WizardPageSimple):
    """"""

    def __init__(self, parent, title):
        """Constructor"""
        WizardPageSimple.__init__(self, parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        title = wx.StaticText(self, -1, title)
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(title, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND|wx.ALL, 5)


def main():
    """"""
    wizard = Wizard(None, -1, "Simple Wizard")
    page1 = TitledPage(wizard, "Page 1")
    page2 = TitledPage(wizard, "Page 2")
    page3 = TitledPage(wizard, "Page 3")
    page4 = TitledPage(wizard, "Page 4")

    WizardPageSimple.Chain(page1, page2)
    WizardPageSimple.Chain(page2, page3)
    WizardPageSimple.Chain(page3, page4)
    wizard.FitToPage(page1)

    wizard.RunWizard(page1)

    wizard.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    main()
    app.MainLoop()

import wx

class MiFrame(wx.Frame):
    def __init__(self, parent, **kwargs):
        wx.Frame.__init__(self, parent=parent, **kwargs)
        panel = wx.Panel(self)  # Crea un panel dentro del frame
        self.bt1 = wx.Button(panel, wx.ID_ANY, u"Botón 1", pos=(50, 60), size=(100, 20))
        self.bt2 = wx.Button(panel, wx.ID_ANY, u"Botón 2", pos=(50, 120), size=(100, 20))
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MiFrame(None, title=u"Posicionamiento absoluto", size=(300, 200))
    app.MainLoop()

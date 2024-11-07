import wx

class grafica(wx.Frame):
    def __init__(self,parent,**kwargs):
        wx.Frame.__init__(self,parent=parent,**kwargs)
        self.Show()

if __name__=='__main__':
    app = wx.App()
    frame = grafica(None, title=u"Hola mundo")
    app.MainLoop()
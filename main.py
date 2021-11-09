import wx
from panicbuying import PanicBuying

if __name__ == '__main__':
    # 窗口加载
    app = wx.App(False)
    p = PanicBuying()
    p.Show()
    app.MainLoop()
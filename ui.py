"""
    time:        2021-11-01 - 2021-11-08
    author:      黄玉胜
    description: 窗口ui设计
"""

import wx
import wx.adv
import time

## 主窗口
class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        ## 状态栏
        self.CreateStatusBar(2)
        self.StatusBar()
        ## 界面
        self.InitUI()
        self.Centre()

    ## 状态栏设计
    def StatusBar(self, status = 0):
        ## 程序状态
        if status == 0:
            self.SetStatusText('Ready', 0)
        elif status == 1:
            self.SetStatusText('Running', 0)
        else:
            self.SetStatusText('Success', 0)
        ## 时间显示
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    ## 获取本地时间
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.SetStatusText(st, 1)

    ## 主界面设计
    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(8, 5)

        text1 = wx.StaticText(panel, label="Happy Shopping")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                  border=15)

        icon = wx.StaticBitmap(panel, bitmap = self.ResizeIcon(wx.Bitmap('images/shopping-cart.png'), 30, 40))
        sizer.Add(icon, pos=(0, 3), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT,
                  border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Shop URL")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        text3 = wx.StaticText(panel, label="Login Selector")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)

        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text4 = wx.StaticText(panel, label='Shop Selector')
        sizer.Add(text4, pos=(4, 0), flag=wx.LEFT | wx.TOP, border=10)

        self.tc3 = wx.TextCtrl(panel)
        sizer.Add(self.tc3, pos=(4, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text5 = wx.StaticText(panel, label='Start Time')
        sizer.Add(text5, pos=(5, 0), flag=wx.LEFT | wx.TOP, border=10)

        self.date = wx.adv.DatePickerCtrl(panel)
        sizer.Add(self.date, pos=(5, 1))

        self.time = wx.adv.TimePickerCtrl(panel, size=(80,27))
        sizer.Add(self.time, pos=(5, 3))

        self.button1 = wx.Button(panel, label='Login')
        sizer.Add(self.button1, pos=(7, 1))
        self.Bind(wx.EVT_BUTTON, self.login, self.button1)

        self.button2 = wx.Button(panel, label="Start")
        sizer.Add(self.button2, pos=(7, 3))
        self.Bind(wx.EVT_BUTTON, self.start, self.button2)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        sizer.Fit(self)

    ## 重置图标大小
    def ResizeIcon(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    ## 登录异常对话框
    def LoginExcpetionMessage(self):
        wx.MessageBox('Login Error!', 'Login Status',
                      wx.OK | wx.ICON_INFORMATION)

    ## 登录成功对话框
    def LoginSuccessMessage(self):
        wx.MessageBox('Login Success!', 'Login Status',
                      wx.OK | wx.ICON_INFORMATION)

    ## 开始异常对话框
    def StartExcpetionMessage(self):
        wx.MessageBox('Start Error!', 'Start Status',
                      wx.OK | wx.ICON_INFORMATION)

    ## 抢购成功对话框
    def SuccessMessage(self):
        wx.MessageBox('Panicbuying Success!', 'Panicbuying Status',
                      wx.OK | wx.ICON_INFORMATION)

    ## 获取商品链接
    def GetUrl(self):
        return self.tc1.GetValue()

    ## 获取登录css_selector
    def GetLoginSelector(self):
        return self.tc2.GetValue()

    ## 获取商品css_selector
    def GetShopSelector(self):
        return self.tc3.GetValue()

    ## 获取抢购时间
    def GetTime(self):
        return str(self.date.GetValue()).split(' ')[0] + ' ' + str(self.time.GetValue()).split(' ')[1] + '.100000'

    ## 登录按钮点击事件重写
    def login(self, event):
        pass

    ## 开始按钮点击事件重写
    def start(self, event):
        pass

## 运行窗口
class RunDialog(wx.Dialog):

    def __init__(self,*args, **kw):
        super(RunDialog, self).__init__(*args, **kw)

    ## 运行对话框界面初始化
    def InitUI(self):
        self.timer = wx.Timer(self, 1)
        self.count = 0

        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)

        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.text1 = wx.StaticText(pnl, label = st)
        self.btn2 = wx.Button(pnl, label = 'stop')
        self.text2 = wx.StaticText(pnl, label = '')
        self.text3 = wx.StaticText(pnl, label = '')
        self.text4 = wx.StaticText(pnl, label = '至')

        self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)

        hbox1.Add(self.text1, proportion=1, flag=wx.CENTER)
        hbox5.Add(self.text4, proportion=1, flag=wx.CENTER)
        hbox4.Add(self.text3, proportion=1, flag=wx.CENTER)
        hbox2.Add(self.btn2, proportion=1, flag=wx.CENTER)
        hbox3.Add(self.text2, proportion=1)

        vbox.Add((0, 30))

        vbox.Add(hbox1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox5, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox4, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox2, proportion=1, flag=wx.ALIGN_CENTRE)
        vbox.Add(hbox3, proportion=1, flag=wx.ALIGN_CENTRE)

        pnl.SetSizer(vbox)

    ## 加载
    def start(self, time_countdown, buy_time):
        self.time_countdown = time_countdown

        self.InitUI()
        self.SetTitle('panicbuying is running')
        self.Centre()
        self.timer.Start(1050)
        self.text3.SetLabel(buy_time)
        self.text2.SetLabel('Wait for the time')
        self.ShowModal()

    ## 抢购暂停
    def OnStop(self, e):
        if self.count == 0 \
                or self.count >= self.time_countdown \
                or not self.timer.IsRunning():
            return

        self.timer.Stop()
        self.text2.SetLabel('Panicbuying Interrupted')
        self.Destroy()

    ## 计时器
    def OnTimer(self, e):
        self.count = self.count + 1
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.text1.SetLabel(st)

        if self.count == self.time_countdown:
            self.timer.Stop()
            self.text2.SetLabel('Panicbuying Completed')
            self.Destroy()
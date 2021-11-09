"""
    time:        2021-11-05 - 2021-11-08
    author:      黄玉胜
    description: 抢购功能设计
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui import MyFrame, RunDialog
from timer import Timer

class PanicBuying(MyFrame):

    def __init__(self):
        MyFrame.__init__(self, parent=None, title='PanicBuying')
        self.url = ''
        self.login_selector = ''
        self.stop_selector = ''
        self.buy_time = ''
        self.time_countdown = 0

    ## 抢购登录，必须手动登录，水平有限，暂时不能实现自动登录
    def login(self, e):
        ## 配置抢购登录参数
        self.url = self.GetUrl()
        self.login_selector = self.GetLoginSelector()

        if self.url == '' \
                or self.url == None \
                or self.login_selector == '' \
                or self.login_selector == None:
            self.LoginExcpetionMessage()
        else:
            ## 设置浏览器驱动器
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            self.driver = webdriver.Chrome(options=options)
            ## 启动浏览器
            self.driver.get(self.url)
            self.driver.maximize_window()

            # 存储原始窗口标题
            original_window_title = self.driver.title

            ## 登录
            self.driver.find_element(By.CSS_SELECTOR, self.login_selector).click()
            WebDriverWait(self.driver, 180).until(EC.title_is(original_window_title))

            ## 弹出对话框login success
            self.LoginSuccessMessage()

    ## 抢购开始
    def start(self, e):
        ## 配置抢购开始参数
        self.shop_selector = self.GetShopSelector()
        self.buy_time = self.GetTime()
        t = Timer(self.buy_time)
        if t.LocalTime() >= t.buy_time_ms \
                or self.shop_selector == '' \
                or self.shop_selector == None \
                or self.buy_time == '' \
                or self.buy_time == None:
            self.StartExcpetionMessage()
        else:
            switch = True
            ## 抢购进入运行状态
            self.run(switch)

    ## 抢购运行
    def run(self, switch):
        ## 倒计时时间(s)
        time_countdown = Timer(self.buy_time).TimeCountDown() // 1000 - 15
        runDialog = RunDialog(None, title = 'panicbuying is running')

        if switch :
            ## 状态栏显示running
            self.StatusBar(1)
            runDialog.start(time_countdown, self.buy_time.split('.')[0])
            ## 网页刷新
            self.driver.refresh()

            original_title = self.driver.title
            while True:
                self.driver.find_element(By.CSS_SELECTOR, self.shop_selector).click()
                ## 抢购成功
                if self.driver.title != original_title:
                    self.StatusBar(2)
                    self.SuccessMessage()
                    break
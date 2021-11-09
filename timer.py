"""
    time:        2021-11-05
    author:      黄玉胜
    description: 时间校对功能设计
"""

import time
import requests
from datetime import datetime

## 本地时间与服务器时间校对，误差在0.1s左右
class Timer():

    def __init__(self, buy_time):
        self.buy_time = datetime.strptime(buy_time,"%Y/%m/%d %H:%M:%S.%f")
        self.buy_time_ms = int(time.mktime(self.buy_time.timetuple()) * 1000.0 + self.buy_time.microsecond / 1000)

    ## 获取服务器毫秒时间
    def ServerTime(self):
        url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
        headers = "User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36"
        ret = requests.get(url, headers)
        x = eval(ret.text)
        return int(x['data']['t'])

    ## 获取本地毫秒时间
    def LocalTime(self):
        return int(round(time.time()) * 1000)

    ## 计算本地与服务器时间差
    def LocalDiffSever(self):
        return self.LocalTime() - self.ServerTime()

    ## 计算倒计时
    def TimeCountDown(self):
        return self.buy_time_ms - self.LocalTime() + self.LocalDiffSever()
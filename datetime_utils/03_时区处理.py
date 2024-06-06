# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 15:09
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 03_时区处理.py
"""
__author__ = "梦无矶小仔"

import datetime
import pytz

# 获取当前时间（带时区）
now_utc = datetime.datetime.now(pytz.utc)
print("当前UTC时间:", now_utc)

# 将当前时间转换为其他时区
now_est = now_utc.astimezone(pytz.timezone('US/Eastern'))
print("当前美国东部时间:", now_est)

# 创建带时区的日期和时间
aware_datetime = datetime.datetime(2023, 6, 4, 14, 30, 15, tzinfo=pytz.timezone('US/Eastern'))
print("带时区的日期和时间:", aware_datetime)


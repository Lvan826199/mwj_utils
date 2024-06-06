# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 15:21
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 06_时间戳和日期转换示列.py
"""
__author__ = "梦无矶小仔"
import time
import datetime
import pytz

# 获取当前时间戳
current_timestamp = time.time()
print("当前时间戳:", current_timestamp)

# 时间戳转换为日期和时间
local_time = time.localtime(current_timestamp)
formatted_local_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("本地时间:", formatted_local_time)

# 使用 datetime 模块
datetime_obj = datetime.datetime.fromtimestamp(current_timestamp)
formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("格式化的 datetime 对象:", formatted_datetime)

# 日期和时间转换为时间戳
datetime_obj = datetime.datetime(2023, 6, 4, 14, 30, 15)
timestamp = datetime_obj.timestamp()
print("时间戳:", timestamp)

# 处理带时区的时间戳
datetime_obj_with_tz = datetime.datetime.fromtimestamp(current_timestamp, pytz.timezone('US/Eastern'))
print("带时区的 datetime 对象:", datetime_obj_with_tz)
timestamp_with_tz = datetime_obj_with_tz.timestamp()
print("带时区的时间戳:", timestamp_with_tz)
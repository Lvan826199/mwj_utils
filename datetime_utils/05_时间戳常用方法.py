# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 15:12
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 05_时间戳常用方法.py
"""
__author__ = "梦无矶小仔"
import time
import datetime
# 获取当前时间戳
current_timestamp = time.time()
print("当前时间戳:", current_timestamp)

# 时间戳转换为日期和时间
# 将时间戳转换为本地时间的 struct_time 对象
local_time = time.localtime(current_timestamp)
print("本地时间:", local_time)

# 将时间戳转换为 UTC 时间的 struct_time 对象
utc_time = time.gmtime(current_timestamp)
print("UTC 时间:", utc_time)

# 将 struct_time 对象格式化为字符串
formatted_local_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("格式化的本地时间:", formatted_local_time)

# 将时间戳转换为 datetime 对象
datetime_obj = datetime.datetime.fromtimestamp(current_timestamp)

print("datetime 对象:", datetime_obj)

# 将时间戳转换为 UTC 的 datetime 对象
utc_datetime_obj = datetime.datetime.utcfromtimestamp(current_timestamp)
print("UTC datetime 对象:", utc_datetime_obj)
# 或
utc_datetime_obj = datetime.datetime.fromtimestamp(current_timestamp, datetime.timezone.utc)  # 默认是本地ip时区时间
print("UTC datetime 对象:", utc_datetime_obj)

# 格式化 datetime 对象为字符串
formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("格式化的 datetime 对象:", formatted_datetime)

# 日期和时间转化为时间戳
# 创建 struct_time 对象
struct_time = time.strptime("2023-06-04 14:30:15", "%Y-%m-%d %H:%M:%S")

# 将 struct_time 对象转换为时间戳
timestamp = time.mktime(struct_time)
print("时间戳:", timestamp)

# 创建 datetime 对象
datetime_obj = datetime.datetime(2023, 6, 4, 14, 30, 15)

# 将 datetime 对象转换为时间戳
timestamp = datetime_obj.timestamp()
print("时间戳:", timestamp)

# 处理带时区的时间戳

import pytz

# 获取当前时间戳
current_timestamp = time.time()

# 将时间戳转换为带时区的 datetime 对象
datetime_obj = datetime.datetime.fromtimestamp(current_timestamp, pytz.timezone('US/Eastern'))
print("带时区的 datetime 对象:", datetime_obj)

# 将带时区的 datetime 对象转换为时间戳
timestamp_with_tz = datetime_obj.timestamp()
print("带时区的时间戳:", timestamp_with_tz)
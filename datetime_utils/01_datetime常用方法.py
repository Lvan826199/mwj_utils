# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 14:33
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 01_datetime常用方法.py
"""
__author__ = "梦无矶小仔"

import datetime

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)

# 获取当前日期
today = datetime.date.today()
print("当前日期:", today)

# 创建特定日期或时间# 创建一个特定的日期
specific_date = datetime.date(2023, 6, 4)
print("特定日期:", specific_date)

# # 创建一个特定的时间
specific_time = datetime.time(14, 30, 15)
print("特定时间:", specific_time)

# # 创建一个特定的日期和时间
specific_datetime = datetime.datetime(2023, 6, 4, 14, 30, 15)
print("特定日期和时间:", specific_datetime)

# 日期加减
tomorrow = today + datetime.timedelta(days=1)
print("明天:", tomorrow)

yesterday = today - datetime.timedelta(days=1)
print("昨天:", yesterday)

# 时间差
time_diff = datetime.datetime(2024, 6, 4) - datetime.datetime(2023, 6, 4)
print("时间差:", time_diff)

# 日期和时间格式化为字符串
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化日期和时间:", formatted_datetime)

# 字符串解析为日期和时间
parsed_datetime = datetime.datetime.strptime("2023-06-04 14:30:15", "%Y-%m-%d %H:%M:%S")
print("解析后的日期和时间:", parsed_datetime)

print("年:", now.year)
print("月:", now.month)
print("日:", now.day)
print("小时:", now.hour)
print("分钟:", now.minute)
print("秒:", now.second)
print("微秒:", now.microsecond)

# 日期和时间的比较
date1 = datetime.date(2023, 6, 4)
date2 = datetime.date(2024, 6, 4)

print("date1 是否早于 date2:", date1 < date2)
print("date1 是否等于 date2:", date1 == date2)
print("date1 是否晚于 date2:", date1 > date2)

# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 15:07
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 02_日期运算.py
"""
__author__ = "梦无矶小仔"

import datetime
from datetime import timedelta

# 创建一个表示10天的 timedelta 对象
delta_days = datetime.timedelta(days=10)
print("10天的 timedelta:", delta_days)

# 创建一个表示2小时30分钟的 timedelta 对象
delta_hours_minutes = datetime.timedelta(hours=2, minutes=30)
print("2小时30分钟的 timedelta:", delta_hours_minutes)

# 创建一个表示1周的 timedelta 对象
delta_weeks = datetime.timedelta(weeks=1)
print("1周的 timedelta:", delta_weeks)

# 获取当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)

# 日期加减 timedelta
future_date = now + delta_days
print("10天后的日期和时间:", future_date)

past_date = now - delta_days
print("10天前的日期和时间:", past_date)

delta = datetime.timedelta(days=5, hours=3, minutes=30, seconds=15)

print("天数:", delta.days)
print("总秒数:", delta.total_seconds())
print("秒数（不包括天）:", delta.seconds)
print("微秒数:", delta.microseconds)


# timedelta对象可以进行比较运算：
delta1 = datetime.timedelta(days=5)
delta2 = datetime.timedelta(days=10)

print("delta1 < delta2:", delta1 < delta2)
print("delta1 == delta2:", delta1 == delta2)
print("delta1 > delta2:", delta1 > delta2)


# 示列代码
import datetime
from datetime import timedelta

# 创建 timedelta 对象
delta_days = datetime.timedelta(days=10)
delta_hours_minutes = datetime.timedelta(hours=2, minutes=30)
delta_weeks = datetime.timedelta(weeks=1)

# 当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)

# 日期加减 timedelta
future_date = now + delta_days
print("10天后的日期和时间:", future_date)

past_date = now - delta_days
print("10天前的日期和时间:", past_date)

# timedelta 的属性
delta = datetime.timedelta(days=5, hours=3, minutes=30, seconds=15)
print("天数:", delta.days)
print("总秒数:", delta.total_seconds())
print("秒数（不包括天）:", delta.seconds)
print("微秒数:", delta.microseconds)

# timedelta 的比较
delta1 = datetime.timedelta(days=5)
delta2 = datetime.timedelta(days=10)
print("delta1 < delta2:", delta1 < delta2)
print("delta1 == delta2:", delta1 == delta2)
print("delta1 > delta2:", delta1 > delta2)
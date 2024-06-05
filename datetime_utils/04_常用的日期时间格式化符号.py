# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 15:11
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 04_常用的日期时间格式化符号.py
"""
__author__ = "梦无矶小仔"

import datetime

import pytz

"""
- `%Y`：四位数的年份，如 2023
- `%m`：两位数的月份（01-12）
- `%d`：两位数的日期（01-31）
- `%H`：两位数的小时（00-23）
- `%M`：两位数的分钟（00-59）
- `%S`：两位数的秒（00-59）
- `%f`：微秒（000000-999999）
- `%z`：时区偏移
- `%Z`：时区名称
- `%a`：简写的星期几名称
- `%A`：完整的星期几名称
- `%b`：简写的月份名称
- `%B`：完整的月份名称
"""
# 当前日期和时间
now = datetime.datetime.now()
print("当前日期和时间:", now)

# 格式化日期和时间
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化日期和时间:", formatted_datetime)

# 解析日期和时间字符串
parsed_datetime = datetime.datetime.strptime("2023-06-04 14:30:15", "%Y-%m-%d %H:%M:%S")
print("解析后的日期和时间:", parsed_datetime)

# 日期加减
tomorrow = now + datetime.timedelta(days=1)
print("明天:", tomorrow)

# 时区处理
now_utc = datetime.datetime.now(pytz.utc)
print("当前UTC时间:", now_utc)
now_est = now_utc.astimezone(pytz.timezone('US/Eastern'))
print("当前美国东部时间:", now_est)
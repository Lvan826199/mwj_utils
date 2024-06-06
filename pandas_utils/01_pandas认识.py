# -*- coding: utf-8 -*-
"""
@Time : 2024/6/3 18:57
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 01_pandas认识.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 创建一个 Series
s = pd.Series([1, 3, 5, 7, 9])
print(s)

print("--------------------")
# 创建一个 DataFrame
data = {
    'Name': ['小仔', '大仔', '梦无矶'],
    'Age': [15, 18, 99],
    'City': ['上海', '长沙', '杭州']
}
df = pd.DataFrame(data)
print(df)

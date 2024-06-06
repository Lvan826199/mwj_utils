# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 13:56
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 08_分组聚合.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

df = pd.read_csv('excel_path/data.csv')

# 按城市分组并计算平均年龄
grouped = df.groupby('City')['Age'].mean()
print(grouped)



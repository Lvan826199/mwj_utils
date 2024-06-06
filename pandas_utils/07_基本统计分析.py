# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 13:43
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 07_基本统计分析.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

df = pd.read_csv('excel_path/data.csv')

# 数据描述性统计
print(df.describe())
print("----------------")
# 计算平均值
print(df['Age'].mean())

# 计算中位数
print(df['Age'].median())

# 计算标准差
print(df['Age'].std())

# 计算最大值
print(df['Age'].max())

# 计算最小值
print(df['Age'].min())

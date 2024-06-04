# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 11:39
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 04_数据选择和过滤.py
"""
__author__ = "梦无矶小仔"

import  pandas as pd

df = pd.read_csv('excel_path/data.csv')

# 选择列
print(df['Name'])
print("------------------------------")
print(df[['Name', 'Age']])
print("------------------------------")

# 根据索引选择行
print(df.iloc[0])  # 第一行
print("------------------------------")
print(df.iloc[1:3])  # 第二行到第三行
print("------------------------------")
# 根据标签选择行
print(df.loc[0])  # 第一行
print("------------------------------")
print(df.loc[0:1])  # 第一行到第二行
print("------------------------------")

# 条件过滤 # 选择年龄大于30的行
print(df[df['Age'] > 30])
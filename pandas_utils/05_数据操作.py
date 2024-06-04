# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 13:29
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 05_数据操作.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

df = pd.read_csv('excel_path/data.csv')

# 添加新列
df['Salary'] = [50000, 60000, 70000]

print(df, end="\n\n")

# 删除列
df = df.drop(columns=['Salary'])
print(df, end="\n\n")

# 修改列 年龄这一列的所有年龄+1
df['Age'] = df['Age'] + 1

print(df, end="\n\n")

# 缺失值处理 填充缺失值 使用每列的均值填充缺失值
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df, end="\n\n")
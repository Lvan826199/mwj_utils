# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 15:10
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 11_读取excel表.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 读取 Excel 文件中的第一个工作表
df = pd.read_excel('excel_path/data.xlsx')
print(df)

# 读取 Excel 文件中的第一个工作表
df = pd.read_excel('excel_path/data.xlsx', sheet_name="Sheet2")
print(df)

# 读取 Excel 文件中的多个工作表
dfs = pd.read_excel('excel_path/data.xlsx', sheet_name=['Sheet1', 'Sheet2'])
print(dfs['Sheet1'])
print(dfs['Sheet2'])

# 读取所有工作表
dfs = pd.read_excel('excel_path/data.xlsx', sheet_name=None)
for sheet_name, df in dfs.items():
    print(f"Sheet name: {sheet_name}")
    print(df)

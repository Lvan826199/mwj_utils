# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 13:59
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 09_合并和连接.py
"""
__author__ = "梦无矶小仔"
import pandas as pd

df = pd.read_csv('excel_path/data.csv')

# 创建另一个 DataFrame
data2 = {
    'Name': ['小美', '梦无矶', '小仔'],
    'Salary': [50000, 60000, 80000]
}
df2 = pd.DataFrame(data2)

# 合并两个 DataFrame
merged_df = pd.merge(df, df2, on='Name', how='inner')

print(merged_df)
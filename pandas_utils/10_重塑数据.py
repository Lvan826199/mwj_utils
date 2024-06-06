# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 14:04
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 10_重塑数据.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 示例数据
data = {
    'Date': ['2024-06-01', '2024-06-02', '2024-06-01', '2024-06-02'],
    'City': ['杭州', '赣州', '赣州', '杭州'],
    'Temperature': [20, 30, 45, 40]
}
df = pd.DataFrame(data)

# 使用 pivot 将长格式数据转换为宽格式
pivot_df = df.pivot(index='Date', columns='City', values='Temperature')
print(pivot_df, end="\n\n")

# 使用 pivot_table 进行聚合
pivot_table_df = df.pivot_table(index='Date', columns='City', values='Temperature', aggfunc='mean')
print(pivot_table_df, end="\n\n")

# melt 方法用于将宽格式数据转换为长格式数据
melted_df = pivot_df.reset_index().melt(id_vars='Date', value_vars=['赣州', '杭州'], var_name='City', value_name='Temperature')
print(melted_df, end="\n\n")

# stack 方法将数据的列索引转换为行索引，而 unstack则相反
print("使用 stack 将列索引转换为行索引")
stacked_df = pivot_df.stack()
print(stacked_df)

print("使用 unstack 将行索引转换为列索引")
unstacked_df = stacked_df.unstack()
print(unstacked_df)
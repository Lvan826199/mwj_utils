# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 13:42
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 06_缺失值拓展.py
"""
__author__ = "梦无矶小仔"

import pandas as pd
import numpy as np

# 创建一个包含缺失值的 DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, 2, 3, np.nan]
}
df = pd.DataFrame(data)

# 检查每个单元格是否缺失
print(df.isna())

# 检查每列的缺失值总数
print(df.isna().sum())

# 删除包含缺失值的行
df_dropped_rows = df.dropna()
print(df_dropped_rows)

# 删除包含缺失值的列
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols)

# 使用常数填充缺失值
df_filled_constant = df.fillna(0)
print(df_filled_constant)

# 使用前一个值（向前填充）填充缺失值
df_filled_ffill = df.fillna(method='ffill')
print(df_filled_ffill)

# 使用后一个值（向后填充）填充缺失值
df_filled_bfill = df.fillna(method='bfill')
print(df_filled_bfill)

# 使用每列的均值填充缺失值
df_filled_mean = df.fillna(df.mean())
print(df_filled_mean)

# 使用每列的中位数填充缺失值
df_filled_median = df.fillna(df.median())
print(df_filled_median)

# 仅填充特定列的缺失值
df['A'] = df['A'].fillna(df['A'].mean())
print(df)

# 使用线性插值法填充缺失值
df_interpolated = df.interpolate()
print(df_interpolated)

# 先向前填充，再向后填充
df_combined_fill = df.fillna(method='ffill').fillna(method='bfill')
print(df_combined_fill)
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 15:20
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 13_写入多个DataFrame到Excel.py.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 创建一个 DataFrame
data = {
    'Name': ['悖谬', '申鹤', '凯茜娅'],
    'Age': [18, 20, 25],
    'City': ['我家', '我房间', '我卧室']
}
df = pd.DataFrame(data)

# 创建另一个 DataFrame
data2 = {
    'Name': ['刻晴', '丽莎', '巴尔泽布'],
    'Age': [19, 21, 24],
    'City': ['璃月', '蒙德', '稻妻']
}

df2 = pd.DataFrame(data2)

# 写入到不同工作表
with pd.ExcelWriter('excel_path/write1.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)

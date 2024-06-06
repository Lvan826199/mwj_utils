# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 15:15
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 12_写入DataFrame到Excel.py
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

# 写入到 Excel 文件
df.to_excel('excel_path/output.xlsx', index=False)
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 11:34
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 03_读取和写入数据.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('excel_path/data.csv')

# 写入 CSV 文件
df.to_csv('excel_path/output.csv', index=False)

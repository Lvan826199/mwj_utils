# -*- coding: utf-8 -*-
"""
@Time : 2024/6/7 11:41
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 08_样式大全_07设置列宽.py
"""
__author__ = "梦无矶小仔"

from openpyxl import  load_workbook

column_widths = {'A': 20, 'B': 10, 'C': 30}  # 设置列宽

file_path = "excelPath/demo1.xlsx"
# 加载现有的工作簿
wb = load_workbook(file_path)
ws = wb.active
# 设置列宽
for col, width in column_widths.items():
    ws.column_dimensions[col].width = width
# 保存工作簿
wb.save(file_path)
# -*- coding: utf-8 -*-
"""
@Time : 2024/6/7 11:42
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 08_样式大全_08设置行高.py.py
"""
__author__ = "梦无矶小仔"

import openpyxl

# 打开 Excel 文件
workbook = openpyxl.load_workbook('excelPath/demo1.xlsx')

# 选择一个工作表
sheet = workbook.active

# 设置行高 (将第 1 行的高度设置为 30)
sheet.row_dimensions[1].height = 30
# 设置行高 (将第 2 行的高度设置为 50)
sheet.row_dimensions[2].height = 50

# 保存修改后的 Excel 文件
workbook.save('excelPath/demo1.xlsx')
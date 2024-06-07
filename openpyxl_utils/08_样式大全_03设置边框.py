# -*- coding: utf-8 -*-
"""
@Time : 2024/6/6 18:56
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 08_样式大全_03设置边框.py
"""
__author__ = "梦无矶小仔"

from openpyxl import Workbook
from openpyxl.styles import Border, Side

# 创建一个新的工作簿和工作表
workbook = Workbook()
sheet = workbook.active

# 定义不同的边框样式
thin_border = Border(
    left=Side(border_style="thin", color="000000"),
    right=Side(border_style="thin", color="000000"),
    top=Side(border_style="thin", color="000000"),
    bottom=Side(border_style="thin", color="000000")
)

thick_border = Border(
    left=Side(border_style="thick", color="FF0000"),
    right=Side(border_style="thick", color="FF0000"),
    top=Side(border_style="thick", color="FF0000"),
    bottom=Side(border_style="thick", color="FF0000")
)

dashed_border = Border(
    left=Side(border_style="dashed", color="00FF00"),
    right=Side(border_style="dashed", color="00FF00"),
    top=Side(border_style="dashed", color="00FF00"),
    bottom=Side(border_style="dashed", color="00FF00")
)

double_border = Border(
    left=Side(border_style="double", color="0000FF"),
    right=Side(border_style="double", color="0000FF"),
    top=Side(border_style="double", color="0000FF"),
    bottom=Side(border_style="double", color="0000FF")
)

# 应用边框样式到不同的单元格
sheet["A1"].value = "Thin Border"
sheet["A1"].border = thin_border

sheet["B1"].value = "Thick Border"
sheet["B1"].border = thick_border

sheet["C1"].value = "Dashed Border"
sheet["C1"].border = dashed_border

sheet["D1"].value = "Double Border"
sheet["D1"].border = double_border

# 保存工作簿
workbook.save("excelPath/demo08_3.xlsx")
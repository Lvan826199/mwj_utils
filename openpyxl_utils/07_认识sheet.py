# -*- coding: utf-8 -*-
"""
@Time : 2024/6/6 16:32
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 07_认识sheet.py
"""
__author__ = "梦无矶小仔"

from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet


def read_sheet_attribute(file_path, sheet_name):
    wb = load_workbook(file_path)
    sheet: Worksheet = wb[sheet_name]
    for i in sheet.values:
        print(i)


if __name__ == '__main__':
    # 调用方法读取特定列的数据
    file_path = 'excelPath/demo1.xlsx'
    sheet_name = 'Sheet1'
    column_data = read_sheet_attribute(file_path, sheet_name)

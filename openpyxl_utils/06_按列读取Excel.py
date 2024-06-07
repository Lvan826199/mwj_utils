# -*- coding: utf-8 -*-
"""
@Time : 2024/6/6 13:25
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 06_按列读取Excel.py
"""
__author__ = "梦无矶小仔"

from openpyxl import load_workbook


def read_column(file_path, sheet_name, column):
    wb = load_workbook(file_path)
    sheet = wb[sheet_name]

    column_values = []
    for cell in sheet[column]:
        column_values.append(cell.value)

    return column_values


if __name__ == '__main__':
    # 调用方法读取特定列的数据
    file_path = 'excelPath/demo1.xlsx'
    sheet_name = 'Sheet1'
    column_letter = 'A'  # 假设要读取A列
    column_data = read_column(file_path, sheet_name, column_letter)
    print(column_data)

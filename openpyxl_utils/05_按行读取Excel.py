# -*- coding: utf-8 -*-
"""
@Time : 2024/6/6 13:24
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 05_按行读取Excel.py
"""
__author__ = "梦无矶小仔"

from openpyxl import load_workbook


def read_row(file_path, sheet_name, row):
    wb = load_workbook(file_path)
    sheet = wb[sheet_name]

    row_values = []
    for cell in sheet[row]:
        row_values.append(cell.value)

    return row_values


if __name__ == '__main__':
    # 调用方法读取特定行的数据
    file_path = 'excelPath/demo1.xlsx'
    sheet_name = 'Sheet1'
    row_number = 3  # 假设要读取第3行
    row_data = read_row(file_path, sheet_name, row_number)
    print(row_data)

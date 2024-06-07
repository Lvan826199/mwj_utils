# -*- coding: utf-8 -*-
"""
@Time : 2024/6/5 17:31
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : 02_按行写入Excel.py
"""
__author__ = "梦无矶小仔"

from openpyxl import Workbook


def write_rows_to_excel(file_path, rows):
    """
    按行写入数据到Excel文件。
    :param file_path: (str)Excel文件路径
    :param rows :(list of list)要写入的行数据，每行是一个列表
    """
    # 创建一个新的工作簿
    wb = Workbook()
    ws = wb.active

    # 按行写入数据
    for row in rows:
        ws.append(row)

    # 保存工作簿
    wb.save(file_path)


if __name__ == '__main__':
    # 示例使用
    file_path = 'excelPath/demo2.xlsx'
    rows = [
        ['Name', 'Age', 'City'],
        ['无矶', 30, '黄山'],
        ['无妨', 25, '泰山'],
        ['无妨游志', 35, '华山']
    ]

    write_rows_to_excel(file_path, rows)

    print(f"文件已保存到 {file_path}")

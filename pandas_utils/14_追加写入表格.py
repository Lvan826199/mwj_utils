# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 15:25
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 14_追加写入表格.py
"""
__author__ = "梦无矶小仔"

import  pandas as pd

# 读取现有的 Excel 文件
existing_df = pd.read_excel('excel_path/output.xlsx', sheet_name='Sheet1')

# 新数据
new_data = {
    'Name': ['无妨', '紫霄'],
    'Age': [55, 60],
    'City': ['木星', '海王星']
}
new_df = pd.DataFrame(new_data)

# 追加新数据到现有 DataFrame
updated_df = pd.concat([existing_df, new_df], ignore_index=True)

# 写入回 Excel 文件
with pd.ExcelWriter('excel_path/output.xlsx', mode='a', if_sheet_exists='replace') as writer:
    updated_df.to_excel(writer, sheet_name='Sheet1', index=False)
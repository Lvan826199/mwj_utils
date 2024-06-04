# -*- coding: utf-8 -*-
"""
@Time : 2024/6/4 15:28
@Email : Lvan826199@163.com
@公众号 : 梦无矶的测试开发之路
@File : 15_写入带有超链接的内容.py
"""
__author__ = "梦无矶小仔"

import pandas as pd

# 创建一个 DataFrame
data = {
    'Name': ['蕾姆'],
    'Age': [20],
    'City': ['独栋别墅']
}
df = pd.DataFrame(data, index=[0]) # 多行写入不需要加index=[0]

goto = 'https://www.baidu.com/s?wd=%E7%8B%AC%E6%A0%8B%E5%88%AB%E5%A2%85'
# 加超链接 0表示写入的位置
df._set_value(0, "City", '=HYPERLINK("{}", "点击跳转详情")'.format(goto))

# 写入到 Excel 文件
df.to_excel('excel_path/write2.xlsx', index=False)
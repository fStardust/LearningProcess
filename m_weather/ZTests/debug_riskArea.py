# import csv
#
# import requests
#
#
# def gbk_trans_utf8(file_path):
#     with open(file_path, 'r', encoding='gbk') as f:
#         content = f.read()
#     print(content)
#     with open(file_path, 'w', encoding='utf8') as f:
#         f.write(content)
#
#
# url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
# r = requests.get(url)
# response_dict = r.json()
#
# # response_dict = response_dict.dumps()
#
# dicts = response_dict['data']
# updatetime = dicts['dateline']
# citymaps = dicts['map']
# count = dicts['count']
#
# # for item in updatetime:
# #     print('风险地区%s更新时间：%s' % (str(item), str(updatetime[item])))
#
# results = []
#
# for item in citymaps:
#     for item1 in item:
#         for item2 in citymaps[item1]:
#             areas = citymaps[item1][item2]
#             for area in areas:
#                 result = []
#                 grade = str(area['grade'])
#
#                 if grade == '1':
#                     result.append('中风险')
#                 if grade == '2':
#                     result.append('高风险')
#                 result.append(str(item2))
#                 result.append(str(area['city']))
#                 result.append(str(area['addr']))
#
#                 results.append(result)
#
# header = ['风险等级', '省级单位', '市级单位', '区域']
# updatetime = ['更新时间：', updatetime[item]]
# filename = '../information/全国最新风险等级区域' + '.csv'
# print(filename)
# with open(filename, 'w', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(updatetime)
#     f_csv.writerow(header)
#     f_csv.writerows(results)
#
# gbk_trans_utf8(filename)

import pandas as pd
import numpy as np

data = pd.read_csv(
    "D:\ProgramTest\LearningProcess\m_weather\information\全国最新风险等级区域.csv",
    header=1
)
data = np.array(data)
print(data)
node = "丰泽区滨海酒店"
if node in data:
    print("Y")
else:
    print("F")

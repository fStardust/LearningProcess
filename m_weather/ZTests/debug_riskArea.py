import csv

import pandas as pd

# url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
# r = requests.get(url)
# response_dict = r.json()
# response_dict = response_dict.dumps()
# dicts = response_dict['data']
# updatetime = dicts['dateline']
# citymaps = dicts['map']
# count = dicts['count']
# for item in updatetime:
#     print('风险地区%s更新时间：%s' % (str(item), str(updatetime[item])))
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
# print(updatetime)
# filename = '../information/全国最新风险等级区域' + '.csv'
# print(filename)
# with open(filename, 'w', newline='', encoding='utf-8') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(header)
#     f_csv.writerows(results)


data_loc = "D:\ProgramTest\LearningProcess\m_weather\information\全国最新风险等级区域.csv"
f = open(data_loc, 'r', encoding='utf-8')

with f:
    reader = csv.DictReader(f)
    i, n, m = 0, 0, 0
    for row in reader:
        print(row)
        if "黑龙江" in row["区域"] or "黑龙江" in row["市级单位"] or "黑龙江" in row["省级单位"]:
            i += 1
            print(row['风险等级'], row['省级单位'], row['市级单位'])
            risk_area = [row['风险等级'], row['省级单位'], row['市级单位']]
            a = str(risk_area)
            if row['风险等级'] == "中风险":
                n += 1
            else:
                m += 1
    print(n)
    print(m)
    print(a)
    print(type(a))


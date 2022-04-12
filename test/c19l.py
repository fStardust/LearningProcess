import csv
import time

import requests

# 执行api调用并存储响应
url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
r = requests.get(url)
# print("Status:", r.status_code)
# 将api响应存储在变量中
response_dict = r.json()
# print(response_dict ['data'])

dicts = response_dict['data']
updatetime = dicts['dateline']
citymaps = dicts['map']
count = dicts['count']

for item in updatetime:
    print('风险地区%s更新时间：%s' % (str(item), str(updatetime[item])))

results = []

for item in citymaps:
    for item1 in item:
        for item2 in citymaps[item1]:
            # print('风险地区:%s,省：%s,具体位置：%s'%(str(item),str(item2),str((citymaps[item1][item2]['city']+citymaps[item1][item2]['addr']))))
            # print(citymaps[item1][item2])
            areas = citymaps[item1][item2]
            for area in areas:
                result = []
                grade = str(area['grade'])
                if grade == '1':
                    result.append('中风险')
                if grade == '2':
                    result.append('高风险')

                result.append(str(item2))
                result.append(str(area['city'] + '市' + area['addr']))
                # print('风险等级:%s,省：%s,具体位置：%s'%(str(area['grade']),str(item2),str(area['city']+area['addr'])))
                # print(area['city']+area['addr'])
                results.append(result)
header = ['风险等级', '省份', '区域']
header1 = ['更新时间：', updatetime['1']]
filename = '全国最新风险等级区域' + '.csv'
print(len(results))
print(filename)
with open(filename, 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header1)
    f_csv.writerow(header)
    f_csv.writerows(results)

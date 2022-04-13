# 如何将json数据解析成我们所熟悉的Python数据类型？
import json

import requests


# 将json格式的str转化成python的数据格式：字典
dic = json.loads('{"name":"Tom","age":23}')
res = json.loads('["name","age","gender"]')
print(f'利用loads将json字符串转化成Python数据类型{dic}', type(dic))
print(f'利用loads将json字符串转化成Python数据类型{res}', type(res))
dics = {"name": "Tom", "age": 23}
result = json.dumps(dics)
print(type(result))
result
# 1.数据的获取(基于request模块)


# 国内疫情数据
China_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
headers = {
    # 浏览器伪装
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'referer': 'https://news.qq.com/',
}
# 发起get请求，获取响应数据
response = requests.get(China_url, headers=headers).json()
data = json.loads(response['data'])
# 保存数据
with open('./2021-02-03国内疫情.json', 'w', encoding='utf-8') as f:
    # 不采用ASCII编码
    f.write(json.dumps(data, ensure_ascii=False, indent=2))
# 读取文件
with open('./2021-02-03国内疫情.json', 'r', encoding='utf-8') as f:
    data = f.read()

# 将数据转成Python数据格式(字符串转换为字典)
data = json.loads(data)
# 1.获取数据最新的更新时间
lastUpdateTime = data['lastUpdateTime']
# 2.获取国内的所有疫情相关的数据
chinaAreaDict = data['areaTree']
# 3.获取省级数据
provinceList = chinaAreaDict[0]['children']
# 将国内数据按城市封装
china_citylist = []
for x in range(len(provinceList)):
    province = provinceList[x]['name']
    province_list = provinceList[x]['children']

    for y in range(len(province_list)):
        # 每一个地级市的数据
        city = province_list[y]['name']
        total = province_list[y]['total']
        today = province_list[y]['today']
        china_dict = {'province': province,
                      'city': city,
                      'total': total,
                      'today': today}
        china_citylist.append(china_dict)
china_citylist
import pandas as pd

chinaTotalData = pd.DataFrame(china_citylist)

# 将整体数据chinaTotalData中的today和total数据添加到DataFrame中
# 处理total字典里面的各个数据项
# ======================================================================
confirmlist = []
suspectlist = []
deadlist = []
heallist = []
deadRatelist = []
healRatelist = []
# print(chinaTotalData['total'].values.tolist()[0])
for value in chinaTotalData['total'].values.tolist():
    confirmlist.append(value['confirm'])
    suspectlist.append(value['suspect'])
    deadlist.append(value['dead'])
    heallist.append(value['heal'])
    deadRatelist.append(value['deadRate'])
    healRatelist.append(value['healRate'])

chinaTotalData['confirm'] = confirmlist
chinaTotalData['suspect'] = suspectlist
chinaTotalData['dead'] = deadlist
chinaTotalData['heal'] = heallist
chinaTotalData['deadRate'] = deadRatelist
chinaTotalData['healRate'] = healRatelist
# ===================================================================
# 创建全国today数据
today_confirmlist = []
today_confirmCutslist = []
for value in chinaTotalData['today'].values.tolist():
    today_confirmlist.append(value['confirm'])
    today_confirmCutslist.append(value['confirmCuts'])

chinaTotalData['today_confirm'] = today_confirmlist
chinaTotalData['today_confirmCuts'] = today_confirmCutslist
# ==================================================================
# 删除total、today两列
chinaTotalData.drop(['total', 'today'], axis=1, inplace=True)
chinaTotalData.head()
# 将其保存到Excel中
chinaTotalData.to_excel('2021-02-03国内疫情.xlsx', index=False)
# 导入对应的绘图工具包


df = pd.read_excel('./2021-02-03国内疫情.xlsx')
# 1.根据绘制国内总疫情图（确诊）
data = df.groupby(by='province', as_index=False).sum()
data_list = list(zip(data['province'].values.tolist(), data['confirm'].values.tolist()))


# 数据格式[(黑龙江,200),(吉林,300),...]

def map_china() -> Map:
    c = (
        Map()
            .add(series_name="确诊病例", data_pair=data_list, maptype='china')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='疫情地图'),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                              pieces=[{"max": 9, "min": 0, "label": "0-9", "color": "#FFE4E1"},
                                                      {"max": 99, "min": 10, "label": "10-99", "color": "#FF7F50"},
                                                      {"max": 499, "min": 100, "label": "100-4999", "color": "#F08080"},
                                                      {"max": 999, "min": 500, "label": "500-999", "color": "#CD5C5C"},
                                                      {"max": 9999, "min": 1000, "label": "1000-9999",
                                                       "color": "#990000"},
                                                      {"max": 99999, "min": 10000, "label": "10000-99999",
                                                       "color": "#660000"}, ]
                                              )
        )
    )
    return c


d_map = map_china()
d_map.render("mapEchrts.html")

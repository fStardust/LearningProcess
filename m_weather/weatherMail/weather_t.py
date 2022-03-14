import json

import requests
import xmltodict

nowcity = "昆明"
utl_str = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + nowcity  # 简单信息使用城市代码 --T.xml +
res_text = requests.get(utl_str, verify=False).text  # 获取数据mxl text 格式
print(res_text)
# res_dict = xmltodict.parse(res_text)
res_dict = json.loads(json.dumps(xmltodict.parse(res_text)))  # 数据mxl Dict 格式 -- 以便分析 +
# res_json = json.dumps(res_dict, ensure_ascii=False)  # 数据  json 标准化 -- 以便存储
print(type(res_dict))

clo = res_dict["resp"]["zhishus"]["zhishu"][0]["detail"] + "\n"   # 万年历 服装推荐
uv = res_dict["resp"]["zhishus"]["zhishu"][1]["detail"] + "\n"   # 万年历 紫外线
skin = res_dict["resp"]["zhishus"]["zhishu"][2]["detail"] + "\n"

recommend = clo + uv + skin

print(type(recommend))

print(recommend)

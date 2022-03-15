import json

# 遍历API建议内容取出其中所有detail--建议 并合并为一个字符串
with open('C:\\Users\\21117\\Desktop\\API.json', 'r', encoding='utf8') as fcc_file:
    res_dict = json.load(fcc_file)
    print(type(res_dict))

print(type(res_dict))

clo = res_dict["resp"]["zhishus"]["zhishu"][0]["detail"] + "\n"  # 万年历 服装推荐
uv = res_dict["resp"]["zhishus"]["zhishu"][1]["detail"] + "\n"  # 万年历 紫外线
# skin = res_dict["resp"]["zhishus"]["zhishu"][2]["detail"] + "\n"

recommend = clo + uv

print(type(recommend))
print(recommend)

zhishus = res_dict["resp"]["zhishus"]["zhishu"]
print(type(zhishus))
print(zhishus)

# 遍历API建议内容取出其中所有detail--建议 并合并为一个字符串 ---核心
per_detail = ""
for i in zhishus:
    per_detail += i["detail"]  # 取出API建议字典各模块中detail内容
    per_detail += "\n"

print(per_detail)

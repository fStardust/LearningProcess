import json

# 遍历API建议内容取出其中所有detail--建议 并合并为一个字符串
with open('C:\\Users\\21117\\Desktop\\API.json', 'r', encoding='utf8') as fcc_file:
    res_dict = json.load(fcc_file)
    print(type(res_dict))

print(type(res_dict))

zhishus = res_dict["resp"]["zhishus"]["zhishu"]
print(type(zhishus))
print(zhishus)

# 遍历API建议内容取出其中所有detail--建议 并合并为一个字符串 ---核心
per_detail = ""
for i in zhishus:
    per_detail += i["detail"]  # 取出API建议字典各模块中detail内容
    per_detail += "\n"

print(per_detail)

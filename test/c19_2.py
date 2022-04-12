import json
import re


def get_json():
    """
    【作用】
     读取本地文件，获取json信息
    【参数】
     无
    【返回】
     json字符串
    """
    # 读取本地文件
    f = open("疫情数据.txt", "r", encoding="utf-8")
    f_content = f.read()
    f.close()

    # json字符串前后关键词
    json_start = "try { window.getAreaStat = "
    # 字符串包含的括号要进行转义
    json_end = "}catch\(e\){}"

    # json字符串正则匹配
    # (.*?)是匹配所有内容
    regular_key = json_start + "(.*?)" + json_end
    # 参数rs.S可以无视换行符，将所有文本视作一个整体进行匹配
    re_content = re.search(regular_key, f_content, re.S)
    # group()用于获取正则匹配后的字符串
    content = re_content.group()

    # 去除json字符串的前后关键词
    content = content.replace(json_start, '')
    # 尾巴要去掉转义符号
    json_end = "}catch(e){}"
    content = content.replace(json_end, '')

    print(content)
    return content


json_content = get_json()


def display_provinces(json_content):
    """
     xiaolanzao, 2022.02.27
    【作用】
     展示省份疫情
    【参数】
     json_content : json字符串
    【返回】
     无
    """
    # 将字符串转化为字典
    json_data = json.loads(json_content)

    # 省份数据展示
    print("全国各省份疫情数据如下：")
    for i in json_data:
        print("【省份名】：" + i["provinceName"])
        print("现存确诊：" + str(i["currentConfirmedCount"]))
        print("累计确诊：" + str(i["confirmedCount"]))
        print("死亡：" + str(i["deadCount"]))
        print("治愈：" + str(i["curedCount"]))
        print()


display_provinces(json_content)


def display_citys(json_content, province_name):
    """
     xiaolanzao, 2022.02.27
    【作用】
     展示城市疫情
    【参数】
     json_content : json字符串
     province_name : 需要查询的省份名
    【返回】
     无
    """
    # 将字符串转化为字典
    json_data = json.loads(json_content)

    # 省份数据展示
    print(province_name + "疫情数据如下：")
    for i in json_data:
        # print(i)
        if (i["provinceName"] == province_name):
            # 读取里面的城市信息
            try:
                citys = i["cities"]
                for ii in citys:
                    print("【城市名】：" + ii["cityName"])
                    print("现存确诊：" + str(ii["currentConfirmedCount"]))
                    print("累计确诊：" + str(ii["confirmedCount"]))
                    print("死亡：" + str(ii["deadCount"]))
                    print("治愈：" + str(ii["curedCount"]))
                    print()
            except Exception as e:
                print(e)
                print("没有相应的城市信息!")


display_citys(json_content, "河北省")

# load T.xml file
import json

import xmltodict


def load_json(xml):
    # 获取xml文件
    xml_file = open(xml, 'r')
    xml_str = xml_file.read()
    print(xml_str)
    print(type(xml_str))
    # 将读取的xml字符串转换为字典
    json_dict = xmltodict.parse(xml_str)
    print(type(json_dict))
    # 将字典转换为json格式的字符串
    json_str = json.dumps(json_dict, indent=2)
    print(json_str)
    print(type(json_str))
    return json_str


load_json('T.xml')

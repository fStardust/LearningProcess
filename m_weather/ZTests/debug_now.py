import os

import pandas as pd

risk_file = os.path.abspath("D:\ProgramTest\LearningProcess\m_weather\information\全国最新风险等级区域.csv")
risk_csv = pd.read_csv(risk_file)


def risk_node(address, test_csv):
    a, b, c, f = 0, 0, 0, 0
    address_index = address[:2]
    for i in range(len(test_csv)):
        if address_index in test_csv['市级单位'][i] or address_index in test_csv['区域'][i] or address_index in \
                test_csv['省级单位'][i]:
            message = "当地有疫情。"
            a += 1
            if test_csv['风险等级'][i] == "中风险":
                b += 1
            else:
                c += 1
            strs = ["共", "个区域。其中低风险地区：", "个。高风险地区：", "个。请勿前往。"]
            risk_message1 = address + message + strs[0] + str(a) + strs[1] + str(b) + strs[2] + str(c) + strs[3]
        else:
            f += 1
            message = "当地无中高风险地区。"
            risk_message2 = address + message
    risk_message = risk_message1 if a != 0 else risk_message2

    return risk_message


a = risk_node("佳木斯市", risk_csv)
print(a)

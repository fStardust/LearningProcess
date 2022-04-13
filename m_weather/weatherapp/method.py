def gbk_trans_utf8(file_path):
    with open(file_path, 'r', encoding='gbk') as f:
        content = f.read()
    print(content)
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(content)


def get_rick_area():
    import csv

    import requests

    url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
    r = requests.get(url)
    response_dict = r.json()

    # response_dict = response_dict.dumps()

    dicts = response_dict['data']
    updatetime = dicts['dateline']
    citymaps = dicts['map']
    count = dicts['count']

    # for item in updatetime:
    #     print('风险地区%s更新时间：%s' % (str(item), str(updatetime[item])))

    results = []

    for item in citymaps:
        for item1 in item:
            for item2 in citymaps[item1]:
                areas = citymaps[item1][item2]
                for area in areas:
                    result = []
                    grade = str(area['grade'])

                    if grade == '1':
                        result.append('中风险')
                    if grade == '2':
                        result.append('高风险')
                    result.append(str(item2))
                    result.append(str(area['city']))
                    result.append(str(area['addr']))

                    results.append(result)

    header = ['风险等级', '省级单位', '市级单位', '区域']
    updatetime = ['更新时间：', updatetime[item]]
    print(updatetime)
    filename = 'D:\ProgramTest\LearningProcess\m_weather\information\全国最新风险等级区域' + '.csv'
    print(filename)
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(results)


def risk_node(address, test_csv):
    risk_message1, risk_message2 = "", ""
    a, b, c, f = 0, 0, 0, 0
    address_index = address[:2]
    for i in range(len(test_csv)):
        if address_index in test_csv['市级单位'][i] or address_index in test_csv['区域'][i] or address_index in test_csv['省级单位'][i]:
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

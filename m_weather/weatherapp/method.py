def gbk_trans_utf8(file_path):
    with open(file_path, 'r', encoding='gbk') as f:
        content = f.read()
    print(content)
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(content)


def get_rick_area():
    import csv
    import requests
    from weatherapp.method import gbk_trans_utf8
    url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
    r = requests.get(url)
    response_dict = r.json()
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

                    results.append(result)
    header = ['风险等级', '省份', '区域']
    header1 = ['更新时间：', updatetime['1']]
    filename = './information/全国最新风险等级区域' + '.csv'
    print(len(results))
    print(filename)
    with open(filename, 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header1)
        f_csv.writerow(header)
        f_csv.writerows(results)
    gbk_trans_utf8(filename)


get_rick_area()

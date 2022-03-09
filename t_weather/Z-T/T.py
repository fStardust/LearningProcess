import re

d = '''
    {
	"data": {
		"yesterday": {
			"date": "8日星期二",
			"high": "高温 25℃",
			"fx": "西南风",
			"low": "低温 12℃",
			"fl": "<![CDATA[3级]]>",
			"type": "晴"
		},
		"city": "昆明",
		"forecast": [
			{
				"date": "9日星期三",
				"high": "高温 25℃",
				"fengli": "<![CDATA[3级]]>",
				"low": "低温 12℃",
				"fengxiang": "西南风",
				"type": "晴"
			},
			{
				"date": "10日星期四",
				"high": "高温 26℃",
				"fengli": "<![CDATA[3级]]>",
				"low": "低温 12℃",
				"fengxiang": "西南风",
				"type": "晴"
			},
			{
				"date": "11日星期五",
				"high": "高温 26℃",
				"fengli": "<![CDATA[3级]]>",
				"low": "低温 14℃",
				"fengxiang": "西南风",
				"type": "晴"
			},
			{
				"date": "12日星期六",
				"high": "高温 25℃",
				"fengli": "<![CDATA[3级]]>",
				"low": "低温 14℃",
				"fengxiang": "西南风",
				"type": "多云"
			},
			{
				"date": "13日星期天",
				"high": "高温 26℃",
				"fengli": "<![CDATA[3级]]>",
				"low": "低温 12℃",
				"fengxiang": "西风",
				"type": "晴"
			}
		],
		"ganmao": "感冒易发期，外出请适当调整衣物，注意补充水分。",
		"wendu": "22"
	},
	"status": 1000,
	"desc": "OK"
}
'''
print(type(d))
# data = '<![CDATA[3级]]>'
# print(type(data))
if 'CDATA' in d:
    r1 = re.split('\\[|\\]', d)
    print(1)
else:
    r1 = d

n = r1.index('CDATA')
print(n)
print(type(r1))
print(r1)

import json

import requests
from pyecharts import options as opts
from pyecharts.charts import Map, Geo
from pyecharts.globals import GeoType, RenderType


url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
data = json.loads(requests.get(url).json()['data'])
china = data['areaTree'][0]['children']
print(china)
china_total = "确诊:" + str(data['chinaTotal']['confirm']) + \
              " 疑似:" + str(data['chinaTotal']['suspect']) + \
              " 死亡:" + str(data['chinaTotal']['dead']) + \
              " 治愈:" + str(data['chinaTotal']['heal']) + \
              " 更新日期:" + data['lastUpdateTime']
excel0 = [data['chinaTotal']['confirm'], data['chinaTotal']['suspect'], data['chinaTotal']['dead'],
          data['chinaTotal']['heal'], data['lastUpdateTime']]
data = []
for i in range(len(china)):
    data.append([china[i]['name'], china[i]['total']['confirm']])
excel1 = data
for i in range(len(china) - 1):
    for j in range(len(china) - 1 - i):
        if excel1[j][1] < excel1[j + 1][1]:
            excel1[j], excel1[j + 1] = excel1[j + 1], excel1[j]
geo = Geo(init_opts=opts.InitOpts(width="1750px", height="800px", bg_color="#404a59", page_title="全国疫情时事报告",
                                  renderer=RenderType.SVG, theme="white"))  # 设置绘图尺寸，背景色
geo.add_schema(maptype="china", itemstyle_opts=opts.ItemStyleOpts(color="rgb(49,60,72)",
                                                                  border_color="rgb(0,0,0)"))  # 中国地图，地图区域颜色，区域边界颜色
geo.add(series_name="geo", data_pair=data, type_=GeoType.EFFECT_SCATTER)  # 设置地图数据，动画方式位涟漪特效 effect scatter
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False), effect_opts=opts.EffectOpts(scale=6))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=0, max_=349),
                    title_opts=opts.TitleOpts(title="全国疫情地图", subtitle=china_total, pos_right="10px", pos_left="center",
                                              pos_top="50px"))
geo.render("chinaMap.html")

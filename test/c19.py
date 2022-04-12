from urllib.request import urlopen
from bs4 import BeautifulSoup


def dxy_data_down(article_url):
    """
    【作用】
     下载疫情数据信息
    【参数】
     article_url : 需要下载数据的地址
    【返回】
     无
    """
    url = urlopen(article_url)
    soup = BeautifulSoup(url, 'html.parser')  # parser解析

    f = open("疫情数据.txt", "w", encoding="utf-8")
    f.write(str(soup))
    f.close()

dxy_data_down("https://ncov.dxy.cn/ncovh5/view/pneumonia")

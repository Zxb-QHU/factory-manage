import csv

from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

def spider():

    csv_title = {
        '项目名称': [], 'url': [], '公告类型': [], '招标方式': [], '地区': [], '时间': []
    }

    AMAZON = 'http://qhszbtbxh.com/page/publicity.html?showType=3'
    driver = webdriver.Firefox()
    driver.get(AMAZON)
    page = BeautifulSoup(driver.page_source, 'lxml')
    for i in range(4):
        if i > 0:
            driver.find_element_by_xpath('//*[@id="publicityPager"]/div[2]/button[6]').click()

        tr_list = etree.HTML(driver.page_source).xpath('//*[@id="publicTable"]/div[2]/table/tbody/tr')
        for tr in tr_list:
            item0 = tr.xpath('./td[1]/a/text()')
            item1 = tr.xpath('./td[2]/text()')
            item2 = tr.xpath('./td[3]/text()')
            item3 = tr.xpath('./td[4]/text()')
            item4 = tr.xpath('./td[5]/text()')
            u = str(tr.xpath('./td[1]/a/@onclick'))
            u = u.split("'")[1]
            csv_title['项目名称'].append(item0[0])
            csv_title['公告类型'].append(item1[0])
            csv_title['招标方式'].append(item2[0])
            csv_title['地区'].append(item3[0])
            csv_title['时间'].append(item4[0])
            csv_title['url'].append(u)

    # print(csv_title)
    ans = pd.DataFrame(csv_title)
    ans.to_csv('./static/bidding.csv', index=False)
    print('update success')

if __name__ == '__main__':
    spider()
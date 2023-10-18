import time
import re
import requests
from lxml import etree
from lxml import html

class WinXin():
    def __init__(self):
        self.url = 'https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=y&_sug_type_=&type=2&query=%E9%A3%8E%E6%99%AF'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
        }
        self.cookie = [
            'ABTEST=0|1697507990|v1; SUID=7D1F0A1B2C83A20A00000000652DEA96; IPLOC=CN5000; SUID=7D1F0A1B8530A40A00000000652DEAA3; SUV=0093CE531B0A1F7D652DEAA3E8558742; SNUID=187A6F7E646263BB8188A47E65B2F0DC',
            'ABTEST=8|1697416064|v1; SUID=7D1F0A1B2C83A20A00000000652C8380; IPLOC=CN5000; SUID=7D1F0A1B5019870A00000000652C8380; SUV=00C360111B0A1F7D652C838156F90819; ariaDefaultTheme=undefined; PHPSESSID=ecl8vqgnj24eghocua5k71me96; seccodeErrorCount=1|Tue, 17 Oct 2023 04:50:48 GMT; SNUID=B6D4C1D7CBCACC2EF9469A85CC6E158F; seccodeRight=success; successCount=1|Tue, 17 Oct 2023 04:50:54 GMT',
            'ABTEST=8|1697416064|v1; SUID=7D1F0A1B2C83A20A00000000652C8380; IPLOC=CN5000; SUID=7D1F0A1B5019870A00000000652C8380; SUV=00C360111B0A1F7D652C838156F90819; SNUID=B6D4C1D7CBCACC2EF9469A85CC6E158F; ariaDefaultTheme=undefined',
            'ABTEST=0|1697507990|v1; SUID=7D1F0A1B2C83A20A00000000652DEA96; IPLOC=CN5000; SUID=7D1F0A1B8530A40A00000000652DEAA3; SUV=0093CE531B0A1F7D652DEAA3E8558742; SNUID=187A6F7E646263BB8188A47E65B2F0DC',
        ]
        self.data_dict = {}
        self.data_list = []


    def add_data(self, **kwargs):
        for key, value in kwargs.items():
            self.data_dict[key] = value
        if len(self.data_dict) == 3:
            self.data_list.append(self.data_dict)
            self.data_dict = {}

    def get_proxy(self):
        '''获取代理，返回代理'''
        ip_list = []
        ip_url = 'https://api.hailiangip.com:8522/api/getIpEncrypt?dataType=0&encryptParam=i6OcePKr4Cq0wPH1UJ%2FCOyBYXf0wSdR0KIhVhoMMPHvy912xFHA3Hogn7b2rQpv2KfD%2Bin%2FOC0BaoQRr%2F3cgG4OyycM%2FAAWa%2FiAuoGqjfUtYs5LyfdnXeU6tPZyaATqNpustHsEAeWpxI7uVTI2aIl9Pmr35mZgGzhPeXj0JQd1XwMMY2Pp7wRNtgRIJmPbHvs3ERyFHZ9FAgNS8WBDIMt0Jv%2FQlqwlcd4gkrYI6AFg%3D'
        resp = requests.get(ip_url).json()['data']
        for data in resp:
            ip_list.append({
                "https": "https://" + str(data['ip']) + ':' + str(data['port']),
            })
        print('ip_list:')
        print(ip_list)
        while ip_list:
            for i in range(2):
                proxy = ip_list[-1]
                yield proxy
            ip_list.pop()


    def first_fetch(self):
        '''第一次访问首地址，并且返回详情页链接'''
        response = requests.get(url=self.url, headers=self.headers).text
        e = etree.HTML(response)
        div = e.xpath("//div[@class='news-box']")[0]
        # print(html.tostring(div, encoding='utf-8', method='html'))
        href_list = div.xpath('./ul//div[@class="txt-box"]/h3/a/@href')
        title_split = div.xpath('./ul//div[@class="txt-box"]')
        for title_split_unit in title_split:
            title_d = ''.join(title_split_unit.xpath('./h3/a//text()'))
            self.add_data(title=title_d)
            author_d = title_split_unit.xpath('./div[@class="s-p"]/span[1]/text()')[0]
            self.add_data(author=author_d)
            href = href_list.pop(0)
            self.fetch_detial_href(href)
            time.sleep(1)





    def fetch_detial_href(self, href):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Cookie': 'ABTEST=0|1697507990|v1; SUID=7D1F0A1B2C83A20A00000000652DEA96; IPLOC=CN5000; SUID=7D1F0A1B8530A40A00000000652DEAA3; SUV=0093CE531B0A1F7D652DEAA3E8558742; SNUID=187A6F7E646263BB8188A47E65B2F0DC',  # 要验证就是cookie过期了或者被封了
        }
        '''访问详情页链接，并获取数据'''
        # proxy_list = self.get_proxy()
        time.sleep(1)
        url = 'https://weixin.sogou.com/' + href
        # proxy = proxy_list.__next__()
        # print(proxy)
        # print(url)
        response = requests.get(url=url, headers=headers).text
        e = etree.HTML(response)
        url_redirected = ''
        url_splits = re.findall("url \+= '(.*?)';", response)
        for url_split in url_splits:
            url_redirected += url_split
            url_redirected.replace("@", "")
            # print(url_redirected)
            self.parse_detail(url_redirected)


    def parse_detail(self, detail_url):
        response = requests.get(url=detail_url, headers=self.headers).text
        e = etree.HTML(response)
        whether_deleted = e.xpath('/html/body/div/div[2]/div/text()')[0]
        if whether_deleted == '该内容已被发布者删除':
            print(whether_deleted)
        else:
            time_d = re.search("var createTime = '(.*?)';", response).group(1)
            self.add_data(time=time_d)
            print(self.data_list)




    def main(self):
        href_list = self.first_fetch()

if __name__ == '__main__':
    go = WinXin()
    go.main()
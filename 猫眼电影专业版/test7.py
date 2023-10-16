import requests
import execjs
import json
import time
import re
from font.parse_font import ParseFont



class MaoYan():
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': '_lxsdk_cuid=18b34e9de35c8-08fcca423466f7-745d5774-4b9600-18b34e9de35c8; _lxsdk=18b34e9de35c8-08fcca423466f7-745d5774-4b9600-18b34e9de35c8; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic',
            'Host': 'piaofang.maoyan.com',
            'Referer': 'https://piaofang.maoyan.com/dashboard',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
            'X-FOR-WITH': '9qt4ciIZeNk94QYMW+BbOWXl4oBBGqPP2LOEnqovUb2ov3c90lOmnFljMmxXN6aDIz7PFqRJ5R0G5Ou0FQEh53378IvT6AiCkKFDLV2s2sxSr/gHqJZHFHj5RK2GFmlnnRdRz2iIBEyOcWhlh6/2Vo7gm5ZkOd6iivS9kS5bit5K5cxs6QxhkefrZ9mMZ9Up1pRa1Zm9CpjCsS2n5Sv06A==',
            'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
        }
        self.url = ''

    def get_Enkey(self):
        content = open('./maoyan.js', 'r').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        EncKey = data_js.call('get_key')
        return EncKey

    def fetch_page(self, EncKey):
        timeStamp = int(time.time() * 1000)
        params = {
            'movieId': '1298384',
            'orderType': '0',
            'uuid': '18b34e9de35c8-08fcca423466f7-745d5774-4b9600-18b34e9de35c8',
            'timeStamp': timeStamp,
            'User-Agent': 'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTguMC4yMDg4LjQ2',
            'index': '961',
            'channelId': '40009',
            'sVersion': '2',
            'signKey': EncKey,
        }

        url = 'https://piaofang.maoyan.com/dashboard-ajax'

        response = requests.get(url=url, headers=self.headers, params=params)
        res = response.text
        return res

    def font_parse(self, response):
        response = response.replace('&#x', '0x')
        css_rule = json.loads(response)['fontStyle']
        url_postfix = re.search(r',url\("(.*)"\);}', css_rule).group(1)
        font_url = 'https:' + url_postfix
        font_file = requests.get(url=font_url).content

        with open('./font/font.woff', 'wb') as f:
            f.write(font_file)
            print('字体文件下载成功，正在解析字体...')

        font_p = ParseFont()
        font_p.path = './font/font.woff'
        font_data_dict = font_p.font_analysis()
        for key, value in font_data_dict.items():
            response = re.sub(key, value, response)
        new_response = response
        return new_response

    def get_data(self, res):
        data_list = json.loads(res)['movieList']['data']['list']
        for data in data_list:
            film_name = data['movieInfo']['movieName']
            releaseInfo = data['movieInfo']['releaseInfo']
            sumBoxDesc = data['sumBoxDesc']
            boxSplitUnit = data['boxSplitUnit']['num'].replace(';', '') + '万'
            splitBoxRate = data['splitBoxRate']
            showCount = data['showCount']
            showCountRate = data['showCountRate']
            avgShowView = data['avgShowView']
            avgSeatView = data['avgSeatView']
            print('电影名字：%s，上映时间：%s，总上座：%s，综合票房：%s，票房占比：%s，排片场次：%s，排片占比：%s，场均人次：%s, 上座率%s' %
                  (film_name, releaseInfo, sumBoxDesc, boxSplitUnit, splitBoxRate, showCount, showCountRate, avgShowView, avgSeatView))

    def run(self):
        EnKey = self.get_Enkey()
        response = self.fetch_page(EnKey)
        new_response = self.font_parse(response)
        self.get_data(new_response)


if __name__ == '__main__':
    go = MaoYan()
    go.run()



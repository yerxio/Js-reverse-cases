import json

import requests
import execjs

class JuChao():
    def __init__(self):
        content = open('./JuChao1.js', 'r').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        EncKey = response_parsed = data_js.call('')
        self.url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
        self.headers = {
            'Accept':'*/*',
            'Accept-EncKey':EncKey,
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection':'keep-alive',
            'Content-Length':'27',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1697400092; MALLSSID=7177644774476634695A57733959412B584C3478324668734149552B4E4C6D646A5A4B776A6B6A54464B6F616C6D51734C766944626E514136516A3748486F62; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1697400109',
            'Host':'webapi.cninfo.com.cn',
            'Origin':'https://webapi.cninfo.com.cn',
            'Referer':'https://webapi.cninfo.com.cn/',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46',
            'X-Requested-With':'XMLHttpRequest',
            'sec-ch-ua':'"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'Windows',
        }
        self.data = {
            'tdate': '2023-10-13',
            'market': 'SZE'
        }

    def fetch_page(self):
        res = requests.post(url=self.url, headers=self.headers, data=self.data).text
        return res
    def parse_data(self, res):
        data_list = json.loads(res)['records']
        for data in data_list:
            Stock_code = data['证券代码']
            profile = data['证券简称']
            Trading_date = data['交易日期']
            open = data['开盘价']
            close = data['最高价']
            high = data['最低价']
            low = data['收盘价']
            Trading_number = data['成交数量']
            print('证券代码:%s、证券简称:%s、交易日期:%s、开盘价:%s、最高价:%s、最低价:%s、收盘价:%s、成交数量（股）:%s'%(Stock_code, profile, Trading_date, open, close, high, low, Trading_number))

    def run(self):
        res = self.fetch_page()
        self.parse_data(res)


if __name__ == '__main__':
    go = JuChao()
    go.run()


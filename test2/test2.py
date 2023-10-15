import datetime

import execjs
import requests
import json

class YiEn():
    def __init__(self):
        self.url = 'https://www.endata.com.cn/API/GetData.ashx'
        self.headers = {
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '46',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.endata.com.cn',
            'Origin': 'https://www.endata.com.cn',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows'
        }
        self.data = {
            'year': '2023',
            'MethodName': 'BoxOffice_GetYearInfoData'
        }

    def fetch_page(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.data)
        return response.text

    def parse_response(self, response):
        content = open('./yien.js', 'r', encoding='utf-8').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        response_parsed = data_js.call('parse_e', response)
        movie_list = json.loads(response_parsed)['Data']['Table']
        return movie_list

    def content_parse(self, data_list):
        for i, j in enumerate(start=1, iterable=data_list):
            movie_rank = i
            name = j['MovieName'].strip()
            genre = j['Genre_Main'].strip()
            box_office = j['BoxOffice']
            prince_avr = j['AvgPrice']
            people_avr = j['AvgPeoPle']
            nation = j['Area']
            screen_time = j['ReleaseTime']
            print(f'{movie_rank}\t\t{name:<12}\t{genre:<4}\t{box_office:<8}\t{prince_avr:<10}{people_avr:^10}{nation:^10}{screen_time}')

    def run(self):
        response = self.fetch_page()
        data_list = self.parse_response(response)
        print('电影排行\t影片名称\t\t\t类型\t\t总票房\t\t平均票价\t\t场次人数\t\t国家\t\t上映时间')
        self.content_parse(data_list)
        print('*' * 20, '\n成功获取艺恩电影排行榜，获取时间：', datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))




if __name__ == '__main__':
    movie = YiEn()
    movie.run()
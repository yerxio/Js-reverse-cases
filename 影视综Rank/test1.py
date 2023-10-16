import requests
import execjs
import datetime

class YinShi():
    def __init__(self):
        self.url = 'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank?channel=movielist&sign=5f3cce6a40c09a221b21104cc98436a3'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43"
        }

    def fetch_page(self):
        response = requests.get(url=self.url, headers=self.headers)
        e = response.json()
        return e

    def parse_data(self, e):
        content = open('./new.js', 'r', encoding='utf-8').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        response_parsed = data_js.call('a', e)
        return response_parsed

    def parse_content(self, response_parsed):
        data_list = response_parsed['data']['listOfRank']
        for data in data_list:
            rank = data['rank']
            object_name = data['object_name']
            active_audience = data['user_day_num']
            user_change_num = data['user_change_num']
            trend = data['rank_change']
            print(f'电影榜电影排名:{rank}，电影名称:{object_name}，活跃受众:{active_audience}，受众变化:{user_change_num}，趋势:{trend}')

    def run(self):
        e = self.fetch_page()
        response_parsed = self.parse_data(e)
        self.parse_content(response_parsed)
        print('*'*20,'\n成功获取影视综电影排行榜，获取时间：', datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))





if __name__ == '__main__':
    get_movie = YinShi()
    get_movie.run()
import requests
import execjs
import json
import os


class JiJiambizhi():
    def __init__(self):
        self.url = 'https://api.zzzmh.cn/bz/v3/getData'
        self.headers = {
            'Accept-Encoding':'gzip, deflate, br',
            'Content-Length':'95',
            'Content-Type':'application/json;charset=UTF-8',
            'Origin':'https://bz.zzzmh.cn',
            'Referer':'https://bz.zzzmh.cn/',
            'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Site':'same-site',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        self.data = {"size": 24, "current": 1, "sort": 0, "category": 0, "resolution": 0, "color": 0, "categoryId": 0, "ratio": 0}
    def fetch_page(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.data)
        print(response.text)
        return response.text

    def parse_data(self, response):
        content = open('./one.js', 'r', encoding='utf-8').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        data_list = json.loads(data_js.call('parse_e', response))['list']
        for data in data_list:
            id = data['i']
            print(f'成功获取图片ID：{id}')
        return data_list

    def download_img(self, id):
        url_0 = 'https://api.zzzmh.cn/bz/v3/getUrl/96b26df8437c44e899f67d2fee4777ae21'
        headers = {
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '__gads=ID=e9c27e45e086bbbc-22dc085ad6e70010:T=1697263341:RT=1697289877:S=ALNI_MZkrWAYzp1Jl-zQ98VEkr71nbsE1A; __gpi=UID=00000c602de8e914:T=1697263341:RT=1697289877:S=ALNI_MY9qELxV6SwHVjFhhjWgbR9milWig',
            'Referer': 'https://bz.zzzmh.cn/',
            'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': 'Windows',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url_0, headers=headers)
        print(response.headers)
        # auth_key = None
        # url = f'https://cdn2.zzzmh.cn/wallpaper/origin/{id}.jpg/fhd?auth_key={auth_key}'
        response = requests(url=url_0, headers=headers)
        print(response.headers)

    def save_img(self, img_name, img_content):

        if not os.path.exists('./img'):
            os.mkdir('./img')
        with open('./img' + img_name + 'jpg', 'wb') as f:
            f.write(img_content)

    def run(self):
        response = self.fetch_page()
        data_list = self.parse_data(response)
        for data in data_list:
            id = data['i']
            img_content = self.download_img(id)
            self.save_img(img_name=id, img_content=img_content)


if __name__ == '__main__':
    get_img = JiJiambizhi()
    get_img.fetch_page()
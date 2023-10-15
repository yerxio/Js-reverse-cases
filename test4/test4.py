import json
import os
import time

import execjs
import requests


class JiJiambizhi():
    def __init__(self):
        self.url = 'https://api.zzzmh.cn/bz/v3/getData'
        self.headers = {
            "content-type": "application/json;charset=UTF-8",
        }

    def fetch_page(self, data):
        response = requests.post(url=self.url, headers=self.headers, data=json.dumps(data))
        res = json.loads(response.text)
        result = res['result']
        return result

    def parse_data(self, response):
        content = open('./one.js', 'r', encoding='utf-8').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        result = json.loads(data_js.call('parse_e', response))
        data_list = result['list']
        pic_list = []
        for data in data_list:
            pic_list.append({
                't': data['t'],
                'id': data['i']
            })
        return pic_list

    def download_img(self, pic):
        headers = {
            'Referer': 'https://bz.zzzmh.cn/',
        }
        id = str(pic['id']) + str(pic['t']) + '9'
        download_url = f'https://api.zzzmh.cn/bz/v3/getUrl/{id}'
        response = requests.get(url=download_url, headers=headers)
        return response.content

    def save_img(self, img_data, img_content):
        if not os.path.exists('./img'):
            os.mkdir('./img')

        if img_data['t'] == 1:
            with open('./img/' + img_data['id'] + '.png', 'wb') as f:
                f.write(img_content)
                id = img_data['id']
                print(f'图片{id}保存成功')

        if img_data['t'] == 2:
            with open('./img/' + img_data['id'] + '.jpg', 'wb') as f:
                f.write(img_content)
                id = img_data['id']
                print(f'图片{id}保存成功')

    def run(self):
        n = int(input('请输入要爬取多少页：'))
        for i in range(1, n + 1):
            print('正在获取第{}页'.format(i))
            data = {
                "size": '24', "current": f'{i}', "sort": '0', "category": '0', "resolution": '0', "color": '0',
                "categoryId": '0', "ratio": '0'
            }
            response = self.fetch_page(data)
            pic_list = self.parse_data(response)
            for pic in pic_list:
                img_content = self.download_img(pic)
                time.sleep(0.2)
                self.save_img(img_data=pic, img_content=img_content)
                time.sleep(0.2)


if __name__ == '__main__':
    get_img = JiJiambizhi()
    get_img.run()

import requests
import execjs
import json
import os


class JiJiambizhi():
    def __init__(self):
        self.url = 'https://api.zzzmh.cn/bz/v3/getData'
        self.headers = {
            "content-type": "application/json;charset=UTF-8",
        }
        self.data = {
            "size":'24', "current":'1', "sort":'0', "category":'0', "resolution":'0', "color":'0', "categoryId":'0', "ratio":'0'
        }
        self.response = "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",

    def fetch_page(self):
        response = requests.post(url=self.url, headers=self.headers, data=json.dumps(self.data))
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
                't':data['t'],
                'id':data['i']
            })
        return pic_list

    def download_img(self, pic):
        headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '__gads=ID=e37659748ae0a4c1-229ba202e6e40034:T=1697264065:RT=1697279756:S=ALNI_Mai1MvgcfGAUBPLps5N1T3CXw9lzw; __gpi=UID=00000c602f5d5808:T=1697264065:RT=1697279756:S=ALNI_MY9-1882Y9vy--lnqnX5enlcpDGEA',
        'Referer': 'https://bz.zzzmh.cn/',
        'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
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
        response = self.response  # getData这个网址不知道为什么无法访问，先用自己从浏览器获取的数据
        pic_list = self.parse_data(response)
        for pic in pic_list:
            img_content = self.download_img(pic)
            self.save_img(img_data=pic, img_content=img_content)

if __name__ == '__main__':
    get_img = JiJiambizhi()
    get_img.run()





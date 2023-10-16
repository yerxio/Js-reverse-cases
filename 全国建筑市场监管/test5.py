import requests
import execjs
import json
import pymysql

class ShiChang():
    def __init__(self):
        self.coon = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='qq250380',
            db='13_class'
        )
        self.cursor = self.coon.cursor()

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

    def fetch_page(self, url):
        e = requests.get(url=url, headers=self.headers).text
        return e

    def parse_data(self, e):
        content = open('./jzsc.js', 'r').read()
        data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
        response_parsed = data_js.call('parse_e', e)
        return response_parsed

    def get_data(self, response_parsed):
        detail_list = []
        data_dict = json.loads(response_parsed)
        data_list = data_dict['data']['list']
        for data in data_list:
            Enterprise_name = data['QY_NAME']
            Legal_representative = data['QY_FR_NAME']
            Place_of_registration = data['QY_REGION_NAME']
            detail_list.append((Enterprise_name, Legal_representative, Place_of_registration))
        return detail_list

    def save_to_mysql(self, detail_list):
        for detail in detail_list:
            Enterprise_name = detail[0]
            Legal_representative = detail[1]
            Place_of_registration = detail[2]
            try:
                sql = 'insert into mohurd(Enterprise_name, Legal_representative, Place_of_registration) values (%s, %s, %s)'
                params = (Enterprise_name, Legal_representative, Place_of_registration)
                self.cursor.execute(sql, params)
                self.coon.commit()
                print(f'企业名称:{Enterprise_name}、法定代表:{Legal_representative}、注册地:{Place_of_registration}，保存成功')
            except Exception as e:
                print(e)
                self.coon.rollback()


    def run(self):
        n = 1
        for i in range(n):
            print(f'正在获取第{i+1}页数据.')
            url = f'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?pg={i}&pgsz=15&total=0'
            e = self.fetch_page(url)
            response_parsed = self.parse_data(e)
            detail_list = self.get_data(response_parsed)
            self.save_to_mysql(detail_list)

if __name__ == '__main__':
    go = ShiChang()
    go.run()
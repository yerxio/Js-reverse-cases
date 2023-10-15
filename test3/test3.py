import execjs
import requests
import time
import json

def encodeapi():
    content = open('./key.js', 'r', encoding='utf-8').read()
    data_js = execjs.compile(content, cwd=r"C:\Users\God\AppData\Roaming\npm\node_modules")
    x_apikey = data_js.call('getApiKey')
    return x_apikey

X_Apikey = encodeapi()

t = int(time.time()*1000)
url = f'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t={t}&offset=0&txType=&limit=20&curType='
headers = {
            'Accept':'application/json',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'App-Type':'web',
            'Referer':'https://www.oklink.com/cn/btc/tx-list',
            'Sec-Ch-Ua':'"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'X-Apikey':X_Apikey,
            'X-Cdn':'https://static.oklink.com',
            'X-Locale':'zh_CN',
            'X-Utc':'8',
            'X-Zkdex-Env':'0'
        }
res = requests.get(url=url, headers=headers)
response = json.loads(res.text)
data_list = response['data']['hits']


for data in data_list:
    hash = data['hash']
    blockHeight = data['blockHeight']
    blocktime = str(data['blocktime'])
    time_get = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(blocktime)))
    inputsCount = data['inputsCount']
    outputsCount = data['outputsCount']
    inputsValue = data['inputsValue']
    fee = int(data['fee'])/(1e+8)
    print(f'交易哈希:{hash}，区块:{blockHeight}，时间:{time_get}，输入:{inputsCount}，输出:{outputsCount}，输入数量:{inputsValue} BTC，手续费:{fee} BTC')







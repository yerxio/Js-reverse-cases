# Task
* Target website： https://bz.zzzmh.cn/index
* Task requirement： use requests crawl pictures. 
---
# work description
1. I can't use requests get the responst.
2. I reversed the js code, and decrypt the ciphertext of response.
3. But in the response, there is no url of any picture, and there's  ID of every picture.
4. I got the url which can download picture with ID supported. ~~But it needs 'authkey'~~.\
5. ~~Maybe I can reverse js-code find how to generate 'authkey', then download pictures.~~

* The plaintext I decrypted, has two useful attributes, 'i' and 't'.
* T can determine the postfix of picture is 'png' or 'jpg', and determine the complete url used in the subsequent procedure. And 'i' is the id to picture.
* "auth_key" is provided by the server 
* When requensts the url:https://api.zzzmh.cn/bz/v3/getUrl/{id}, it will redirect to url https://cdn2.zzzmh.cn/wallpaper/origin/{id}.jpg?response-content-disposition=attachment&auth_key={}. the post url contains img_content, but we don't know auth_key.
* use requests.get the url:https://api.zzzmh.cn/bz/v3/getUrl/{id} can get the picture without auth_key, ~~but it's strange that use browser like chrome or edge cant get any picture~~(the url need headers{'Referer': 'https://bz.zzzmh.cn/'}, when Referer supported, the status_code is 200, and can get the img_data, but in browser, it will tell you some error). 
* The {id} in the url is constituted by 'i' and 't' and '9'. 
* but use the headers of the url:https://api.zzzmh.cn/bz/v3/getUrl/{id} provided by browser couldn't get picture information. But when I use it which from url:https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=225&li=gda_r20231011&jk=1836487286614186&rc=, can through requests.get(url='https://api.zzzmh.cn/bz/v3/getUrl/{id}') download the picture.


# chatGpt help me solve a crucial problem
He said:\
在使用 Python 的 requests 库发送 HTTP 请求时，当我们设置 "content-type": "application/json"（意味着我们告诉服务器我们正在发送 JSON 格式的数据）时，我们需要确保我们发送的 body 数据确实是一个 JSON 格式的字符串。这就是为什么我们使用 json.dumps() 函数的原因。


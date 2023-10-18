import requests
def ttt():
    print('执行了一次')
    ip_list = []
    ip_url = 'https://api.hailiangip.com:8522/api/getIpEncrypt?dataType=0&encryptParam=i6OcePKr4Cq0wPH1UJ%2FCOyBYXf0wSdR0KIhVhoMMPHvy912xFHA3Hogn7b2rQpv2KfD%2Bin%2FOC0BaoQRr%2F3cgG4OyycM%2FAAWa%2FiAuoGqjfUtYs5LyfdnXeU6tPZyaATqNpustHsEAeWpxI7uVTI2aIl9Pmr35mZgGzhPeXj0JQd1XwMMY2Pp7wRNtgRIJmPbHvs3ERyFHZ9FAgNS8WBDIMt0Jv%2FQlqwlcd4gkrYI6AFg%3D'
    resp = requests.get(ip_url).json()['data']
    for data in resp:
        ip_list.append({
            'ip': data['ip'],
            'port': data['port']
        })
    print('ip_list:')
    print(ip_list)
    while ip_list:
        proxy = 'https://' + str(ip_list[-1]['ip']) + ':' + str(
            ip_list[-1]['port'])
        yield proxy
        ip_list.pop()
        print(ip_list)


# n = ttt()
# for i in range(6):
#     print(n.__next__())
#
# for i in range(2):
#     print(ttt().__next__())



def get_ip():
    ip_list = []
    ip_url = 'https://api.hailiangip.com:8522/api/getIpEncrypt?dataType=0&encryptParam=i6OcePKr4Cq0wPH1UJ%2FCOyBYXf0wSdR0KIhVhoMMPHvy912xFHA3Hogn7b2rQpv2KfD%2Bin%2FOC0BaoQRr%2F3cgG4OyycM%2FAAWa%2FiAuoGqjfUtYs5LyfdnXeU6tPZyaATqNpustHsEAeWpxI7uVTI2aIl9Pmr35mZgGzhPeXj0JQd1XwMMY2Pp7wRNtgRIJmPbHvs3ERyFHZ9FAgNS8WBDIMt0Jv%2FQlqwlcd4gkrYI6AFg%3D'
    resp = requests.get(ip_url).json()['data']
    for data in resp:
        ip_list.append({
            "http": "http://" + str(data['ip']) + ':' + str(data['port']),
        })
    print('ip_list:')
    print(ip_list)

    while ip_list:
        for i in range(2):
            proxy = ip_list[-1]
            yield proxy
        ip_list.pop()
    else:
        yield None


url = "http://httpbin.org/ip"
p = get_ip()
for i in range(11):
    prox = p.__next__()
    print(prox)
    r = requests.get(url, proxies=prox)
    print(r.text)


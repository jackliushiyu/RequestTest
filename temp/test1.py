import requests,json

data = {'name': 'xaioxiong', 'pwd': '111'}
url = 'http://127.0.0.1/index'


def send_get():
    res = requests.get(url, data)
    return res


def send_post(url, data):
    res = requests.post(url, data)
    return res

if __name__ == '__main__':
    for i in range(2, 100):
        flag = True
        for j in range(2, int(i / 2) + 1):
            if i % j == 0 & i != 2:
                flag = False
                break
        if flag:
            print(i)
    pass

eval()
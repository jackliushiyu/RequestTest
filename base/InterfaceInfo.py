import csv
import requests


class InterfaceInfo:
    def get_cookies(self, method, url, data=None):
        if method == 'get' or method == 'GET':
            res = requests.get(url=url, data=data)
        elif method == 'post' or method == 'POST':
            res = requests.post(url=url, data=data)
        else:
            raise Exception('目前仅支持get和post两种请求方式')
        cookies_data = {}
        if res.cookies.items():
            for k, v in res.cookies.items():
                cookies_data[k] = v
            return cookies_data
        else:
            return None

    def get_request(self, method, url, data=None, cookies=None):
        if method == 'get' or method == 'GET':
            res = requests.get(url=url, data=data, cookies=cookies)
            return res
        elif method == 'post' or method == 'POST':
            res = requests.post(url=url, data=data, cookies=cookies)
            return res
        else:
            raise Exception('目前仅支持get和post两种请求方式')

    def get_csv_data(self, file, mode='r', encoding='utf8'):
        l = []
        with open(file=file, mode=mode, encoding=encoding) as f:
            csv_data = csv.reader(f)
            flag = True
            for i in csv_data:
                if flag:
                    flag = False
                    continue
                l.append(tuple(i))
        return l
if __name__ == '__main__':
    t = InterfaceInfo()
    csv_data_s = t.get_csv_data(r'C:\Users\THINK\Desktop\test.csv')
    for m in csv_data_s:
        res_s = t.get_request(m[0], m[1], eval(m[2]))
        print(res_s.json())
    pass

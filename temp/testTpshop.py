import requests

login_url = 'http://www.tpshop.com/index.php?m=Home&c=User&a=do_login'
verify_url = 'http://www.tpshop.com/index.php/Home/User/verify.html'
list_url = 'http://www.tpshop.com/index.php/Home/User/order_list.html'
cart_list = 'http://www.tpshop.com/index.php/Home/Cart/ajaxCartList.html'
data = {'username': '13800138006',
        'password': '123456',
        'referurl': 'http://www.tpshop.com/',
        'verify_code': '111'
        }


res = requests.get(verify_url, data)
print(res.cookies)
cookies_data = {}
for k, v in res.cookies.items():
    cookies_data[k] = v
print(cookies_data)

r = requests.post(login_url, data=data, cookies=cookies_data)

res = requests.get(list_url, cookies=cookies_data)

# for i in res.text.split('\n'):
#     if '订单号' in i:
#         print(i.split('"">')[1].split('</a>')[0])
#     pass

# session = requests.session()
#
# session.get(verify_url)
# session.post(login_url, data=data)
# res = session.get(list_url)
# res = session.get(cart_list)
# for i in res.text.split('\n'):
#     if '订单号' in i:
#         print(i.split('"">')[1].split('</a>')[0])
#     pass
# res = requests.get(cart_list, cookies=cookies_data)
# # print(res.text)
# for i in res.text.split('\n'):
#     if 'vertical-align:middle' in i:
#         print(i.split('">')[1].split('</a>')[0])
url = 'http://localhost/phpwind/upload/login.php'
url3 = 'http://localhost/phpwind/upload/login.php#breadCrumb'
url2 = 'http://localhost/phpwind/upload/apps.php?q=article'
data2 = {
    'jumpurl': 'http://localhost/phpwind/upload/index.php',
    'step': '2',
    'pwuser': 'mike',
    'pwpwd': '123456',
    'head_login': '',
    'lgt': '0'
}
data3={
    "forward": "",
    "jumpurl": "index.php",
    "step": "2",
    "lgt": "0",
    "pwuser": "admin",
    "pwpwd": "123456",
    "hideid": "0",
    "cktime": "31536000",
    "submit": ""
}
session = requests.session()
session.post(url3, data=data3)
res = session.get(url2)
print(res.text)
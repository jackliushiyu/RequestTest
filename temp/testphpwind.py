from base.InterfaceInfo import InterfaceInfo


url = 'http://localhost/phpwind/upload/register.php'
data = {
    "forward": "",
    "step": "2",
    "_hexie": "48eed561",
    "regname": "mike2",
    "regpwd": "123456",
    "regpwdrepeat": "123456",
    "regemail": "mike2@163.com",
    "apartment": "110101",
    "rgpermit": "1"}
driver = InterfaceInfo()
# res = driver.get_request('post', url, data)
# print(res.text)
data2 = {
    'jumpurl': 'http%3A%2F%2Flocalhost%2Fphpwind%2Fupload%2Findex.php',
    'step': '2',
    'pwuser': 'mike2',
    'pwpwd': '123456',
    'head_login': '',
    'lgt': '0'
}
data3 = {
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
url3 = 'http://localhost/phpwind/upload/login.php#breadCrumb'

login_url = 'http://localhost/phpwind/upload/login.php'
my_blog_url = 'http://localhost/phpwind/upload/apps.php?q=article'

cookie_data = driver.get_cookies('post', url3, data3)
print(cookie_data)
# res = driver.get_request('post', url3, data2, cookies=cookie_data)
# print(res)
r = driver.get_request('get', my_blog_url, data3, cookies=cookie_data)
print(r.text)


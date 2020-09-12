import unittest

from base.InterfaceInfo import InterfaceInfo


class PhpWindLogin(unittest.TestCase):
    url = 'http://localhost/phpwind/upload/login.php'
    data = {
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

    def test_phpwind_login(self):
        res = InterfaceInfo().get_request('post', self.url, self.data)
        self.assertIn('admin', res.text, msg='登录失败')

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/index', methods=['get', 'post'])
def index():
    user_name = request.values.get('name')
    pwd = request.values.get('pwd')
    if user_name and pwd:
        if user_name == 'xiaoming' and pwd == '111':
            resu = {'code': '200', 'message': '登录成功'}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code': '-1', 'message': '帐号密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(resu, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')

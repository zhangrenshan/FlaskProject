from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    name = 'Jack'
    return render_template('index.html', **locals())


@app.route('/login/')
def login():
    return render_template('login.html', **locals())


# 注意点： 在初期，执行哪个文件下的视图函数和路由，就运行哪个文件
if __name__ == '__main__':
    # host 地址       port 端口     debug 是否打开调试
    app.run(host='127.0.0.1', port=8000, debug=True)    # 启动这个应用
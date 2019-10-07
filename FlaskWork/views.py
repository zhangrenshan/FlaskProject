"""
flask当中，可以直接创建应用，进行开发，而django是现有项目，再创建应用，但是在工作当中flask
也会遇到多应用问题，也需要有项目框架，只不过这个框架被称为 蓝图（blueprint）
"""

from flask import Flask


# 创建一个应用
app = Flask(__name__)


@app.route("/")             # 路由
def index():                # 视图
    return "hello world"


if __name__ == "__main__":
    # 三个参数（host:本地登录； port:端口； debug:调试）
    app.run(host="127.0.0.1", port=8000, debug=True)      # 启动这个应用

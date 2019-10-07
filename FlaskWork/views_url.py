
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world，I am Flask"


@app.route("/list/")
def list():
    return "hello list"


@app.route("/content/<username>/<int:age>/")
def content(age, username):
    return "hello ,I am %s,I am %s years old"%(username, age)


# methods参数默认GET,如果是POST，需在GET的原基础上添加（而不是删除GET）
@app.route("/method/", methods=["GET", "POST"])
def method():
    return "hello ,this is mentod"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)  # 启动这个应用

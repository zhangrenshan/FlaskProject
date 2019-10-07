import sys
from models import models
from views import app
from flask_script import Manager

# print(sys.argv)
# command = sys.argv[1]
# if command == 'migrate':
#     models.create_all()
# elif command == 'runserver':
#     app.run(host='127.0.0.1', port=8000, debug=True)

manage = Manager(app)

@manage.command
def hello():
    print('hello')


@manage.command
def migrate():
    models.create_all()


# 如果想不用再Terminal命令行输入命令，直接在项目里运行
# 需要在Edit Config中更改Target为manage.py


if __name__ == '__main__':
    manage.run()

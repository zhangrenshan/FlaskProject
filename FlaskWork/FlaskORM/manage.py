import sys
from models import models
from views import app

print(sys.argv)
command = sys.argv[1]
if command == 'migrate':
    models.create_all()
elif command == 'runserver':
    app.run(host='127.0.0.1', port=8000, debug=True)

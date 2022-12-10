from flask import Flask
from flask_restful import Api

from config import config

from resources.login import UserRegisterResource

# __name__ 이란
app = Flask(__name__)

app.config.from_object(config)

api = Api(app)

#--- Api

api.add_resource(UserRegisterResource, '/users/register')

#---

# app.py가 app.py를 실행시킬 때 app.run() = flask 동작해라.
if __name__ == '__main__' :
    app.run()
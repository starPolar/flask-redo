from flask import Flask
from flask_restful import Api

from config import Config

from resources.login import UserRegisterResource

app = Flask(__name__)

api = Api(app)

app.config.from_object(Config)

#--- Api

api.add_resource(UserRegisterResource, '/users/register')

#---

# app.py가 app.py를 실행시킬 때 app.run() = flask 동작해라.
if __name__ == '__main__' :
    app.run()
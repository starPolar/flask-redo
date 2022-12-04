from flask_restful import Resource
from flask import request

from mysql_connection import get_con

class UserRegisterResource(Resource) :
    def post(self) :

        data = request.get_json()

        try :

        except :
            pass
        return



from flask_restful import Resource
from flask import request

from mysql_connection import get_con

class UserRegisterResource(Resource) :
    def post(self) :

        data = request.get_json()
        # /todo 1. jwt 연결
        # /todo 2. 블로그 보강
        try :

        except :
            pass
        return



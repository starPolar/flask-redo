from flask_restful import Resource
from flask import request

from mysql_connection import get_connection
import mysql.connector

class UserRegisterResource(Resource) :
    def post(self) :

        # {
        #     "email": "user1@gmail.com",
        #     "password": "abcd1234",
        #     "name": "nana",
        #     "gender": "2"
        # }

        data = request.get_json()

        try :
            connection = get_connection()

            query = '''insert into user
                    (email, password, name, gender)
                    values
                    (%s, %s, %s, %s);'''

            record = (data['email'],
                    data['password'],
                    data['name'],
                    data['gender'])

            cursor = connection.cursor()

            cursor.execure(query, record)

            connection.commit()

            cursor.close()
            connection.close()

        except mysql.connector.Error as e :
            cursor.close()
            connection.close()
            return {'error' : str(e), 'error_no' : 1}, 503

        return {'result' : 'success'}, 200

# todo :sql문들, utils go 


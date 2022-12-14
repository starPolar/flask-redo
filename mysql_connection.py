import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'star-db.clmt07jbjcoe.ap-northeast-2.rds.amazonaws.com',
        database = 'flask_redo_db', #database가 아닌 schemas 이다
        user = 'starPolar',
        password = 'godqhr24'
    )
    return connection
import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'sp-db.clmt07jbjcoe.ap-northeast-2.rds.amazonaws.com',
        database = 'flaskRedo', #database가 아닌 schemas 이다
        user = 'starPolar',
        password = 'godqhr24'
    )
    return connection
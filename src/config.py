
class Config:
    SECRET_KEY = 'merosmeros123'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'mysql.railway.internal'
    MYSQL_USER='root'
    MYSQL_PASSWORD='rjKwBkMpnLOpJWjEOkTniBqworHimTZX'
    MYSQL_DB = 'railway'


config = {
    'development': DevelopmentConfig
}

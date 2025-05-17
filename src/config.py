
class Config:
    SECRET_KEY = 'merosmeros123'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'mysql://root:rjKwBkMpnLOpJWjEOkTniBqworHimTZX@shinkansen.proxy.rlwy.net:30015/railway'
    MYSQL_USER='root'
    MYSQL_PASSWORD='rjKwBkMpnLOpJWjEOkTniBqworHimTZX'
    MYSQL_DB = 'railway'


config = {
    'development': DevelopmentConfig
}

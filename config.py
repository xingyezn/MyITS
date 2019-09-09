import os
"""
这里是系统配置文件
"""

# 设置为debug模式，可以实时更新修改后的py文件，不需要重新运行
DEBUG = True

# 数据库的相关配置
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'csits'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)
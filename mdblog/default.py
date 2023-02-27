import os

SECRET_KEY = b'\x8eJ|P7\x8c\xe6X\xb3\x9c\xaf\x17C\xbaz\x17\xbb\xc81`_\xe3\xac\xc2'
# Login

USERNAME = "admin"
PASSWORD = "admin"

#SQL
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///./blog.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True

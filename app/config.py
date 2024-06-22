import os


class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'admin')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'admin')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'mydb')

    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'asflakjsdfa;lsdjfasldkfja')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

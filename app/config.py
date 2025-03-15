import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Đường dẫn đến file cơ sở dữ liệu SQLite
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', f'sqlite:///{os.path.join(BASEDIR, "site.db")}')
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'


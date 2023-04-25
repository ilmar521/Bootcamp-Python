import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'Hhjkhj54kfjk5o650jmk09ojop099Ikljk[kp9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'crypto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

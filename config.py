from os.path import join, dirname
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_PATH = join(dirname(__file__), 'app/static/images/uploads/')

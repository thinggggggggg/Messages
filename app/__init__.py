from flask import Flask
from config import Config

app = Flask(__name__)  # init flask object
app.config.from_object(Config)

from app import routes  # leave as last line !!!!!!!!!
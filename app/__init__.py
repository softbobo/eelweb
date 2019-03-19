# initialization module, knows all the application instances

from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')

from app import routes, models
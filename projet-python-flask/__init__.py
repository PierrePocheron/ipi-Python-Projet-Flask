import os
from flask import Flask
import sqlite3



def create_app():
    app = Flask(__name__)
    from . import  db
    from . import  route
    app.config.form_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sneakers.sqlite'),
    )

    db.init_app(app)
    return app


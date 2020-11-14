from flask import Flask, render_template, app, request

import sqlite3
import os

# from db import get_db
from . import db


def create_app():
    app = Flask(__name__)


    db.init_app(app)
    return app

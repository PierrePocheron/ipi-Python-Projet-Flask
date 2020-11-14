from flask import Flask, render_template
from flask import request
from . import db


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return render_template("view_connexion.html")

    @app.route('/connexion')
    def connexion():
        return render_template("view_connexion.html")

    @app.route('/produit')
    def produit():
        return render_template("view_produit.html")

    @app.route('/panier')
    def panier():
        return render_template("view_panier.html")

    db.init_app(app)
    return app

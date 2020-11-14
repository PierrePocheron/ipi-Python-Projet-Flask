from flask import (
    Flask,
    redirect,
    render_template,
    app,
    request,
    session,
    url_for
)
import sqlite3
import os

# from db import get_db
from . import db


def create_app():
    class User:
        def __init__(self, id, username, password):
            self.id = id
            self.username = username
            self.password = password

        def __repr__(self):
            return f'<User: {self.username}>'

    users = []
    users.append(User(id=1, username='Pierre', password='Pierre'))
    users.append(User(id=2, username='root', password='root'))

    print(users)

    currentdirectory = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__)
    app.secret_key = 'somesecretkey'


    # @app.route('/')
    # def defaultPage():
    #     return render_template("view_connexion.html")

    @app.route('/connexion', methods=['GET', 'POST'])
    def connexion():
        if request.method == 'POST':
            session.pop('user_id', None)

            result = request.form
            u = result['username']
            p = result['password']

            user = [x for x in users if x.username == u][0]
            if user and user.password == p:
                session['user_id'] = user.id
                return redirect(url_for('produit'))

            return redirect(url_for('connexion'))

        return render_template("view_connexion.html")

    @app.route('/produit')
    def produit():
        return render_template("view_produit.html")

    # @app.route("/produit", methods=["POST"])
    # def userConnected():
    #     result = request.form
    #     u = result['username']
    #     p = result['password']
    #     return render_template("view_produit.html", username=u, password=p)

    @app.route('/panier')
    def panier():
        return render_template("view_panier.html")

    db.init_app(app)
    return app

# @app.route('/produit')
#     def produit():
#         # a l'initialisation, charger les produits
#         # db = get_db()
#         # produits = db.execute(
#         #     'SELECT *'
#         #     ' FROM produit'
#         #     ' ORDER BY name'
#         # ).fetchall()
#         # return render_template("view_produit.html", produits=produits)
#         return render_template("view_produit.html")


# @app.route("/connexion", methods=["POST"])
# def addUtilisateur():
#     username = request.form["Username"]
#     password = request.form["Password"]
#     connexion = sqlite3.connect(currentdirectory + "\projet-python-flask.db")
#     cursor = connexion.cursor()
#     query = "INSERT INTO Utilisateur VALUES('{use}',{pas})".format(use=username, pas=password)
#     cursor.execute(query)
#     connexion.commit()

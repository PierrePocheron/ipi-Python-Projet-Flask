from flask import (
    Flask,
    g,
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

    class Produit:
        def __init__(self, id, code, marque, modele, coloris, prix, image):
            self.id = id
            self.code = code
            self.marque = marque
            self.modele = modele
            self.coloris = coloris
            self.prix = prix
            self.image = image

        def __repr__(self):
            return f'<Produit: {self.code}>'

    listProduits = []
    listProduits.append(Produit(id=1, code='SNKRS-001', marque='Nike', modele='Vaporwaffle Sacai', coloris='Black White', prix=570, image='Nike-Sacai-Vaporwaffle-black-white.png'))
    listProduits.append(Produit(id=2, code='SNKRS-002', marque='Nike', modele='Vaporwaffle Sacai', coloris='Sport Fuchsia Game Royal', prix=590, image='Nike-Sacai-VaporWaffle-Game-Royal-Fuchsia.png'))
    listProduits.append(Produit(id=3, code='SNKRS-003', marque='Nike', modele='Vaporwaffle Sacai', coloris='Tour Yellow Stadium Green', prix=490, image='Nike-Sacai-VaporWaffle-Tour-Yellow-Stadium-Green.png'))
    listProduits.append(Produit(id=4, code='SNKRS-004', marque='Nike', modele='Vaporwaffle Sacai', coloris='Villain Red Neptune Green', prix=510, image='Nike-Sacai-Vaporwaffle-Villain-Red-Neptune-Green.png'))

    listProduits.append(Produit(id=4, code='SNKRS-005', marque='Nike', modele='Air Jordan 1 Retro High Travis Scott', coloris='Cactus Jack', prix=1520, image='Air-Jordan-1-Cactus-Jack-Travis-Scott.webp'))
    listProduits.append(Produit(id=4, code='SNKRS-006', marque='Nike', modele='Air Jordan 1 Retro High Off-White', coloris='NRG White', prix=2370, image='Air-Jordan-1-Retro-High-Off-White-The-Ten-NRJ.webp'))
    listProduits.append(Produit(id=4, code='SNKRS-007', marque='Nike', modele='Air Jordan 1 Retro High', coloris='UNC Patent', prix=730, image='Air-Jordan-1-Retro-High-UNC-Patent.webp'))
    listProduits.append(Produit(id=4, code='SNKRS-008', marque='Nike', modele='Air Jordan 1 Retro High', coloris='Fearless OG', prix=460, image='Air-Jordan-1-Retro-High-OG-Fearless.webp'))
    print(listProduits)

    listPanier = []
    print(listPanier)

    # currentdirectory = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__)
    app.secret_key = 'somesecretkey'

    @app.before_request
    def before_request():
        g.user = None
        if 'user_id' in session:
            user = [x for x in users if x.id == session['user_id']][0]
            g.user = user




    @app.route('/')
    def defaultPage():
        return redirect(url_for('produit'))


    @app.route('/connexion', methods=['GET', 'POST'])
    def connexion():
        if request.method == 'POST':
            session.pop('user_id', None)

            result = request.form
            username = result['username']
            password = result['password']

            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('produit'))

            return redirect(url_for('connexion'))

        return render_template("view_connexion.html")


    @app.route('/produit')
    def produit():
        if not g.user:
            return redirect(url_for('connexion'))

        return render_template("view_produit.html", listProduits=listProduits)


    @app.route('/addPanier', methods=['GET', 'POST'])
    def addPanier():
        if not g.user:
            return redirect(url_for('connexion'))

        if request.method == 'POST':
            result = request.form
            unProduit = result['produitCode']
            listPanier.append(Produit(id='', code=unProduit, marque='', modele='', coloris='', prix='', image=''))
            print(listPanier)
            return render_template("view_panier.html", listPanier=listPanier)
        return render_template("view_panier.html", listPanier=listPanier)





    @app.route('/panier')
    def panier():
        if not g.user:
            return redirect(url_for('connexion'))
        return render_template("view_panier.html", listPanier=listPanier)

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

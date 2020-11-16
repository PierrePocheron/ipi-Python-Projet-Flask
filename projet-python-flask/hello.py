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
    # Class User + implementation
    class User:
        def __init__(self, id, username, password):
            self.id = id
            self.username = username
            self.password = password

        def __repr__(self):
            return f'<User: {self.username}>'

    users = []
    users.append(User(id=1, username='Pierre', password='Pierre'))
    users.append(User(id=2, username='Ayoub', password='Guillaume'))
    users.append(User(id=3, username='root', password='root'))

    # Class Produit + implementation
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
    listProduits.append(
        Produit(id=1, code='SNKRS-001', marque='Nike', modele='Vaporwaffle Sacai', coloris='Black White', prix=570,
                image='Nike-Sacai-Vaporwaffle-black-white.png'))
    listProduits.append(
        Produit(id=2, code='SNKRS-002', marque='Nike', modele='Vaporwaffle Sacai', coloris='Sport Fuchsia Game Royal',
                prix=590, image='Nike-Sacai-VaporWaffle-Game-Royal-Fuchsia.png'))
    listProduits.append(
        Produit(id=3, code='SNKRS-003', marque='Nike', modele='Vaporwaffle Sacai', coloris='Tour Yellow Stadium Green',
                prix=490, image='Nike-Sacai-VaporWaffle-Tour-Yellow-Stadium-Green.png'))
    listProduits.append(
        Produit(id=4, code='SNKRS-004', marque='Nike', modele='Vaporwaffle Sacai', coloris='Villain Red Neptune Green',
                prix=510, image='Nike-Sacai-Vaporwaffle-Villain-Red-Neptune-Green.png'))

    listProduits.append(Produit(id=5, code='SNKRS-005', marque='Nike', modele='Air Jordan 1 Retro High Travis Scott',
                                coloris='Cactus Jack', prix=1520, image='Air-Jordan-1-Cactus-Jack-Travis-Scott.webp'))
    listProduits.append(
        Produit(id=6, code='SNKRS-006', marque='Nike', modele='Air Jordan 1 Retro High Off-White', coloris='NRG White',
                prix=2370, image='Air-Jordan-1-Retro-High-Off-White-The-Ten-NRJ.webp'))
    listProduits.append(
        Produit(id=7, code='SNKRS-007', marque='Nike', modele='Air Jordan 1 Retro High', coloris='UNC Patent', prix=730,
                image='Air-Jordan-1-Retro-High-UNC-Patent.webp'))
    listProduits.append(
        Produit(id=8, code='SNKRS-008', marque='Nike', modele='Air Jordan 1 Retro High', coloris='Fearless OG',
                prix=460, image='Air-Jordan-1-Retro-High-OG-Fearless.webp'))

    listProduits.append(
        Produit(id=9, code='SNKRS-009', marque='Adidas', modele='Yeezy Boost 350 V2', coloris='Tail Light', prix=380,
                image='Adidas-Yeezy-Boost-350-V2-Tail-Light.png'))
    listProduits.append(
        Produit(id=10, code='SNKRS-010', marque='Adidas', modele='Yeezy Boost 350 V2', coloris='Natural', prix=310,
                image='Adidas-Yeezy-350-V2-Natural.png'))
    listProduits.append(
        Produit(id=11, code='SNKRS-010', marque='Adidas', modele='Yeezy Boost 350 V2', coloris='Cinder', prix=390,
                image='Adidas-Yeezy-350-V2-Cinder.png'))
    listProduits.append(
        Produit(id=12, code='SNKRS-010', marque='Adidas', modele='Yeezy Boost 350 V2', coloris='Zebra', prix=420,
                image='Adidas-Yeezy-Boost-350-V2-Zebra.png'))

    listPanier = []

    app = Flask(__name__)
    app.secret_key = 'somesecretkey'

    @app.before_request
    def before_request():
        # Instanciation of the global variable user
        g.user = None
        if 'user_id' in session:
            # Retrieving the connected user_id
            user = [x for x in users if x.id == session['user_id']][0]
            g.user = user

    # default route
    @app.route('/')
    def defaultPage():
        return redirect(url_for('produit'))

    #test
    # Route to connect User
    @app.route('/connexion', methods=['GET', 'POST'])
    def connexion():
        # Verification of the past method
        if request.method == 'POST':
            session.pop('user_id', None)

            # Retrieving the username and password fields of the form
            result = request.form
            username = result['username']
            password = result['password']

            # Retrieving a User object corresponding to the Username retrieved
            user = [x for x in users if x.username == username][0]
            # Verification Password matches Username
            if user and user.password == password:
                # Implementation of the session variable: user_id
                session['user_id'] = user.id
                return redirect(url_for('produit'))

            return redirect(url_for('connexion'))

        return render_template("view_connexion.html")

    # Route to Deconnexion
    @app.route('/deconnexion')
    def deconnexion():
        # Empty all session variables
        session.clear()
        # empty the basket
        listPanier.clear()
        return redirect(url_for('connexion'))

    # Route to Product
    @app.route('/produit')
    def produit():
        # Verification that the user is logged in
        if not g.user:
            return redirect(url_for('connexion'))

        return render_template("view_produit.html", listProduits=listProduits, listPanier=listPanier)

    # Route to add Product from Card
    @app.route('/addPanier', methods=['GET', 'POST'])
    def addPanier():
        # Verification that the user is logged in
        if not g.user:
            return redirect(url_for('connexion'))

        if request.method == 'POST':
            # Recovering a Product object
            result = request.form
            unProduit = result['produitCode']
            leProduit = [x for x in listProduits if x.code == unProduit][0]
            # Adding a product item in the listPanier
            listPanier.append(leProduit)
            return render_template("view_panier.html", listPanier=listPanier)

        return render_template("view_panier.html", listPanier=listPanier)

    # Route to delete Product from Card
    @app.route('/delPanier', methods=['GET', 'POST'])
    def delPanier():
        # Verification that the user is logged in
        if not g.user:
            return redirect(url_for('connexion'))

        if request.method == 'POST':
            # Recovering a Product object
            result = request.form
            unProduit = result['produitCode']
            leProduit = [x for x in listProduits if x.code == unProduit][0]
            # Deleting a product object from the listPanier
            listPanier.remove(leProduit)
            return render_template("view_panier.html", listPanier=listPanier)

        return render_template("view_panier.html", listPanier=listPanier)

    # Route to validate an order
    @app.route('/addCommande', methods=['GET', 'POST'])
    def addCommande():
        # Verification that the user is logged in
        if not g.user:
            return redirect(url_for('connexion'))

        if request.method == 'POST':
            # Empty the listPanier
            listPanier.clear()
            return render_template("view_confirmationCommande.html")

        return render_template("view_panier.html", listPanier=listPanier)

    # Route for the card
    @app.route('/panier')
    def panier():
        # Verification that the user is logged in
        if not g.user:
            return redirect(url_for('connexion'))
        return render_template("view_panier.html", listPanier=listPanier)

    #Route for the unknown URL
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    db.init_app(app)
    return app

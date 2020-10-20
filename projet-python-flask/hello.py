from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!Heeeyy ! Bienvenu sur ce projet !     Le site web vient d être mit à jour !'


@app.route('/connexion')
def hello_world2():
    return 'Bienvenue sur la page : Connexion !'


@app.route('/produit')
def hello_world3():
    return 'Bienvenue sur la page : Produit !'


@app.route('/panier')
def hello_world4():
    return 'Bienvenue sur la page : Panier !'



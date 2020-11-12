from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
from db import get_db

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("view_connexion.html")


@app.route('/connexion')
def index():
    return render_template("view_connexion.html")


@app.route('/produit')
def hello_produit():
    db = get_db()
    produits = db.execute(
        'SELECT *'
        ' FROM produit'
        ' ORDER BY name'
    ).fetchall()
    # return render_template("view_produit.html", produits=produits)
    return render_template("view_produit.html")


@app.route('/panier')
def hello_panier():
    return render_template("view_panier.html")


if __name__ == "__main__":
    app.run(debug=true)

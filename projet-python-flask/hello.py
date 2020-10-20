from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("view_connexion.html")


@app.route('/connexion')
def index():
    return render_template("view_connexion.html")



@app.route('/produit')
def hello_produit():
    return render_template("view_Produit.html")


@app.route('/panier')
def hello_panier():
    return render_template("view_panier.html")


app.run(debug=True)
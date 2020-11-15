Projet IPI - Python - Flask - Sneakers

Board du projet : https://miro.com/app/board/o9J_kibrMIk=/

==============================

Présentation de mon projet :

Le projet Sneakers à été développé dans le cadre de mon BAC+3 CDEV a l'IPI.
J'ai utilisé python avec son framework Flask.

Cette Application Web reprend l'idée d'un site de e-commerce dans le monde de la Sneakers, tenue par un personal-shopper.
Lorsque qu'un utilsiateur se connecte grâce à ses identifiants, il accède a une page "Produit" contenant toutes les sneakers disposible en ce moment.
Il peut les ajouter au panier et passer une commande.

==============================

Mise en place du projet :

Etape 1 ==============================

Récupérer le projet Github avec Git

    - Dans le dossier que vous souhaitez :
    Ouvrez un terminal 

git clone adresse_du_projet_github

Etape 2 ==============================

Création de l'environnement virtuel

    - Dans le dossier du projet :
    Ouvrez un terminal
    
python3 -m venv venv

Etape 3 ==============================

Activer l'environnement virtuel

venv\Scripts\activate

Etape 4 ==============================
    
Vérifier que l'environnement virtuel est bien activé
-> vous devez avoir (venv) devant votre chemin

(venv) C:\...\projet-python-flask
 
Etape 5 ==============================

Installer les différents modules

pip install -r requirements.txt

Etape 6 ==============================

Initialiser les differentes variables du package

set FLASK_APP=hello.py
set FLASK_ENV=development
flask run

Etape 7 ==============================

Vous pouvez désormait accèder a l'application web a l'adresse suivante : http://127.0.0.1:5000/



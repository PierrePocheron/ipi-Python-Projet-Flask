# Projet IPI - Python - Flask - Sneakers

Board du projet : https://miro.com/app/board/o9J_kibrMIk=/


## Présentation de mon projet :

Le projet Sneakers à été développé dans le cadre de mon BAC+3 CDEV a l'IPI.
J'ai utilisé python avec son framework Flask.

Cette Application Web reprend l'idée d'un site de e-commerce dans le monde de la Sneakers, tenue par un personal-shopper.
Lorsque qu'un utilsiateur se connecte grâce à ses identifiants, il accède à une page "Produit" contenant toutes les sneakers disposible en ce moment.
Il peut les ajouter au panier et passer une commande.



# Mise en place du projet :

### Etape 1 - Récupérer le projet Github avec Git



Dans le dossier que vous souhaitez :
Ouvrez un terminal 
Cas git clone https :

    git clone https://github.com/PierrePocheron/ipi-Python-Projet-Flask.git

### Etape 2 - Création de l'environnement virtuel

Dans le dossier du projet :
Ouvrez un terminal
    
    cd ipi-Python-Projet-Flask
    python3 -m venv venv

### Etape 3 - Activer l'environnement virtuel

    venv\Scripts\activate

### Etape 4 - Vérifier que l'environnement virtuel est bien activé
    
Vous devez avoir (venv) devant votre chemin

    (venv) C:\...\projet-python-flask
 
### Etape 5 - Installer les différents modules

    pip install -r requirements.txt

### Etape 6 - Initialiser les différentes variables du package
    
    cd projet-python-flask
    set FLASK_APP=hello.py
    set FLASK_ENV=development
    flask run
    
### Etape 7 - Véfification déployement !

La commande "flask run" devrait renvoyer :

    Serving Flask app "hello.py" (lazy loading)
    Environment: development
    Debug mode: on
    Restarting with stat
    Debugger is active!
    Debugger PIN: 100-911-901
    Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

### Etape 8 - Bonne visite !

Vous pouvez désormait accèder à l'application web à l'adresse suivante : http://127.0.0.1:5000/
Identificants de connexion : 
    
    login : Ayoub
    password : Guillaume



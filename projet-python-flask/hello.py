from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!dsdqs'

print('Heeeyy ! Bienvenu sur ce projet !')
print('Le site web vient d être mit à jour !')
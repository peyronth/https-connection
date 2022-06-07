# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask, redirect, render_template, url_for
from flask import request

from build import RESOURCES_DIR, SERVER_PRIVATE_KEY_FILENAME, SERVER_PUBLIC_KEY_FILENAME
from tools.core import verify_user

# définir le message secret
SECRET_MESSAGE = "ThomasPeyron" # A modifier
app = Flask(__name__)

#Generation de la page avec le message
def get_secret_message():
    fichier_begin = open(RESOURCES_DIR+"/page/page1.html", "r")
    fichier_end = open(RESOURCES_DIR+"/page/page2.html", "r")
    return fichier_begin.read() + SECRET_MESSAGE + fichier_end.read()

#Page d'accueil qui affiche le mot de passe si un mot de passe valide est fourni, sinon redirectin vers la page de connexion
@app.route("/", methods = ['GET','POST'])
def index():
    #Si soumission d'un mot de passe
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if verify_user(username, password):
            return get_secret_message()
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    
#page de connexion
@app.route('/login')
def login():
    fichier = open(RESOURCES_DIR+"/page/page_login.html", "r")
    return fichier.read()



app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=(SERVER_PUBLIC_KEY_FILENAME, SERVER_PRIVATE_KEY_FILENAME))
   

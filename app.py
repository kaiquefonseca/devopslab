from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

csrf = CSRFProtect(app) 

@app.route("/")
def pagina_inicial():
    return "Hello Kaique Fonseca RM341751 V3"

@app.route('/bug')
def bad():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)  

@app.route("/teste")
def teste():
    try:
        raise TypeError()
    except TypeError as e:
        print(e)       

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)  
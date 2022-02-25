from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'titulo' : 'Bienvenido',
        'nombre' : 'Jorge'   
    }
    return render_template('index.html',data=data)

@app.route('/about/')
def estudios():
    estudios = ['Tecnico en Redes','Tecnico en Reparacion de Computadoras','Tecnico en Reparacion de Celulares','Ciencia de Computadoras - CS50',
                'Estudiante Ingeniria en Computacion','Graduado Br Escuela Normal Maria Mazzarello','Academia Sabatina Jovenes Talento']
    data={
        'estudios': estudios} 
    return render_template('about.html',data=data)

def noencontrado(error):
    return render_template("404.html")
     
if __name__ == '__main__':
    app.register_error_handler(404, noencontrado)
    app.run(debug=True)
    
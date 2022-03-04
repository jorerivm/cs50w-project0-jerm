from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        'titulo' : 'Bienvenido',
        'nombre' : 'Jorge'   
    }
    return render_template('index.html',data=data)

@app.route('/about')
def about():
    #estudios = ['Tecnico en Redes','Tecnico en Reparacion de Computadoras','Tecnico en Reparacion de Celulares',
    #            'Ciencia de Computadoras - CS50','Estudiante Ingeniria en Computacion',
    #            'Graduado Br Escuela Normal Maria Mazzarello','Academia Sabatina Jovenes Tlento']
    #data={ 
    #    'estudios': estudios} 
    return render_template('about.html')

def noencontrado(error):
    print('404')
    return render_template("404.html")
     
if __name__ == '__main__':
    app.register_error_handler(404, noencontrado)
    app.run(debug=True)
    
    
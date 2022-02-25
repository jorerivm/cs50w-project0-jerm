from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'abaco'

conexion = MySQL(app)

@app.before_request
def before_request():
    print("Antes peticion...")
    
    
@app.after_request
def after_request(response):
    print("Despues peticion")
    return response

@app.route('/')
def index():
    data = {
        'titulo' : 'Bienvenido',
        'nombre' : nombre   
    }
    return render_template('estudios.html',data=data)

@app.route('/estudios/')
def estudios():
    estudios = ['Tecnico en Redes','Tecnico en Reparacion de Computadoras','Tecnico en Reparacion de Celulares','Ciencia de Computadoras - CS50',
                'Estudiante Ingeniria en Computacion','Graduado Br Escuela Normal Maria Mazzarello','Academia Sabatina Jovenes Talento']
    data={
        'estudios': estudios}
    return render_template('estudios.html',data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

def noencontrado(error):
    return render_template("404.html")
    
if __name__ == '__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404, noencontrado)
    app.run(debug=True)
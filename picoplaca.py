#Importamos las librerias
from crypt import methods
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__, template_folder='templates')
#Creamos la lista para almacenar datos
lista_registro = []
#Decoradores de la ruta
@app.route('/')
def index():
    return render_template('index.html', lista_registro = lista_registro )
#Controlador para agregar y almacenamiento
@app.route('/agregar', methods = ['POST'])
def agregar():
    if request.method == 'POST':                                    
        matricula = request.form['matricula']       
        fecha = request.form['fecha']                   
        hora = request.form['hora']           
        
        if matricula == '' :            
            return redirect(url_for('index'))         
        elif fecha == '':            
            return redirect(url_for('index'))   
        elif hora == '':            
            return redirect(url_for('index'))                 
        else:
            lista_registro.append({'matricula': matricula, 'fecha': fecha, 'hora': hora })
            return redirect(url_for('index'))
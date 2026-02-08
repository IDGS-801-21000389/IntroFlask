from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask (__name__)
app.secret_key="clave secreta"

csrf = CSRFProtect()

@app.route('/')
def index():
    titulo ="Flask IDGS801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/alumnos')
def alumnos():
    return render_template("alumnos.html")

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    mat = 0
    nom = ""
    apa = ""
    ama = ""
    email = ""
    usuarios_class = forms.UserForm(request.form)
    if request.method == "POST" and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data
        mensaje = "Bienvenido {}" .format(nom)
        flash(mensaje)

    return render_template("usuarios.html", form = usuarios_class, mat = mat, nom = nom, apa = apa, ama = ama, email = email)


@app.route('/operasBas', methods=['GET', 'POST'])
def operasBas():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        res = float (n1) +float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    tem = float (n1) +float(n2)
    return f'La suma es: {tem}'

@app.route('/hola')
def hola():
    return "Hola, mundo"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return f"<h1>El numero es: {n}</h1>"

'''
@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"<h1>Hola, {username}, tu id es: {id}</h1>"

@app.route('/suma/<int:num1>/<int:num2')
def sumas(num1, num2):
    return f"La suma es: {num1 + num2}"

@app.route('/default')
@app.route('/default/<string:param')
def default(param= "juanito"):
    return f"Hola, {param}"
'''
@app.route('/operas')
def operas():
    return '''
        <form>
        <label for = "name"> Name: </label>
        <input type = "text" id="name" name="name" requiered>
        </br>
        <label for = "name"> apaterno: </label>
        <input type = "text" id="name" name="name" requiered>
</form>
'''

@app.route('/cinepolis')#decorador o ruta de la aplicacion
def cinepolis():
    return render_template('cinepolis.html')

@app.route('/entradas', methods=['GET', 'POST'])
def pagar():
    resultado = ""  

    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantidad_compradores = int(request.form['compradores'])  
            cineco = int(request.form['cineco'])
            boletos = int(request.form['boletos'])  
            
            boletos_permitidos = (cantidad_compradores + 1) * 7  

            if boletos > boletos_permitidos:
                resultado = f"Solo se permiten comprar 7 boletos por persona"
            else:
                precioBoleto = 12.00
                total = boletos * precioBoleto

                if boletos > 5:
                    descuento = 0.15
                elif 3 <= boletos <= 5:
                    descuento = 0.10
                else:
                    descuento = 0.0

                totalDescuento = total * (1 - descuento)

                if cineco == 1:
                    totalDescuento *= 0.9  

                resultado = f"${totalDescuento:,.2f}"  
        except ValueError:
            resultado = "Error en los datos ingresados, por favor verifica los campos."

    return render_template('cinepolis.html', resultado=resultado)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)
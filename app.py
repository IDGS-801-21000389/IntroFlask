from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Hello, world!"

@app.route('/hola')
def hola():
    return "Hola, mundo"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "<h1>El numero es: {n}</h1>"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "<h1>Hola, {username}, tu id es: {id}</h1>"

@app.route('/suma/<int:num1>/<int:num2')
def sumas(num1, num2):
    return f"La suma es: {num1 + num2}"

@app.route('/default')
@app.route('/default/<string:param')
def default(param= "juanito"):
    return f"Hola, {param}"

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

if __name__ == "__main__":
    app.run(debug=True)
from bottle import Bottle,route,run,request
import BDController
@route('/begin')
def inicio():
    return '''<p>Identificate o registrate</p>
              <form action="/login" >
                <input value="Identificate" type="submit" />
              </form>
              <form action="/registro" >
                <input value="Registrate" type="submit" />
            </form>'''
@route('/login') 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''

@route('/login',method='POST') 
def do_login():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    if BDController.ValidaLogin(username, password):
        return "<p>Login correcto</p>" + main()
    else:
        return "<p>Login incorrecto.</p>"

@route('/registro')
def registro():
     return '''
        <form action="/registro" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="Registro" type="submit" />
        </form>'''
        
@route('/registro', method='POST') 
def do_registro():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    if BDController.existeUsuario(username):
        return "<p> Este usuario ya existe. Escoge otro nombre de usuario</p>" + registro()
    else:
        
        BDController.AniadirUsuario(username, password)  
        return "<p>REGISTRO CORRECTO</p>" + login()
        
@route('/main')
def main():
    return '''<p>Gestion de Biblioteca Online</p>
            <form action="/listaLibros" >
                <input value="Introducir un libro" type="submit" />
            </form>
            <form action="/listaLibros" >
                <input value="Mostrar todos los libros" type="submit" />
            </form>
            <form action="/listaLibros" >
                <input value="Buscar un libro" type="submit" />
            </form>
            <form action="/listaLibros" >
                <input value="Eliminar un libro" type="submit" />
            </form>
            <form action="/listaLibros" >
                <input value="Modificar un libro" type="submit" />
            </form>'''
@route('/listaLibros')
def listaLibros():
    return "<p>Lista de Libros</p>"
BDController.CreateDBLibreria()
BDController.InsertToDB()     
run(host='localhost', port=8080)

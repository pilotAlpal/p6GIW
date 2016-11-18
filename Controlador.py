from bottle import Bottle,route,run,request, template, response
import BDController
@route('/')
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
        response.set_cookie("cuenta", username, secret="123456789")
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
        response.set_cookie("cuenta", username, secret="123456789")
        return "<p>REGISTRO CORRECTO</p>" + main()
        
@route('/addBook')
def addBook():
    user = request.get_cookie("cuenta", secret="123456789")
    if user:
        return '''<form action="/addBook" method="post">
                Nombre del Libro: <input name="nombreLibro" type="text" />
                Autor: <input name="autor" type="text" />
                Genero    <input name="genero" tyoe="text" />
                <input value="Login" type="submit" />
            </form>'''
    else:
        return "<p>Zona Restringida</p>" + inicio()
@route('/addBook', method='POST')
def do_addBook():
    nombreLibro = request.forms.get('nombreLibro')
    genero = request.forms.get('genero')
    autor = request.forms.get('autor')
    if BDController.existeLibro(nombreLibro):
        return "<p>Ya existe este libro</p>" + addBook()
    else:
        BDController.AniadirLibro(nombreLibro, autor, genero)
        return "<p>Libro introducido correctamente</p>" + main()
@route('/main')
def main():
    user = request.get_cookie("cuenta", secret="123456789")
    if user:
        return '''<p>Gestion de Biblioteca Online</p>
                <form action="/addBook" >
                    <input value="Introducir un libro" type="submit" />
                </form>
                <form action="/listaLibros" >
                    <input value="Mostrar todos los libros" type="submit" />
                </form>
                <form action="/buscarLibro" >
                    <input value="Buscar un libro" type="submit" />
                </form>
                <form action="/eliminarLibro" >
                    <input value="Eliminar un libro" type="submit" />
                </form>
                <form action="/listaLibros" >
                    <input value="Modificar un libro" type="submit" />
                </form>'''
    else:
        return "<p>Zona Restringida</p>" + inicio()
@route('/eliminarLibro')
def eliminarLibro():
    user = request.get_cookie("cuenta", secret="123456789")
    if user:
        return '''<p> Eliminar un libro </p>
                    <form action="/eliminarLibro" method="post">
                        Libro: <input name="nombreLibro" type="text" />
                        <input value="Eliminar" type="submit" />
                    </form>'''
    else: return "<p>Zona Restringida</p>" + inicio()
    
@route('/eliminarLibro', method='POST')
def do_eliminarLibro():
    nombreLibro = request.forms.get('nombreLibro')
    if BDController.existeLibro(nombreLibro):
        BDController.BorrarLibro(nombreLibro)
        return "<p>Libro borrado correctamente</p>" + main()
    else:
        return "<p>Libro no existe</p>"+ eliminarLibro()
        
@route('/buscarLibro')
def buscarLibro():
    user = request.get_cookie("cuenta", secret="123456789")
    if user:
        return '''<p>Buscar un Libro</p>
                  <form action="/buscarLibro" method="post">
                        Titulo: <input name="nombreLibro" type="text" />
                        <input value="Buscar" type="submit" />
                    </form> 
                  <form action="/buscarLibroPorGenero" method="post">
                        Genero: <input name="genero" type="text" />
                        <input value="Buscar" type="submit" />
                    </form>
                  <form action="/buscarLibroPorAutor" method="post">
                        Autor: <input name="autor" type="text" />
                        <input value="Buscar" type="submit" />
                    </form>'''
    else:
        return "<p>Zona Restringida</p>" + inicio()
@route('/buscarLibro', method= 'POST')
def do_buscarLibro():
    nombreLibro = request.forms.get('nombreLibro')
    if BDController.existeLibro(nombreLibro):
        datos = BDController.getLibro(nombreLibro)
        return template("template_lista.tpl", lista=datos)
    else:
        return "<p>Libro no existe</p>"
@route('/listaLibros')
def listaLibros():
    user = request.get_cookie("cuenta", secret="123456789")
    if user:
        lista = BDController.ListarLibros()
        return template('template_lista.tpl', lista=lista)
    else: return "<p>Zona Restringida</p>" + inicio()
BDController.CreateDBLibreria()
BDController.InsertToDB()     
run(host='localhost', port=8080)

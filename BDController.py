# -*- coding: utf-8 -*-
import sqlite3

def CreateDBLibreria():
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    #creamos la tabla Usuarios
    cur.execute("DROP TABLE IF EXISTS Usuarios")
    tabla_compradores = "CREATE TABLE Usuarios ("
    tabla_compradores += "id INTEGER PRIMARY KEY,"
    tabla_compradores += "name CHAR(50) UNIQUE DEFAULT ' ',"
    tabla_compradores += "password CHAR(50) NOT NULL DEFAULT ' ')"
    cur.execute(tabla_compradores)
    #creamos la tabla Libros
    cur.execute("DROP TABLE IF EXISTS Libros")
    tabla_libros = "CREATE TABLE Libros ("
    tabla_libros += "id INTEGER PRIMARY KEY,"
    tabla_libros += "titulo CHAR(50) UNIQUE DEFAULT ' ',"
    tabla_libros += "autor CHAR(50) NOT NULL DEFAULT ' ',"
    tabla_libros += "genero CHAR(50) NOT NULL DEFAULT ' ')"
    cur.execute(tabla_libros)
    cur.close()
    conn.commit()  
    
    
def InsertToDB():
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    insert = "INSERT INTO Usuarios (name,password) VALUES"
    insert += "('andres','admin'),"    
    insert += "('lucas','admin'),"
    insert += "('amador','admin')" 
    cur.execute(insert)
    insert_l = "INSERT INTO Libros (titulo,autor,genero) VALUES"
    insert_l += "('El Quijote','Miguel de Cervantes','Novela'),"
    insert_l += "('Marina','Carlos Ruíz Zafón','Novela'),"
    insert_l += "('La hogera de la vanidades','Tom Wolfe','Historia'),"
    insert_l += "('Los pilares de la Tierra','Ken Follet','Terror'),"
    insert_l += "('Otelo','William Shakespeare','Obra Teatral'),"
    insert_l += "('Rimas y Leyendas','Gustavo Adolfo Becquer','Poesia')"
    cur.execute(insert_l)
    cur.close()
    conn.commit()

def existeUsuario(username):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    usuario = cur.execute("SELECT name FROM Usuarios WHERE name=?",(username,))
    aux = ''
    for i in usuario:
        aux = i
    cur.close()
    conn.commit() 
    if (len(aux) > 0): return True
    else: return False

def existeLibro(nombreLibro):
    con=sqlite3.connect("Libreria.sqlite3")
    cur=con.cursor()
    libros= cur.execute("SELECT name FROM Libros WHERE name=?",(nombreLibro,))
    aux = ''
    for i in libros:
        aux = i
    cur.close()
    con.commit() 
    aux = False
    if (len(aux) > 0): return True
    else: return False    
    
    
def AniadirLibro(titulo,autor,genero):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("INSERT INTO Libros (titulo,autor,genero) VALUES (?,?,?)",(titulo,autor,genero))
    cur.close()
    conn.commit()
    
    
def AniadirUsuario(nombre,contrasena):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("INSERT INTO Usuarios (name,password) VALUES (?,?)",(nombre,contrasena))
    cur.close()
    conn.commit()    
    
    
def ListarUsuarios():
    print "Usuarios"
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    select = "SELECT * FROM Usuarios"
    cur.execute(select)
    for (id,name,password) in cur.fetchall():
        print id,"-",name,"-",password
    cur.close()
    
    
def ListarLibros():
    print "Libros"
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    select = "SELECT * FROM Libros"
    cur.execute(select)
    for (id,titulo,autor,genero) in cur.fetchall():
        print id,"-",titulo,"-",autor,"-",genero
    cur.close()
    

def ActualizaLibro(id,titulo,autor,genero):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE Libros SET titulo=?, autor=?, genero=? WHERE id=?",[titulo,autor,genero,id])    
    cur.close()
    conn.commit()
    
def ActualizaUsuario(id,name,password):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE Usuarios SET name=?, password=? WHERE id=?",[name,password,id])    
    cur.close()
    conn.commit()

    
def BorrarLibro(id):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("DELETE FROM Libros WHERE id=?",[id])
    cur.close()
    conn.commit()


def BorraUsuario(id):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("DELETE FROM Usuarios WHERE id=?",[id])
    cur.close()
    conn.commit()    
    
    
def ValidaLogin(name,password):
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Usuarios WHERE name=? AND password=?",(name,password))
    if cur.fetchone() is not None:
        return True
    else:
        return False
    cur.close()
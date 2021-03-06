import easygui as easygui

__author__ = 'aquinoacordero'

import buscar
import borrar
import menu
import datos
import dnierror
import Doc

import sqlite3 as dbapi

class BD:
    """se crea el objeto bd que que genera una base de datos con el nombre designado"""
    bd=dbapi.connect("basedatos.dat")
    #se asigna un cursor a la base de datos
    cursor = bd.cursor()

    def __init__(self):
        """etodo principal donde se crea la base de datos mediante una secuencia sql"""
        self.cursor.execute('''create table if not exists abonados(id dni text primary key, nombre text, apellido text, cuota text, tiempoIngreso text, actividades text)''')
        self.bd.commit()

    def insertar(self,nom,ape,dni_,cuot,ti,act):
        """metodo para insertar en la base de datos"""
        val=(dni_,nom,ape,cuot,"meses "+ti,act)
        print(val)
        self.cursor.execute("select * from abonados where id='" + str(dni_) + "'")
        resultado = self.cursor.fetchone()
        print(resultado)
        if resultado == None:
            self.cursor.execute("insert into abonados values(?,?,?,?,?,?)",val)
            self.bd.commit()
            easygui.msgbox("Datos del cliente Insertados", title="Mensaje")
        else:
            easygui.msgbox("El dni ya existe en la base", title="ERROR")

    def buscar(self,dni_,opc):
        """Metodo para seleccionar"""
        id=dni_ #cargamos el dni_ en una variable propia
        #Recorremos los campos que pertenezcan a la fila con la id correspondiente
        self.cursor.execute("select * from abonados where id='" + str(id) + "'")
        #recogemos todos los campos en la varible resultado
        resultado = self.cursor.fetchone()
        print(resultado)
        if resultado == None:
            print("DNI no encontrado")
            menu.principal()
            dnierror.adv()
        else:#dependiendo del estado de busqueda llama a una funcion u otra
            print(resultado)
            if opc==1:
                buscar.busqueda(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4], resultado[5])
            if opc==2:
                borrar.eliminar(resultado[0],resultado[1],resultado[2])
            if opc==3:
                Doc.tool(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4], resultado[5])

    def borrar(self,dni):
        """metodo para borrar"""
        print("borrando bd")
        id=dni
        print(id)
        self.cursor.execute("delete from abonados where id='" + str(id) + "'")
        self.bd.commit()

    def mostrar(self, *args):
        """metodo que muestra los datos del cliente"""
        c=self.cursor.execute("select * from abonados")
        dat=""
        a="DNI: "
        for resultado in c:
            dat=dat+(a+str(resultado[0])+" NOMBRE: "+str(resultado[1])+" APELLIDO: "+str(resultado[2])+" CUOTA: "+str(resultado[3])+
                     " TIEMPO: "+str(resultado[4])+" ACTIVIDADES: "+str(resultado[5])+"\n")
        datos.datos(dat)

    def modificar(self, cuot, act, dni):
        """metodo que modifica los datos del cliente"""
        print (cuot,act,dni)
        val=(cuot,act,dni)
        self.cursor.execute("Update abonados set cuota=(?), actividades=(?) where id=(?)",val)
        self.bd.commit()
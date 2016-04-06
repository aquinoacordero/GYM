#!/usr/bin/env python
# -*- coding: utf-8 -*-

import menu
import BD
from gi.repository import Gtk

class eliminar:
    """creamos el constructor"""
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("eliminar.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("window1")
    #declaramos los objetos del archivo glade en variables
    nombre = builder.get_object("lName")
    apellido = builder.get_object("lLastname")
    dni = builder.get_object("dni")

    def __init__(self,dni,nombre,apellido):
        """señales que enlazan as acciones creadas en glade con metodos de la clase"""
        signals = { "onButtonPressedDeleteSi" : self.onButtonPressedDeleteSi,
                    "onButtonPressedDeleteNo" : self.onButtonPressedDeleteNo
                    }
        #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        #recogemos el nombre y apellido
        self.nombre.set_text(str(nombre))
        self.apellido.set_text(str(apellido))
        self.dni.set_text(str(dni))

        self.win.show_all()

    def onButtonPressedDeleteSi(self,*args):
        """metodo para borrar una fila de la base de datos"""
        print ("Borrado")
        self.win.hide()
        dni_=self.dni.get_text()
        print(dni_)
        #se llama al metodo borrar de la base de datos pasandole nom y ape
        BD.BD().borrar(dni_)
        menu.principal()

    def onButtonPressedDeleteNo(self, *args):
        """metodo para regresar al menu"""
        print ("Saliendo")
        self.win.hide()
        menu.principal()


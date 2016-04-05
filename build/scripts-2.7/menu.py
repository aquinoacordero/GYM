#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import BD
import add
import adv
import Doc
import borrar

from gi.repository import Gtk

class principal:
    #creamos el constructor
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("menu.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("window1")
    #declaramos los objetos del archivo glade en variable
    nombre = builder.get_object("entryName")
    apellido = builder.get_object("entryLast")
    dni = builder.get_object("entryDNI")

    #metodo principal
    def __init__(self):

        #señales que enlazan as acciones creadas en glade con metodos de la clase
        signals = { "onButtonPressedAdd" : self.onButtonPressedAdd,
                    "onButtonPressedSearch" : self.onButtonPressedSearch,
                    "onButtonPressedDelete" : self.onButtonPressedDelete,
                    "onButtonShow" : self.onButtonShow,
                    "onButtonDoc":self.onButtonDoc
                    }
        #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        #mostramos contenido
        self.win.show_all()
        #cargamos la base de datos
        BD.BD()

    def onButtonPressedAdd(self, *args):
        #metodo añadir
        print ("Añadiendo")
        print(self.nombre.get_text(),self.apellido.get_text(),self.dni.get_text())
        #variables que recogen el texto que pasa por los objetos de clase
        nom = self.nombre.get_text()
        ape = self.apellido.get_text()
        dni_ = self.dni.get_text()
        self.win.hide()
        #llamamos a la clase abonado
        add.abonado(nom,ape,dni_)

    def onButtonPressedSearch(self, *args):
        #metodo buscar
        print ("Buscando")
        dni_ = self.dni.get_text()
        if dni_=="":
            print("Se requiere de un DNI")
            adv.adv()#muestra solicitando datos

        else:
            self.win.hide()
            #llamamos a la clase base de datos al metodo buscar
            BD.BD().buscar(dni_,1)

    def onButtonPressedDelete(self, *args):
        #metodo borrar
        print ("Borrando")
        #variables que recogen el texto que pasa por los objetos de clase
        dni_ = self.dni.get_text()
        #comprobamos si hay los parametros necesarios
        if dni_=="":
            print("DATOS NECESARIOS")
            adv.adv()
        else:
             self.win.hide()
             BD.BD().buscar(dni_,2)

    def onButtonShow(self, *args):
        #muestra informacion global del conjunto de abonados
        print("Mostrar")
        self.win.hide()
        BD.BD().mostrar()

    def onButtonDoc(self, *args):
        self.win.hide()
        dni_ = self.dni.get_text()
        BD.BD().buscar(dni_,3)
#llamada al metodo principal
if __name__== "__main__":
    principal()
    Gtk.main()


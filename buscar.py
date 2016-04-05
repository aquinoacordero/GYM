#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import avisoActividades

import menu
import BD
from gi.repository import Gtk

class busqueda:
    """creamos el constructor"""
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("busqueda.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("window1")
    #declaramos los objetos del archivo glade en variables
    nombre=builder.get_object("labelNombre")
    apellido=builder.get_object("labelApellido")
    cuota=builder.get_object("entryCuot")
    tiempo=builder.get_object("entryTi")
    dni=builder.get_object("labelDNI")
    spa=builder.get_object("checkSpa")
    spinning=builder.get_object("checkSpinning")
    sala=builder.get_object("checkSala")
    artes=builder.get_object("checkArt")

    def __init__(self, dni,name,ape,cuot,ti,ac):
        """Señales que enlazan as acciones creadas en glade con metodos de la clase"""
        signals = { "onButtonBack" : self.onButtonBack,
                    "onButtonMod" : self.onButtonMod
                    }
        #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        #recogemos el nombre, apellido, cuota, tiempo y actividades
        self.nombre.set_text(str(name))
        self.apellido.set_text(str(ape))
        self.cuota.set_text(str(cuot))
        self.tiempo.set_text(str(ti))
        self.dni.set_text(str(dni))
        #comprobamos que actividades practica el usuario y las señalamos en el checkbox
        if ac=="['Spa']" or ac=="Spa":
            self.spa.set_active(True)
        if ac=="['Spinning']" or ac=="Spinning":
            self.spinning.set_active(True)
        if ac=="['Sala de Maquinas']" or ac=="Sala de Maquinas":
            self.sala.set_active(True)
        if ac=="['Artes Marciales']" or ac=="Artes Marciales":
            self.artes.set_active(True)
        self.win.show_all()

    def onButtonBack(self, *args):
        """metodo para volver al menu principal"""
        print ("Regresando")
        self.spa.set_active(False)
        self.spinning.set_active(False)
        self.sala.set_active(False)
        self.artes.set_active(False)
        self.win.hide()
        menu.principal()

    def onButtonMod(self, *args):
        """Metodo para cambiar la actividad de un ciente"""
        cuot=self.cuota.get_text()
        dni=self.dni.get_text()
        cond=0;
        act=""
        print(cond)
        if self.spa.get_active()==True:
            act="Spa"
            cond+=1
            print(cond)
        if self.spinning.get_active()==True:
            act="Spinning"
            cond+=1
            print(cond)
        if self.sala.get_active()==True:
            act="Sala de Maquinas"
            cond+=1
            print(cond)
        if self.artes.get_active()==True:
            act="Artes Marciales"
            cond+=1
            print(cond)
        if cond==1:

            BD.BD().modificar(cuot,act,dni)
        else:
            print (cond,"SELECCIONE UN UNICO CAMPO", act)
            avisoActividades.adv()
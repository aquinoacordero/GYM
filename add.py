#!/usr/bin/env python
# -*- coding: utf-8 -*-

import menu
import BD
from gi.repository import Gtk

class abonado:
    """creamos el constructor"""
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("add.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("window1")
    #declaramos los objetos del archivo glade en variables
    nombre = builder.get_object("entryName")
    apellido = builder.get_object("entryLast")
    dni = builder.get_object("entryDNI")
    tiempo=builder.get_object("entryPeriodo")
    #declaramos la lista que reunira las actividades
    actividad = ""
    #spa=builder.get_object("checkbuttonSpa")
    #spinning=builder.get_object("checkbuttonSpinning")

    #metodo principal
    def __init__(self, nom, ape, dni_):

        """señales que enlazan as acciones creadas en glade con metodos de la clase"""
        signals = { "onButtonBack" : self.onButtonBack,
                    "onButtonConfirm" : self.onButtonConfirm,
                    "buttonSpa" : self.activeSpa,
                    "buttonSpinning" : self.activeSpinning,
                    "buttonSala" : self.activeSala,
                    "buttonArt" : self.activeArt
                    }
        #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        #recogemos el nombre,apellido y dni de la clase menu y los añadimos a los objetos
        # nombre,apellido y dni de la clase add
        self.nombre.set_text(str(nom))
        self.apellido.set_text(str(ape))
        self.dni.set_text(str(dni_))
        self.actividad=""
        #self.spa.connect("toggled",self.activeSpa())
        #self.spinning.connect("toggled",self.activeSpinning())

        self.win.show_all()

    def onButtonBack(self, *args):
        """metodo para volver al menu"""
        print ("Retroceder")
        self.win.hide()
        menu.principal()

    def onButtonConfirm(self, *args):
        """metodo que nos lleva ingresar en la base de datos"""
        print ("Confirmar")
        act=str(self.actividad)
        actN=len(self.actividad)
        nom=self.nombre.get_text()
        ape=self.apellido.get_text()
        dni_=self.dni.get_text()
        ti=self.tiempo.get_text()
        ti_=int(ti)
        #calcula la cuota en base a unos parametros
        if(ti_<3):
            valBa=25
        else:
            valBa=20
        if(actN<3):
            actBa=1.2
        else:
            actBa=2.8
        cuot=valBa*actBa
        cuot_=str(cuot)
        print(nom,ape,dni_,ti,cuot_,act)
        #Llama a la base de datos pasando los parametros a ingresar
        BD.BD().insertar(nom,ape,dni_,cuot_,ti,act)

    #metodos que cargan las actividades
    def activeSpa(self, *args):
        self.actividad="Spa"
    def activeSpinning(self, *args):
        self.actividad="Spinning"
    def activeSala(self, *args):
        self.actividad="Sala de Maquinas"
    def activeArt(self, *args):
        self.actividad="Artes Marciales"
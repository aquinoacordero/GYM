#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import menu
from gi.repository import Gtk

#Esta clase sera la encargada de mostrar el contenido de la base de datos
class datos:
    #creamos el constructor
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("datos.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("window1")
    #declaramos los objetos del archivo glade en variables
    datos = builder.get_object("labelDatos")

    def __init__(self, dat):
        #señales que enlazan as acciones creadas en glade con metodos de la clase
        signals = { "onButtonBack" : self.onButtonBack,
                    "onButtonExit" : self.onButtonExit
                    }
        #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        #recogemos el nombre, apellido, cuota, tiempo y actividades
        self.datos.set_text(str(dat))
        self.win.show_all()

    def onButtonExit(self, *args):
        sys.exit(0)

    def onButtonBack(self, *args):
        self.win.hide()
        menu.principal()
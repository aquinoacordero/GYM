#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class adv:
    """creamos el constructor"""
    builder = Gtk.Builder()
    #asignamos el archivo glade al constructor
    builder.add_from_file("avisoActividades.glade")
    #cargamos la ventana del archivo glade
    win = builder.get_object("messagedialog1")

    #metodo principal
    def __init__(self):

        #señales que enlazan as acciones creadas en glade con metodos de la clase
        signals = { "onButtonok" : self.onButtonok
                    }
         #asignamos al constructor las señales
        self.builder.connect_signals(signals)
        self.win.show_all()

    def onButtonok(self, *args):
        self.win.hide()
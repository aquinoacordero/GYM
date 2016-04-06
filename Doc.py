#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
import os
import menu

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

'forma xml de nuestra barra de tareas'

UI_INFO = """
<ui>
  <menubar name='TestMenubar'>
    <menu action='FileMenu'>
      <menuitem action='MenuAction' />
    </menu>
  </menubar>
  <toolbar name='TestToolbar'>
    <toolitem action='ToolbarAction' />
    <toolitem action='FileBack' />
  </toolbar>
</ui>
"""

class MyWindow(Gtk.Window,):

    """clase principal"""

    label = Gtk.Label("CLIENTE")

    def __init__(self,dni,nom,ape,cuot,ti,act):
        """metodo de inicio"""

        Gtk.Window.__init__(self, title="Test")

        self.set_default_size(250, 250)

        action_group = Gtk.ActionGroup(name="test_actions")

        self.add_menu_action(action_group)
        self.add_toolbar_action(action_group)

        uimanager = self.create_ui_manager()
        uimanager.insert_action_group(action_group)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        menubar = uimanager.get_widget("/TestMenubar")
        box.pack_start(menubar, False, False, 0)

        toolbar = uimanager.get_widget("/TestToolbar")
        box.pack_start(toolbar, False, False, 0)

        box.add(self.label)

        self.add(box)

        self.dni=dni
        self.nom=nom
        self.ape=ape
        self.cuot=cuot
        self.ti=ti
        self.act=act

    def add_menu_action(self, action_group):
        """Asocia una accion a cada componente de la barra de menu"""
        action_filemenu = Gtk.Action(name="FileMenu", label="Generar")
        action_group.add_action(action_filemenu)


        action = Gtk.Action(name='MenuAction',
                            label="Doc",
                            stock_id=Gtk.STOCK_NEW)
        action.connect('activate', self.on_menu_action)
        action_group.add_action_with_accel(action, 'N')

    def add_toolbar_action(self, action_group):
        """Asocia una accion a cada componente de la barra de tareas"""

        action = Gtk.Action(name='ToolbarAction',
                            label="Press me",
                            stock_id=Gtk.STOCK_FIND)
        action.connect('activate', self.on_toolbar_action)
        action_group.add_action_with_accel(action, 'X')

        action = Gtk.Action(name='FileBack',
                            label="back",
                            stock_id=Gtk.STOCK_GO_BACK)
        action.connect('activate', self.on_menu_back)
        action_group.add_action_with_accel(action, 'Z')

    def on_menu_action(self, widget):
        """metodo que genera el pdf"""
        #cabecera

        follaEstilo=getSampleStyleSheet()

        guion=[]

        cabecera=follaEstilo['Heading4']
        cabecera.pageBreakBefore=0
        cabecera.KepWithNext=0  #Empezar pagina en blanco o no
        cabecera.backColor=colors.red

        parrafo=Paragraph("GYM python", cabecera)

        guion.append(parrafo)
        guion.append(Spacer(0,20))
        #cuerpo
        estilo=follaEstilo['BodyText']

        parrafo2=Paragraph("NOMBRE: "+self.nom,estilo)
        guion.append(parrafo2)
        guion.append(Spacer(0,10))

        parrafo3=Paragraph("APELLIDOS: "+self.ape,estilo)
        guion.append(parrafo3)
        guion.append(Spacer(0,10))

        parrafo4=Paragraph("TIEMPO: "+self.ti,estilo)
        guion.append(parrafo4)
        guion.append(Spacer(0,10))

        parrafo5=Paragraph("ACTIVIDADES: "+self.act,estilo)
        guion.append(parrafo5)
        guion.append(Spacer(0,10))

        parrafo6=Paragraph("Total a pagar: "+self.cuot,estilo)
        guion.append(parrafo6)
        guion.append(Spacer(0,10))

        #imagen
        imagen="./imagenes/gym.jpg"
        imagen_logo=Image(os.path.realpath(imagen),width=100,height=50)
        guion.append(imagen_logo)

        nomdoc=self.dni
        doc=SimpleDocTemplate(nomdoc+".pdf", pagesize=A4, showBoundary=1)
        doc.build(guion)

    def on_toolbar_action(self, widget):
        """Muestra los datos del cliente para el que se va agenerar el pdf"""

        print("DNI: "+self.dni+"NOMBRE: "+self.nom+"APELLIDOS: "+self.ape)
        self.label.set_text("DNI: "+self.dni+"\n"+"NOMBRE: "+self.nom+"\n"+"APELLIDOS: "+self.ape)
        '= Gtk.Label("DNI: "+self.dni+"\n"+"NOMBRE: "+self.nom+"\n"+"APELLIDOS: "+self.ape)'

    def on_menu_back(self, widget):
        """regrea a la ventana de inicio"""

        menu.principal()

    def create_ui_manager(self):
        uimanager = Gtk.UIManager()

        uimanager.add_ui_from_string(UI_INFO)

        self.add_accel_group(uimanager.get_accel_group())

        return uimanager

def tool(dni,nom,ape,cuot,ti,act):
    window = MyWindow(dni,nom,ape,cuot,ti,act)
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
import os
from setuptools import setup
from distutils.core import setup

setup(name="gimnasio",
          version="1",
          description="programa para la gestion de un gimnasio",
          author="Aitor",
          author_email="zootropo en gmail",
          license="GPL",
          scripts=["menu.py"],
          py_modules=["datos","add","adv","avisoActividades","BD","borrar","buscar","Doc","dnierror"]
    )
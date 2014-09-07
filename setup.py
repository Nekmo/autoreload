#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup

DESCRIPTION = "\
No recargues nunca más. Autoreload vigila por ti un directorio en busca de \
cambios, permitiéndote iniciar un programa en cuanto suceda uno. Autoreload, \
a diferencia de otros de la competencia, permite que dicho programa sea un \
daemon, terminando el ya existente e iniciando el nuevo. Además, cuenta con \
muchas cosas más como definir un comando a ejecutar antes o después, por qué \
extensión de archivo se vigilará, ¡¡o incluso recargar una ventana tras un \
cambio!!"

setup(name='autoreload',
      version='1.0',
      description=DESCRIPTION,
      author='Nekmo',
      author_email='contacto@nekmo.com',
      url='http://nekmo.com/',
      packages=[],
      scripts=['autoreload'],
      install_requires=['watchdog'],
     ) 

from setuptools import setup

setup(
    name= "Paquete" ,
    version= "1.0", 
    description= "Paquete que contiene en paquete1 la Segunda Pre-Entrega y en paquete2 la Primera Pre-Entrega",
    author= "Martin Navarro",
    author_email= "martinnavarro1503@gmail.com",
    packages=["paquete1", "paquete2"] #todas las carpetas que va a contener el Paquete   
)

#EN LA TERMINAL
# sdist le dice a python que quiero crear un paquete distribuible
# --> python .\setup.py sdist
# Crea 2 carpetas (dist y nombre_archivo.egg-info).
# De la carpeta dist el archivo (Paquete Distribuible-1.0.tar.gz) lo puedo compartir con los clientes, 
# para que lo puedan instalar en sus equipos, con los siguientes comandos.

#COMANDOS PARA INSTALAR EN EL EQUIPO
# cd dist
# dir
# pip install .\Paquete-1.0.tar.gz

#SI DESEA COMPROBAR QUE SE INSTALO
#pip list (para ver si esta instalado)

#SI DESEA DESINSTALARLO 
# pip uninstall .\Paquete-1.0.tar.gz
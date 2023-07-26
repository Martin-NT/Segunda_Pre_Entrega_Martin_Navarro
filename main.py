# main.py
from paquete1.modulo1 import *
from paquete1.modulo2 import menu1

# Catálogo de Productos Disponibles
producto1 = Ropa("0001", "Remera", 1500, "Mercado Libre", "Nuevo", "L", "Blanco")
producto2 = Ropa("0002", "Pantalon", 3000, "Mercado Libre", "Nuevo", 40, "Negro")
producto3 = Ropa("0003", "Zapatillas", 5000, "Mercado Libre", "Nuevo", 44, "Blanco")
producto4 = Ropa("0004", "Buzo", 12500, "Mercado Libre", "Nuevo", "XL", "Azul")
producto5 = Ropa("0005", "Campera", 12000, "Mercado Libre", "Usado", "L", "Gris")
producto6 = Tecnologia("0006", "Celular", 100000, "Mercado Libre", "Nuevo", "IPhone", "12 Pro")
producto7 = Tecnologia("0007", "Celular", 150000, "Mercado Libre", "Usado", "IPhone", "13 Pro")
producto8 = Tecnologia("0008", "Celular", 200000, "Mercado Libre", "Nuevo", "IPhone", "14 Pro")
producto9 = Tecnologia("0009", "Notebook", 300000, "Mercado Libre", "Nuevo, Memoria Ram: 16GB - SSD: 512GB - Procesador: Intel Core I7", "HP", "Pavilion")
producto10 = Tecnologia("0010", "Notebook", 200000, "Mercado Libre", "Nuevo, Memoria Ram: 8GB - SSD: 512GB - Procesador: Intel Core I5", "HP", "Pavilion")
productos_disponibles = [producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9, producto10]

print("Bienvenido al programa creado por Martin Navarro ")
# Solo la persona que tenga la clave maestra, puede ver y borrar la información de todos los clientes
# clave == "Clave Maestra1"
menu1(productos_disponibles)

#paquete1  
     #modulo1.py --> clases 
     #modulo2.py --> menus
     #__init__.py
#main.py --> Catálogo de Productos Disponibles y donde se ejecuta
#setup.py

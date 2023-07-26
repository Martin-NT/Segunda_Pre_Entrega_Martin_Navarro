# modulo2.py
from paquete1.modulo1 import *
def menu1(productos_disponibles):
    # Menu Principal de opciones 
    while True:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("Elija una opción del Menú: ")
        print("1. Registrar Cliente")
        print("2. Iniciar Sesión")
        print("3. Informacion de Clientes Registrados")
        print("4. Eliminar Clientes Registrados")
        print("5. Salir")
        try:
            opcion = int(input("¿Qué opción del Menú desea realizar?: "))
            print("--------------------------------------------------------------------------------------------------------------------------------------")
        except ValueError:
            print("--> Por favor ingrese solo el número de la opción del Menú que desea ejecutar.")
            continue

        if opcion == 1:
            print("---- Ha elegido la opción de Registrar Cliente ----")
            while True:
                try:
                    dni = int(input("Ingrese su DNI: "))
                    break
                except ValueError:
                    print("--> Porfavor ingrese su DNI en formato numerico")
                    continue
                
            while True:
                nombre = input("Ingrese su Nombre: ")
                if nombre == "":
                    print("--> Porfavor ingrese su nombre")
                    continue
                else:
                    break
            
            while True:
                apellido = input("Ingrese su Apellido: ")
                if apellido == "":
                    print("--> Porfavor ingrese su apellido")
                    continue
                else:
                    break

            while True:
                try:
                    edad = int(input("Ingrese su Edad: "))
                    break
                except ValueError:
                    print("--> Porfavor ingrese su Edad en formato numerico")
                    continue  
            
            while True:
                domicilio = input("Ingrese su Domicilio: ")
                if domicilio == "":
                    print("--> Porfavor ingrese su domicilio")
                    continue
                else:
                    break    

            while True:
                try:
                    saldo = int(input("Ingrese su Saldo: "))
                    break
                except:
                    print("--> Porfavor ingrese su Saldo en formato numerico y sin puntos")
                    continue
            
            while True:
                email = input("Ingrese su Email: ")
                if email == "":
                    print("--> Porfavor ingrese su email")
                    continue
                else:
                    break 
            
            while True:
                usuario = input("Ingrese nombre de usuario: ")
                if usuario == "":
                    print("--> Porfavor ingrese su usuario")
                    continue
                else:
                    break 
                
            while True:
                password = input("Ingrese contraseña: ")
                if password == "":
                    print("--> Porfavor ingrese su contraseña")
                    continue
                else:
                    break 
          
            cliente_nuevo = Cliente(dni, nombre, apellido, edad, domicilio, email, saldo, usuario, password)
            cliente_nuevo.registrar_cliente()
            print("--------------------------------------------------------------------------------------------------------------------------------------")

        elif opcion == 2:
            print("---- Ha elegido la opción de Iniciar Sesión ----")
            if len(Cliente.clientes_registrados) != 0:
                while True:
                    usuario_ingresado = input("Ingrese nombre de usuario: ")
                    if usuario_ingresado == "":
                        print("--> Porfavor ingrese su usuario")
                        continue
                    else:
                        break
                    
                while True:
                    password_ingresado = input("Ingrese contraseña: ")
                    if password_ingresado == "":
                        print("--> Porfavor ingrese su contraseña")
                        continue
                    else:
                        break 

                encontrado = Cliente.login_usuarios(usuario_ingresado, password_ingresado)
                if encontrado:
                    menu2(encontrado, productos_disponibles)
                print("--------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print("--> No puedes Iniciar sesión porque no hay usuarios registrados")
        
        elif opcion == 3:
            print("---- Ha elegido la opción de Ver Información de los Clientes Registrados ----")
            print("---- Solo puedes acceder a esta opción del Menú, si tienes la Clave Maestra ----")
            pregunta = input("¿Tienes la Clave maestra? (SI/NO): ")
            if pregunta.lower() == "si":
                clave = input("¿Cuál es la Clave maestra?: ")
                if clave == "Clave Maestra1":
                    Cliente.informacion_clientes()
                    print("--------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    print("--> Contraseña Incorrecta!")
            elif pregunta.lower() == "no":
                print("--> Entonces usted solo puede elegir la opción 1,2 y 5")
            else:
                print("--> Debe responder 'Si' o 'No'")
            
        elif opcion == 4:
            print("---- Ha elegido la opción de Eliminar Clientes Registrados ----")
            print("---- Solo puedes acceder a esta opción del Menú, si tienes la Clave Maestra ----")
            pregunta = input("¿Tienes la Clave maestra? (SI/NO): ")
            if pregunta.lower() == "si":
                clave = input("¿Cuál es la Clave maestra?: ")
                if clave == "Clave Maestra1":
                    Cliente.eliminar_informacion_clientes()
                    print("--------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    print("--> Contraseña Incorrecta!")
            elif pregunta.lower() == "no":
                print("--> Entonces usted solo puede elegir la opción 1,2 y 5")
            else:
                print("--> Debe responder 'Si' o 'No'")
                
        elif opcion == 5:
            print("--> Hasta luego!")
            break
        
        else:
            print("--> Opción inválida. Por favor, seleccione una opción válida.")
            ("--------------------------------------------------------------------------------------------------------------------------------------")

def menu2(cliente_logeado, productos_disponibles):
    # Menu de opciones al Iniciar Sesion
    while True:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("Elija una opción del Menú: ")
        print("6. Mostrar Información Personal")
        print("7. Modificar Información Personal")
        print("8. Eliminar Información Personal")
        print("9. Ver Saldo")
        print("10. Agregar Saldo Disponible")
        print("11. Ver Catálogo de Productos")
        print("12. Ver Carrito")
        print("13. Comprar Carrito")
        print("14. Cerrar Sesión")
        try:
            opcion = int(input("¿Qué opción del Menú desea realizar?: "))
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            
        except ValueError:
            print("--> Por favor ingrese solo el número de la opción del Menú que desea ejecutar.")
            continue

        if opcion == 6:
            print("---- Ha elegido la opción de Mostrar Información ----")
            #Usamos cliente_logeado para llamar a informacion_usuario
            if cliente_logeado:
                cliente_logeado.informacion_usuario()
                print("--------------------------------------------------------------------------------------------------------------------------------------")
        
        elif opcion == 7:
            print("---- Ha elegido la opción de Modificar Información ----")
            cliente_logeado.modificar_informacion_usuario()
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            
        elif opcion == 8: 
            print("---- Ha elegido la opción de Eliminar Información ----")
            cliente_logeado.eliminar_informacion_usuario()
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            break
            
        elif opcion == 9:
            print("---- Ha elegido la opción de Ver Saldo Disponible ----")
            print(cliente_logeado.ver_saldo_disponible())
            print("--------------------------------------------------------------------------------------------------------------------------------------")

        elif opcion == 10:
            print("---- Ha elegido la opción de Agregar Saldo ----")
            try:
                saldo_agregado = int(input("¿Cuánto desea agregar?: "))
                print(cliente_logeado.agregar_saldo(saldo_agregado))
                print("--------------------------------------------------------------------------------------------------------------------------------------")
            except:
                print("--> Porfavor ingrese el Saldo en formato numerico.")
                continue
        
        elif opcion == 11:
            print("---- Ha elegido la opción de Ver Catálogo de Productos ----")
            Producto.ver_catalogo(productos_disponibles)
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            pregunta = input("¿Desea agregar algún Producto? (SI/NO): ")
            if pregunta.lower() == "si":
                if cliente_logeado:
                    while True:
                        try:
                            c_producto= int(input("¿Qué Producto desea agregar?: "))
                            if c_producto == 0:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[0]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[0])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 1:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[1]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[1])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 2:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[2]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[2])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 3:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[3]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[3])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 4:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[4]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[4])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 5:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[5]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[5])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 6:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[6]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[6])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 7:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[7]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[7])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 8:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[8]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[8])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                            elif c_producto == 9:
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                print("Se agrego el Producto Seleccionado")
                                print(f"--> El Producto selecionado es:\n{productos_disponibles[9]}")
                                cliente_logeado.agregar_al_carrito(productos_disponibles[9])
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                
                            pregunta2 = input("¿Desea agregar algún otro Producto? (SI/NO): ")
                            if pregunta2.lower() == "no":
                                print("--> Ok, Se han agregado al carrito los productos seleccionados")
                                break
                            elif pregunta2.lower() == "si":
                                print("--> Perfecto")    
                            else:
                                print("--> Porfavor solo responda SI o NO")
                        except ValueError:
                            print("--> Por favor ingrese solo el número del Producto que desea agregar.")
                            continue
            elif pregunta.lower() == "no":
                print("--> No se han agregado Productos al Carrito")
            else:
                print("--> Por favor solo responda 'Si' o 'No'")
                              
        elif opcion == 12:
            print("---- Ha elegido la opción de Ver Carrito ----")
            if cliente_logeado:
                print(cliente_logeado.ver_carrito())
           
        elif opcion == 13:
            print("---- Ha elegido la opción de Comprar Carrito ----")
            if cliente_logeado:
                print(cliente_logeado.comprar_carrito())
                
        elif opcion == 14:
            print(f"--> Cerrando Sesión, ¡Hasta luego!")
            break
        
        else:
            print("--> Opción inválida. Por favor, seleccione una opción válida.")
            ("--------------------------------------------------------------------------------------------------------------------------------------")

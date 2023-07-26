## ACTIVIDAD 3 - BASE DE DATOS - DE LA PRIMER PRE-ENTREGA

#--> No funciona en Visual 
#from google.colab import drive

#Funcion que guarda la info del usuario al registrarse en la Base de Datos
def almacenar_Informacion(nombre_usuario, password, base_de_datos):
    if nombre_usuario in base_de_datos:
        print(f"--> El usuario {nombre_usuario} ya se encuentra registrado en la Base de Datos ")
    else:
        base_de_datos[nombre_usuario] = password
        print(f"--> El usuario '{nombre_usuario}' ha sido registrado en la Base de Datos.")

#Funcion que muestra la info de los usuarios registrado en la Base de Datos
def mostrar_informacion(base_de_datos):
    if len(base_de_datos) != 0:
        print("---- Información de usuarios ----")
        for nombre_usuario, password in base_de_datos.items():
            print("-----------------------------------------")
            print(f"Usuario: {nombre_usuario}")
            print(f"Contraseña: {password}")
            print("-----------------------------------------")
        print(f"Total de usuarios registrados: {len(base_de_datos)}")
    else:
        print("--> No hay nada registrado en la Base de Datos.")

#Funcion para que los usuarios puedan iniciar sesion 
def login_usuarios(nombre_usuario, password, base_de_datos):
    if nombre_usuario in base_de_datos:
        contador_intentos = 0
        while contador_intentos < 3:
            if base_de_datos[nombre_usuario] == password:
                print(f"--> Ha iniciado sesión correctamente. Bienvenido, '{nombre_usuario}'")
                return
            else:
                contador_intentos += 1
                if contador_intentos < 3:
                    print(f"--> Ha ingresado mal su contraseña. Intento {contador_intentos} de 3")
                    password = input("Ingrese su contraseña: ")
                else:
                    print(f"--> Se le acabaron los intentos. Intento {contador_intentos} de 3 ")
                    print("No ha podido iniciar sesión")
                    return
        password = input("Ingrese su contraseña: ")
        if base_de_datos[nombre_usuario] == password:
            print(f"--> Ha iniciado sesión correctamente. Bienvenido, '{nombre_usuario}'")
        else:
            print("--> Contraseña incorrecta.")
    else:
        print(f"--> El usuario '{nombre_usuario}' no está registrado en la base de datos.")

#Funcion que elimina a un usuario de la base de datos
def eliminar_usuario(nombre_usuario, base_de_datos):
    if nombre_usuario in base_de_datos:
        password = input("Ingrese la contraseña para eliminar el usuario: ")
        contador_intentos = 0
        while contador_intentos < 3:
            if password == base_de_datos[nombre_usuario]:
                del base_de_datos[nombre_usuario]
                print(f"--> El usuario {nombre_usuario} ha sido eliminado de la Base de Datos.")
                return
            else:
                contador_intentos += 1
                print(f"--> Ha ingresado mal su contraseña. Intento {contador_intentos} de 3")
                if contador_intentos < 3:
                    password = input("Ingrese la contraseña para eliminar el usuario: ")
        print(f"--> Se le acabaron los intentos. No se ha podido eliminar al usuario {nombre_usuario}")
    else:
        print("--> El usuario no está registrado en la base de datos.")

#Funcion para que un usuario pueda cambiar su nombre de usuario 
def cambiar_nombre_usuario(nombre_usuario, nuevo_nombre_usuario, password, base_de_datos):
    if nombre_usuario in base_de_datos:
        if base_de_datos[nombre_usuario] == password:
            if nombre_usuario != nuevo_nombre_usuario:
                base_de_datos[nuevo_nombre_usuario] = base_de_datos.pop(nombre_usuario)
                print(f"--> Se ha cambiado el nombre de usuario '{nombre_usuario}' por '{nuevo_nombre_usuario}'")
            else:
                print("--> Los Nombres de Usuario son iguales")
        else:
            print("--> Contraseña incorrecta. No se ha podido cambiar el nombre de usuario.")
    else:
        print(f"--> El usuario '{nombre_usuario}' no está registrado en la base de datos.")

#Funcion para que un usuario pueda cambiar su contraseña   
def cambiar_password(nombre_usuario, password_actual, nueva_password, base_de_datos):
    if nombre_usuario in base_de_datos:
        if base_de_datos[nombre_usuario] == password_actual:
            if base_de_datos[nombre_usuario] != nueva_password:
                base_de_datos[nombre_usuario] = nueva_password
                print(f"--> Se ha cambiado la contraseña para el usuario '{nombre_usuario}'.")
            else:
                print("--> Las Contraseñas son iguales")
        else:
            print("--> Contraseña incorrecta. No se ha podido cambiar la contraseña.")
    else:
        print(f"--> El usuario '{nombre_usuario}' no está registrado en la base de datos.")

#Funcion que vacia la base de datos 
def vaciar_base_de_datos(base_de_datos):
    if len(base_de_datos) != 0:
        base_de_datos.clear()
        print("--> La base de datos ha sido vaciada")
        return base_de_datos
    else:
        print("--> No hay nada que vaciar en la Base de Datos")

#Funcion para guardar la info de los usuarios en un archivo txt
def guardar_informacion_en_archivo(base_de_datos):
    drive.mount('/content/drive')

    ruta_archivo = '/content/drive/MyDrive/nombre_archivo.txt'
    
    with open(ruta_archivo, 'w') as archivo:
        for nombre_usuario, password in base_de_datos.items():
            linea = f"usuario = {nombre_usuario} - contraseña = {password}\n"
            archivo.write(linea)

    print("--> La información ha sido guardada en el archivo.")

 
base_de_datos = {}
opcion_valida = False
print("Bienvenido! a la Base de Datos creada por Martin Navarro ")
#Menu de opciones
while True: 
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print("Elija una opción del Menú: ")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Mostrar Información")
    print("4. Eliminar Usuario")      
    print("5. Cambiar Nombre de Usuario")
    print("6. Cambiar Contraseña")
    print("7. Vaciar Base de Datos")
    print("8. Guardar Base de Datos en Archivo")
    print("9. Salir")
    try: 
        opcion = int(input("¿Qué opción del Menú desea realizar?: "))
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        opcion_valida = True
    except:
        print("--> Por favor ingrese solo el numero de la opción del Menu que desea ejecutar.")
        opcion_valida = False
        continue
    
    if opcion == 1:
        print("---- Ha elegido la opción de Registrar Usuario ----")    
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        almacenar_Informacion(nombre_usuario, password, base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 2:
        print("---- Ha elegido la opción de Iniciar Sesión ----") 
        nombre_usuario = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        login_usuarios(nombre_usuario, password, base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 3:
        print("---- Ha elegido la opción de Mostrar Información ----")   
        mostrar_informacion(base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 4:
        print("---- Ha elegido la opción de Registrar Usuario ----")
        nombre_usuario = input("Ingrese el nombre de usuario a eliminar: ")
        eliminar_usuario(nombre_usuario, base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 5:
        print("---- Ha elegido la opción de Cambiar Nombre de Usuario ----")
        nombre_usuario = input("Ingrese el nombre de usuario actual: ")
        password = input("Ingrese su contraseña: ")
        nuevo_nombre_usuario = input("Ingrese el nuevo nombre de usuario: ")
        cambiar_nombre_usuario(nombre_usuario, nuevo_nombre_usuario, password, base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 6:
        print("---- Ha elegido la opción de Cambiar Contraseña ----")
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        password_actual = input("Ingrese su contraseña actual: ")
        nueva_password = input("Ingrese la nueva contraseña: ")
        cambiar_password(nombre_usuario, password_actual, nueva_password, base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
    
    elif opcion == 7:
        print("---- Ha elegido la opción de Vaciar Base de Datos ----") 
        vaciar_base_de_datos(base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        
    elif opcion == 8:
        print("---- Ha elegido la opción de Guardar la Base de Datos en Archivo  ----") 
        guardar_informacion_en_archivo(base_de_datos)
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        
    elif opcion == 9:
       print("--> Usted ha salido del sistema, ¡Hasta luego!")
       break
   
    else:
        print("--> Opción inválida. Por favor, seleccione una opción válida.")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        opcion_valida = False
    


# modulo1.py
class Producto:
    def __init__(self, articulo, n_producto, precio, lugar, descripcion):
        self.articulo = articulo
        self.n_producto = n_producto
        self.precio = precio
        self.lugar = lugar
        self.descripcion = descripcion
        self.productos_disponibles = []
        
    def __str__(self):
        return f"Articulo -> {self.articulo}\nProducto -> {self.n_producto}\nPrecio -> ${self.precio}\nLugar: {self.lugar}\nDescripción: {self.descripcion}"
    
    #def ver_catalogo(self, productos_disponibles):
        #if len(productos_disponibles) != 0:
            #print("---- Catálogo de Productos ----")
            #for n, producto in enumerate(productos_disponibles):
                #print("-----------------------------------------")
                #print(n, producto)
                #print("-----------------------------------------")
        #else:
            #print("--> No hay Productos Disponibles en el Catálogo.")
    
    @classmethod
    #@classmethod en Django es un decorador que se utiliza para definir métodos de clase en modelos. 
    #Estos métodos se invocan en la clase en lugar de en instancias y se utilizan para realizar operaciones que involucran la clase en su totalidad.
    def ver_catalogo(cls, productos_disponibles):
        if len(productos_disponibles) != 0:
            print("---- Catálogo de Productos ----")
            for n, producto in enumerate(productos_disponibles):
                print("-----------------------------------------")
                print(n, producto)
                print("-----------------------------------------")
        else:
            print("--> No hay Productos Disponibles en el Catálogo.")
            
class Ropa(Producto):
    def __init__(self, articulo, n_producto, precio, lugar, descripcion, talle, color):
        super().__init__(articulo, n_producto, precio, lugar, descripcion)   
        self.talle = talle
        self.color = color
        
    def __str__(self):
        return f"{super().__str__()}\nTalle -> {self.talle}\nColor -> {self.color}" 
       
class Tecnologia(Producto):
    def __init__(self, articulo, n_producto, precio, lugar, descripcion, marca, modelo):
        super().__init__(articulo, n_producto, precio, lugar, descripcion) 
        self.marca = marca
        self.modelo = modelo 
        
    def __str__(self):
        return f"{super().__str__()}\nMarca -> {self.marca}\nModelo -> {self.modelo} "
    
class Persona:
    def __init__(self,dni, nombre, apellido, edad, domicilio):
        self.dni = dni 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.domicilio = domicilio

    def __str__(self):
        return f"DNI: {self.dni}\nNombre: {self.nombre.capitalize()}\nApellido: {self.apellido.capitalize()}\nEdad: {self.edad}\nDomicilio: {self.domicilio.title()}"
    
class Cliente(Persona):
    clientes_registrados = []

    def __init__(self, dni, nombre, apellido, edad, domicilio, email, saldo, usuario, password):
        super().__init__(dni, nombre, apellido, edad, domicilio)
        self.email = email
        self.__saldo = saldo
        self.usuario = usuario
        self.__password = password
        self.carrito = []

    def __str__(self):
        return f"---- Información del Cliente ----\nDNI: {self.dni}\nNombre: {self.nombre.title()}\nApellido: {self.apellido.title()}\nEdad: {self.edad}\nDomicilio: {self.domicilio.title()}\nCorreo: {self.email}"
    
    def registrar_cliente(self):
        Cliente.clientes_registrados.append(self)
        print(f"--> El Cliente {self.nombre.title()} {self.apellido.title()} ha sido registrado")

    def login_usuarios(usuario_ingresado, password_ingresado):
        for cliente in Cliente.clientes_registrados:
            if cliente.usuario == usuario_ingresado and cliente.__password == password_ingresado:
                print(f"--> Ha iniciado sesión correctamente. Bienvenido, '{cliente.nombre.title()}'")
                return cliente
            else:
                print("--> Usuario o contraseña incorrectos.")
                return None 

    #def login_usuarios(self, usuario, password):
     #   encontrado = False 
      #  for cliente in Cliente.clientes_registrados:
       #     if cliente.usuario == usuario and cliente.__password == password:
        #        encontrado = True
         #       print(f"--> Ha iniciado sesión correctamente. Bienvenido, '{cliente.nombre.title()}'")
          #      return cliente
          #  else:
          #      encontrado = False
          #      print("--> Usuario o contraseña incorrectos.")

       # if not encontrado:
        #    print("--> Usuario o contraseña incorrectos.")
            
       # return encontrado
    
    def informacion_usuario(self):
        print(super().__str__())
        print(f"Usuario: {self.usuario}\nContraseña: {self.__password}")
    
    def eliminar_informacion_usuario(self):
        print("¿Está seguro que desea eliminar su información? Esta acción no se puede deshacer.")
        confirmacion = input("Ingrese 'SI' si está seguro, de lo contrario, ingrese 'NO': ")
        if confirmacion.lower() == "si":
            Cliente.clientes_registrados.remove(self)
            print("--> Su información ha sido eliminada. ¡Hasta luego!")
        elif confirmacion.lower() == "no":
            print("--> Acción cancelada. Su información sigue intacta.")
        else:
            print("--> Por favor solo responda 'Si' o 'No'. Por precaución, la acción ha sido cancelada. Su información sigue intacta.")
    
    def modificar_informacion_usuario(self):
        print("¿Está seguro que desea modificar su información?")
        confirmacion = input("Ingrese 'SI' si está seguro, de lo contrario, ingrese 'NO': ")
        while True:
            if confirmacion.lower() == "si":
                pregunta = input("¿Que desea modificar?(Exit para salir): ")
                if pregunta.lower() == "dni":
                    print("--> Ha elegido modificar su DNI")
                    try:
                        dni_editado = int(input("Ingrese su DNI: "))
                        self.dni = dni_editado
                        print("--> Su DNI ha sido modificado. ¡Hasta luego!")
                        print("--------------------------------------------------------------------------------------------------------------------------------------")
                    except:
                        print("--> Porfavor ingrese el DNI en formato numerico.")
                        continue
                
                elif pregunta.lower() == "nombre":
                    print("--> Ha elegido modificar su Nombre")
                    while True:
                        nombre_editado = input("Ingrese su Nombre: ")
                        if nombre_editado == "":
                            print("--> Porfavor ingrese su Nombre")
                            continue
                        else:
                            self.nombre = nombre_editado.title()
                            print("--> Su Nombre ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                        
                elif pregunta.lower() == "apellido":
                    print("--> Ha elegido modificar su Apellido")
                    while True:
                        apellido_editado = input("Ingrese su Apellido: ")
                        if apellido_editado == "":
                            print("--> Porfavor ingrese su Apellido")
                            continue
                        else:
                            self.apellido = apellido_editado.title()
                            print("--> Su Apellido ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                        
                elif pregunta.lower() == "edad":
                    print("--> Ha elegido modificar su Edad")
                    try:
                        edad_editado = int(input("Ingrese su Edad: "))
                        self.edad = edad_editado
                        print("--> Su Edad ha sido modificado. ¡Hasta luego!")
                        print("--------------------------------------------------------------------------------------------------------------------------------------")
                    except:
                        print("--> Porfavor ingrese el Edad en formato numerico.")
                        continue
                
                elif pregunta.lower() == "domicilio":
                    print("--> Ha elegido modificar su Domicilio")
                    while True:
                        domicilio_editado = input("Ingrese su Domicilio: ")
                        if domicilio_editado == "":
                            print("--> Porfavor ingrese su Domicilio")
                            continue
                        else:
                            self.domicilio = domicilio_editado.title()
                            print("--> Su Domicilio ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                
                elif pregunta.lower() == "email":
                    print("--> Ha elegido modificar su Email")
                    while True:
                        email_editado = input("Ingrese su Email: ")
                        if email_editado == "":
                            print("--> Porfavor ingrese su Email")
                            continue
                        else:
                            self.email = email_editado
                            print("--> Su Email ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                        
                elif pregunta.lower() == "usuario":
                    print("--> Ha elegido modificar su Usuario")
                    while True:
                        usuario_editado = input("Ingrese su Usuario: ")
                        if usuario_editado == "":
                            print("--> Porfavor ingrese su Usuario")
                            continue
                        else:
                            self.usuario = usuario_editado
                            print("--> Su Usuario ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                        
                elif pregunta.lower() == "contraseña":
                    print("--> Ha elegido modificar su Contraseña")
                    while True:
                        password_editado = input("Ingrese su Contraseña: ")
                        if password_editado == "":
                            print("--> Porfavor ingrese su Contraseña")
                            continue
                        else:
                            self.__password = password_editado
                            print("--> Su Contraseña ha sido modificado. ¡Hasta luego!")
                            print("--------------------------------------------------------------------------------------------------------------------------------------")
                            break
                
                elif pregunta.lower() == "exit":
                    print("--> Saliendo de Modificar información Personal")
                    print("--------------------------------------------------------------------------------------------------------------------------------------")
                    break
                        
                else:
                    print("--> Opción Incorrecta, las opciones son:\n-> DNI\n-> Nombre\n-> Apellido\n-> Edad\n-> Domicilio\n-> Email\n-> Usuario\n-> Contraseña\n-> Exit (para salir)")
                    print("--------------------------------------------------------------------------------------------------------------------------------------")
                    
            elif confirmacion.lower() == "no":
                print("--> Acción cancelada. Su información sigue intacta.")
                break
             
            else:
                print("--> Por favor solo responda 'Si' o 'No'. Por precaución, la acción ha sido cancelada. Su información sigue intacta.")
                break   
                    
    def informacion_clientes():
        if len(Cliente.clientes_registrados) != 0:
            print("---- Información de Clientes Registrados ----")
            for cliente in Cliente.clientes_registrados:
                print(cliente)
        else:
            print("--> No se encuentran Clientes registrados")
            
    def eliminar_informacion_clientes():
        if len(Cliente.clientes_registrados) != 0:
                print("¿Está seguro que desea eliminar todos los Clientes? Esta acción no se puede deshacer.")
                confirmacion = input("Ingrese 'SI' si está seguro, de lo contrario, ingrese 'NO': ")
                if confirmacion.lower() == "si":        
                    Cliente.clientes_registrados.clear()
                    print("Se han borrado todos los clientes registrados")
                elif confirmacion.lower() == "no":
                    print("--> Acción cancelada. Su información sigue intacta.")
                else:
                    print("--> Por favor solo responda 'Si' o 'No'")
                    print("--> Por Precaución la acción ha sido cancelada. Su información sigue intacta.")
        else:
            print("--> No se puede borrar porque no se encuentran Clientes registrados")
    
    def agregar_al_carrito(self, producto):
        return self.carrito.append(producto)

    def ver_carrito(self):
        if len(self.carrito) != 0:
            total_carrito = sum(producto.precio for producto in self.carrito)
            productos_en_carrito = "\n".join(f"->Producto {i + 1}\n{producto}\n{'-' * 50}" for i, producto in enumerate(self.carrito))
            return f"--> Los Productos agregados al carrito son: \n{productos_en_carrito}\n--> Total del Carrito: ${total_carrito}"
        else:
            return "--> No se han encontrado Productos en el Carrito"
        
    def comprar_carrito(self):
        total_carrito = sum(producto.precio for producto in self.carrito)
        if self.__saldo >= total_carrito:
            self.__saldo -= total_carrito
            self.carrito.clear()
            return f"--> Gracias {self.nombre} por la compra, le quedan ${self.__saldo}\n--> Enviando Factura a {self.email}"
        else:
            return f"--> Saldo Insuficiente, le faltan ${total_carrito - self.__saldo}"

    def agregar_saldo(self, saldo_agregado):  
        self.__saldo += saldo_agregado
        return f"--> Ahora tiene disponible en su cuenta ${self.__saldo}"

    def ver_saldo_disponible(self):
        return f"--> Tiene disponible en su cuenta ${self.__saldo}"
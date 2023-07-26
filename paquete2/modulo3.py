# ACTIVIDADES 1 Y 2 DE LA PRIMER PRE-ENTREGA

nombre = (input("Ingrese su nombre: ")).capitalize()

while True: 
    print("--------------------------------------------------------")
    print(f" {nombre } elige una opción del Menú de Actividades: ")
    print("1. Actividad 1")
    print("2. Actividad 2 Ejercicio 1")
    print("3. Actividad 2 Ejercicio 2")
    print("4. Actividad 2 Ejercicio 3")
    print("5. Actividad 2 Ejercicio 4")
    print("6. Actividad 2 Ejercicio 5")
    print("7. Actividad 2 Ejercicio 6")
    print("8. Salir")
    print("--------------------------------------------------------")
    
    try: 
        opcion = int(input("¿Qué opción del Menú desea realizar?: "))
    except ValueError:
        print("--> Por favor ingrese solo el numero de la opción del Menu que desea ejecutar.")
    
    if opcion == 1:
        print(f"---- {nombre} ha elegido la Actividad 1 ----")
        def anio_bisiesto(anio):
            if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
                respuesta = "Es bisiesto"
                return respuesta
            else:
                respuesta = "No es bisiesto" 
                return respuesta
        
        print(f"Bienvenid@ {nombre}, este programa le dirá si el año ingresado es bisiesto o no")
           
        while True:
            try:
                anio = input("Ingrese un año (o escriba 'fin' para salir): ") 
                
                if anio.lower() == "fin":
                    break
                anio = int(anio)  
                respuesta = anio_bisiesto(anio) 
                print(f"El año {anio} {respuesta}")
            except ValueError:
                print("Por favor ingrese el año en formato númerico.")
    
    elif opcion == 2:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 1 ----")
        def area_rectangulo(base, altura):
            area = round(base * altura)
            return area 
        
        print(f"Bienvenid@ {nombre}, este programa le dirá el área de un rectángulo ")
        print("Ejemplo de uso: ")
        ejemplo = area_rectangulo(15,10)
        print(f"El área del rectángulo de base 15 y altura 10 es de {ejemplo}")
        print("-------------------------------------------------------------------------------------------------------------")
        
        while True:
            try:
                base = input("Ingrese la base de su rectángulo (fin para salir): ")
                if base.lower() == "fin":
                    break
                altura = input("Ingrese la altura de su rectángulo (fin para salir): ")
                if altura.lower() == "fin":
                    break
                base = float(base)
                altura = float(altura)
                area_r = area_rectangulo(base, altura)
                print(f"El área del rectángulo de base {base} y altura {altura} es de {area_r} ")
                print("-------------------------------------------------------------------------------------------------------------")
            except ValueError:
                print("Por favor ingrese la base y altura en formato númerico.")
    
    elif opcion == 3:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 2 ----")
        import math
        def area_circulo(radio):
            # Acceder al número pi
            pi = math.pi
            area = round((radio**2) * pi)
            return area 
        
        print(f"Bienvenid@ {nombre}, este programa le dirá el área de un círculo ") 
        
        print("Ejemplo de uso: ")
        ejemplo = area_circulo(5)
        print(f"El área del círculo de radio 5 es de {ejemplo} ")
        print("-------------------------------------------------------------------------------------------------------------")
        
        while True:
            try:
                radio = input("Ingrese el radio de su círculo (fin para salir): ")
                if radio.lower() == "fin":
                    break
                radio = float(radio)
                area_c = area_circulo(radio)
                print(f"El área del círculo de radio {radio} es de {area_c} ")
                print("-------------------------------------------------------------------------------------------------------------")
            except ValueError:
                print("Por favor ingrese el radio en formato númerico.")
    
    elif opcion == 4:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 3 ----")
        def relacion(num1,num2):
            if num1 > num2:
                return 1, f"El {num1} es mayor que el {num2}"
            elif num1 < num2:
                return -1, f"El {num1} es menor que el {num2}"
            else:
                return 0, f"El {num1} es igual que el {num2}"
            
        print(f"Bienvenid@ {nombre}, este programa le dirá la relación de los números ingresados ")     
        
        print("Ejemplos de uso")
        ejemplo1, respuesta = relacion(5,10)
        print(f"{respuesta} ----------> {ejemplo1}")
        ejemplo2, respuesta = relacion(10,5)
        print(f"{respuesta} ----------> {ejemplo2}")
        ejemplo3, respuesta = relacion(5,5)
        print(f"{respuesta} ----------> {ejemplo3}")
        print("-------------------------------------------------------------------------------------------------------------")
        
        while True: 
            try:
                num1 = input("Ingrese el primer número (fin para salir): ")
                if num1.lower() == "fin":
                    break
                num2 = input("Ingrese el segundo número (fin para salir): ")
                if num2.lower() == "fin":
                    break
                num1 = float(num1)
                num2 = float(num2)
                resultado, respuesta = relacion(num1,num2)
                print(f"{respuesta} ----------> {resultado}")
                print("-------------------------------------------------------------------------------------------------------------")
            except ValueError:
                print("Por favor ingrese los números en formato númerico.")
    
    elif opcion == 5:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 4 ----")
        def intermedio(num1, num2):
            punto_intermedio = (num1 + num2) / 2
            return punto_intermedio
        
        print(f"Bienvenid@ {nombre}, este programa le dirá el número intermedio de los números ingresados ") 
        
        print("Ejemplos de uso")
        ejemplo = intermedio(-12,24)
        print(f"El punto intermedio entre el -12 y el 24 es {ejemplo} ")
        print("-------------------------------------------------------------------------------------------------------------")
        
        while True:
            try:
                num1 = input("Ingrese el primer número (fin para salir): ")
                if num1.lower() == "fin":
                    break
                num2 = input("Ingrese el segundo número (fin para salir): ")
                if num2.lower() == "fin":
                    break
                num1 = float(num1)
                num2 = float(num2)
                resultado = intermedio(num1,num2)
                print(f"El punto intermedio entre el {num1} y el {num2} es {resultado} ")
                print("-------------------------------------------------------------------------------------------------------------")
            except ValueError:
                print("Por favor ingrese los números en formato númerico.")
                
    elif opcion == 6:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 5 ----")
        def recortar(num,limite_inferior,limite_superior):
            if num < limite_inferior:
                return limite_inferior
            elif num > limite_superior:
                return limite_superior
            else:
                return num
            
        print(f"Bienvenid@ {nombre}, este programa le devolverá el número recortado entre los límites ingresados ") 
        
        print("Ejemplos de uso") 
        ejemplo = recortar(15,0,10)
        print("El resultado de recortar el número 15 entre los límites 0 y 10 es:", ejemplo)
        print("-----------------------------------------------------------------------------------------------------------------------------")
        
        while True:
            try:
                num = input("Ingrese un número a recortar (fin para salir): ")
                if num.lower() == "fin":
                    break
                limite_inferior = input("Ingrese un límite inferior (fin para salir): ")
                if limite_inferior.lower() == "fin":
                    break
                limite_superior = input("Ingrese un límite superior (fin para salir): ")
                if limite_superior.lower() == "fin":
                    break
                num = int(num)
                limite_inferior = int(limite_inferior)
                limite_superior = int(limite_superior)
                resultado = recortar(num,limite_inferior,limite_superior)
                print(f"El resultado de recortar el número {num} entre los límites {limite_inferior} y {limite_superior} es {resultado}")
                print("-----------------------------------------------------------------------------------------------------------------------------")
            except ValueError:
                print("Por favor ingrese el número y los límites en formato númerico.")
                
    elif opcion == 7:
        print(f"---- {nombre} ha elegido la Actividad 2 Ejercicio 6 ----")
        def separar(lista):
            pares = []
            impares = []
            
            for num in lista:
                if num % 2 == 0:
                    pares.append(num)
                else:
                    impares.append(num)
            
            pares.sort()
            impares.sort()
            return pares, impares
        
        print(f"Bienvenid@ {nombre}, este programa le dirá que números de la lista ingresada son pares e impares ") 
        lista_numeros = []
        while True:
            num = input("Ingrese los números que desee (fin para terminar): ")
            if num.lower() == "fin":
                break
            try:
                num = int(num)
                lista_numeros.append(num)
            except ValueError:
                print("Por favor ingrese un número")
        
        print(f"Lista = {lista_numeros}")
        pares, impares = separar(lista_numeros)
        print(f"Los Números Pares son {pares}")
        print(f"Los Números Impares son {impares}")
    
    elif opcion == 8:
       print(f"--> Usted ha salido del sistema, ¡Hasta luego! {nombre}")
       break
   
    else:
        print("--> Opción inválida. Por favor, seleccione una opción válida.")
    
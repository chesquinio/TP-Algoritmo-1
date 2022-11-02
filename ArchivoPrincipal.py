"""
Librerias del programa
"""
import random

"""
Almacenaje de variables principales
"""

ultimaCompraProductos = "-x-"

ultimaCompraGasto = "-x-"

ultimaTarjetaUtilizada = "xxxx-xxxx-xxxx-xxxx"
    
productos = [
     #FRUTAS
     ["Banana", 15], ["Manzana", 10], ["Mango", 25], ["Durazno", 20], ["Mandarina", 16], ["Piña", 46], ["Sandia", 51], ["Melon", 29],
     #VERDURAS
     ["Tomate", 10], ["Lechuga", 13], ["Palta", 24], ["Morron verde", 23], ["Morron rojo", 21], ["Limon", 19],
     #GOLOSINAS
     ["Chocolate", 40], ["Confites", 37], ["Bombon", 20], ["Chicle", 25],
     #BEBIDAS
     ["Agua", 15], ["Agua saborizada", 20], ["Coca cola", 30], ["Fanta", 28], ["Sprite", 27], ["Trompis", 14], ["Cordoba", 12], ["Cerveza", 35],
     #PRODUCTOS PREMIUM
     ["Yerba", 55]
]

"""
Funciones para el programa
"""
def listado():
    for i in range(len(productos)):
                    
        if i == 0:
            print("")
            print("FRUTAS")
        if i == 8:
            print("")
            print("VERDURAS")
        if i == 14:
            print("")
            print("GOLOSINAS")
        if i == 18:
            print("")
            print("BEBIDAS")
        if i == 26:
            print("")
            print("PRODUCTOS PREMIUM")
                    
        print("---", productos[i][0], "------ $",productos[i][1], "---")   
        
        
        
"""
Menu principal
"""

while True:
    
    print("")
    print("Escriba el procedimiento que desee")
    print("")
    print("---[REALIZAR COMPRA]---")
    print("")
    print("---[LISTA DE PRODUCTOS]---")
    print("")
    print("---[ULTIMA OPERACION]---")
    print("")
    print("---[SALIR]---")
    print("")
    eleccionPrincipal = input()
    
    
    
    
    """
    Ultima operacion realizada
    """
    
    if eleccionPrincipal == "ultima operacion":
        
        print("La lista de los ultimos productos comprados es la siguiente:") 
        for prod in ultimaCompraProductos:
            print(prod)
        print("") 
        
        print("Y ha gastado un total de:")
        print(f"${ultimaCompraGasto}")
        print("")
        
        print("Tarjeta utilizada:")
        print(ultimaTarjetaUtilizada)
        print("")
    
    
    
    
    
    
        """
        Listado de los productos en venta
        """
    
    elif eleccionPrincipal == "lista de productos":
    
        print("")
        listado()            
        print("")
    
    
    
    
    
    
        """
        Proceso de compra
        """  
    
    elif eleccionPrincipal == "realizar compra":
        
        """
        #Datos del Usuario
        """
        
        print("")
        print("Por favor, ingrese su nombre")
        persona = input()
        
        
        """
        #Operacion de compra
        """
        
        for x in range(1):
            
            """
            #Validador de tarjetas
            """
            
            validacionTarjeta = False
            validacionTarjetaGuiones = False
            
            while validacionTarjeta == False and validacionTarjetaGuiones == False:
                print("")
                print(f"Hola {persona}, a continuacion ingrese su numero de tarjeta de la siguiente manera xxxx-xxxx-xxxx-xxxx correspondiendo la x a los numeros correspondientes")
                
                numeroTarjeta = input()
                
                cont1 = 0
                
                for guiones in numeroTarjeta:
                    
                    if guiones == "-":
                        cont1 = cont1 + 1
                """
                Evaluacion guiones
                """
                            
                if cont1 == 3:
                        validacionTarjetaGuiones = True
                        
                elif cont1 != 3:
                        print("El numero de tarjeta tiene un error de tipeo, corrija la cantidad de guiones que haya utilizado")
                        
                """
                Evaluacion cantidad de cifras
                """        
                        
                if len(numeroTarjeta) == 19:
                    validacionTarjeta = True
                    
                elif len(numeroTarjeta) != 19:
                    print("El numero de tarjeta no es correcto")
                    
                """
                Evaluacion de codigo de seguridad
                """
                
                if validacionTarjeta == True and validacionTarjetaGuiones == True:
                    
                    validacionCodigo = False
        
                    while validacionCodigo == False:
                        print("")
                        print("Ahora a continuacion ingrese el codigo de seguridad de la siguiente manera xxx siendo x el numero correspondiente")
                        numeroCodigo = input()
                        
                        """
                        Evaluacion de numeros correctos en el codigo de seguridad
                        """
                        
                        ayudaCertificador = ["0","1","2","3","4","5","6","7","8","9"]
                        Certificador = 0                            
                        
                        for numeroIndividual in numeroCodigo:  
                            
                            for numero in ayudaCertificador:
                                
                                if numeroIndividual == numero:
                                    Certificador = Certificador + 1
                                    break
                                
                        if Certificador == 3:
                            validacionCodigo = True
                        else:
                            print("Ese codigo no coincide")
                            
            """
            #Ingreso del dinero     
            """
            print("")
            print("Ingrese el dinero que desea abonar al cajero, como termino de seguridad antes de introducir los productos que comprara")
            dineroPersona = int(input())
            
            """
            #Cartel de los Productos
            """
            listado()
            
            alimentosSeleccionCompra = []
            
            dineroTotalGastado = 0
            
            """
            #Seleccion de Productos
            """
            var = 0
            while True:
                
                print("")
                print("Escriba en pantalla los elementos que desea llevar, cuando alla terminado, toque el boton")
                print("Recuerde utilizar mayuscula en la primera letra cuando se refiera a un producto")
                print("")
                print("--[Terminar]--")
                print("")     
                print("Lista:") 
                for x in alimentosSeleccionCompra:
                    print(f"{x}")
                
                seleccionCompra = input()
                
                #Contabilidad del Producto
                
                var = False
                
                for i in range(len(productos)):
        
                        if seleccionCompra == productos[i][0]:
                            
                            alimentosSeleccionCompra.append(seleccionCompra)
                            
                            dineroTotalGastado = dineroTotalGastado + productos[i][1]                   
                            
                            var = True
                            
                if seleccionCompra == "terminar":
                    
                    break
            
                elif var == False:
                    print("")
                    print("Este producto no se encuentra en la lista, intente nuevamente")
                
                
                
            """
            #Contabilidad del Dinero 
            """
            
            if dineroTotalGastado <= dineroPersona:
                
                if dineroTotalGastado == 0:
                    
                    break
                
                vuelto = dineroPersona - dineroTotalGastado
                
                print(f"El total es de ${dineroTotalGastado}--- ---Le sobran un total de ${vuelto}")
                print("")
                print("Escriba la opcion que desee")
                print("")
                print("--[PAGAR]--")
                print("")
                print("--[CANCELAR COMPRA]--")
                opcionario1 = input()
                
                if opcionario1 == "pagar":
                
                    if vuelto >= 0:  
                    
                        print(f"Su compra se ha realizado con exito, se le reintegraran a la tarjeta la suma de ${vuelto} que no ha llegado a utilizar")
                                
                    else:
                            
                        print("Su compra se a realizado con excito")
                    
                elif opcionario1 == "cancelar compra":
                     
                    break
            
            elif dineroTotalGastado > dineroPersona:
                
                print(f"El total de la compra es de ${dineroTotalGastado}--- --- Su dinero es solo ${dineroPersona}: ")
                print("")
                print("Elija alguna de estas opciones")
                print("")
                print("--[REINTEGRAR EFECTIVO]--")
                print("")
                print("--[REMOVER]--")
                print("")
                print("--[CANCELAR COMPRA]--")
                opcionario2 = input()
                
                """
                #Removedor de productos
                """
                
                if opcionario2 == "remover":
                    
                    
                    while dineroTotalGastado > dineroPersona:
                        
                        print("")
                        print("Ingrese el producto a remover")
                        removedor = input()
                        
                        var1 = False
                        
                        for i in range(len(alimentosSeleccionCompra)):                    
                            
                            if removedor == alimentosSeleccionCompra[i]:
                                    
                                    var1 = True
                                
                                    alimentosSeleccionCompra[i] = ""
                                    
                                    print(f"Se remevio {removedor}")
                                    
                                    for v in range(len(productos)):
                
                                        if removedor == productos[v][0]:
                                    
                                            dineroTotalGastado = dineroTotalGastado - productos[v][1]
                                            
                                            varAlt2 = dineroTotalGastado - dineroPersona
                                            
                                            print(f"Se le descontara ${productos[v][1]}")
                                            
                                            if varAlt2 > 0:
                                                
                                                print(f"Dinero faltante a pagar: ${varAlt2}")
                                            
                                            break
                                    break 
                                
                        if var1 == False:
                                 
                                print("El producto que ingreso no coincide, intente nuevamente")
                                        
                        if dineroTotalGastado < dineroPersona and dineroTotalGastado != 0:
                            
                            
                            vuelto = dineroPersona - dineroTotalGastado
                       
                            print(f"Ahora el total a abonar es de ${dineroTotalGastado}--- --- Usted dispone de ${dineroPersona}: ")
                            print("")
                            print("Escriba la opcion que desee")
                            print("")
                            print("--[PAGAR]--")
                            print("")
                            print("--[CANCELAR COMPRA]--")
                            
                            opcionario3 = input()
                            
                            if opcionario3 == "pagar":
                            
                                if vuelto >= 0:  
                    
                                    print(f"Su compra se ha realizado con exito, se le reintegraran a la tarjeta la suma de ${vuelto} que no ha llegado a utilizar")
                                
                                else:
                            
                                    print("Su compra se a realizado con excito")
                                
                            elif opcionario3 == "cancelar compra":
                                 
                                break
                            
                        elif dineroTotalGastado == 0: 
                            
                            print("")
                            print("Acaba de remover todos los productos, si desea volver a intentarlo, reinicia el programa")
                            
                    """
                    #Cancelacion de la compra 
                    """
                
                elif opcionario2 == "cancelar compra": 
        
                    break
            
                    """
                    #Reintegro de efectivo
                    """
            
                elif opcionario2 == "reintegrar efectivo":
                    
                    while dineroPersona < dineroTotalGastado:
                        
                        print("Ingrese la cantidad de dinero que desea reintegrar al cajero: ")
                        
                        reintegracion = int(input())
                    
                        dineroPersona = dineroPersona + reintegracion
                        
                        if dineroPersona < dineroTotalGastado:
                            
                            varAlt = dineroTotalGastado - dineroPersona
                            
                            print(f"Acaba de reintegrar ${reintegracion}")
                            print(f"Ahora dispone de ${dineroPersona}")
                            print(f"Falta la cantidad de ${varAlt}")
                            
                    vuelto = dineroPersona - dineroTotalGastado
                    
                    print(f"El total a abonar es de ${dineroTotalGastado}--- --- Ahora dispone de ${dineroPersona}: ")
                    print("")
                    print("Escriba la opcion que desee")
                    print("")
                    print("--[PAGAR]--")
                    print("")
                    print("--[CANCELAR COMPRA]--")
                    
                    opcionario4 = input()
                            
                    if opcionario4 == "pagar":
                        
                        if vuelto > 0:  
                    
                            print(f"Su compra se ha realizado con exito, se le reintegraran a la tarjeta la suma de ${vuelto} que no ha llegado a utilizar")
                            
                        else:
                            
                            print("Su compra se a realizado con excito")
                            
                    elif opcionario4 == "cancelar compra":
                                
                        break
                    
            """
            Asignacion de variables principales dentro de la compra
            """
            
            ultimaCompraProductos = alimentosSeleccionCompra
            
            ultimaCompraGasto = dineroTotalGastado
            
            ultimaTarjetaUtilizada = numeroTarjeta
           
            
                       
           
        """ 
        Salir del programa
        """        
     
    elif eleccionPrincipal == "salir":
        
        print("Saliendo del programa...") 
          
        break
      
        
      
        """
        Eleccion principal erronea
        """
      
    else:
        
        x = random.randint(1,2)
        
        if x == 1:
            print("Seleccione una opcion correcta")
            print("")
            
        else:
            print("Vuelva a elegir una opcion")
            print("")
            
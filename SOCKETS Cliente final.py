import socket
import sys
import ast
#-------------------------------------------------------------
def menuC():
    print("Para realizar una venta digite: compras\n")
    print("Para realizar una devolucion digite: devolucion\n")
    print("Para concluir una compra digite: facturacion\n")
    print("Para ver el precio de un articulo digite: consultar_precio\n")
    print("Para consultar ultimo descuento de un cliente digite: ultimo_descuento\n")
    print("Para salir digite: salir\n")
    c=input("Digite que funcion quiere realizar:")
    while c!="salir" and c!="Salir":
        if c=="Compras" or c=="compras":
            break
        if c=="consultar_precio" or c== "Consultar_precio" :
            break
        if c=="ultimo_descuento" or c=="Ultimo_descuento":
            break
        if c=="compra" or "Compra":
            break
        print("Para realizar una venta digite: compras\n")
        print("Para realizar una devolucion digite: devolucion\n")
        print("Para concluir una compra digite: facturacion\n")
        print("Para ver el precio de un articulo digite: consultar_precio\n")
        print("Para consultar ultimo descuento de un cliente digite: ultimo_descuento\n")
        print("Para salir digite: salir\n")
        c=input("Digite que funcion quiere realizar:")
    return c
#--------------------------------------------------------------
def verinveC(lista):
    for i in lista:
        cont=0
        for j in i:
            if cont==0:
                codsup="En el supermercado:",j
                print("\n")
                print(codsup)
                cont+=1
                
            elif cont==1:
                codprod="Producto:",j
                print(codprod)
                cont+=1
                
            elif cont==2:
                canti="Hay disponibles:",j
                print(canti)
                cont+=1
                
            elif cont==3:
                preci="A un precio unitario de:",j
                print(preci)
                print("\n")
                cont+=1
#--------------------------------------------------------------
def paslis(string):
    string=ast.literal_eval(string)
    return string
#--------------------------------------------------------------
def main():
    try:
        #Crear un socket
        mi_socket_cliente = socket.socket()
        #conectar con el servidor
        mi_socket_cliente.connect(("localhost",6969))
        #establecer maximo de datos enviados
        bufsize = 1000
        cedula=input("Digite su cedula:")
        cedula2=cedula
        vali=False
        while vali!=True:
            try:
                int()
                vali=True
            except:
                print("La cedula digitada no corresponde a un numero")
                cedula=input("Digite su cedula:")
          
        datos_a_enviar = bytes((cedula),"utf-8")
        mi_socket_cliente.send(datos_a_enviar)
        datos_recibidos = mi_socket_cliente.recv(bufsize)
        datos_recibidos = datos_recibidos.decode("utf-8")
        print(datos_recibidos)
#------------------------------------------------------------
        if datos_recibidos=="0":
            print("Este es un funcionario, no es cliente")
            return
#----------------------------------------------------------
        if datos_recibidos=="1":
            cedula_enviar= bytes((cedula),"utf-8")
            mi_socket_cliente.send(datos_a_enviar)
            nombre = mi_socket_cliente.recv(bufsize)
            nombre = nombre.decode("utf-8")
            print("Hola",nombre)
            momo=True
            #-------------------------------------------------------------------
            while momo==True:
                mensaje=menuC()
                if mensaje=="salir":
                    momo=False
                #-----------------------------------------------------------
                datos_a_enviar = bytes((mensaje),"utf-8")
                mi_socket_cliente.send(datos_a_enviar)
                #-----------------------------------------------------------
                if mensaje=="compras" or mensaje=="Compras":
                    codsup= input("Introduzca el código de supermercado donde se realizará la compra: ")
                    #3
                    datos_a_enviar = bytes(codsup,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    #4 espera el invetario que llega
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    inventario= datos_recibidos.decode("utf-8")
                    while inventario=="[]":
                        print("El supermercado digitado no existe, digite otro")
                        codsup= input("Introduzca el código de supermercado donde se realizará la compra: ")
                        datos_a_enviar = bytes(codsup,"utf-8")
                        mi_socket_cliente.send(datos_a_enviar)
                        datos_recibidos = mi_socket_cliente.recv(bufsize)
                        inventario= datos_recibidos.decode("utf-8")
                        
                    inventario=paslis(inventario)
                    print(verinveC(inventario))
                    codprodu= input("Digite el código del producto a comprar:")
                    #5  envia el cod de producto
                    datos_a_enviar = bytes(codprodu,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    #6 recibe confirmacion de que el producto esta en el super
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    confirmacion= datos_recibidos.decode("utf-8")
                    #print(confirmacion)
                    if confirmacion=="productono":
                        print("El producto no es valido")
                    else:
                        #7 envia la cantidad de producto
                        canti= input("Digite la cantidad que desea comprar:")
                        datos_a_enviar = bytes(canti,"utf-8")
                        mi_socket_cliente.send(datos_a_enviar)
                        #8 espera confirmacion de si hay cantidad especificada
                        datos_recibidos = mi_socket_cliente.recv(bufsize)
                        confirmacion= datos_recibidos.decode("utf-8")
                        if confirmacion=="no":
                            print("La cantidad ingresada no es valida")
                        else:
                            otro= input("Desea agregar otro producto?:")
                            #envia si quiere otro producto o no
                            #9
                            datos_a_enviar = bytes(otro,"utf-8")
                            mi_socket_cliente.send(datos_a_enviar)
                            
                            while otro!= "No" or otro!="no":
                                if otro=="Si" or otro=="si":
                                    #10 envia de nuevo el codigo de producto
                                    q2=input("Digite el código del producto a vender:")
                                    datos_a_enviar = bytes(q2,"utf-8")
                                    mi_socket_cliente.send(datos_a_enviar)
                                    #11 recibe confirmacion de que exista el cod produ
                                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                                    confirmacion= datos_recibidos.decode("utf-8")
                                    #print("confirmacion", confirmacion)
                                    if confirmacion=="El codigo no es un producto valido":
                                        #print(confirmacion)
                                        otro=input("Desea añadir otro producto?:")
                                    else:
                                        print("Si de nuevo")
                                        canti2= input("Digite la cantidad a comprar:")
                                        #12
                                        datos_a_enviar = bytes(canti2,"utf-8")
                                        mi_socket_cliente.send(datos_a_enviar)
                                        #13
                                        datos_recibidos = mi_socket_cliente.recv(bufsize)
                                        confirmacion3= datos_recibidos.decode("utf-8")
                                        #print("confirmacion3",confirmacion3)
                                        #-----------------------------------------------------
                                        if confirmacion3=="no":
                                            print("La cantidad no es valida")
                                            otro= input("Desea agregar otro producto?:")
                                        #-----------------------------------------------------    
                                        else:
                                            otro=input("Desea agregar otro producto?:")
                                            #14
                                            datos_a_enviar = bytes(otro,"utf-8")
                                            mi_socket_cliente.send(datos_a_enviar)
                                            #---------------------------------------
                                if otro=="no" or otro=="No":
                                    break
                                #------------------------------------------------------
                #15
                datos_recibidos = mi_socket_cliente.recv(bufsize)
                orden= datos_recibidos.decode("utf-8")
                print(orden)
                print("Descuento, Precio")
                opcion=input("Desea facturar?:")
                #16
                datos_a_enviar = bytes(opcion,"utf-8")
                mi_socket_cliente.send(datos_a_enviar)
                #--------------------------------------
                if mensaje=="consultar_precio":
                    codproducto=input("Ingrese el código de producto que desea consultar:")
                    datos_a_enviar = bytes(codproducto,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    codsuper=input("Ingrese el código de super que desea consultar:")
                    datos_a_enviar = bytes(codsuper,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    print("\n")
                    print(datos_recibidos.decode("utf-8"))
                    print("\n")
                #------------------------------------------
                if mensaje=="ultimo_descuento":
                    datos_a_enviar = bytes(cedula,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    print("\n")
                    print( datos_recibidos.decode("utf-8"))
                    print("\n")
                #------------------------------------------
                if mensaje=="facturacion":
                    datos_a_enviar = bytes(cedula,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    print("\n")
                    print( datos_recibidos.decode("utf-8"))
                    print("\n")
                #------------------------------------------
                if mensaje=="devolucion":
                    datos_a_enviar = bytes(cedula,"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    datos_recibidos = mi_socket_cliente.recv(bufsize)
                    print("\n")
                    print( datos_recibidos.decode("utf-8"))
                    print("\n")     
#-------------------------------------------------------
        if datos_recibidos=="2":
            print("Su cedula no esta registrada")
            c=input("Desea registrarse:")
            while c!="No" and c!="no":
                if c=="si" or c=="Si":
                    datosC=[]
                    print("Digite sus datos para registralo")
                    codciu=input("Digite su codigo de ciudad:")
                    datosC+=[codciu]
                    datosC+=[cedula]
                    nombre=input("Digite su nombre (sin tildes):")
                    datosC+=[nombre]
                    telef=input("Digite su telefono:")
                    datosC+=[telef]
                    datosC+=[0]
                    datosC=str(datosC)
                    print(datosC)
                    c="No"
                    datos_a_enviar = bytes((datosC),"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    print("Se han enviado sus datos para registrarlo")
                    regis= mi_socket_cliente.recv(bufsize)
                    regis = regis.decode("utf-8")
                    print(regis)
                    cedula_enviar= bytes((cedula2),"utf-8")
                    mi_socket_cliente.send(datos_a_enviar)
                    nombre = mi_socket_cliente.recv(bufsize)
                    nombre = nombre.decode("utf-8")
                    print("\n")
                    print("Hola",nombre)
                    print("\n")
                    momo=True
                    #-------------------------------------------------------------------
                    while momo==True:
                        mensaje=menuC()
                        if mensaje=="salir":
                            momo=False
                        #-----------------------------------------------------------
                        datos_a_enviar = bytes((mensaje),"utf-8")
                        print(datos_a_enviar)
                        mi_socket_cliente.send(datos_a_enviar)
                        #-----------------------------------------------------------
                        

#------------------------------------------------------------------------                   
                else:
                    print("Digite Si para registrarse o No para salir")
                    c=input("Desea registrase:")
            print("Adios")
            return
           
    except:
        print("El servidor no esta conectado")
        print("Intentando reconectar")
        main()
    
##    #Escoger que datos enviar
##    datos_a_enviar = bytes((input("Que hacer:")),"utf-8")
##    #enviar los datos
##    mi_socket_cliente.send(datos_a_enviar)
##    #recibir los datos
##    datos_recibidos = mi_socket_cliente.recv(bufsize)
##    #imprimir los datos recibidos
##    print (datos_recibidos)

main()
#---------------------------------------------------


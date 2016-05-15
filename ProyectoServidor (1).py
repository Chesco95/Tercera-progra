#proyecto final 1.6
#Elias Solano Gamboa
Ciudades="Ciudades.txt"
Usuarios="Usuarios.txt"
Supermercado="Supermercado.txt"
Inventario="Inventario.txt"
#--------------------------------------------
import socketserver
import ast
import threading
#permite al usuario leer los archivos
def lee(x):
   try:
        f=open(x,"r")
        for linea in f.readlines():
            print(linea)
        f.close()
   except:
        print ("Error, en el archivo",x)
#--------------------------------------------
#mete los archivos en listas
def archlista(x):
    lista=[]
    elemento=""
    f=open(x,"r+")
    line="f)"
    while line!="":
        line=f.readline(1)
        if line!="," and  line!="\n":
            a=line
            elemento+=a
        if line=="," or line=="\n":
            if elemento!="":
                lista+=[elemento]
                elemento=""
            else:
                lista=lista
    if elemento!="":
       lista+=[elemento]
       elemento=""
   
    f.close()            
    return(lista)
    print(lista)
#----------------------------------------------
#quita los datos repetidos de la lista Ciudades
def Ciudadeslist():
   lista=archlista(Ciudades)
   i=0
   largo=len(lista)-1
   while i<=largo:
      num=lista[i]
      cont=i+2
      while cont<largo:
         num1=lista[cont]
         if num==num1:
            del lista[cont]
            del lista[cont]
            largo=len(lista)-1
         else:
            cont+=2
      i+=2
      largo=len(lista)-1
   return(lista)
#----------------------------------------------
#quita usuarios con un codigo de ciudad que no este en ciudadeslist y quita
#los funcionarios con codigos diferentes de 0, 1 o 2
def usuarioslist():
   lista=archlista(Usuarios)
   ciudades=Ciudadeslist()
   cont=0
   i=0
   limiteu=len(lista)-1
   limitec=len(ciudades)-1
   while cont<limiteu:
      i=0
      valido="false"
      codiu=lista[cont]
      while i<limitec:
         codic=ciudades[i]
         if codic==codiu:
            valido="true"
            i=limitec+1
            cont+=5
         else:
            i+=2
      if valido=="false":
         del lista[cont]
         del lista[cont]
         del lista[cont]
         del lista[cont]
         del lista[cont]
         i=limitec+1
      limiteu=len(lista)-1

   #print(lista)   
   cont=4
   while cont<=limiteu:
      b=lista[cont]
      b=int(b)
      #print(b)
      if b!=0 and b!=1 and b!=2:
         #print("borrado",lista[cont])
         del lista[cont]
         #print("borrado",lista[cont-1])
         del lista[cont-1]
         #print("borrado",lista[cont-2])
         del lista[cont-2]
         #print("borrado",lista[cont-3])
         del lista[cont-3]
         #print("borrado",lista[cont-4])
         del lista[cont-4]
      else:
         cont+=5
      limiteu=len(lista)-1
   return(lista)
#---------------------------------------------
#Lista de usuarios revisa que no hayan cedulas repetidas y si las hay, borra
#todas menos la primera
def usuarioslist2():
   lista=usuarioslist()
   ced=1
   ced2=6
   nombre=2
   nombre2=7
   largo=len(lista)-1
   while ced<largo and nombre<largo:
      cedu1=lista[ced]
      name=lista[nombre]
      while ced2 < largo and nombre2 < largo:
         cedu2=lista[ced2]
         name2=lista[nombre2]
         
         if cedu1==cedu2 and name!=name2:
            ced2-=1
            del lista[ced2]
            del lista[ced2]
            del lista[ced2]
            del lista[ced2]
            del lista[ced2]
            ced2+=1
            largo=len(lista)-1
            
         if cedu1==cedu2 and name==name2:
            codciu=lista[ced-1]
            codciu2=lista[ced2-1]
            if codciu==codciu2:
               ced2+=5
               nombre2+=5
            else:
               ced2-=1
               del lista[ced2]
               del lista[ced2]
               del lista[ced2]
               del lista[ced2]
               del lista[ced2]
               ced2+=1
               largo=len(lista)-1
         else:
            ced2+=5
            nombre2+=5
            
      ced+=5
      ced2=ced+5
      nombre+=5
      nombre2=nombre+5
   return(lista)   
#--------------------------------------------
#lista de usuarios,se revisa si un mismo funcionario tiene un 1 y un 0 se cambia por un 2
def usuarioslist3():
   lista=usuarioslist2()
   contced=1
   contced2=6
   contfun=4
   contfun2=9
   largo=len(lista)-1
   while contced<=largo and contfun<=largo:
      ced=lista[contced]
      codfun=lista[contfun]
      while contced2<=largo and contfun2<=largo :
         cod=lista[contced2]
         cfn=lista[contfun2]
         if ced==cod and codfun!=cfn:
            lista[contfun]="2"
            contced2-=1
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            contced2+=1
         if ced==cod and codfun==cfn:
            contced2-=1
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            del lista[contced2]
            contced2+=1
         else:
            contced2+=5
            contfun2+=5
         largo=len(lista)-1
         #print("aqui",ced,cod,cfn,codfun)
      contced+=5
      contfun+=5
      contced2=contced+5
      contfun2=contfun+5
      #print("contced:",contced,contfun,largo)
      #print(lista)
   return(lista)
#----------------------------------------------
#verifica cod de ciudad de los supermercados
def superlist():
   lista=archlista(Supermercado)
   lisciudades=Ciudadeslist()
   cont=0
   cont2=0
   limitesu=len(lista)-1
   limitec=len(lisciudades)-1
   verify="false"
   while cont < limitesu:
      cod1=lista[cont]
      while cont2 < limitec:
         cod2=lisciudades[cont2]
         if cod1 == cod2:
            cont2=limitec+1
            verify="true"
            cont+=2
         else:
            cont2+=2
      if verify=="false":
         del lista[cont]
         del lista[cont]
         limitesu=len(lista)-1
      cont2=0
      verify="false"
   return(lista)
#----------------------------------------------
#Verifica que no hayan codigos de supermercado repetidos
def superlist2():
   lista=superlist()
   cont=1
   cont2=3
   largo=len(lista)-1
   while cont<=largo:
      codi1=lista[cont]
      while cont2<= largo:
         codi2=lista[cont2]
         
         if codi1==codi2:
            cont2-=1
            del lista[cont2]
            del lista[cont2]
            cont2+=1
         else:
            cont2+=2
         largo=len(lista)-1
      cont+=2
      cont2=cont+2
   return(lista)
#----------------------------------------------
#crea una lista de listas para el inventario
def archlistainve():
    lista1=[]
    lista2=[]
    elemento=""
    f=open(Inventario,"r+")
    line="f)"
    while line!="":
        line=f.readline(1)
        if line!="," and  line!="\n":
            a=line
            elemento+=a
        if line=="," :
           lista1+=[elemento]
           elemento=""
        if line=="\n":
           if elemento!="":
              lista1+=[elemento]
              lista2+=[lista1]
              lista1=[]
              elemento=""
           else:
              lista2=lista2
              elemento=""
        else:
           lista1=lista1
    if elemento!="":
       lista1+=[elemento]
       lista2+=[lista1]
       lista1=[]
       elemento=""
    f.close()            
    return(lista2)
#-----------------------------------------------
#verifica codigo de supermercado
def archlistainve2():
   lista=archlistainve()
   supe=superlist()
   contli=0
   contsu=1
   largo1=len(lista)
   largo2=len(supe)
   verify="false"
   while contli < largo1:
      cod1=lista[contli][0]
      while contsu < largo2:
         cod2=supe[contsu]
         if cod1==cod2:
            verify="true"
            contsu=largo2+1
            contli+=1
         else:
            contsu+=2
      if verify=="false":
         del lista[contli]
      contsu=1
      largo1=len(lista)
      verify="false"
   return(lista)
#----------------------------------------------
#elimina los codigos de producto repetidos en el mismo supermercado
def archlistainve3():
   lista=archlistainve2()
   contli=0
   contli2=1
   contsp=0
   largo=len(lista)-1
   verify="false"
   while contli < largo:
      codsu1=lista[contli][contsp]
      while contli2 < largo:
         codsu2=lista[contli2][contsp]
         
         if codsu1 == codsu2:
            contsp+=1
            cop1=lista[contli][contsp]
            cop2=lista[contli2][contsp]
            
            if cop1 ==cop2:
               del lista[contli2]
               contsp=0
               verify="true"
               largo=len(lista)-1
               
            else:
               contsp=0
               contli2+=1

         else:
            contli2+=1
      if verify=="true":
         contli+=1
         
      if verify=="false":
         contli+=1
         contli2=contli+1
   return(lista)
#----------------------------------------------
#Funcion para consultar precio de un articulo
def precio(x,y):
   x=str(x)
   y=str(y)
   lista=archlistainve3()
   cont=0
   cont2=1
   cont3=3
   largo=len(lista)-1
   verify="false"
   while cont <= largo:
      arti=lista[cont][cont2]
      if x==arti:
         precio=lista[cont][cont3]
         supe=lista[cont][0]
         if supe==y:
            print("El precio del articulo es:",precio)
            return(precio)
            verify="true"
            cont=largo+1
         else:
            cont+=1
      else:
         cont+=1
   if verify=="false":
      return("No se encontro el articulo en el supermercado deseado")
#----------------------------------------------
#Funcion para guardar los cambios en el inventario
def guardainve(x):
   lista=x
   largo=len(lista)-1
   cont1=0
   cont2=0
   f=open(Inventario,"w")
   while cont1 <= largo:
      f.write(lista[cont1][cont2])
      f.write(",")
      f.write(lista[cont1][cont2+1])
      f.write(",")
      f.write(lista[cont1][cont2+2])
      f.write(",")
      f.write(lista[cont1][cont2+3])
      f.write("\n")
      cont1+=1
   f.close()
#--------------------------------------------------
#Funcion para guardar los cambios en el archivo de usuarios
def guardausuari(x):
   f=open(Usuarios,"w")
   cont=0
   largo=len(x)-1
   while cont < largo:
      f.write(x[cont])
      f.write(",")
      f.write(x[cont+1])
      f.write(",")
      f.write(x[cont+2])
      f.write(",")
      f.write(x[cont+3])
      f.write(",")
      f.write(x[cont+4])
      f.write("\n")
      cont+=5
   f.close()
   print("Se han realizado los cambios")
   return
#----------------------------------------------
#Funcion para borrar un cliente 
def elimiC(x):
   cedula=int(x)
   c=usuarioslist3()
   cont=1
   largo=len(c)-1
   userfound="nop"
   while cont < largo:
      ced=c[cont]
      ced=int(ced)
      if ced==cedula:
         userfound="sip"
         break
      else:
         cont+=5
   if userfound=="sip":
      del c[cont-1]
      del c[cont-1]
      del c[cont-1]
      del c[cont-1]
      del c[cont-1]
      return (guardausuari(c))
   if userfound=="nop":
      return("Cliente que desea borrar no esta registrado")
#----------------------------------------------
#Funcion para borrar un articulo
def delprod(x):
   x=str(x)
   lista=archlistainve3()
   cont=0
   cont2=1
   largo=len(lista)-1
   verify="false"
   while cont <= largo:
      codprod=lista[cont][cont2]
      if x==codprod:
         del lista[cont]
         verify="true"
         largo=len(lista)-1
         print("Se elimino el articulo",x,"con exito")
         guardainve(lista)
      else:
         cont+=1
   if verify=="false":
      print("No se encontro el producto:",x)
#----------------------------------------------
def agrega(x):
   x=str(x)
   lista=archlistainve3()
   cont=0
   cont2=1
   largo=len(lista)-1
   newar=[]
   verify="false"
   while cont <= largo:
      codprod=lista[cont][cont2]
      if x==codprod:
         print("El articulo",x,"ya existe")
         verify="true"
         cont=largo+1
      else:
         cont+=1
   if verify=="false":
      print("Digite la informacion para el nuevo producto")
      codsup=input("Digite el codigo del supermercado para el nuevo producto:")
      newar+=[codsup]
      codproduc=x
      newar+=[x]
      cantidad=input("Digite la cantidad del producto:")
      newar+=[cantidad]
      prec=input("Digite el precio del producto:")
      newar+=[prec]
      lista+=[newar]
      guardainve(lista)
      print("El nuevo articulo se guardo con exito")
   #print(lista)
   
#----------------------------------------------
#funcion para ver cedula y ver si un cliente esta registrado
def vcedu(cedula):
   c=usuarioslist3()
   cont=1
   largo=len(c)-1
   userfound="nop"
   while cont < largo:
      ced=c[cont]
      ced=int(ced)
      if ced==cedula:
         userfound="sip"
         cont=largo+1
      else:
         cont+=5
   if userfound=="sip":
      return("Cliente Registrado")
   if userfound=="nop":
      return("Cliente no Registrado")
#---------------------------------------------
#funcion para ver el inventario
def leerinve(codsuper):
   codsuper=str(codsuper)
   lista=archlistainve3()
   listainve=[]
   for i in (lista):
      codsu=i[0]
      if codsuper==codsu:
         listainve+=[i]
   if listainve==[]:
      print("El supermercado no existe")
      return []
   return listainve
#---------------------------------------------
#funcion para mostrar el inventario (Cliente)
def verinveC(lista):
   ver=[]
   for i in lista:
      cont=0
      for j in i:
         if cont==0:
            codsup=("En el supermercado:",j)
            ver+=[codsup]
            cont+=1
            
         elif cont==1:
            codprod=("Producto:",j)
            ver+=[codprod]
            cont+=1
            
         elif cont==2:
            canti=("Hay disponibles:",j)
            ver+=[canti]
            cont+=1
            
         elif cont==3:
            preci=("A un precio unitario de:",j)
            ver+=[preci]
            cont+=1
   return(ver)
   print(ver)
#---------------------------------------------
#funcion para mostrar el inventario
def verinve(lista):
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
#-------------------------------------------------
#Funcion para saber los datos del usuario
def Cdatos(cedula):
   cedula=int(cedula)
   usuario=usuarioslist3()
   cont=1
   datos=[]
   largo=len(usuario)-1
   while cont<=largo:
      cedu=usuario[cont]
      cedu=int(cedu)
      if cedula==cedu:
         codciu=usuario[cont-1]
         datos+=[codciu]
         nombre=usuario[cont+1]
         datos+=[nombre]
         telef=usuario[cont+2]
         datos+=[telef]
         return(datos)
      else:
         cont+=5
   print("No se encontro usuario")
   
#---------------------------------------------------------
#Funcion para hacer los cambios en el inventario
def cambinve(codsup,codprod,canti):
   print(codprod)
   lista=archlistainve3()
   codsup=str(codsup)
   contin=0
   cont=0
   for csuper in lista:
      codsuper=csuper[contin]
      print(codsuper,codsup)
      if codsup==codsuper:
         produinve=csuper[contin+1]
         produinve=int(produinve)
         codp=codprod[cont]
         print("aqui",produinve,codp)
         if produinve==codp:
            cantic=canti[cont]
            print(cantic)
            cantic=int(cantic)
            caninve=csuper[contin+2]
            caninve=int(caninve)
            nuevoin=caninve-cantic
            nuevoin=str(nuevoin)
            csuper[contin+2]=nuevoin
            if  1 <len(codprod):
               cont+=1
   print(lista)
   guardainve(lista)
   return      
   
#---------------------------------------------------------
#Funcion para ver si un producto esta en un supermercado
def producto(codsup,codprod):
   codprod=str(codprod)
   lista=leerinve(codsup)
   for i in lista:
      produ=i[1]
      if codprod==produ:
         return True
   return False
#---------------------------------------------
#Funcion para ver si la cantidad disponible de un producto es menor a la cantidad que se pide
def cantidad(codsup,codprod,canti):
   codprod=str(codprod)
   lista=leerinve(codsup)
   cont=1
   for i in lista:
      produ=i[cont]
      if codprod==produ:
         eninve=i[cont+1]
         eninve=int(eninve)
         if canti > eninve:
            print("No hay suficiente producto para vender")
            return False
         else:
            return eninve
#---------------------------------------------
#funcion de compras
def compras(codsup,produli,cantili,clienC):
   lista=leerinve(codsup)
   cont=0
   total=0
   for produ in produli:
      preci=precio(produ,codsup)
      preci=int(preci)
      canti=cantili[cont]
      canti=int(canti)
      total+=preci*canti
      cont+=1
   descu=descuento(total)
   historial(clienC,codsup,produli,cantili,descu)
   ceduC=clienC
   ceduC=str(ceduC)
   archname=ceduC+"historial.txt"
   histori=archisto(archname)
   histori[2]=ast.literal_eval(histori[2])
   codprod=histori[2]
   histori[3]=ast.literal_eval(histori[3])
   canti=histori[3]
   cambinve(codsup,codprod,canti)
   return(descu)
#---------------------------------------------
#Funcion de ventas para los cliente nuevos
def comprasnoregi(codsup,produli,cantili,clienC):
   lista=leerinve(codsup)
   cont=0
   total=0
   for produ in produli:
      preci=precio(produ,codsup)
      preci=int(preci)
      canti=cantili[cont]
      canti=int(canti)
      total+=preci*canti
      cont+=1
   descu=descunore(total)
   historial(clienC,codsup,produli,cantili,descu)
   ceduC=clienC
   ceduC=str(ceduC)
   archname=ceduC+"historial.txt"
   histori=archisto(archname)
   histori[2]=ast.literal_eval(histori[2])
   codprod=histori[2]
   histori[3]=ast.literal_eval(histori[3])
   canti=histori[3]
   cambinve(codsup,codprod,canti)
   return()
         
#---------------------------------------------
def descunore(total):
   descuento=(total/100)*2
   ganancia=total-descuento
   print("Se vende por:",ganancia)
   return ([descuento,ganancia])
#-----------------------------------------------           
# funcion para aplicar descuentos
def descuento(total):
   if total < 5000:
      ganancia=total
      descuento=0
      print("Se vende por:",ganancia)
      return ([descuento,ganancia])
      
   if 5000 <= total <= 10000:
      descuento=(total/100)*5
      ganancia=total-descuento
      print("Se vende por:",ganancia)
      return ([descuento,ganancia])
      
   if 10000 < total <= 50000:
      descuento=(total/100)*7
      ganancia=total-descuento
      print("Se vende por:",ganancia)
      return ([descuento,ganancia])
      
   if 50000 < total:
      descuento=(total/100)*10
      ganancia=total-descuento
      print("Se vende por:",ganancia)
      return ([descuento,ganancia])
#--------------------------------------------------------------------------
#Funcion para completar una orden de compra
def facturacion(ceduC,codsup):
   ceduC=str(ceduC)
   archname=ceduC+"historial.txt"
   historial=archisto(archname)
   dat=Cdatos(ceduC)
   codciu=dat[0]
   nombre=dat[1]
   telef=dat[2]
   codisup=historial[1]
   historial[2]=ast.literal_eval(historial[2])
   codprod=historial[2]
   canti=historial[3]
   historial[4]=ast.literal_eval(historial[4])
   precio=historial[4][1]
   descuento=historial[4][0]
   print (ceduC,nombre,telef,codciu,codisup,codprod,canti,precio,descuento)
   factura(ceduC,nombre,telef,codciu,codisup,codprod,canti,precio,descuento)
#clienC,codsup,produli,cantili,descu
#------------------------------------------------------------------------------
def facturacion2(ceduC,codsup):
   ceduC=str(ceduC)
   archname=ceduC+"historial.txt"
   historial=archisto(archname)
   dat=Cdatos(ceduC)
   codciu=dat[0]
   nombre=dat[1]
   telef=dat[2]
   codisup=historial[1]
   historial[2]=ast.literal_eval(historial[2])
   codprod=historial[2]
   canti=historial[3]
   #cambinve(codsup,codprod,canti)
   historial[4]=ast.literal_eval(historial[4])
   precio=historial[4][1]
   descuento=historial[4][0]
   print (ceduC,nombre,telef,codciu,codisup,codprod,canti,precio,descuento)
   factura(ceduC,nombre,telef,codciu,codisup,codprod,canti,precio,descuento)
#clienC,codsup,produli,cantili,descu
#--------------------------------------------------------------------------
#Crea una factura
def factura(a,nombre,telef,codciu,codisup,x,canti,precio,ganancia):
   archname=a +".txt"
   f=open(archname,"a")
   f.write("Cedula:")
   f.write(a)
   f.write("\n")
   f.write("Nombre:")
   f.write(nombre)
   f.write("\n")
   f.write("Telefono:")
   f.write(telef)
   f.write("\n")
   f.write("Codigo de ciudad:")
   f.write(codciu)
   f.write("\n")
   f.write("En el supermercado:")
   f.write(codisup)
   f.write("\n")
   cont=0
   for codprod in x:
      f.write("Del producto codigo:")
      codprod=str(codprod)
      f.write(codprod)
      f.write("\n")
      f.write("Una cantidad de:")
      f.write(canti[cont])
      cant=str(canti)
      f.write("\n")
      cont+=1
   f.write("Por un precio:")
   precio=str(precio)
   f.write(precio)
   f.write("\n")
   f.write("Teniendo un descuento de:")
   ganancia=str(ganancia)
   f.write(ganancia)
   f.write("\n")
   f.write("-----------------------")
   f.write("\n")  
#---------------------------------------------
#Funcion para crear una lista con el historial
def archisto(x):
    lista=[]
    elemento=""
    f=open(x,"r+")
    line="f)"
    while line!="":
        line=f.readline(1)
        if line!="-" and  line!="\n":
            a=line
            elemento+=a
        if line=="-" or line=="\n":
            if elemento!="":
                lista+=[elemento]
                elemento=""
            else:
                lista=lista
    if elemento!="":
       lista+=[elemento]
       elemento=""
    f.close()
    print(lista)
    return(lista)
#---------------------------------------------
#Funcion para crear el historial de ventas
def historial(clienC,codsup,produli,cantili,descu):
   clienC=str(clienC)
   codsup=str(codsup)
   produli=str(produli)
   cantili=str(cantili)
   descu=str(descu)
   archname=clienC +"historial.txt"
   f=open(archname,"w")
   f.write(clienC)
   f.write("-")
   f.write(codsup)
   f.write("-")
   f.write(produli)
   f.write("-")
   f.write(cantili)
   f.write("-")
   f.write(descu)
   f.write("\n")
#---------------------------------------------
#Funcion para devoluciones
def devolucion(x,a,canti):
   canti=int(canti)
   x=str(x)
   lista=archlistainve3()
   cont=0
   cont1=1
   largo=len(lista)-1
   verify="false"

   while cont <= largo:
      codp=lista[cont][cont1]
      #print(cont,largo)

      if x==codp:
         canti2=input("Digite la cantidad a devolver:")
         canti2=int(canti2)
         if canti<canti2:
            print("No se puede hacer la devolucion por que la cantidad comprada es menor a la cantidad a devolver")
            return(canti)
         else:
            cantlist=lista[cont][2]
            cantlist=int(cantlist)
            newcant=canti2+cantlist
            canti=canti-canti2
            lista[cont][2]=str(newcant)
            guardainve(lista)
            verify="true"
            cont=largo+1
            print("Se realizo la devolucion con exito")
            return(canti)

      else:
         cont+=1
         
   if verify=="false":
      print("El codigo del producto no coincide con ninguno de la lista")
#---------------------------------------------
#funcion para consultar ultimo descuento
def ultdescuento(cedula):
   descuento="El usuario no ha realizado no ha realizado ninguna compra"
   try:
      lista= archisto(str(cedula) + "historial.txt")
      #print(lista)
      lista[4]=ast.literal_eval(lista[4])
      descuento= lista[4][0]
      
               
   except:
      descuento="El usuario no ha realizado ninguna compra"
   return descuento
      
#----------------------------------------------------------------
#registrar usuario
def register(x):
   x=str(x)
   ciu=input("Digite codigo de ciudad del cliente:")
   nombre=input("Digite nombre del cliente:")
   tele=input("Digite telefono del cliente:")
   f=open(Usuarios,"a")
   f.write("\n")
   f.write(ciu)
   f.write(",")
   f.write(x)
   f.write(",")
   f.write(nombre)
   f.write(",")
   f.write(tele)
   f.write(",")
   f.write("0")
#----------------------------------------------
def register2(x):
   cedu=x[1]
   ciu=x[0]
   nombre=x[2]
   tele=x[3]
   f=open(Usuarios,"a")
   f.write("\n")
   f.write(ciu)
   f.write(",")
   f.write(cedu)
   f.write(",")
   f.write(nombre)
   f.write(",")
   f.write(tele)
   f.write(",")
   f.write("0")
#---------------------------------------------
#verifica los usuarios y los permisos de estos
def verusuario(x):
   try:
      x=int(x)
   except:
      print("La cedula digitada no corresponde a un numero")
      x=input("Digite su cedula:")
      return(verusuario(x))
   c=usuarioslist3()
   a=Ciudadeslist()
   cont=1
   verifi="false"
   permi="no"
   largo=len(c)-1
   while cont<=largo:
      cedu=c[cont]
      cedu=int(cedu)
      if x==cedu:
         tipo=c[cont+3]
         tipo=int(tipo)
         if tipo==1 or tipo==2:
            nombre=c[cont+1]
            cont=largo+1
            print("Buenos dias",nombre)
            verifi="true"
            permi="si"
         if tipo==0:
            print("No se tiene permiso para continuar")
            cont=largo+1
            verifi="true"
      else:
         cont+=5
   if verifi=="false":
      print("Cedula no registrada")
      x=input("Digite su cedula:")
      x=int(x)
      verusuario(x)

   if permi=="no" and verifi=="true":
      x=input("Digite su cedula:")
      x=int(x)
      verusuario(x)
   servidor=0
      
   if permi=="si" and verifi=="true":
      print("Digite Si para ser servidor o Digite no para hacer las funciones offline")
      compro=input("¿Desea usar el modo servidor?:")
      while compro!="No" and compro!="no":
         if compro=="si" or compro=="Si":
            servidor=1
            break
            
            
            
         print("Digite Si para ser servidor o Digite no para hacer las funciones offline")
         compro=input("¿Desea usar el modo servidor?:")
      if servidor==1:
         main()
      else:
         menu2(nombre)
#------------------------------------------------------------
#funcion para comprobar si un cliente esta registrado
def verusuario2(x):
   x=int(x)
   c=usuarioslist3()
   a=Ciudadeslist()
   cont=1
   largo=len(c)-1
   while cont<=largo:
      cedu=c[cont]
      cedu=int(cedu)
      if x==cedu:
         tipo=c[cont+3]
         tipo=int(tipo)
         if tipo==1:
            nombre=c[cont+1]
            #la cedula que digito el cliente es de un funcionario que no es un cliente
            return(0)
     
         if tipo==0 or tipo==2:
            #la cedula que digito el cliente es valida retorna 1 al programa del cliente
            return(1)
      else:
         cont+=5
   return(2)
#--------------------------------------------------------------------
#funcion para el nombre asdasdadada
def nombreC(cedula):
   cedula=int(cedula)
   c=usuarioslist3()
   a=Ciudadeslist()
   cont=1
   largo=len(c)-1
   while cont<=largo:
      cedu=c[cont]
      cedu=int(cedu)
      if cedula==cedu:
         nombre=c[cont+1]
         print(nombre)
         return(nombre)
      else:
         cont+=5


#------------------------------------------------------------
#funcion para el menu (aqui se llama a todo lo demas)
class MiTcpHandler(socketserver.BaseRequestHandler):
   def handle(self):
      print("Estamos en handle")
      

      print ("Esperando que cliente inicie...")
      cedulaC = self.request.recv(1000)
      cedulaC= cedulaC.decode("utf-8")
      mensaje=str(verusuario2(cedulaC))
      enviar = bytes(mensaje,"utf-8")
      self.request.send(enviar)

      if mensaje=="2":
         # recibe los datos del cliente en una lista desde el programa del cliente
         DatosC = self.request.recv(1000)
         print(DatosC)
         DatosC = DatosC.decode("utf-8")
         DatosC=ast.literal_eval(DatosC)
         register2(DatosC)
         mensaje="Se a registrado con exito al cliente"
         enviar = bytes(mensaje,"utf-8")
         self.request.send(enviar)
         #--------------------------------------
         cedulaC = self.request.recv(1000)
         cedulaC = cedulaC.decode("utf-8")
         print(cedulaC)
         cedulaC = ast.literal_eval(cedulaC)
         mensaje = cedulaC[2]
         enviar = bytes(mensaje,"utf-8")
         self.request.send(enviar)         

      if mensaje=="1":
         cedulaC = self.request.recv(1000)
         cedulaC = cedulaC.decode("utf-8")
         print(cedulaC)
         cedulaC = int(cedulaC)
         mensaje = nombreC(cedulaC)
         enviar = bytes(mensaje,"utf-8")
         self.request.send(enviar)     
         
      if mensaje=="0":
         print("Se recibio la cedula de un funcionario que no era cliente")
         return
         
      print ("Esperando que cliente de una funcion...")
      mensajes = self.request.recv(1000)
      mensajes = mensajes.decode("utf-8")
      while mensajes != "salir" or mensajes!="Salir":
         
         if mensajes=="xxx":
            #poner funcion aqui
            mensajes="No hay funcion"
            enviar = bytes(mensajes,"utf-8")
            self.request.send(enviar)
            #---------------------------------------------------------------------------
         if mensajes=="Compras"or mensajes=="compras":
            #3
            codsup=self.request.recv(1000)
            codsup=codsup.decode("utf-8")
            #print("llego",codsup)
            inventario=leerinve(codsup)
            #4
            enviar= bytes(str(inventario),"utf-8")
            self.request.send(enviar)
            while inventario==[]:   
               codsup=self.request.recv(1000)
               codsup=codsup.decode("utf-8")
               inventario=leerinve(codsup)
               enviar= bytes(str(inventario),"utf-8")
               self.request.send(enviar)
               print("Se ha solicitado un supermercado que no existe")
         
            #5 recibe el codigo de producto
            codprodu= self.request.recv(1000)
            codprodu= codprodu.decode("utf-8")
            #print("cod produ recibido",codprodu)
            q=int(codprodu)
            if producto(codsup,q)==False:
               print("El producto no es valido")
               c=input("Indique funcion a realizar:")
               #6
               enviar= bytes("productono","utf-8")
               self.request.send(enviar)
            else:
               #6
               enviar= bytes("si","utf-8")
               self.request.send(enviar)
               produli=[]
               cantili=[]
               produli+=[q]
               #7 recibe la cantidad
               canti= self.request.recv(1000)
               canti= canti.decode("utf-8")
               #canti=input("Digite la cantidad a vender:")
               canti=int(canti)
               if cantidad(codsup,q,canti)==False:
                  print("La cantidad no es valida")
                  c=input("Indique funcion a realizar:")
                  #8 envia confirmacion de la cantidad de producto, no
                  confirmacion="no"
                  enviar= bytes(confirmacion,"utf-8")
                  self.request.send(enviar)
               else:
                  #8 envia confirmacion de la cantidad de producto si
                  confirmacion="si"
                  enviar= bytes(confirmacion,"utf-8")
                  self.request.send(enviar)

                  cantili+=[canti]
                  #  9 recibe si quiere otro producto o no
                  #otro=input("¿Quiere agregar otro producto?:")
                  otro= self.request.recv(1000)
                  otro= otro.decode("utf-8")

                  while otro!="No" or otro!="no":
                     if otro=="Si"or otro=="si":
                        #10 recibe de nuevo el codio de producto
                        #q2=input("Digite el codigo del producto a vender:")
                        q2= self.request.recv(1000)
                        q2= q2.decode("utf-8")
                        q2=int(q2)
                        
                        if producto(codsup,q2)==False:
                           print("El codigo no es un producto valido")
                           otro=input("¿Quiere agregar otro producto?")
                           #11
                           confirmacion= "El codigo no es un producto valido"
                           enviar= bytes(confirmacion,"utf-8")
                           self.request.send(enviar)
                           
                        else:
                           #11
                           confirmacion= "si"
                           enviar= bytes(confirmacion,"utf-8")
                           self.request.send(enviar)
                           #12
                           canti2= self.request.recv(1000)
                           canti2= canti2.decode("utf-8")
                           print("canti2",2)
                           
                           
                           #canti2=input("Digite la cantidad a vender:")
                           canti2=int(canti2)
                           
                           if cantidad(codsup,q2,canti2)==False:
                              #13
                              confirmacion3="no"
                              enviar= bytes(confirmacion,"utf-8")
                              self.request.send(enviar)
##                                    print("La cantidad no es valida")
##                                    otro=input("¿Quiere agregar otro producto?:")
                           else:
                              #13
                              confirmacion3= "si"
                              enviar= bytes(confirmacion,"utf-8")
                              self.request.send(enviar)
                              produli+=[q2]
                              cantili+=[canti2]
                              #14
                              #otro=input("¿Quiere agregar otro producto?:")
                              otro= self.request.recv(1000)
                              otro= otro.decode("utf-8")
                              
                     if otro=="no" or "No":
                        break

                  print("Aqui")
                  #15
                  orden= compras(codsup,produli,cantili,a)
                  enviar= bytes(str(orden),"utf-8")
                  
                  self.request.send(enviar)
                  #espera confirmacion de si desea facturar
                  #16
                  opcion= self.request.recv(1000)
                  opcion= opcion.decode("utf-8")
                  if opcion=="si" or opcion=="Si":
                     fac= facturacion2(cedulaC,codsup)
                        
                        
                     
                        
         #----------------------------------------------------------------------------------------------------------------------------------
         if mensajes=="Compras2"or mensajes=="compras2":
            #El horror continua
            print("dsds")
            #----------------------------------------------------------------------
         if mensajes=="salir":
            break
            #---------------------------------------------------------------------
         if mensajes=="consultar_precio" or mensajes=="Consultar_precio":
            print("Estamos dentro de la opcion de consultar precio")
            #recibe el codu de producto
            cod_produ = self.request.recv(1000)
            #decodifica el codigo de producto
            deco_cod_produ= cod_produ.decode("utf-8")
            #Recibe el codigo de super
            cod_super = self.request.recv(1000)
            #Decodifica el codigo de super
            deco_cod_super= cod_super.decode("utf-8")
            #Se mete a la funcion de precio 
            precios=str(precio(deco_cod_produ,deco_cod_super))
            print(precios)
            enviar = bytes(precios,"utf-8")
            self.request.send(enviar)
            #---------------------------------------------------------------------
         if mensajes=="ultimo_descuento"or mensajes=="Ultimo_descuento":
            cedula = self.request.recv(1000)
            cedula= cedula.decode("utf-8")
            descuento= str(ultdescuento(cedula))
            print(descuento)
            enviar = bytes(descuento,"utf-8")
            self.request.send(enviar)
            #---------------------------
         print ("Esperando que cliente de una funcion...")
         mensajes = self.request.recv(1000)
         mensajes = mensajes.decode("utf-8")
#-----------------------------------------------------------
#final del ciclo
      print("cliente salio")
      mensajes=("adios")
      enviar = bytes(mensajes,"utf-8")
      self.request.send(enviar)
      return

##
      # Le enviamos chau al cliente.
##         enviar = bytes("Chau","utf-8")
##         socket_cliente.send(enviar)
##      socket_cliente.close() 
##      server.close()
   
#------------------------------------------------
# menu offline
def menu2(nombre):
   print("Estamos en menu2")
   c=input("Indique funcion a realizar:")
   while c!="salir":

      #El horror
      if c=="ventas":
         a=input("Introduzca cedula del cliente:")
         a=int(a)
         b=vcedu(a)
         print(b)

         if b=="Cliente Registrado":
            codsup=input("Introduzca el codigo del supermercado:")
            inventario=leerinve(codsup)
            if inventario==[]:
               print("El supermercado digitado no existe")
               print("Compra cancelada")
               c=input("Indique funcion a realizar:")
            else:
               verinve(inventario)
               q=input("Digite el codigo del producto a vender:")
               q=int(q)
               if producto(codsup,q)==False:
                  print("El producto no es valido")
                  c=input("Indique funcion a realizar:")
               else:    
                  produli=[]
                  cantili=[]
                  produli+=[q]
                  canti=input("Digite la cantidad a vender:")
                  canti=int(canti)
                  if cantidad(codsup,q,canti)==False:
                     print("La cantidad no es valida")
                     c=input("Indique funcion a realizar:")
                  else:
                     cantili+=[canti]
                     otro=input("¿Quiere agregar otro producto?:")
                     while otro!="No" or otro!="no":
                        if otro=="Si"or otro=="si":
                           q2=input("Digite el codigo del producto a vender:")
                           q2=int(q2)
                           
                           if producto(codsup,q2)==False:
                              print("El codigo no es un producto valido")
                              otro=input("¿Quiere agregar otro producto?")
                           else:
                              canti2=input("Digite la cantidad a vender:")
                              canti2=int(canti2)
                              
                              if cantidad(codsup,q2,canti2)==False:
                                 print("La cantidad no es valida")
                                 otro=input("¿Quiere agregar otro producto?:")
                              else:
                                 produli+=[q2]
                                 cantili+=[canti2]
                                 otro=input("¿Quiere agregar otro producto?:")
                        if otro=="no" or "No":
                           break

                     print("Aqui")         
                     compras(codsup,produli,cantili,a)
                     c=input("Indique funcion a realizar:")
#----------------------------------------------------------------------------------------------------------------------------------
         #El horror continua
         else:
            print("El cliente no esta registrado, por favor registrelo")
            register(a)
            print("Usuario registrado")
            codsup=input("Introduzca el codigo del supermercado:")
            inventario=leerinve(codsup)
            if inventario==[]:
               print("El supermercado digitado no existe")
               print("Compra cancelada")
               c=input("Indique funcion a realizar:")
            else:
               verinve(inventario)
               q=input("Digite el codigo del producto a vender:")
               q=int(q)
               if producto(codsup,q)==False:
                  print("El producto no es valido")
                  c=input("Indique funcion a realizar:")
               else:    
                  produli=[]
                  cantili=[]
                  produli+=[q]
                  canti=input("Digite la cantidad a vender:")
                  canti=int(canti)
                  if cantidad(codsup,q,canti)==False:
                     print("La cantidad no es valida")
                     c=input("Indique funcion a realizar:")
                  else:
                     cantili+=[canti]
                     otro=input("¿Quiere agregar otro producto?:")
                     while otro!="No" or otro!="no":
                        if otro=="Si"or otro=="si":
                           q2=input("Digite el codigo del producto a vender:")
                           q2=int(q2)
                           
                           if producto(codsup,q2)==False:
                              print("El codigo no es un producto valido")
                              otro=input("¿Quiere agregar otro producto?")
                           else:
                              canti2=input("Digite la cantidad a vender:")
                              canti2=int(canti2)
                              
                              if cantidad(codsup,q2,canti2)==False:
                                 print("La cantidad no es valida")
                                 otro=input("¿Quiere agregar otro producto?:")
                              else:
                                 produli+=[q2]
                                 cantili+=[canti2]
                                 otro=input("¿Quiere agregar otro producto?:")
                        if otro=="no" or "No":
                           break

                     print("Aqui")         
                     comprasnoregi(codsup,produli,cantili,a)
                     c=input("Indique funcion a realizar:")
            
            c=input("Indique funcion a realizar:")
      #Fin del horror
      if c=="Agregar_Cliente":
         print("Registre el cliente por favor")
         a=input("Introdusca cedula del cliente:")
         register(a)
         c=input("Indique funcion a realizar:")
            
      if c=="devolucion":
         a=input("Digite el codigo del producto:")
         devolucion(a)
         c=input("Indique funcion a realizar:")
         
      if c=="leer":
         a=input("Digite el nombre del archivo a leer:")
         if a=="Usuarios" or a=="usuarios":
            lee(Usuarios)
         if a=="Ciudades" or a=="ciudades":
            lee(Ciudades)
         if a=="Inventario" or a=="inventario":
            lee(Inventario)
         if a=="Supermercado" or a=="supermercado":
            lee(Supermercado)
         c=input("Indique funcion a realizar:")

      if c=="precio":
         a=input("Digite el codigo del producto:")
         b=input("Digite el codigo del supermercado donde desea buscar:")
         precio(a,b)
         c=input("Indique funcion a realizar:")

      if c=="borrar":
         a=input("Digite el codigo del producto a borrar:")
         delprod(a)
         c=input("Indique funcion a realizar:")

      if c=="EliminarC":
         a=input("Digite la cedula del cliente que desea borrar:")
         elimiC(a)
         c=input("Indique funcion a realizar:")

      if c=="agregar":
         a=input("Digite el codigo del producto que quiere agregar:")
         agrega(a)
         c=input("Indique funcion a realizar:")

      if c=="info":
         print("\n")
         print("Para realizar una orden de compra digite: ventas")
         print("Para finalizar una compra digite: facturacion")
         print("Para realizar una devolucion digite: devolucion")
         print("Para leer los archivos digite: leer")
         print("Para ver el precio de un articulo digite: precio")
         print("Para borrar un articulo digite: borrar")
         print("Para agregar un articulo digite: agregar")
         print("Para consultar ultimo descuento de un cliente digite: descuento")
         print("Para salir digite: salir")
         print("\n")
         c=input("Indique funcion a realizar:")

      if c=="facturacion":
         a=input("Introdusca cedula del cliente:")
         a=int(a)
         b=vcedu(a)
         print(b)
         if b=="Cliente Registrado":
            print("Para confirmar su orden de compra digite Si")
            print("Para volver al menu digite No")
            deci=input("Introduzca su desicion:" )
            while deci!="no" or deci!="No":
               if deci=="si" or deci=="Si":
                  facturacion(a)
                  c=input("Indique funcion a realizar:")
                  break
                  
               else:
                  print("Para confirmar su orden de compra digite Si")
                  print("Para volver al menu digite No")
                  deci=input("Introduzca su desicion:" )
         else:
            print("El cliente no esta registrado")
            c=input("Indique funcion a realizar:")
               
      if c=="descuento":
         c=input("Indique funcion a realizar:")
         
         
      if c=="salir":
         break
      
      if c!="ventas" and c!="leer" and c!="devolucion"  and c!="facturacion" and c!="precio" and c!="borrar" and c!="agregar" and c!="info" and c!="Agregar_Cliente" and c!="EliminarC" and c!="descuento":
         print("La funcion",c,"no es valida para mas informacion digite: info")
         c=input("Indique funcion a realizar:")
         
   if c=="salir":
      print("Adios",nombre)
      print ("Cerrando..." )
      return

def bienvenido():
   print("Bienvenido")
   x=input("Digite su cedula:")
   try:
      x=int(x)
   except:
      print("La cedula digitada no corresponde a un numero")
   verusuario(x)

class ThreadServer(socketserver.ThreadingMixIn,socketserver.ForkingTCPServer):
    
    pass


def main():
   print("Estamos en main")
   server = ThreadServer(("localhost",6969),MiTcpHandler)
   server_thread = threading.Thread(target=server.serve_forever)
   server_thread.start()
   print("Server conectado y corriendo")


def ventas2():
   a=input("Introduzca cedula del cliente:")
   a=int(a)
   b=vcedu(a)
   print(b)

   if b=="Cliente Registrado":
      codsup=input("Introduzca el codigo del supermercado:")
      inventario=leerinve(codsup)
      if inventario==[]:
         print("El supermercado digitado no existe")
         print("Compra cancelada")
         c=input("Indique funcion a realizar:")
      else:
         verinve(inventario)
         q=input("Digite el codigo del producto a vender:")
         q=int(q)
         if producto(codsup,q)==False:
            print("El producto no es valido")
            c=input("Indique funcion a realizar:")
         else:    
            produli=[]
            cantili=[]
            produli+=[q]
            canti=input("Digite la cantidad a vender:")
            canti=int(canti)
            if cantidad(codsup,q,canti)==False:
               print("La cantidad no es valida")
               c=input("Indique funcion a realizar:")
            else:
               cantili+=[canti]
               otro=input("¿Quiere agregar otro producto?:")
               while otro!="No" or otro!="no":
                  if otro=="Si"or otro=="si":
                     q2=input("Digite el codigo del producto a vender:")
                     q2=int(q2)
                     
                     if producto(codsup,q2)==False:
                        print("El codigo no es un producto valido")
                        otro=input("¿Quiere agregar otro producto?")
                     else:
                        canti2=input("Digite la cantidad a vender:")
                        canti2=int(canti2)
                        
                        if cantidad(codsup,q2,canti2)==False:
                           print("La cantidad no es valida")
                           otro=input("¿Quiere agregar otro producto?:")
                        else:
                           produli+=[q2]
                           cantili+=[canti2]
                           otro=input("¿Quiere agregar otro producto?:")
                  if otro=="no" or "No":
                     break

               print("Aqui")         
               compras(codsup,produli,cantili,a)
               c=input("Indique funcion a realizar:")
#----------------------------------------------------------------------------------------------------------------------------------
   #El horror continua
   else:
      print("El cliente no esta registrado, por favor registrelo")
      register(a)
      print("Usuario registrado")
      codsup=input("Introduzca el codigo del supermercado:")
      inventario=leerinve(codsup)
      if inventario==[]:
         print("El supermercado digitado no existe")
         print("Compra cancelada")
         c=input("Indique funcion a realizar:")
      else:
         verinve(inventario)
         q=input("Digite el codigo del producto a vender:")
         q=int(q)
         if producto(codsup,q)==False:
            print("El producto no es valido")
            c=input("Indique funcion a realizar:")
         else:    
            produli=[]
            cantili=[]
            produli+=[q]
            canti=input("Digite la cantidad a vender:")
            canti=int(canti)
            if cantidad(codsup,q,canti)==False:
               print("La cantidad no es valida")
               c=input("Indique funcion a realizar:")
            else:
               cantili+=[canti]
               otro=input("¿Quiere agregar otro producto?:")
               while otro!="No" or otro!="no":
                  if otro=="Si"or otro=="si":
                     q2=input("Digite el codigo del producto a vender:")
                     q2=int(q2)
                     
                     if producto(codsup,q2)==False:
                        print("El codigo no es un producto valido")
                        otro=input("¿Quiere agregar otro producto?")
                     else:
                        canti2=input("Digite la cantidad a vender:")
                        canti2=int(canti2)
                        
                        if cantidad(codsup,q2,canti2)==False:
                           print("La cantidad no es valida")
                           otro=input("¿Quiere agregar otro producto?:")
                        else:
                           produli+=[q2]
                           cantili+=[canti2]
                           otro=input("¿Quiere agregar otro producto?:")
                  if otro=="no" or "No":
                     break

               print("Aqui")         
               comprasnoregi(codsup,produli,cantili,a)
               c=input("Indique funcion a realizar:")
            
            c=input("Indique funcion a realizar:")

bienvenido()
   

   
          
